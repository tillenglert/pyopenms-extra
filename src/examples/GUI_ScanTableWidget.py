import sys
from PyQt5.QtWidgets import QApplication

import pyopenms

from GUI_EXAMPLE_BASE import GUI_EXAMPLE_BASE
sys.path.insert(0, '../view')
from ScanTableWidget import ScanTableWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI_EXAMPLE_BASE() # plain QMainWindow with basic layout and menu bar

    # load spectra and add example widget to window
    exp = pyopenms.MSExperiment()
    pyopenms.MzMLFile().load("../data/190509_Ova_native_25ngul_R.mzML", exp)
    example_widget = ScanTableWidget(exp)
    ex.setExampleWidget(example_widget)
    ex.show()
    sys.exit(app.exec_())
