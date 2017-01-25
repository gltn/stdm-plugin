"""
/***************************************************************************
Name                 : GPS Feature Import Dialog
Description          : Dialog for importing GPX data i.e. waypoints, tracks and routes
Date                 : 17/January/2017
copyright            : (C) 2015 by UN-Habitat and implementing partners.
                       See the accompanying file CONTRIBUTORS.txt in the root
email                : stdm@unhabitat.org
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

import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
import qgis.core as q_core
from ui_gps_tool import Ui_Dialog
from .forms.editor_dialog import EntityEditorDialog
from ..utils import util
from ..data.pg_utils import vector_layer
import gps_tool_data_source_utils as gpx_source
import gps_tool_data_view_utils as gpx_view


class GPSToolDialog(qg.QDialog, Ui_Dialog):
    def __init__(self, iface, entity, sp_table, sp_col):
        qg.QDialog.__init__(self, iface.mainWindow())
        self.setupUi(self)
        self.iface = iface
        self.entity = entity
        self.sp_table = sp_table
        self.sp_col = sp_col
        self.entity_editor = None
        gpx_view.enable_drag_drop(self.table_widget)
        self._init_entity_editor()
        self.active_layer = self.iface.activeLayer()
        self.map_canvas = self.iface.mapCanvas()
        self.init_gpx_file = None
        self.point_row_attr = None
        self.prev_point_row_attr = None
        self.prev_selected_rows = None
        self.gpx_layer = None
        self.qgs_point_list = None
        self.geom_type = None
        self.uncheck_counter = 0
        self.temp_layer_name = None
        self.temp_mem_layer = None
        self.prev_temp_mem_layer = None
        self.prev_item_position = None
        self.prev_item_value = None
        self.data_changed = None
        self.drag_drop = None
        self.item_changed = None

        # Source and slot signal connections
        self.file_select_bt.clicked.connect(self._set_file_path)
        self.file_le.textChanged.connect(self._file_source_change)
        self.feature_type_cb.currentIndexChanged.connect(self._show_data)
        self.table_widget.itemClicked.connect(self._table_widget_checkbox_clicked)
        self.table_widget.itemSelectionChanged.connect(self._table_widget_row_selection)
        self.table_widget.connect(self.table_widget, qc.SIGNAL('itemDragEnter'), self._table_widget_drag_enter)
        self.table_widget.connect(self.table_widget, qc.SIGNAL('itemDropped'), self._table_widget_row_dropped)
        self.table_widget.itemDoubleClicked.connect(self._table_widget_item_double_clicked)
        self.table_widget.itemChanged.connect(self._table_widget_item_changed)
        self.select_all_bt.clicked.connect(self._select_all_items)
        self.clear_all_bt.clicked.connect(self._clear_all_items)
        self.load_bt.clicked.connect(self._load_feature)
        self.cancel_bt.clicked.connect(self.close)

    def _init_entity_editor(self):
        """
        Instantiates entity editor and add its widgets to
        the GPX import tool as tabs
        :return: None
        :rtype:None
        """
        self.entity_editor = EntityEditorDialog(self.entity, None, self)
        self.entity_editor.buttonBox.hide()  # Hide entity editor buttons
        for tab_text, tab_object in self.entity_editor.entity_editor_widgets.items():
            if tab_text != 'no_tab':
                self.gpx_import_tab.addTab(tab_object, str(tab_text))
            else:
                self.gpx_import_tab.addTab(tab_object, 'Primary')

    def _set_file_path(self):
        """
        Open file select dialog when browse button is clicked
        :return: None
        :rtype: None
        """
        (gpx_file, encoding) = util.openDialog(self)
        if gpx_file:
            self.file_le.clear()
            self.file_le.setText(gpx_file)

    def _file_source_change(self):
        """
        Enable or disable widgets based on the validity of the file path
        :return: None
        :rtype: None
        """
        gpx_file = str(self.file_le.text()).strip()
        if gpx_source.validate_file_path(gpx_file):
            if self.point_row_attr:
                self._refresh_map_canvas()
                self._reset_widget()
            self._enable_widget(gpx_file)
        else:
            self._disable_widget()

    def _enable_widget(self, gpx_file=None):
        """
        Enables all widgets
        :return: None
        :rtype: None
        """
        if self.table_widget.columnCount() > 0:
            self._reset_widget(gpx_file)
            if gpx_file == self.init_gpx_file:
                self._enable_disable_button_widgets(True)
            self.table_widget.setEnabled(True)
        self.feature_type_cb.setEnabled(True)

    def _reset_widget(self, gpx_file=None, feature_type_change=False):
        """
        Resets widget table properties
        :param gpx_file: Input GPX file
        :param feature_type_change: Flag for feature type when changed in
                                    the combobox
        :return: None
        :rtype: None
        """
        if gpx_file:
            if gpx_file != self.init_gpx_file:
                self._reset_table_layer()
                self._disable_widget()
            elif feature_type_change and gpx_file == self.init_gpx_file:
                self._reset_table_layer()
                self._disable_widget(True)
        else:
            self._reset_table_layer()
            self._disable_widget(False, True)

    def _remove_prev_layer(self):
        """
        Removes previous temporary layer
        :return: None
        :rtype: None
        """
        if self.prev_temp_mem_layer and len(gpx_view.get_layer_by_name(self.temp_layer_name)) != 0:
            gpx_view.remove_vertex(self.map_canvas, self.prev_point_row_attr)
            gpx_view.remove_map_layer(self.map_canvas, self.prev_temp_mem_layer)
            return True

    def _disable_widget(self, enable_cb=False, on_load=None):
        """
        Disables all widgets
        :return: None
        :rtype: None
        """
        self.feature_type_cb.setEnabled(enable_cb)
        if on_load:
            self.table_widget.setEnabled(True)
            self.feature_type_cb.setCurrentIndex(-1)
        elif self.table_widget.columnCount() > 0:
            self.table_widget.setEnabled(False)
        elif self.table_widget.columnCount() == 0:
            self.feature_type_cb.setCurrentIndex(-1)
        self._enable_disable_button_widgets()

    def _reset_table_layer(self):
        """
        Calls column and row reset and removes temporary layer
        :return: None
        :return: None
        """
        self._reset_column_rows()
        self._remove_prev_layer()
        self.prev_temp_mem_layer = None

    def _reset_column_rows(self):
        """
        Removes all columns and rows in the table widget
        :return: None
        :rtype: None
        """
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(0)

    def _enable_disable_button_widgets(self, state=False, load_state=None):
        """
        Disables or enables table widget buttons
        :param state: True or false to enable or disable all buttons
        :return: None
        :rtype: None
        """
        if state is not None:
            self.select_all_bt.setEnabled(state)
            self.clear_all_bt.setEnabled(state)
            self.load_bt.setEnabled(state)
        else:
            self.load_bt.setEnabled(load_state)

    def _refresh_map_canvas(self):
        """
        Refresh map canvas on file source or feature type change
        :return: None
        :rtype: None
        """
        curr_layer = vector_layer(self.sp_table, geom_column=self.sp_col)
        layer_extent = curr_layer.extent()
        gpx_view.remove_vertex(self.map_canvas, self.point_row_attr)
        self.map_canvas.setExtent(layer_extent)
        self.map_canvas.refresh()

    def _show_data(self, index):
        """
        Initializes loading of GPX data
        :param index: Comboxbox item index
        :return: None
        :rtype: None
        """
        gpx_file = str(self.file_le.text()).strip()
        feature_type = self.feature_type_cb.currentText()
        columns = 4
        headers = ["", "Point Name", "Longitude", "Latitude"]
        if feature_type:
            gpx_data_source = gpx_source.open_gpx_file(gpx_file)
            self.gpx_layer, feature_count = gpx_source.get_feature_layer(gpx_data_source, feature_type)
            self.uncheck_counter = feature_count
            if self.gpx_layer:
                self.geom_type, int_geom_type = gpx_source.get_active_layer_type(self.active_layer)
                if self.geom_type:
                    self._populate_data(feature_count, columns, headers)
                    self._enable_disable_load_on_feature_type_click(int_geom_type)
                    self.prev_temp_mem_layer = self.temp_mem_layer
                    self.prev_point_row_attr = list(self.point_row_attr)
                    self.init_gpx_file = gpx_file
                else:
                    qg.QMessageBox.information(None, 'STDM', 'Current active layer not compatible with GPS data. '
                                                             'Geometry type "POINT", "LINE" or "POLYGON" required')
            else:
                qg.QMessageBox.information(None, 'STDM', 'The selected feature type has no features')
                if self.table_widget.columnCount() > 0:
                    if self.point_row_attr:
                        self._refresh_map_canvas()
                    self._reset_widget(gpx_file, True)
                return None

    def _populate_data(self, feature_count, columns, headers):
        """
        Populates table widget with data and creates temporary layer
        :param feature_count: Number of features
        :param columns: Number of table widget columns
        :param headers: Table widget field names
        :return: None
        :rtype: None
        """
        point_list = []
        self.qgs_point_list = []
        self.point_row_attr = []
        self.data_changed = False
        table_widget = self.table_widget
        self.temp_layer_name = 'temp_layer'
        self._set_table_structure(table_widget, feature_count, columns, headers)
        for feature_attr, row in gpx_view.get_feature_attributes(self.gpx_layer):
            point = q_core.QgsPoint(feature_attr[1], feature_attr[2])
            point_list.append(point)
            check_box = self._set_table_widget_item(feature_attr, table_widget, row)
            checkbox_state = check_box.checkState()
            marker = gpx_view.set_feature_vertex_marker(self.map_canvas, feature_attr[1], feature_attr[2])
            self.point_row_attr.append({
                'row': row, 'marker': marker, 'checkbox': check_box, 'check_state': checkbox_state, 'qgs_point': point
            })
        self._set_table_header_property(table_widget)
        self._remove_prev_layer()
        self.temp_mem_layer = gpx_view.create_feature(self.active_layer, self.geom_type, point_list, self.temp_layer_name)
        gpx_view.add_map_layer(self.temp_mem_layer, )
        gpx_view.set_layer_extent(self.map_canvas, self.gpx_layer)
        self.qgs_point_list = list(point_list)
        self.data_changed = True

    def _set_table_structure(self, table_widget, rows, columns, headers):
        """
        Sets table widget rows, columns and headers
        :param rows: Number of rows
        :param columns: Number of columns
        :param headers: Table headers
        :param table_widget: Table widget object
        :return: None
        :rtype: None
        """
        table_widget.setRowCount(rows)
        table_widget.setColumnCount(columns)
        table_widget.setHorizontalHeaderLabels(headers)

    def _set_table_widget_item(self, feature_attr, table_widget, row):
        """
        Sets table widget items
        :param feature_attr: Data from the GPX feature
        :param table_widget: Table widget object
        :param row: Feature count. To be used to set table row number
        :return:
        """
        check_box = None
        for column_num, attr in enumerate(feature_attr):
            if column_num == 0:
                check_box = self._set_checkbox_item()
                table_widget.setItem(row, column_num, check_box)
            column_num += 1
            if type(attr) is not str:
                attr = str(attr)
            table_widget.setItem(row, column_num, qg.QTableWidgetItem(attr))
        return check_box

    def _set_checkbox_item(self):
        """
        Sets the checkbox item
        :return: Table widget item
        :rtype: Object
        """
        check_box = qg.QTableWidgetItem()
        check_box.setCheckState(qc.Qt.Checked)
        check_box.setFlags(qc.Qt.ItemIsUserCheckable | qc.Qt.ItemIsEnabled | qc.Qt.ItemIsSelectable)
        return check_box

    def _set_table_header_property(self, table_widget, enable=True):
        """
        Sets table widget header properties
        :param table_widget: Table widget object
        :param enable: Parameter to set header property to True or False
        :return: None
        :rtype: None
        """
        table_widget.resizeColumnsToContents()
        table_widget.horizontalHeader().setStretchLastSection(enable)

    def _enable_disable_load_on_feature_type_click(self, int_geom_type):
        """
        Enables or disables load button on feature type load to the table
        widget based on the number of features and geometry type.
        :param int_geom_type: Geometry type as an integer
        :return: None
        :rtype: None
        """
        if self.uncheck_counter > int_geom_type:
            self._enable_disable_button_widgets(True)
        elif self.uncheck_counter <= int_geom_type:
            self._enable_disable_button_widgets(None, False)

    def _table_widget_checkbox_clicked(self, item):
        """
        Handles checkbox value change
        :param item: Clicked item or checkbox widget
        :return: None
        :rtype: None
        """
        if item.checkState() == qc.Qt.Unchecked:
            qgs_point = gpx_view.check_uncheck_item(self.point_row_attr, self.map_canvas, item)
            self._unchecked_gpx_point(qgs_point)
            self._enable_disable_load_on_checkbox_click()
        else:
            qgs_point = gpx_view.check_uncheck_item(self.point_row_attr, self.map_canvas, item)
            self._checked_gpx_point(qgs_point)
            self._enable_disable_load_on_checkbox_click()

    def _unchecked_gpx_point(self, qgs_point):
        """
        Removes feature vertex from a list
        :param qgs_point: Feature vertex
        :return: None
        :rtype: None
        """
        if qgs_point:
            qgs_point_list = gpx_view.remove_from_list(self.qgs_point_list, qgs_point)
            if qgs_point_list:
                self.qgs_point_list = qgs_point_list
                point_list, new_point_row_attr = gpx_view.get_qgs_points(self.table_widget)
                self._update_feature(point_list, new_point_row_attr)

    def _checked_gpx_point(self, qgs_point):
        """
        Adds feature vertex to a list
        :param qgs_point: Feature vertex
        :return: None
        :rtype: None
        """
        if qgs_point:
            qgs_point = gpx_view.add_to_list(self.qgs_point_list, qgs_point)
            if qgs_point:
                self.qgs_point_list.append(qgs_point)
                point_list, new_point_row_attr = gpx_view.get_qgs_points(self.table_widget)
                self._update_feature(point_list, new_point_row_attr)

    def _enable_disable_load_on_checkbox_click(self):
        """
        Counts clicks if a checkbox is checked or unchecked and
        enables or disables the load button.
        :return: None
        :rtype: None
        """
        if self.data_changed:
            check_state_count = 0
            active_geom_type = int(self.iface.activeLayer().geometryType())
            for row, point_attr in enumerate(self.point_row_attr):
                if point_attr['check_state'] == 2 and point_attr['qgs_point']:
                    check_state_count += 1
            if check_state_count > active_geom_type:
                self.uncheck_counter += 1
                self._enable_disable_button_widgets(None, True)
            elif check_state_count <= active_geom_type:
                self.uncheck_counter -= 1
                self._enable_disable_button_widgets(None, False)

    def _table_widget_row_selection(self):
        """
        Set vertex color on row selection change
        :return: None
        :rtype: None
        """
        current_selected_rows = sorted(set([index.row() for index in self.table_widget.selectedIndexes()]))
        gpx_view.row_selection_change(self.map_canvas, self.point_row_attr, current_selected_rows, '#0000FF')
        gpx_view.row_selection_change(self.map_canvas, self.point_row_attr, self.prev_selected_rows)
        if current_selected_rows:
            self.prev_selected_rows = []
            self.prev_selected_rows.extend(current_selected_rows)

    def _table_widget_drag_enter(self):
        """
        On start of drag and drop set data change
        and drag and drop flag to false
        :return: None
        :rtype: None
        """
        self.data_changed = False
        self.drag_drop = True

    def _table_widget_row_dropped(self):
        """
        Update feature on end of drag and drop event
        :return: None
        :rtype: None
        """
        point_list, new_point_row_attr = gpx_view.get_qgs_points(self.table_widget)
        self._update_feature(point_list, new_point_row_attr)
        self.data_changed = True

    def _table_widget_item_double_clicked(self, item):
        """
        On double click get previous item values
        :param item: Current item
        :return: None
        :rtype: None
        """
        if item.column() != 0:
            self.prev_item_value = item.text().strip()

    def _table_widget_item_changed(self, item):
        """
        On item change update GPX feature
        :param item: Table widget item
        :return: None
        :rtype: None
        """
        current_item_value = item.text().strip()
        if self.data_changed and item.column() != 0:
            if current_item_value != self.prev_item_value:
                point_list, new_point_row_attr = gpx_view.get_qgs_points(self.table_widget)
                self._update_feature(point_list, new_point_row_attr)
        self._enable_disable_load_on_checkbox_click()

    def _update_feature(self, point_list, new_point_row_attr):
        """
        Update feature
        :param point_list: Updated QGS points
        :param new_point_row_attr: Updated GPX data attributes
        :return: None
        :rtype: None
        """
        if point_list:
            self.qgs_point_list = list(point_list)
            gpx_view.remove_vertex(self.map_canvas, self.prev_point_row_attr)
            gpx_view.delete_feature(self.map_canvas, self.temp_mem_layer)
            self.point_row_attr = gpx_view.update_point_row_attr(self.map_canvas, self.point_row_attr, new_point_row_attr)
            self.point_row_attr = gpx_view.set_feature_vertices_marker(self.map_canvas, self.point_row_attr)
            new_geometry = gpx_view.create_geometry(self.geom_type, point_list)
            data_provider = self.temp_mem_layer.dataProvider()
            gpx_view.add_feature(data_provider, new_geometry)
            gpx_view.commit_feature_edits(self.temp_mem_layer)
            self.prev_point_row_attr = list(self.point_row_attr)
        else:
            gpx_view.remove_vertex(self.map_canvas, self.prev_point_row_attr)
            gpx_view.delete_feature(self.map_canvas, self.temp_mem_layer)

    def _select_all_items(self):
        """
        Checks all items which are unchecked
        :return: None
        :rtype: None
        """
        qgs_point = gpx_view.check_uncheck_item(self.point_row_attr, self.map_canvas, None, 'check')
        self._checked_gpx_point(qgs_point)
        self._enable_disable_button_widgets(None, True)
        if self.data_changed or self.drag_drop:
            point_list, new_point_row_attr = gpx_view.get_qgs_points(self.table_widget)
            self._update_feature(point_list, new_point_row_attr)
            self.drag_drop = None

    def _clear_all_items(self):
        """
        Unchecks all items which are checked and slears the feature
        :return: None
        :rtype: None
        """
        qgs_point = gpx_view.check_uncheck_item(self.point_row_attr, self.map_canvas, None, 'uncheck')
        self._unchecked_gpx_point(qgs_point)
        self._enable_disable_button_widgets(None, False)
        point_list, new_point_row_attr = gpx_view.get_qgs_points(self.table_widget)
        self._update_feature(point_list, new_point_row_attr)

    def _load_feature(self):
        """
        Load and save feature to current active layer
        :return: None
        :rtype: None
        """
        new_geometry = gpx_view.create_geometry(self.geom_type, self.qgs_point_list)
        geometry_wkb = new_geometry.exportToWkt()
        srid = self.entity.columns[self.sp_col].srid
        model = self.entity_editor.model()
        setattr(model, self.sp_col, 'SRID={};{}'.format(srid, geometry_wkb))
        self.entity_editor.submit()
        self._reload_entity_editor()

    def _reload_entity_editor(self):
        """
        Reloads entity editor and its widget
        to the GPX import tab widget.
        :return: None
        :rtype: None
        """
        tab_count = self.gpx_import_tab.count()
        if tab_count > 1:
            for i in reversed(range(tab_count)):
                if i != 0:
                    tab_object = self.gpx_import_tab.widget(i)
                    self.gpx_import_tab.removeTab(i)
                    tab_object.deleteLater()
                    del tab_object
            if self.entity_editor is not None:
                self.entity_editor.deleteLater()
                self.entity_editor = None
            self._init_entity_editor()

    def closeEvent(self, event):
        """
        Closes the import dialog when called
        :param event: Close event
        :return: None
        :rtype: None
        """
        if len(gpx_view.get_layer_by_name(self.temp_layer_name)) != 0:
            gpx_view.remove_vertex(self.map_canvas, self.point_row_attr)
            gpx_view.remove_map_layer(self.map_canvas, self.temp_mem_layer)
        if self.point_row_attr:
            self._refresh_map_canvas()
        event.accept()