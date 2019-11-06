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
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from sqlalchemy import exc
from sqlalchemy.orm.base import object_mapper
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.exc import UnmappedInstanceError


class DataRoutine(object):
    """
    Common data manipulation methods
    """
    def __int__(self):
        self._collection_name = None
        self._collection_filter = None

    @staticmethod
    def get_value(query_obj, column, attr=None):
        """
        Returns entity column value
        :param query_obj: Entity query object
        :type query_obj: Entity
        :param column: Column or related entity name
        :type column: String/Dictionary
        :param attr: Related entity column
        :type attr: String
        :return value: Field value
        :rtype value: Multiple types
        """
        if attr:
            fk_entity_object = getattr(query_obj, attr, None)
            return getattr(fk_entity_object, column.get(attr), None)
        return getattr(query_obj, column, None)

    def to_pyqt(self, obj):
        """
        Converts data from python object type to PyQt equivalent
        :param obj: Python object
        :type obj: Multiple types
        :return: Converted value
        :rtype: Multiple types
        """
        obj = float(obj) if self._is_number(obj) else obj
        if isinstance(obj, (Decimal, int, float)):
            return float(obj)
        elif type(obj) is datetime.date:
            return QDate(obj)
        elif type(obj) is datetime.datetime:
            return QDateTime(obj).toLocalTime()
        return unicode(obj) if obj is not None else obj

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

    def valid_collection_item(self, query_obj, column):
        """
        Return valid collection item
        :param query_obj: Query object
        :type query_obj: Entity
        :param column: Column or related entity name
        :type column: Dictionary
        :return item: Entity query object
        :rtype item: Entity
        """
        fk_name = column.keys()[0]
        for item in self.get_collection_item(query_obj, self._collection_name):
            if hasattr(item, fk_name) or hasattr(item, column.get(fk_name)):
                if isinstance(self._collection_filter, dict):
                    item_filter = self.item_filter(item, self._collection_filter)
                    if item_filter == self._collection_filter:
                        return item
                else:
                    return item

    @staticmethod
    def get_collection_item(query_obj, collection_name):
        """
        Returns a collection of related entity values
        :param query_obj: Entity query object
        :type query_obj: Entity Object
        :param collection_name: Name of relationship
        :return item: Collection item of values
        :rtype item:
        """
        for name in collection_name:
            collection = getattr(query_obj, name, None)
            if isinstance(collection, InstrumentedList):
                for item in reversed(collection):
                    yield item

    @staticmethod
    def is_mapped(value):
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

    @staticmethod
    def append_(item, container):
        """
        Append unique items to a list
        :param item: Data attribute
        :type item: Multiple types
        :param container: Items container
        :type container: List
        """
        if item not in container:
            container.append(item)

    @staticmethod
    def item_filter(item, collection_filter):
        """
        Returns item filter
        :param item: Entity query object
        :type item: Entity
        :param collection_filter: Collection record data filter
        :type collection_filter: Dictionary
        :return item_filter: Item record data filter
        :rtype item_filter: Dictionary
        """
        item_filter = {
            column: getattr(item, column, None) for column, value in
            collection_filter.iteritems()
        }
        return item_filter


