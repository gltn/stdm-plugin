def valueHandler(ctl):
    """
    Factory that returns the corresponding value handler based on the control type.
    """

    from stdm.ui.helpers.dirtytracker import (
        ControlDirtyTracker,
        ControlDirtyTrackerCollection,
        ControlReaderMapper
    )
    from stdm.ui.helpers.valuehandlers import (
        CheckBoxValueHandler,
        ControlValueHandler,
        LineEditValueHandler,
        ComboBoxValueHandler,
        TextEditValueHandler,
        DateEditValueHandler,
        SourceDocManagerValueHandler,
        ForeignKeyMapperValueHandler,
        SpinBoxValueHandler,
        DoubleSpinBoxValueHandler,
        CoordinatesWidgetValueHandler,
        AutoGeneratedLineEditValueHandler
    )
    from stdm.ui.helpers.datamanagemixin import SupportsManageMixin

    ctlName = str(ctl.metaObject().className())

    if ctlName in ControlValueHandler.handlers:
        return ControlValueHandler.handlers[ctlName]
    else:
        return None

