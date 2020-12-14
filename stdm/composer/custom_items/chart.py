# /***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

"""
Contains custom layout item types
"""

from qgis.PyQt.QtCore import (
    QCoreApplication
)
from qgis.core import (
    QgsLayoutItemRegistry,
    QgsLayoutItemAbstractMetadata,
    QgsLayoutItemPicture
)

from stdm.ui.gui_utils import GuiUtils

STDM_CHART_ITEM_TYPE = QgsLayoutItemRegistry.PluginItem + 2337 + 5


class StdmChartLayoutItem(QgsLayoutItemPicture):

    def __init__(self, layout):
        super().__init__(layout)

    def type(self):
        return STDM_CHART_ITEM_TYPE

    def icon(self):
        return GuiUtils.get_icon('chart.png')


class StdmChartLayoutItemMetadata(QgsLayoutItemAbstractMetadata):

    def __init__(self):
        super().__init__(STDM_CHART_ITEM_TYPE, QCoreApplication.translate('StdmItems', 'STDM Chart'))

    def createItem(self, layout):
        return StdmChartLayoutItem(layout)