class Load(DataRoutine):
    """
    Loads query results to be used in the table view
    """
    def __init__(self, data_service, collection_filter=None):
        """
        :param data_service: Data service
        :type data_service: DataService
        :type collection_filter: View data collection identifier
        :type collection_filter: Multiple types
        """
        super(Load, self).__int__()
        self._data_service = data_service
        self._fk_entity_name = data_service.related_entities()
        self._collection_name = data_service.collections
        self._collection_filter = collection_filter
        self._results = []
        self._headers = []

    def load(self):
        """
        Load data based on query results
        """
        self._query_data()
        return self._results, self._headers

    def load_collection(self):
        """
        Loads data based on collection items in the query results
        """
        self._query_collection()
        return self._results, self._headers

    def _query_collection(self):
        """
        Gets data based on collection items in the query results
        """
        try:
            query_objs = self._data_service.run_query()
            load_collections = self._data_service.load_collections
            for row in query_objs:
                for item in self.get_collection_item(row, load_collections):
                    store = self._get_query_data(item)
                    if store:
                        store["data"] = item
                        self._results.append(store)
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def _query_data(self):
        """
        Gets data based on query results
        """
        try:
            query_objs = self._data_service.run_query()
            for row in query_objs:
                store = self._get_query_data(row)
                if store:
                    store["data"] = row
                    self._results.append(store)
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def _get_query_data(self, query_obj):
        """
        Returns query data from specific columns
        :param query_obj: Query object
        :type query_obj: Entity
        :return store: Query data from specific columns
        :rtype store: Dictionary
        """
        store = {}
        for n, prop in enumerate(self._data_service.columns):
            column = prop.values()[0]
            header = prop.keys()[0]
            if isinstance(column, dict):
                fk_name = column.keys()[0]
                if fk_name in self._fk_entity_name and hasattr(query_obj, fk_name):
                    store[n] = self._cast_value(query_obj, column, fk_name)
                    self.append_(header, self._headers)
                    continue
                store[n] = self._get_collection_value(query_obj, column)
                self.append_(header, self._headers)
                continue
            elif hasattr(query_obj, column):
                store[n] = self._cast_value(query_obj, column)
                self.append_(header, self._headers)
                continue
            store[n] = self.to_pyqt(column)
            self.append_(header, self._headers)
        return store

    def _get_collection_value(self, query_obj, column):
        """
        Gets collection value(s)
        :param query_obj: Query object
        :type query_obj: Entity
        :param column: Column or related entity name
        :type column: Dictionary
        :return: Collection value
        :rtype: Multiple types
        """
        item = self.valid_collection_item(query_obj, column)
        if item:
            return self._get_item_value(item, column)
        return None

    def _get_item_value(self, item, column):
        """
        Returns collection item value
        :param item: Entity query object
        :type item: Entity
        :param column: Column as it appears in the database
        :type column: Dictionary
        :return: Collection value
        :rtype: Multiple types
        """
        fk_name = column.keys()[0]
        if self.is_mapped(getattr(item, fk_name, None)):
            return self._cast_value(item, column, fk_name)
        return self._cast_value(item, column.get(fk_name))

    def _cast_value(self, query_obj, column, attr=None):
        """
        Returns type converted entity column value
        :param query_obj: Entity query object
        :type query_obj: Entity
        :param column: Column or related entity name
        :type column: String/Dictionary
        :param attr: Related entity column
        :type attr: String
        :return value: Cast value
        :rtype value: Multiple types
        """
        if attr:
            value = self.get_value(query_obj, column, attr)
        else:
            value = self.get_value(query_obj, column)
        return self.to_pyqt(value)


class Update(DataRoutine):
    """
    Update database record(s) on edit
    """

    def __init__(self, updates, model_items, data_service):
        """
        :param updates: Update items - values and column indexes
        :type updates: Dictionary
        :param model_items: Model items/records
        :type model_items: List
        :param data_service: Data service
        :type data_service: DataService
        """
        super(Update, self).__int__()
        self._updates = updates
        self._model_items = model_items
        self._fk_entity_name = data_service.related_entities()
        self._collection_name = data_service.collections

    def update(self):
        """
        Update database record(s) on client edit
        :return count: Number of updated items
        :rtype count: Integer
        """
        try:
            query_obj, count = self._set_update()
            if query_obj:
                query_obj.update()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e
        else:
            return count

    def _set_update(self):
        """
        Sets update attribute value for the appropriate field
        :return count: Number of updated items
        :rtype count: Integer
        """
        try:
            count = 0
            query_obj = None
            for row_idx, columns in self._updates.iteritems():
                updated = None
                query_obj = self._model_items[row_idx].get("data")
                for column, new_value, collection_filter in columns:
                    if isinstance(column, dict):
                        fk_name = column.keys()[0]
                        if fk_name in self._fk_entity_name and hasattr(query_obj, fk_name):
                            updated = self._set_update_value(
                                query_obj, column.get(fk_name), new_value
                            )
                            continue
                        self._collection_filter = collection_filter
                        updated = self._set_collection_value(query_obj, column, new_value)
                        continue
                    elif hasattr(query_obj, column):
                        updated = self._set_update_value(query_obj, column, new_value)
                        continue
                count = count + 1 if updated else count
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e
        else:
            return query_obj, count

    def _set_collection_value(self, query_obj, column, new_value):
        """
        Sets collection update attribute value
        :param query_obj: Query object
        :type query_obj: Entity
        :param column: Column or related entity name
        :type column: Dictionary
        :param new_value: New value for update
        :type new_value: Multiple types
        :return: Entity query object or None
        :rtype: Entity, NoneType
        """
        item = self.valid_collection_item(query_obj, column)
        if item:
            return self._set_item_value(item, column, new_value)
        return None

    def _set_item_value(self, item, column, new_value):
        """
        Sets collection item value
        :param item: Entity query object
        :type item: Entity
        :param column: Column as it appears in the database
        :type column: Dictionary
        :param new_value: New value for update
        :type new_value: Multiple types
        :return: Collection value
        :rtype: Multiple types
        """
        column, fk_name = self._get_update_attr(item, column)
        if fk_name:
            item = self.get_value(item, fk_name)
        return self._set_update_value(item, column, new_value)

    def _get_update_attr(self, item, column):
        """
        Return update item attribute (column name or
        related entity name)
        :param item: Entity query object
        :type item: Entity
        :param column: Column or related entity name
        :type column: Dictionary
        :return: Related entity column name
        :rtype: String
        :return: Related entity name/None
        :rtype : String/NoneType
        """
        fk_name = column.keys()[0]
        if self.is_mapped(getattr(item, fk_name, None)):
            return column.get(fk_name), fk_name
        return column.get(fk_name), None

    @staticmethod
    def _set_update_value(query_obj, column, value):
        """"
        Sets update attribute value
        :param query_obj: Entity query object
        :type query_obj: Entity
        :param column: Column or related entity name
        :type column: String/Dictionary
        :param value: New value for update
        :type value: Multiple types
        :return query_obj: Entity query object
        :rtype query_obj: Entity
        """
        setattr(query_obj, column, value)
        return query_obj


