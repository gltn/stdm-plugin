"""
/***************************************************************************
Name                 : Second Examination Wizard
Description          : Dialog for performing first examination  on a scheme.
Date                 : 01/July/2019
copyright            : (C) 2019 by Joseph Kariuki
email                : joehene@gmail.com
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
from PyQt4.QtGui import (
    QWizard
)

from ui_second_examination import Ui_SecondExam_Wzd


class SecondExaminationWizard(QWizard, Ui_SecondExam_Wzd):
    """
    Wizard that compiles information necessary to perform second examination
    """
    def __init__(self, parent=None):
        QWizard.__init__(self, parent)

        self.setupUi(self)
