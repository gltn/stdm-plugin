"""
/***************************************************************************
Name                 : Workflow Manager Model
Description          : Model for handling scheme table data in
                       Scheme Establishment and First, Second and
                       Third Examination FLTS modules.
Date                 : 11/August/2019
copyright            : (C) 2019
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import datetime
from decimal import Decimal
from PyQt4.QtCore import *
from sqlalchemy import exc
from sqlalchemy.orm.base import object_mapper
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.exc import UnmappedInstanceError


class WorkflowManagerModel(QAbstractTableModel):
    """
    Handles data for Scheme Establishment and First, Second
    and Third Examination FLTS modules
    """
    def __init__(self, data_service):
        super(WorkflowManagerModel, self).__init__()
        self.data_service = data_service
        self.query_object = None
        self.results = []
        self._headers = []
        self.fk_entity_name, self.collection_name = \
            self.data_service.related_entity_name()

    def flags(self, index):
        """
        Implementation of QAbstractTableModel
        flags method
        """
        column = index.column()
        if not index.isValid():
            return Qt.ItemIsEnabled
        elif self._headers[column].flag == Qt.ItemIsUserCheckable:
            return Qt.ItemFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index))

    def data(self, index, role=Qt.DisplayRole):
        """
        Implementation of QAbstractTableModel
        data method
        """
        if not index.isValid() or \
           not (0 <= index.row() < len(self.results)):
            return
        result = self.results[index.row()]
        column = index.column()
        value = result.get(column, None)
        flag = self._headers[column].flag
        if role == Qt.DisplayRole and flag != Qt.ItemIsUserCheckable:
            return value
        elif role == Qt.CheckStateRole and flag == Qt.ItemIsUserCheckable:
            if isinstance(value, float):
                return Qt.Checked if int(value) == 1 else Qt.Unchecked
        elif role == Qt.TextAlignmentRole:
            if flag == Qt.ItemIsUserCheckable:
                return int(Qt.AlignCenter | Qt.AlignVCenter)
            return int(Qt.AlignLeft | Qt.AlignVCenter)
        return

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """
        Implementation of QAbstractTableModel
        headerData method
        """
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return int(Qt.AlignLeft | Qt.AlignVCenter)
            return int(Qt.AlignRight | Qt.AlignVCenter)
        elif role != Qt.DisplayRole:
            return
        if orientation == Qt.Horizontal:
            if self._headers:
                return self._headers[section].name
        elif orientation == Qt.Vertical:
            return
        return int(section + 1)

    def rowCount(self, index=QModelIndex()):
        """
        Implementation of QAbstractTableModel
        rowCount method
        """
        return len(self.results)

    def columnCount(self, index=QModelIndex()):
        """
        Implementation of QAbstractTableModel
        columnCount method
        """
        try:
            return len(self._headers)
        except IndexError as e:
            return 0

    def setData(self, index, value, role=Qt.EditRole):
        """
        Implementation of QAbstractTableModel
        setData method
        """
        if not index.isValid() and \
                not (0 <= index.row() < len(self.results)):
            return False
        result = self.results[index.row()]
        column = index.column()
        flag = self._headers[column].flag
        if isinstance(result.get(column, None), float):
            if flag == Qt.ItemIsUserCheckable:
                result[column] = 1.0 if value == Qt.Checked else 0.0
            else:
                result[column] = float(value)
        else:
            result[column] = value
        self.dataChanged.emit(index, index)
        return True

    def get_record_id(self, row=0):
        """
        Gets record/entity id (primary key)
        :param row: Row index/number
        :rtype row: Integer
        :return: Record id
        :rtype: integer
        """
        return self.results[row]["data"].id

    @staticmethod
    def get_column_index(index, position):
        """
        Get item index at a column position
        :param index: Table view item identifier
        :type index: QModelIndex
        :param position: Required column position
        :type position: Integer
        :return row: Row position or None
        :rtype row: Integer
        :return column: Column position or None
        :rtype column: Integer
        """
        row = index.row()
        column = index.column()
        if column != position:
            return None, None
        return row, column

    def load(self):
        """
        Loads query results to be used in the table view
        """
        # TODO: Too long/ugly method. To be broken potentially into class objects
        try:
            self.query_object = self.data_service.run_query()
            for row in self.query_object:
                store = {}
                for n, prop in enumerate(self.data_service.columns):
                    column = prop.values()[0]
                    header = prop.keys()[0]
                    if isinstance(column, dict):
                        fk_name = column.keys()[0]
                        if fk_name in self.fk_entity_name and hasattr(row, fk_name):
                            store[n] = self._get_value(row, column, fk_name)
                            self._append(header, self._headers)
                            continue
                        elif self.collection_name:
                            store[n] = None
                            for item in self._get_collection_item(row, self.collection_name):
                                if hasattr(item, fk_name) or hasattr(item, column.get(fk_name)):
                                    if self._is_mapped(getattr(item, fk_name, None)):
                                        store[n] = self._get_value(item, column, fk_name)
                                    else:
                                        store[n] = self._get_value(item, column.get(fk_name))
                            self._append(header, self._headers)
                            continue
                    elif hasattr(row, column):
                        store[n] = self._get_value(row, column)
                        self._append(header, self._headers)
                        continue
                    else:
                        store[n] = self._cast_data(column)
                        self._append(header, self._headers)
                store["data"] = row
                self.results.append(store)
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def _get_value(self, row_obj, column, attr=None):
        """
        Returns entity column value
        :param row_obj: Entity row object
        :type row_obj: Entity
        :param column: Field or related entity name
        :type column: String/Dictionary
        :param attr: Related entity column
        :type attr: String
        :return value: Field value
        :rtype value: Multiple types
        """
        if attr:
            fk_entity_object = getattr(row_obj, attr, None)
            value = getattr(fk_entity_object, column.get(attr), None)
        else:
            value = getattr(row_obj, column, None)
        value = self._cast_data(value)
        return value

    def _cast_data(self, value):
        """
        Cast data from one type to another
        :param value: Item data
        :type value: Multiple types
        :return value: Cast data
        :rtype value: Multiple types
        """
        value = float(value) if self._is_number(value) else value
        if isinstance(value, (Decimal, int, float)):
            return float(value)
        elif type(value) is datetime.date:
            return QDate(value)
        elif type(value) is datetime.datetime:
            return QDateTime(value).time()
        return unicode(value) if value is not None else value

    @staticmethod
    def _append(item, container):
        """
        Append unique items to a list
        :param item: Data attribute
        :type item: Multiple types
        :param container: Items container
        :type container: List
        """
        if item not in container:
            container.append(item)
    @property
    def entity_name(self):
        """
        Entity name
        :return _name: Entity name
        :rtype _name: String
        """
        return self.data_service.entity_name

    @staticmethod
    def _is_number(value):
        """
        Checks if value is a number
        :param value: Input value
        :type value: Multiple types
        :return: True if number otherwise return false
        :rtype: Boolean
        """
        try:
            float(value)
            return True
        except (ValueError, TypeError, Exception):
            return False

    def update(self, values):
        """
        Update database record(s) on client edit
        """
        # TODO: Too long/ugly method. To be broken potentially into class objects
        try:
            for row_idx, (column, column_idx, new_value) in values.iteritems():
                row = self.results[row_idx]
                data = row["data"]
                if isinstance(column, dict):
                    fk_name = column.keys()[0]
                    if fk_name in self.fk_entity_name and hasattr(data, fk_name):
                        fk_entity_object = getattr(data, fk_name, None)
                        setattr(fk_entity_object, column.get(fk_name), new_value)
                        fk_entity_object.update()
                    elif self.collection_name:
                        for item in self._get_collection_item(data, self.collection_name):
                            if hasattr(item, fk_name) or hasattr(item, column.get(fk_name)):
                                if self._is_mapped(getattr(item, fk_name, None)):
                                    fk_entity_object = getattr(item, fk_name, None)
                                    setattr(fk_entity_object, column.get(fk_name), new_value)
                                    fk_entity_object.update()
                                else:
                                    setattr(item, column.get(fk_name), new_value)
                                    item.update()
                elif hasattr(data, column):
                    setattr(data, column, new_value)
                    data.update()
                index = self.create_index(row_idx, column_idx)
                if index:
                    row[column_idx] = new_value
                    self.dataChanged.emit(index, index)
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    @staticmethod
    def _get_collection_item(row, collection_name):
        """
        Returns a collection of related entity values
        :param row: Entity record
        :type row: Entity
        :param collection_name: Name of relationship
        :return item: Collection item of values
        :rtype item:
        """
        for name in collection_name:
            collection = getattr(row, name, None)
            if isinstance(collection, InstrumentedList):
                for item in collection:
                    yield item

    @staticmethod
    def _is_mapped(value):
        """
        Check if value is an ORM mapped object
        :param value: Input value
        :type value: Multiple type
        :return: True if mapped otherwise false
        :rtype: Boolean
        """
        try:
            object_mapper(value)
            return True
        except UnmappedInstanceError:
            return False

    def create_index(self, row, column):
        """
        Safely creates and returns the index
        :param row: Table view row index
        :param column: Table view column
        :return index: Table view item identifier or False
        :rtype index: QModelIndex or Boolean
        """
        index = self.index(row, column)
        if not index.isValid() and \
                not (0 <= index.row() < len(self.results)) and \
                not (0 <= index.column() < len(self._headers)):
            return False
        return index
