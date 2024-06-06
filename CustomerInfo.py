from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sqlite3
from PyQt5.QtCore import QAbstractTableModel, Qt

class Ui_customerInfo(QMainWindow):

    def __init__(self, customerData):
        super(Ui_customerInfo, self).__init__()
        self.customerData = customerData
        self.setupUi()
        self.populateTable()

        # Establish a connection to the SQLite database named 'BankDatabase.db'
        self.connect = sqlite3.connect('BankDatabase.db')
        
        # Create a cursor object to perform database operations
        self.cursor = self.connect.cursor()

    def setupUi(self):
        self.setObjectName("customerInfo")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(350, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(350, 500))
        self.setMaximumSize(QtCore.QSize(350, 500))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 11, 331, 451))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.customerDataTable = QtWidgets.QTableWidget(self.widget)
        self.customerDataTable.setEnabled(True)
        self.customerDataTable.setObjectName("customerDataTable")
        self.customerDataTable.setColumnCount(2)
        self.customerDataTable.setRowCount(10)
        self.customerDataTable.setHorizontalHeaderLabels(["Field", "Value"])
        self.verticalLayout.addWidget(self.customerDataTable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("customerInfo", "Customer Information"))

    def populateTable(self):
            for row, (field, value) in enumerate(self.customerData):
                self.customerDataTable.setItem(row, 0, QTableWidgetItem(field))
                self.customerDataTable.setItem(row, 1, QTableWidgetItem(str(value)))
            self.customerDataTable.setEnabled(False)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_customerInfo()
    window.show()
    sys.exit(app.exec_())