class Save(DataRoutine):
    """
    Update database record(s) on edit
    """

    def __init__(self, save_items, model_items, data_service, parents=None):
        """
        :return save_items: Save items; columns, values and entity
        :rtype save_items: List
        :param model_items: Model items/records
        :type model_items: List
        :param data_service: Data service
        :type data_service: DataService
        :param parents: Parent entity query objects
        :type parents: Dictionary
        """
        super(Save, self).__int__()
        self._save_items = save_items
        self._model_items = model_items
        self._data_service = data_service
        self._fk_entity_name = data_service.related_entities()
        self._collection_name = data_service.collections
        self._parents = parents
        self._entity_items = {}

    def save(self):
        """
        Saves values to database
        :return count: Number of saved items
        :rtype count: Integer
        """
        try:
            count = 0
            if not self._valid_save_items(self._save_items):
                self._set_save_items()
            if self._entity_items:
                for entity_name, items in self._entity_items.iteritems():
                    model = self._data_service.entity_model_(entity_name)
                    entity_obj = model()
                    model = [model(**columns) for columns in items]
                    entity_obj.saveMany(model)
                    count += 1
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e
        else:
            return count

    def save_collection(self):
        """
        Saves related collection values to database
        :return count: Number of saved items
        :rtype count: Integer
        """
        try:
            count = 0
            if not self._valid_save_items(self._save_items):
                self._set_save_items()
            if self._entity_items:
                for row, parent_entity_obj in self._parents.iteritems():
                    for entity_name, items in self._entity_items.iteritems():
                        model = self._data_service.entity_model_(entity_name)
                        model = [model(**columns) for columns in items]
                        collection = self._data_service.load_collections[0]
                        if hasattr(parent_entity_obj, collection):
                            collection = getattr(parent_entity_obj, collection)
                            collection.extend(model)
                        count += 1
                entity_obj = self._parents.values()[0]
                entity_obj.save()  # Commit session
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e
        else:
            return count

    def _valid_save_items(self, items):
        """
        Checks if items are valid for save
        :param items: Dictionary
        :type items: Dictionary
        :return: True if valid otherwise False
        :rtype: Boolean
        """
        valid = all(
            isinstance(k, str) or isinstance(k, unicode)
            for k in items.keys()
        )
        if valid:
            self._entity_items = items
        return valid

    def _set_save_items(self):
        """
        Sets valid save items; entity names, column name and values
        """
        try:
            for row_idx, columns in self._save_items.iteritems():
                query_obj = self._model_items[row_idx].get("data")
                for column, new_value, entity in columns:
                    if isinstance(column, dict):
                        fk_name = column.keys()[0]
                        if fk_name in self._fk_entity_name and hasattr(query_obj, fk_name):
                            entity_name = self._query_entity_name(query_obj)
                            self._set_entity_items(entity_name, column.get(fk_name), new_value)
                            continue
                        self._set_collection_items(query_obj, column, new_value)
                        continue
                    elif hasattr(query_obj, column):
                        entity_name = self._query_entity_name(query_obj)
                        self._set_entity_items(entity_name, column, new_value)
                        continue
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e

    def _set_collection_items(self, query_obj, column, value):
        """
        Sets valid save collection items; entity names, column name and values
        :param query_obj: Query object
        :type query_obj: Entity
        :param column: Column or related entity name
        :type column: Dictionary
        :param value: Value to be saved
        :type value: Multiple types
        """
        item = self.valid_collection_item(query_obj, column)
        if item:
            column, fk_name = self._get_mapped_entity(item, column)
            if fk_name:
                item = self.get_value(item, fk_name)
            entity_name = self._query_entity_name(item)
            self._set_entity_items(entity_name, column, value)

    def _get_mapped_entity(self, item, column):
        """
        Returns ORM mapped column and entity name
        :param item: Entity query object
        :type item: Entity
        :param column: Column or related entity name
        :type column: Dictionary
        :return: Entity column name
        :rtype: String
        :return: ORM mapped entity name or None
        :rtype : String, NoneType
        """
        fk_name = column.keys()[0]
        if self.is_mapped(getattr(item, fk_name, None)):
            return column.get(fk_name), fk_name
        return column.get(fk_name), None

    def _query_entity_name(self, query_obj):
        """
        Returns query object entity short name
        :param query_obj: Query object
        :type query_obj: Entity
        :return: Entity short name
        :rtype: String
        """
        entity_name = query_obj.__table__.name
        return self._entity_short_name(entity_name)

    @staticmethod
    def _entity_short_name(name):
        """
        Returns entity short name
        :param name: Entity long name
        :type name: String
        :return: Entity short name
        :rtype: String
        """
        prefix = "cb_"
        if name.startswith(prefix):
            name = name.split(prefix, 1)[1]
            return name.capitalize()
        return name.capitalize()

    def _set_entity_items(self, entity_name, column, value):
        """
        Sets valid save entity items; entity names, column name and values
        :param entity_name: Entity short name
        :type entity_name: String
        :param column: Column name
        :type column: String
        :param value: Value to be saved
        :type value: Multiple types
        """
        if entity_name in self._entity_items:
            items = self._entity_items[entity_name]
            for index, columns in enumerate(items):
                if column not in columns:
                    columns[column] = value
                elif column in columns and len(items) == index + 1:
                    items.append({column: value})
                    break
        else:
            self._entity_items[entity_name] = [{column: value}]


class WorkflowManagerModel(QAbstractTableModel):
    """
    Handles data for Scheme Establishment and First, Second
    and Third Examination FLTS modules
    """
    def __init__(self, data_service, collection_filter=None):
        super(WorkflowManagerModel, self).__init__()
        self._data_service = data_service
        self._icons = self._data_service.icons \
            if hasattr(self._data_service, "icons") else None
        self._collection_filter = collection_filter
        self.results = []
        self._headers = []

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
        if role == Qt.DecorationRole and flag == Qt.DecorationRole:
            if self._icons:
                if isinstance(value, float):
                    value = float(value)
                return self._icons[value]
            return None
        elif role == Qt.DisplayRole and flag not in(
                Qt.ItemIsUserCheckable, Qt.DecorationRole
        ):
            return value
        elif role == Qt.CheckStateRole and flag == Qt.ItemIsUserCheckable:
            if isinstance(value, float):
                return Qt.Checked if int(value) == 1 else Qt.Unchecked
        elif role == Qt.TextAlignmentRole:
            if flag == Qt.ItemIsUserCheckable or flag == Qt.DecorationRole:
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

    def model_item(self, row, column):
        """
        Return model item
        :param row: Row index
        :rtype row: Integer
        :param column: Column index
        :rtype column: Integer
        :return item: Table field value
        :rtype item: Multiple types
        """
        item = self.results[row].get(column)
        return item

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

    @property
    def entity_name(self):
        """
        Entity name
        :return _name: Entity name
        :rtype _name: String
        """
        return self._data_service.entity_name

    def load(self):
        """
        Load query results to be used in the table view
        """
        self.results, self._headers = Load(
            self._data_service, self._collection_filter
        ).load()

    def load_collection(self):
        """
        Load collection query results to be used in the table view
        """
        self.results, self._headers = Load(
            self._data_service, self._collection_filter
        ).load_collection()

    def update(self, updates):
        """
        Update database record(s) on client edit
        :param updates: Update items - values and column indexes
        :type updates: Dictionary
        :return: Number of updated items
        :rtype: Integer
        """
        updated = 0
        try:
            updated = Update(
                updates, self.results, self._data_service
            ).update()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e
        finally:
            return updated

    def save(self, save_items):
        """
        Saves values to database
        :param save_items: Save items; columns, values and entity
        :type save_items: Dictionary
        :param parent: Parent entity query objects
        :type parent: List
        :return: Number of saved items
        :rtype: Integer
        """
        saved = 0
        try:
            saved = Save(
                save_items, self.results, self._data_service
            ).save()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e
        finally:
            return saved

    def save_collection(self, save_items, parents=None):
        """
        Saves related collection values to database
        :param save_items: Save items; columns, values and entity
        :type save_items: Dictionary
        :param parents: Parent entity query objects
        :type parents: Dictionary
        :return: Number of saved items
        :rtype: Integer
        """
        saved = 0
        try:
            saved = Save(
                save_items, self.results, self._data_service, parents
            ).save_collection()
        except (AttributeError, exc.SQLAlchemyError, Exception) as e:
            raise e
        finally:
            return saved

    def refresh(self):
        """
        Refresh model
        """
        self.layoutAboutToBeChanged.emit()
        self.results = []
        self._headers = []
        self.load()
        self.layoutChanged.emit()