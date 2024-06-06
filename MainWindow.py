from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import datetime
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import CustomerInfo


class Ui_MainWindow(QMainWindow):
    def __init__(self):

        """
        Initialize the class instance and establish a connection to the SQLite database.
        
        This method is the constructor of the class and is automatically called when an instance of the class is created.
        It establishes a connection to the SQLite database named 'BankDatabase.db' and creates a cursor object to perform database operations.

        Parameters:
        - self: The instance of the class.
            
        Returns:
        None
        """

        super(Ui_MainWindow, self).__init__()

        # Establish a connection to the SQLite database named 'BankDatabase.db'
        self.connect = sqlite3.connect('BankDatabase.db')
        
        # Create a cursor object to perform database operations
        self.cursor = self.connect.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 940)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 940))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 940))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(340, 430, 641, 481))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txt_lastActivity = QtWidgets.QLineEdit(self.groupBox_5)
        self.txt_lastActivity.setEnabled(False)
        self.txt_lastActivity.setFrame(False)
        self.txt_lastActivity.setObjectName("txt_lastActivity")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_lastActivity)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.tct_openingDate = QtWidgets.QLineEdit(self.groupBox_5)
        self.tct_openingDate.setEnabled(False)
        self.tct_openingDate.setFrame(False)
        self.tct_openingDate.setObjectName("tct_openingDate")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tct_openingDate)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txt_nameSurname = QtWidgets.QLineEdit(self.groupBox_5)
        self.txt_nameSurname.setEnabled(False)
        self.txt_nameSurname.setFrame(False)
        self.txt_nameSurname.setObjectName("txt_nameSurname")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_nameSurname)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txt_customerNumber = QtWidgets.QLineEdit(self.groupBox_5)
        self.txt_customerNumber.setEnabled(False)
        self.txt_customerNumber.setFrame(False)
        self.txt_customerNumber.setObjectName("txt_customerNumber")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_customerNumber)
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txt_accountName = QtWidgets.QLineEdit(self.groupBox_5)
        self.txt_accountName.setEnabled(False)
        self.txt_accountName.setFrame(False)
        self.txt_accountName.setObjectName("txt_accountName")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_accountName)
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.txt_balance = QtWidgets.QLineEdit(self.groupBox_5)
        self.txt_balance.setEnabled(False)
        self.txt_balance.setFrame(False)
        self.txt_balance.setObjectName("txt_balance")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txt_balance)
        self.txt_accountNumber = QtWidgets.QLineEdit(self.groupBox_5)
        self.txt_accountNumber.setEnabled(False)
        self.txt_accountNumber.setFrame(False)
        self.txt_accountNumber.setObjectName("txt_accountNumber")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txt_accountNumber)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.txt_currency = QtWidgets.QLineEdit(self.groupBox_5)
        self.txt_currency.setEnabled(False)
        self.txt_currency.setFrame(False)
        self.txt_currency.setObjectName("txt_currency")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_currency)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.btn_changeAccount = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_changeAccount.sizePolicy().hasHeightForWidth())
        self.btn_changeAccount.setSizePolicy(sizePolicy)
        self.btn_changeAccount.setObjectName("btn_changeAccount")
        self.verticalLayout.addWidget(self.btn_changeAccount)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 160, 321, 271))
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_6)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 29, 301, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.txt_accountName_Account = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_accountName_Account.setFrame(False)
        self.txt_accountName_Account.setObjectName("txt_accountName_Account")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_accountName_Account)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.currency_choice = QtWidgets.QComboBox(self.formLayoutWidget)
        self.currency_choice.setObjectName("currency_choice")
        self.currency_choice.addItem("")
        self.currency_choice.addItem("")
        self.currency_choice.addItem("")
        self.currency_choice.addItem("")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.currency_choice)
        self.btn_newBankAccount = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_newBankAccount.setObjectName("btn_newBankAccount")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.btn_newBankAccount)
        self.btn_deleteBankAccount = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_deleteBankAccount.setObjectName("btn_deleteBankAccount")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.btn_deleteBankAccount)
        self.btn_updateBankAccount = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_updateBankAccount.setObjectName("btn_updateBankAccount")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.btn_updateBankAccount)
        self.chckBox_mainAccount = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.chckBox_mainAccount.setObjectName("chckBox_mainAccount")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.chckBox_mainAccount)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 430, 321, 241))
        self.groupBox_7.setObjectName("groupBox_7")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_7)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(9, 29, 301, 201))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.btn_loadAccounts = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.btn_loadAccounts.setObjectName("btn_loadAccounts")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.btn_loadAccounts)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.account_choice_Money = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.account_choice_Money.setFrame(False)
        self.account_choice_Money.setObjectName("account_choice_Money")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.account_choice_Money)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.txt_amount_Money = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txt_amount_Money.setFrame(False)
        self.txt_amount_Money.setObjectName("txt_amount_Money")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_amount_Money)
        self.btn_withDrawMoney = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.btn_withDrawMoney.setObjectName("btn_withDrawMoney")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.btn_withDrawMoney)
        self.btn_DepositMoney = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.btn_DepositMoney.setObjectName("btn_DepositMoney")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.btn_DepositMoney)
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 670, 321, 241))
        self.groupBox_8.setObjectName("groupBox_8")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_8)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(9, 30, 301, 201))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.customer_choice_Transfer = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.customer_choice_Transfer.setFrame(False)
        self.customer_choice_Transfer.setObjectName("customer_choice_Transfer")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.customer_choice_Transfer)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.account_chose_transfer = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.account_chose_transfer.setFrame(False)
        self.account_chose_transfer.setObjectName("account_chose_transfer")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.account_chose_transfer)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_amount_Transfer = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.txt_amount_Transfer.setFrame(False)
        self.txt_amount_Transfer.setObjectName("txt_amount_Transfer")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_amount_Transfer)
        self.btn_loadCustomers = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.btn_loadCustomers.setObjectName("btn_loadCustomers")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.btn_loadCustomers)
        self.btn_moneyTransfer = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.btn_moneyTransfer.setObjectName("btn_moneyTransfer")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.btn_moneyTransfer)
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(340, 10, 641, 221))
        self.groupBox_9.setObjectName("groupBox_9")
        self.widget = QtWidgets.QWidget(self.groupBox_9)
        self.widget.setGeometry(QtCore.QRect(10, 29, 621, 185))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_newCreditCard = QtWidgets.QPushButton(self.widget)
        self.btn_newCreditCard.setObjectName("btn_newCreditCard")
        self.verticalLayout_5.addWidget(self.btn_newCreditCard)
        self.btn_useCard = QtWidgets.QPushButton(self.widget)
        self.btn_useCard.setObjectName("btn_useCard")
        self.verticalLayout_5.addWidget(self.btn_useCard)
        self.btn_payCreditCardDept = QtWidgets.QPushButton(self.widget)
        self.btn_payCreditCardDept.setObjectName("btn_payCreditCardDept")
        self.verticalLayout_5.addWidget(self.btn_payCreditCardDept)
        self.btn_showCreditCardDept = QtWidgets.QPushButton(self.widget)
        self.btn_showCreditCardDept.setObjectName("btn_showCreditCardDept")
        self.verticalLayout_5.addWidget(self.btn_showCreditCardDept)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.txt_cardLimit_CreditCard = QtWidgets.QLineEdit(self.widget)
        self.txt_cardLimit_CreditCard.setFrame(False)
        self.txt_cardLimit_CreditCard.setObjectName("txt_cardLimit_CreditCard")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_cardLimit_CreditCard)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.txt_spendMoney_CreditCard = QtWidgets.QLineEdit(self.widget)
        self.txt_spendMoney_CreditCard.setFrame(False)
        self.txt_spendMoney_CreditCard.setObjectName("txt_spendMoney_CreditCard")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_spendMoney_CreditCard)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.txt_payDebt_CreditCard = QtWidgets.QLineEdit(self.widget)
        self.txt_payDebt_CreditCard.setFrame(False)
        self.txt_payDebt_CreditCard.setObjectName("txt_payDebt_CreditCard")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_payDebt_CreditCard)
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setObjectName("label_24")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.cardNumber_chose = QtWidgets.QComboBox(self.widget)
        self.cardNumber_chose.setFrame(False)
        self.cardNumber_chose.setObjectName("cardNumber_chose")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cardNumber_chose)
        self.btn_loadCards = QtWidgets.QPushButton(self.widget)
        self.btn_loadCards.setObjectName("btn_loadCards")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.btn_loadCards)
        self.horizontalLayout.addLayout(self.formLayout_7)
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(340, 230, 641, 201))
        self.groupBox_10.setObjectName("groupBox_10")
        self.widget1 = QtWidgets.QWidget(self.groupBox_10)
        self.widget1.setGeometry(QtCore.QRect(10, 26, 621, 151))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_newCredit = QtWidgets.QPushButton(self.widget1)
        self.btn_newCredit.setObjectName("btn_newCredit")
        self.verticalLayout_3.addWidget(self.btn_newCredit)
        self.btn_payCreditLoan = QtWidgets.QPushButton(self.widget1)
        self.btn_payCreditLoan.setObjectName("btn_payCreditLoan")
        self.verticalLayout_3.addWidget(self.btn_payCreditLoan)
        self.btn_showLoan = QtWidgets.QPushButton(self.widget1)
        self.btn_showLoan.setObjectName("btn_showLoan")
        self.verticalLayout_3.addWidget(self.btn_showLoan)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_22 = QtWidgets.QLabel(self.widget1)
        self.label_22.setObjectName("label_22")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.txt_CreditAmount_Credit = QtWidgets.QLineEdit(self.widget1)
        self.txt_CreditAmount_Credit.setFrame(False)
        self.txt_CreditAmount_Credit.setObjectName("txt_CreditAmount_Credit")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_CreditAmount_Credit)
        self.creditNumber_chose = QtWidgets.QComboBox(self.widget1)
        self.creditNumber_chose.setFrame(False)
        self.creditNumber_chose.setObjectName("creditNumber_chose")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.creditNumber_chose)
        self.label_23 = QtWidgets.QLabel(self.widget1)
        self.label_23.setObjectName("label_23")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.txt_payLoan_Credit = QtWidgets.QLineEdit(self.widget1)
        self.txt_payLoan_Credit.setFrame(False)
        self.txt_payLoan_Credit.setObjectName("txt_payLoan_Credit")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_payLoan_Credit)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.btn_loadCredits = QtWidgets.QPushButton(self.widget1)
        self.btn_loadCredits.setObjectName("btn_loadCredits")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.btn_loadCredits)
        self.horizontalLayout_2.addLayout(self.formLayout_8)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 321, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.widget2 = QtWidgets.QWidget(self.groupBox_4)
        self.widget2.setGeometry(QtCore.QRect(9, 30, 301, 111))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_username_User = QtWidgets.QLineEdit(self.widget2)
        self.txt_username_User.setEnabled(False)
        self.txt_username_User.setFrame(False)
        self.txt_username_User.setObjectName("txt_username_User")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_username_User)
        self.txt_email_User = QtWidgets.QLineEdit(self.widget2)
        self.txt_email_User.setEnabled(False)
        self.txt_email_User.setFrame(False)
        self.txt_email_User.setObjectName("txt_email_User")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_email_User)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.btn_customerInformations = QtWidgets.QPushButton(self.widget2)
        self.btn_customerInformations.setObjectName("btn_customerInformations")
        self.verticalLayout_2.addWidget(self.btn_customerInformations)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect button clicks to corresponding methods for customer information
        self.btn_customerInformations.clicked.connect(self.showCustomerInfo)
        self.btn_newBankAccount.clicked.connect(self.CreateBankAccount)
        self.btn_deleteBankAccount.clicked.connect(self.deleteBankAccount)
        self.btn_updateBankAccount.clicked.connect(self.updateBankAccount)

        # Connect button clicks to methods for loading lists
        self.btn_loadAccounts.clicked.connect(self.getAccountList)
        self.btn_loadCustomers.clicked.connect(self.getCustomerList)
        self.btn_loadCustomers.clicked.connect(self.getCustomerAccountList)

        # Connect button clicks to methods for financial transactions
        self.btn_withDrawMoney.clicked.connect(self.withdrawMoney)
        self.btn_DepositMoney.clicked.connect(self.depositMoney)

        # Connect button clicks to methods for account management
        self.btn_changeAccount.clicked.connect(self.changeAccount)
        self.btn_moneyTransfer.clicked.connect(self.transferMoney)

        # Connect button clicks to methods for credit card operations
        self.btn_newCreditCard.clicked.connect(self.newCreditCard)
        self.btn_useCard.clicked.connect(self.useCreditCard)
        self.btn_loadCards.clicked.connect(self.getCreditCardNumbers)
        self.btn_payCreditCardDept.clicked.connect(self.payCreditCard)
        self.btn_showCreditCardDept.clicked.connect(self.showCardDebt)

        # Connect button clicks to methods for loan operations
        self.btn_newCredit.clicked.connect(self.takeCredit)
        self.btn_payCreditLoan.clicked.connect(self.payCreditLoan)
        self.btn_loadCredits.clicked.connect(self.getLoanNumbers)
        self.btn_showLoan.clicked.connect(self.showLoanDetails)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bank System"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Account Details"))
        self.label_5.setText(_translate("MainWindow", "Last Activity:"))
        self.label_6.setText(_translate("MainWindow", "Opening Date:"))
        self.label_7.setText(_translate("MainWindow", "Name Surname:"))
        self.label_8.setText(_translate("MainWindow", "Customer Number:"))
        self.label_9.setText(_translate("MainWindow", "Account Name:"))
        self.label_10.setText(_translate("MainWindow", "Balance:"))
        self.label_11.setText(_translate("MainWindow", "Account Number:"))
        self.label_12.setText(_translate("MainWindow", "Currency:"))
        self.btn_changeAccount.setText(_translate("MainWindow", "Account Details"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Account"))
        self.label_13.setText(_translate("MainWindow", "Account Name:"))
        self.label_14.setText(_translate("MainWindow", "Currency:"))
        self.currency_choice.setItemText(0, _translate("MainWindow", "USD"))
        self.currency_choice.setItemText(1, _translate("MainWindow", "CAD"))
        self.currency_choice.setItemText(2, _translate("MainWindow", "TRY"))
        self.currency_choice.setItemText(3, _translate("MainWindow", "EUR"))
        self.btn_newBankAccount.setText(_translate("MainWindow", "New Bank Account"))
        self.btn_deleteBankAccount.setText(_translate("MainWindow", "Delete Bank Account"))
        self.btn_updateBankAccount.setText(_translate("MainWindow", "Update Bank Account"))
        self.chckBox_mainAccount.setText(_translate("MainWindow", "Main Account"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Money Transactions"))
        self.btn_loadAccounts.setText(_translate("MainWindow", "Load Accounts and Customers"))
        self.label_16.setText(_translate("MainWindow", "Account:"))
        self.label_15.setText(_translate("MainWindow", "Amount:"))
        self.btn_withDrawMoney.setText(_translate("MainWindow", "Withdraw Money"))
        self.btn_DepositMoney.setText(_translate("MainWindow", "Deposit Money"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Transfer"))
        self.label_18.setText(_translate("MainWindow", "Customer:"))
        self.label_17.setText(_translate("MainWindow", "Account:"))
        self.label_3.setText(_translate("MainWindow", "Amount:"))
        self.btn_loadCustomers.setText(_translate("MainWindow", "Load Customers"))
        self.btn_moneyTransfer.setText(_translate("MainWindow", "Money Transfer"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Credit Card"))
        self.btn_newCreditCard.setText(_translate("MainWindow", "New Credit Card"))
        self.btn_useCard.setText(_translate("MainWindow", "Use Card"))
        self.btn_payCreditCardDept.setText(_translate("MainWindow", "Pay Card Dept"))
        self.btn_showCreditCardDept.setText(_translate("MainWindow", "Show Card Debt"))
        self.label_19.setText(_translate("MainWindow", "Card Limit:"))
        self.label_20.setText(_translate("MainWindow", "Spend Money:"))
        self.label_21.setText(_translate("MainWindow", "Pay Debt:"))
        self.label_24.setText(_translate("MainWindow", "Card Number:"))
        self.btn_loadCards.setText(_translate("MainWindow", "Load Card Numbers"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Credit"))
        self.btn_newCredit.setText(_translate("MainWindow", "Take Credit"))
        self.btn_payCreditLoan.setText(_translate("MainWindow", "Pay Loan"))
        self.btn_showLoan.setText(_translate("MainWindow", "Show Loan"))
        self.label_22.setText(_translate("MainWindow", "Credit Amount:"))
        self.label_23.setText(_translate("MainWindow", "Pay Loan:"))
        self.label_4.setText(_translate("MainWindow", "Credit Number:"))
        self.btn_loadCredits.setText(_translate("MainWindow", "Load Credit Numbers"))
        self.groupBox_4.setTitle(_translate("MainWindow", "User"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.label_2.setText(_translate("MainWindow", "E-mail:"))
        self.btn_customerInformations.setText(_translate("MainWindow", "Customer Informations"))

    def showCustomerInfo(self):
        """
        Retrieve and display the customer information associated with the current customer ID.
        
        This method retrieves the current customer ID using the getCustomerID method,
        fetches the customer data from the Customers table in the database based on the retrieved customer ID,
        and displays the customer information in a new form.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Retrieve the current customer ID
            customer_id = self.getCustomerID()
            
            # Execute the SQL query to fetch the customer data based on the retrieved customer ID
            customer_data = self.cursor.execute('''
                SELECT * FROM Customers WHERE id = ?        
            ''', (customer_id,)).fetchone()

            # Check if customer data exists
            if customer_data:
                # Extract customer data into a list of tuples
                data = [
                    ("Name", f"{customer_data[1]}"),
                    ("Surname", f"{customer_data[2]}"),
                    ("Age", customer_data[3]),
                    ("Username", customer_data[4]),
                    ("Password", customer_data[5]),
                    ("Email", customer_data[6]),
                    ("Number of Accounts", customer_data[7]),
                    ("Join Date", customer_data[8]),
                    ("Number of Credit Cards", customer_data[9]),
                    ("Balance", f"{customer_data[10]} $"),
                    ("Debt", f"{customer_data[11]} $")
                ]

                # Create and show the CustomerInfo form
                self.customerInfoWindow = CustomerInfo.Ui_customerInfo(data)
                self.customerInfoWindow.show()
            else:
                # Display an error message if customer data is not found
                self.messageBox(QMessageBox.Warning, "Error", "Customer not found.")
                
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")


    def getCustomerID(self):
        """
        Retrieve the customer ID associated with the provided username from the database.
        
        This method retrieves the username entered by the user from the UI,
        executes an SQL query to retrieve the customer ID associated with the provided username,
        and returns the retrieved customer ID.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        int - The customer ID associated with the provided username.
        """
        
        try:
            # Retrieve the username entered by the user from the UI
            username = self.txt_username_User.text()
            
            # Execute the SQL query to retrieve the customer ID associated with the provided username
            customer_id = self.cursor.execute('''
                SELECT id FROM Customers WHERE username = ?
            ''', (username,)).fetchone()[0]
            
            # Return the retrieved customer ID
            return customer_id
        
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")
            return None

    def messageBox(self, icon, title, message):
        """
        Display a QMessageBox with the specified icon, title, and message.

        Parameters:
        - icon: QMessageBox.Icon (e.g., QMessageBox.Warning, QMessageBox.Information)
        - title: str - The title of the QMessageBox
        - message: str - The message to display in the QMessageBox
            
        Returns:
        None
        """
        
        try:
            # Create a QMessageBox instance
            msg_box = QMessageBox()
            
            # Set the icon, title, and message for the QMessageBox
            msg_box.setIcon(icon)
            msg_box.setWindowTitle(title)
            msg_box.setText(message)
            
            # Execute the QMessageBox
            msg_box.exec_()
            
        except Exception as e:
            # Display an error message for any unexpected exceptions
            print(f"An error occurred: {str(e)}")

    def CreateBankAccount(self):
        """
        Create a new bank account for the current customer.

        This method retrieves the account name, currency choice, and main account checkbox status from the UI,
        generates a random account number, sets the initial balance and opening date,
        retrieves the customer ID using the getCustomerID method,
        inserts the new account details into the Accounts table in the database,
        and displays a success or warning message based on the result of the account creation operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Retrieve account name, currency choice, and main account checkbox status from the UI
            account_name = self.txt_accountName_Account.text()
            
            if account_name:
                account_number = random.randint(10000000000, 999999999999)
                balance = 0.0
                currency = self.currency_choice.currentText()
                opening_date = datetime.now()
                last_activity = opening_date
                customer_id = self.getCustomerID()
                is_main = 1 if self.chckBox_mainAccount.isChecked() else 0

                # Pass values as a tuple
                values = (account_name, account_number, balance, currency, opening_date, last_activity, customer_id, is_main)

                # Execute the SQL query to insert the new account details into the Accounts table
                self.cursor.execute('''
                        INSERT INTO Accounts (account_name, account_number, balance, currency, opening_date, last_activity, customer_id, is_main)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', values)
                
                # Commit the changes to the database
                self.connect.commit()
                
                # Clear the account name field in the UI
                self.txt_accountName_Account.setText("")

                # Display a success message
                self.messageBox(QMessageBox.Information, "Success", "Account created successfully.")
            else:
                # Display a warning message for invalid account name
                self.messageBox(QMessageBox.Warning, "Warning", "Invalid account name.")
                
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")
    
    def getAccountID(self):
        """
        Retrieve the account ID associated with the current customer from the database.
        
        This method retrieves the customer ID using the getCustomerID method,
        executes an SQL query to retrieve the account ID associated with the retrieved customer ID,
        and returns the retrieved account ID.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        int - The account ID associated with the current customer.
        """
        
        try:
            # Retrieve the customer ID using the getCustomerID method
            customer_id = self.getCustomerID()
            
            # Execute the SQL query to retrieve the account ID associated with the retrieved customer ID
            account_id = self.cursor.execute('''
                    SELECT id FROM Accounts WHERE customer_id = ?
            ''', (customer_id,)).fetchone()
            
            # Return the retrieved account ID if found, otherwise return None
            return account_id[0] if account_id else None
        
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")
            return None

    def getAccountName(self, account_id):
        """
        Retrieve the account name associated with the provided account ID from the database.
        
        This method executes an SQL query to retrieve the account name associated with the provided account ID,
        and returns the retrieved account name or "No Account Yet" if the account does not exist.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
        - account_id: int - The ID of the account for which the account name is to be retrieved.
            
        Returns:
        str - The account name associated with the provided account ID, or "No Account Yet" if the account does not exist.
        """
        
        try:
            # Execute the SQL query to retrieve the account name associated with the provided account ID
            account_name = self.cursor.execute('''
                SELECT account_name FROM Accounts WHERE id = ?
            ''', (account_id,)).fetchone()
            
            # Return the retrieved account name if found, otherwise return "No Account Yet"
            return account_name[0] if account_name else "No Account Yet"
        
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")
            return "No Account Yet"

    def deleteBankAccount(self):
        """
        Delete a bank account associated with the current customer.

        This method retrieves the customer ID and account name from the UI,
        checks if the provided account name exists for the current customer in the Accounts table,
        deletes the account from the Accounts table if it exists,
        and displays a success or warning message based on the result of the account deletion operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Retrieve customer ID and account name from the UI
            customer_id = self.getCustomerID()
            account_name = self.txt_accountName_Account.text()

            # Check if the provided account name exists for the current customer in the Accounts table
            does_Exist = self.cursor.execute('SELECT account_name FROM Accounts WHERE account_name = ? AND customer_id = ?', (account_name, customer_id)).fetchone()

            if does_Exist:
                # Execute the SQL query to delete the account from the Accounts table
                self.cursor.execute('DELETE FROM Accounts WHERE customer_id = ? AND account_name = ?', (customer_id, account_name))
                
                # Commit the changes to the database
                self.connect.commit()
                
                # Display a success message
                self.messageBox(QMessageBox.Information, "Success", "Account deleted successfully.")
            else:
                # Display a warning message if the account does not exist
                self.messageBox(QMessageBox.Warning, "Warning", "Account doesn't exist.")
            
            # Clear the account name field in the UI
            self.txt_accountName_Account.setText("")
            
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def updateBankAccount(self):
        """
        Update the details of a bank account associated with the current customer.

        This method retrieves the customer ID, account name, currency choice, and main account checkbox status from the UI,
        checks if the provided account name exists for the current customer in the Accounts table,
        updates the currency and is_main fields of the account in the Accounts table if it exists,
        and displays a success or warning message based on the result of the account update operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Retrieve customer ID, account name, currency choice, and main account checkbox status from the UI
            customer_id = self.getCustomerID()
            account_name = self.txt_accountName_Account.text()
            currency = self.currency_choice.currentText()
            is_main = 1 if self.chckBox_mainAccount.isChecked() else 0

            # Check if the provided account name exists for the current customer in the Accounts table
            does_Exist = self.cursor.execute('SELECT account_name FROM Accounts WHERE account_name = ? AND customer_id = ?', (account_name, customer_id)).fetchone()
            
            if does_Exist:
                # Execute the SQL query to update the currency and is_main fields of the account in the Accounts table
                self.cursor.execute('''
                    UPDATE Accounts 
                    SET currency = ?, is_main = ? 
                    WHERE customer_id = ? AND account_name = ?
                ''', (currency, is_main, customer_id, account_name))
                
                # Commit the changes to the database
                self.connect.commit()
                
                # Display a success message
                self.messageBox(QMessageBox.Information, "Success", "Account updated successfully.")
            else:
                # Display a warning message if the account does not exist
                self.messageBox(QMessageBox.Warning, "Warning", "Account doesn't exist.")
                
            # Clear the account name field in the UI
            self.txt_accountName_Account.setText("")
            
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def getAccountList(self):
        """
        Retrieve and populate the combo box with the account names associated with the current customer.

        This method retrieves the customer ID using the getCustomerID method,
        executes an SQL query to fetch the account names associated with the retrieved customer ID,
        extracts the account names from the fetched rows,
        and populates the combo box with the account names.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Clear the existing items in the combo box
            self.account_choice_Money.clear()
            
            # Retrieve customer ID using the getCustomerID method
            customer_id = self.getCustomerID()
            
            # Execute the SQL query to fetch the account names associated with the retrieved customer ID
            account_names = self.cursor.execute('SELECT account_name FROM Accounts WHERE customer_id = ?', (customer_id,)).fetchall()

            # Extract account names from the fetched rows
            account_names_list = [row[0] for row in account_names]

            # Populate the combo box with the account names
            self.account_choice_Money.addItems(account_names_list)
            
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def depositMoney(self):
        """
        Deposit money into a selected bank account associated with the current customer.

        This method retrieves the selected account name, deposit amount, and customer ID from the UI,
        validates the deposit amount,
        updates the account balance and total balance of the customer in the database,
        and displays a success or warning message based on the result of the deposit operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Retrieve selected account name, deposit amount, and customer ID from the UI
            account_name = self.account_choice_Money.currentText()
            amount = float(self.txt_amount_Money.text())
            customer_id = self.getCustomerID()

            # Retrieve current account balance
            balance = self.cursor.execute('SELECT balance FROM Accounts WHERE customer_id = ? AND account_name = ?', (customer_id, account_name)).fetchone()

            # Validate deposit amount
            if amount <= 0:
                self.messageBox(QMessageBox.Warning, "Warning", "Amount can't be less than zero.")
                return

            # Calculate new account balance
            new_balance = balance[0] + amount

            # Update account balance
            self.cursor.execute('UPDATE Accounts SET balance = ? WHERE customer_id = ? AND account_name = ?', (new_balance, customer_id, account_name))

            # Update total balance of the customer
            current_total_balance = self.cursor.execute('SELECT balance FROM Customers WHERE id = ?', (customer_id,)).fetchone()[0]
            new_total_balance = current_total_balance + amount
            self.cursor.execute('UPDATE Customers SET balance = ? WHERE id = ?', (new_total_balance, customer_id))

            # Commit the changes to the database
            self.connect.commit()

            # Display a success message
            self.messageBox(QMessageBox.Information, "Success", f"New balance: {new_balance}")
            
            # Clear the deposit amount field in the UI
            self.txt_amount_Money.setText("")

        except ValueError:
            # Display an error message for invalid amount format
            self.messageBox(QMessageBox.Warning, "Warning", "Please enter a valid amount.")
            
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def withdrawMoney(self):
        """
        Withdraw money from a selected bank account associated with the current customer.

        This method retrieves the selected account name, withdrawal amount, and customer ID from the UI,
        validates the withdrawal amount,
        updates the account balance and total balance of the customer in the database,
        and displays a success or warning message based on the result of the withdrawal operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Retrieve selected account name, withdrawal amount, and customer ID from the UI
            account_name = self.account_choice_Money.currentText()
            amount = float(self.txt_amount_Money.text())
            customer_id = self.getCustomerID()

            # Retrieve current account balance
            balance = self.cursor.execute('SELECT balance FROM Accounts WHERE customer_id = ? AND account_name = ?', (customer_id, account_name)).fetchone()

            # Validate withdrawal amount
            if amount <= 0:
                self.messageBox(QMessageBox.Warning, "Warning", "Amount can't be less than zero.")
                return

            if amount > balance[0]:
                self.messageBox(QMessageBox.Warning, "Warning", "Amount can't be more than balance.")
                return

            # Calculate new account balance
            new_balance = balance[0] - amount

            # Update total balance of the customer
            current_total_balance = self.cursor.execute('SELECT balance FROM Customers WHERE id = ?', (customer_id,)).fetchone()[0]
            new_total_balance = current_total_balance - amount
            self.cursor.execute('UPDATE Customers SET balance = ? WHERE id = ?', (new_total_balance, customer_id))

            # Update account balance
            self.cursor.execute('UPDATE Accounts SET balance = ? WHERE customer_id = ? AND account_name = ?', (new_balance, customer_id, account_name))

            # Commit the changes to the database
            self.connect.commit()

            # Display a success message
            self.messageBox(QMessageBox.Information, "Success", f"Here is your money. New balance: {new_balance}")
            
            # Clear the withdrawal amount field in the UI
            self.txt_amount_Money.setText("")

        except ValueError:
            # Display an error message for invalid amount format
            self.messageBox(QMessageBox.Warning, "Warning", "Please enter a valid amount.")
            
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def getCustomerList(self):
        """
        Retrieve and populate the combo box with the usernames of all customers.

        This method executes an SQL query to fetch the usernames of all customers,
        extracts the usernames from the fetched rows,
        and populates the combo box with the usernames.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Clear the existing items in the combo box
            self.customer_choice_Transfer.clear()

            # Execute the SQL query to fetch the usernames of all customers
            customer_names = self.cursor.execute('SELECT username FROM Customers').fetchall()

            # Extract usernames from the fetched rows
            customer_names_list = [row[0] for row in customer_names]

            # Populate the combo box with the usernames
            self.customer_choice_Transfer.addItems(customer_names_list)

        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def getCustomerAccountList(self):
        """
        Retrieve and populate the combo box with the account names associated with the chosen customer.

        This method retrieves the chosen customer's username and ID from the UI,
        executes an SQL query to fetch the account names associated with the chosen customer,
        extracts the account names from the fetched rows,
        and populates the combo box with the account names.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Clear the existing items in the combo box
            self.account_chose_transfer.clear()

            # Retrieve the chosen customer's username and ID from the UI
            customer_username = self.customer_choice_Transfer.currentText()
            customer_id = self.getChosenCustomerID(customer_username)

            # Execute the SQL query to fetch the account names associated with the chosen customer
            account_names = self.cursor.execute('SELECT account_name FROM Accounts WHERE customer_id = ?', (customer_id,)).fetchall()

            # Extract account names from the fetched rows
            account_names_list = [row[0] for row in account_names]

            # Populate the combo box with the account names
            self.account_chose_transfer.addItems(account_names_list)

        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def transferMoney(self):
        """
        Transfer money from one account to another.

        This method retrieves the sender's customer ID and transfer details from the UI,
        checks if the sending account has sufficient balance,
        deducts the transfer amount from the sending account,
        adds the transfer amount to the receiving account,
        and updates the balances and total balances of the sender and receiver in the database.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Retrieve sender's customer ID
            sender_customer_id = self.getCustomerID()

            # Retrieve transfer details from the UI
            amount = float(self.txt_amount_Transfer.text())
            receiver_customer = self.customer_choice_Transfer.currentText()
            receiver_account = self.account_chose_transfer.currentText()
            sender_account = self.account_choice_Money.currentText()

            # Check if the sending account has sufficient balance
            sender_balance = self.cursor.execute('SELECT balance FROM Accounts WHERE customer_id = ? AND account_name = ?', (sender_customer_id, sender_account)).fetchone()

            if not sender_balance:
                self.messageBox(QMessageBox.Warning, "Warning", "Sending account not found.")
                return

            if amount <= 0:
                self.messageBox(QMessageBox.Warning, "Warning", "Transfer amount must be greater than zero.")
                return

            if amount > sender_balance[0]:
                self.messageBox(QMessageBox.Warning, "Warning", "Insufficient balance.")
                return

            # Deduct the transfer amount from the sending account
            new_sender_balance = sender_balance[0] - amount
            self.cursor.execute('UPDATE Accounts SET balance = ? WHERE customer_id = ? AND account_name = ?', (new_sender_balance, sender_customer_id, sender_account))

            # Fetch the current total balance of the sender
            current_sender_total_balance = self.cursor.execute('SELECT balance FROM Customers WHERE id = ?', (sender_customer_id,)).fetchone()[0]
            new_sender_total_balance = current_sender_total_balance - amount

            # Update the total balance of the sender
            self.cursor.execute('UPDATE Customers SET balance = ? WHERE id = ?', (new_sender_total_balance, sender_customer_id))

            # Add the transfer amount to the receiving account
            receiver_customer_id = self.cursor.execute('SELECT id FROM Customers WHERE username = ?', (receiver_customer,)).fetchone()[0]
            receiver_balance = self.cursor.execute('SELECT balance FROM Accounts WHERE customer_id = ? AND account_name = ?', (receiver_customer_id, receiver_account)).fetchone()

            if not receiver_balance:
                self.messageBox(QMessageBox.Warning, "Warning", "Receiving account not found.")
                return

            new_receiver_balance = receiver_balance[0] + amount
            self.cursor.execute('UPDATE Accounts SET balance = ? WHERE customer_id = ? AND account_name = ?', (new_receiver_balance, receiver_customer_id, receiver_account))

            # Fetch the current total balance of the receiver
            current_receiver_total_balance = self.cursor.execute('SELECT balance FROM Customers WHERE id = ?', (receiver_customer_id,)).fetchone()[0]
            new_receiver_total_balance = current_receiver_total_balance + amount

            # Update the total balance of the receiver
            self.cursor.execute('UPDATE Customers SET balance = ? WHERE id = ?', (new_receiver_total_balance, receiver_customer_id))

            # Commit the changes to the database
            self.connect.commit()

            # Display a success message
            self.messageBox(QMessageBox.Information, "Success", f"Transfer successful. New balance: {new_sender_balance}")

            # Clear the transfer amount field in the UI
            self.txt_amount_Transfer.setText("")

        except ValueError:
            # Display an error message for invalid amount format
            self.messageBox(QMessageBox.Warning, "Warning", "Please enter a valid amount.")

        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def getChosenCustomerID(self, username):
        """
        Retrieve the customer ID based on the provided username.

        This method executes an SQL query to fetch the customer ID associated with the provided username.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
        - username: str - The username of the customer
            
        Returns:
        int: The customer ID associated with the provided username
        """
        
        try:
            # Execute the SQL query to fetch the customer ID based on the provided username
            customer_id = self.cursor.execute('SELECT id FROM Customers WHERE username = ?', (username,)).fetchone()[0]
            return customer_id

        except TypeError:
            # Display an error message if the customer is not found
            self.messageBox(QMessageBox.Warning, "Warning", "Customer not found.")
            return None

        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")
            return None

    def changeAccount(self):
        """
        Populate the UI fields with account details based on the selected account name.

        This method retrieves the account and customer details associated with the selected account name,
        and populates the corresponding UI fields with the fetched details.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
                
        Returns:
        None
        """
        
        try:
            # Retrieve the selected account name from the UI
            selected_account_name = self.account_choice_Money.currentText()

            # Retrieve the customer ID associated with the current user
            customer_id = self.getCustomerID()

            # Fetch account data based on the selected account name
            account_data = self.cursor.execute('SELECT * FROM Accounts WHERE customer_id = ? AND account_name = ?', (customer_id, selected_account_name)).fetchone()
            
            # Fetch customer data
            customer_data = self.cursor.execute('SELECT * FROM Customers WHERE id = ?', (customer_id,)).fetchone()

            if account_data and customer_data:
                # Extract and display account and customer details in the UI
                name = customer_data[1]
                surname = customer_data[2]

                last_activity = account_data[6]
                opening_date = account_data[5]
                currency = account_data[4]
                balance = account_data[3]
                account_number = account_data[2]

                self.txt_lastActivity.setText(str(last_activity))  # Assuming last_activity is a datetime object
                self.tct_openingDate.setText(str(opening_date))    # Assuming opening_date is a datetime object
                self.txt_nameSurname.setText(f"{name} {surname}")
                self.txt_customerNumber.setText(str(customer_id))
                self.txt_accountName.setText(selected_account_name)
                self.txt_currency.setText(currency)
                self.txt_balance.setText(str(balance))
                self.txt_accountNumber.setText(str(account_number))
            else:
                # Handle the case where no matching account or customer is found
                self.messageBox(QMessageBox.Warning, "Warning", "No account found for the customer and selected account name.")

        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def newCreditCard(self):
        """
        Creates a new credit card for the customer and updates the database with the new credit card details.

        This method retrieves the card limit entered by the user from the UI,
        validates the provided card limit,
        generates a new credit card number and sets the initial card balance and debt,
        inserts the new credit card details into the database,
        updates the credit card quantity for the customer in the database,
        and displays an appropriate message based on the result of the credit card creation operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
                
        Returns:
        None
        """
        
        try:
            # Retrieve the card limit entered by the user from the UI
            card_limit_str = self.txt_cardLimit_CreditCard.text()

            # Convert the card limit to an integer
            card_limit = int(card_limit_str)

            # Validate the provided card limit
            if card_limit <= 0:
                self.messageBox(QMessageBox.Warning, "Warning", "Card limit must be greater than zero.")
                return

            # Generate a new credit card number
            card_number = random.randint(100000000000, 999999999999)
            
            # Set initial card balance and debt
            card_balance = card_limit
            card_debt = 0.0
            
            # Get the customer ID associated with the current user
            customer_id = self.getCustomerID()

            # Insert the new credit card details into the database
            self.cursor.execute('''
                INSERT INTO CreditCards (card_number, card_limit, card_balance, card_debt, card_last_use, customer_id)
                VALUES(?,?,?,?,?,?)
            ''', (card_number, card_limit, card_balance, card_debt, datetime.now(), customer_id))

            # Update the credit card quantity for the customer in the database
            credit_card_quantity = self.cursor.execute('SELECT card_quantity FROM Customers WHERE id = ?', (customer_id,)).fetchone()[0]
            new_quantity = credit_card_quantity + 1
            self.cursor.execute('UPDATE Customers SET card_quantity = ? WHERE id = ?', (new_quantity, customer_id))

            # Commit the changes to the database
            self.connect.commit()

            # Display a success message
            self.messageBox(QMessageBox.Information, "Success", f"New credit card accepted. Card Limit: {card_limit}")

            # Clear the card limit field in the UI
            self.txt_cardLimit_CreditCard.setText("")

        except ValueError:
            # Display a warning message for invalid card limit input
            self.messageBox(QMessageBox.Warning, "Warning", "Invalid card limit. Please enter a valid number.")
        
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Warning, "Error", f"An error occurred: {str(e)}")

    def useCreditCard(self):
        """
        Processes a transaction using the selected credit card, updates the credit card balance and debt,
        and updates the user's total debt in the database.

        This method retrieves the transaction amount and credit card details entered by the user from the UI,
        validates the provided amount and credit card details,
        fetches the credit card details from the database,
        updates the credit card balance and debt,
        updates the user's total debt,
        and displays an appropriate message based on the result of the transaction.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
                
        Returns:
        None
        """
        
        try:
            # Retrieve the transaction amount entered by the user from the UI
            amount_str = self.txt_spendMoney_CreditCard.text()

            # Convert the transaction amount to a float
            amount = float(amount_str)

            # Validate the provided amount
            if amount <= 0:
                self.messageBox(QMessageBox.Warning, "Warning", "Amount must be greater than zero.")
                return

            # Retrieve the selected credit card number and the current username from the UI
            card_number = self.cardNumber_chose.currentText()
            username = self.txt_username_User.text()

            # Get the customer ID associated with the current user
            customer_id = self.getCustomerID()

            # Fetch the credit card details from the database
            card_data = self.cursor.execute('SELECT * FROM CreditCards WHERE card_number = ? AND customer_id = ?', (card_number, customer_id)).fetchone()

            if not card_data:
                # Display a warning message if the credit card is not found
                self.messageBox(QMessageBox.Warning, "Warning", "Credit card not found.")
                return

            # Extract the current card balance and debt from the fetched credit card data
            card_balance = card_data[3]
            card_debt = card_data[4]

            # Validate if the amount is greater than the available card balance
            if amount > card_balance:
                self.messageBox(QMessageBox.Warning, "Warning", "Insufficient funds.")
                return

            # Calculate the new card balance and debt after the transaction
            new_card_balance = card_balance - amount
            new_card_debt = card_debt + amount

            # Update the user's total debt in the database
            actual_debt = self.cursor.execute('SELECT debt FROM Customers WHERE username = ?', (username,)).fetchone()[0]
            new_total_debt = actual_debt + new_card_debt
            self.cursor.execute('UPDATE Customers SET debt = ? WHERE username = ?', (new_total_debt, username))

            # Update the credit card balance and debt in the database
            self.cursor.execute('UPDATE CreditCards SET card_balance = ?, card_debt = ? WHERE card_number = ? AND customer_id = ?', 
                                (new_card_balance, new_card_debt, card_number, customer_id))

            # Commit the changes to the database
            self.connect.commit()

            # Display a success message
            self.messageBox(QMessageBox.Information, "Success", f"Transaction successful. New card balance: {new_card_balance}")

            # Clear the transaction amount field in the UI
            self.txt_spendMoney_CreditCard.setText("")

        except ValueError:
            # Display a warning message for invalid amount input
            self.messageBox(QMessageBox.Warning, "Warning", "Invalid amount. Please enter a valid number.")
        
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Warning, "Error", f"An error occurred: {str(e)}")

    def getCreditCardNumbers(self):
        """
        Retrieves and populates the credit card numbers associated with the current customer in the database.

        This method fetches the credit card numbers associated with the current customer,
        extracts the credit card numbers from the fetched data,
        populates the combo box with the credit card numbers,
        and handles any exceptions that may occur during the database operations.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
                
        Returns:
        None
        """

        try:
            # Clear the existing items in the combo box
            self.cardNumber_chose.clear()

            # Retrieve the customer ID associated with the current user
            customer_id = self.getCustomerID()

            # Fetch the credit card numbers associated with the current customer from the database
            cardNumbers = self.cursor.execute('SELECT card_number FROM CreditCards WHERE customer_id = ?', (customer_id,)).fetchall()

            # Extract credit card numbers from the fetched rows
            card_number_list = [str(row[0]) for row in cardNumbers]

            # Populate the combo box with the credit card numbers
            self.cardNumber_chose.addItems(card_number_list)

        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Warning, "Error", f"An error occurred: {str(e)}")

    def payCreditCard(self):
        """
        Handles the payment of credit card debt by updating the credit card balance and customer's total debt in the database.

        This method retrieves the payment amount entered by the user,
        validates the payment amount and credit card details,
        calculates the new credit card balance and debt,
        updates the credit card balance and customer's total debt in the database,
        and handles any exceptions that may occur during the database operations.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
                
        Returns:
        None
        """

        amount_str = self.txt_payDebt_CreditCard.text()

        try:
            # Convert the payment amount to float
            amount = float(amount_str)

            # Validate the payment amount
            if amount <= 0:
                self.messageBox(QMessageBox.Warning, "Warning", "Amount must be greater than zero.")
                return

            # Retrieve the selected credit card number and customer ID
            card_number = self.cardNumber_chose.currentText()
            customer_id = self.getCustomerID()

            # Fetch the credit card details based on the credit card number and customer ID
            card_data = self.cursor.execute('SELECT * FROM CreditCards WHERE card_number = ? AND customer_id = ?', (card_number, customer_id)).fetchone()

            # Validate if the credit card exists
            if not card_data:
                self.messageBox(QMessageBox.Warning, "Warning", "Credit card not found.")
                return

            # Extract relevant credit card details
            card_balance = card_data[3]
            card_debt = card_data[4]
            card_limit = card_data[2]  # Assuming card_limit is at index 2 in the card_data tuple

            # Validate if the payment amount exceeds the total debt
            if amount > card_debt:
                self.messageBox(QMessageBox.Warning, "Warning", "Payment amount exceeds total debt.")
                return

            # Calculate new card balance and debt
            new_card_balance = card_balance + amount
            new_card_debt = card_debt - amount

            # Validate if new card balance exceeds card limit
            if new_card_balance > card_limit:
                self.messageBox(QMessageBox.Warning, "Warning", "Total card balance exceeds card limit.")
                return

            # Update the credit card balance and debt in the database
            self.cursor.execute('UPDATE CreditCards SET card_balance = ?, card_debt = ? WHERE card_number = ? AND customer_id = ?', 
                                (new_card_balance, new_card_debt, card_number, customer_id))

            # Update the total debt of the customer in the database
            username = self.cursor.execute('SELECT username FROM Customers WHERE id = ?', (customer_id,)).fetchone()[0]
            actual_debt = self.cursor.execute('SELECT debt FROM Customers WHERE username = ?', (username,)).fetchone()[0]
            new_total_debt = actual_debt - amount
            self.cursor.execute('UPDATE Customers SET debt = ? WHERE username = ?', (new_total_debt, username))

            # Commit the changes to the database
            self.connect.commit()

            # Display a success message to the user
            self.messageBox(QMessageBox.Information, "Success", f"Payment successful. New card balance: {new_card_balance}")

            # Clear the payment amount text field
            self.txt_payDebt_CreditCard.setText("")
        except ValueError:
            # Handle invalid payment amount input
            self.messageBox(QMessageBox.Warning, "Warning", "Invalid amount. Please enter a valid number.")
        except Exception as e:
            # Handle any unexpected exceptions
            self.messageBox(QMessageBox.Warning, "Error", f"An error occurred: {str(e)}")

    def showCardDebt(self):
        """
        Retrieve and display the details of a selected credit card, including its balance, debt, and limit.

        This method fetches the selected credit card's details based on the card number and customer ID,
        and then displays the card details in a message box.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
                
        Returns:
        None
        """
        try:
            # Retrieve the selected card number and customer ID
            card_number = self.cardNumber_chose.currentText()  # Assuming you have a text field to input the card number
            customer_id = self.getCustomerID()

            # Fetch the credit card details
            card_data = self.cursor.execute('SELECT * FROM CreditCards WHERE card_number = ? AND customer_id = ?', (card_number, customer_id)).fetchone()

            # Check if the card exists
            if not card_data:
                self.messageBox(QMessageBox.Warning, "Warning", "Credit card not found.")
                return

            # Extract card details
            card_balance = card_data[3]
            card_debt = card_data[4]
            card_limit = card_data[2]  # Assuming card_limit is at index 2 in the card_data tuple

            # Construct the message to display
            message = (
                f"Card Number: {card_number}\n"
                f"Card Balance: {card_balance}\n"
                f"Card Debt: {card_debt}\n"
                f"Card Limit: {card_limit}"
            )
            
            # Display the credit card details in a message box
            self.messageBox(QMessageBox.Information, "Credit Card Details", message)

        except Exception as e:
            # Handle any exceptions that occur during the process
            self.messageBox(QMessageBox.Warning, "Error", f"An error occurred: {str(e)}")

    def takeCredit(self):
        """
        Process a credit request from the user, updating their balance, debt, and loan records accordingly.

        This method validates the credit amount provided by the user, generates a new loan number,
        and updates the user's balance, debt, and loan details in the database. It also updates the
        main account balance with the new credit amount.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.

        Returns:
        None
        """
        credit_amount_str = self.txt_CreditAmount_Credit.text()
        
        try:
            # Convert credit amount to integer
            credit_amount = int(credit_amount_str)

            # Check if credit amount is valid
            if credit_amount <= 0: 
                self.messageBox(QMessageBox.Warning, "Warning", "Credit amount must be greater than zero.")
                return

            # Generate a new loan number
            loan_number = random.randint(100000000000, 999999999999)
            
            # Set loan details
            loan_limit = credit_amount
            loan_debt = credit_amount
            loan_take_date = datetime.now()
            customer_id = self.getCustomerID()

            # Update user's balance and debt
            current_balance = self.cursor.execute('SELECT balance FROM Customers WHERE id = ?', (customer_id,)).fetchone()[0]
            current_debt = self.cursor.execute('SELECT debt FROM Customers WHERE id = ?', (customer_id,)).fetchone()[0]

            new_balance = current_balance + credit_amount
            new_debt = current_debt + credit_amount

            # Update the customer's balance and debt in the database
            self.cursor.execute('UPDATE Customers SET balance = ?, debt = ? WHERE id = ?', (new_balance, new_debt, customer_id))

            # Insert the new credit into the Loans table
            self.cursor.execute('INSERT INTO Loans (loan_number, loan_limit, loan_take_date, loan_debt, customer_id) VALUES(?,?,?,?,?)',
                                (loan_number, loan_limit, loan_take_date, loan_debt, customer_id))

            # Update the main account balance with the new credit amount
            current_mainAccount_balance = self.cursor.execute('SELECT balance FROM Accounts WHERE id = ?', (customer_id,)).fetchone()[0]
            new_mainAccount_balance = current_mainAccount_balance + credit_amount
            mainAccount_name = "Main Account"

            self.cursor.execute('UPDATE Accounts SET balance = ? WHERE customer_id = ? AND account_name = ?',
                                (new_mainAccount_balance, customer_id, mainAccount_name))

            # Commit the changes to the database
            self.connect.commit()

            # Display success message
            self.messageBox(QMessageBox.Information, "Success", f"New credit accepted. Credit Amount: {credit_amount}")

            # Clear the credit amount input field
            self.txt_CreditAmount_Credit.setText("")

        except ValueError:
            # Handle invalid credit amount input
            self.messageBox(QMessageBox.Warning, "Warning", "Invalid credit amount. Please enter a valid number.")

        except Exception as e:
            # Handle other exceptions
            self.messageBox(QMessageBox.Warning, "Error", f"An error occurred: {str(e)}")

    def payCreditLoan(self):
        """
        Process a loan payment from the user, updating their loan debt and total debt accordingly.

        This method validates the payment amount provided by the user, fetches the loan details,
        and updates the loan debt in the Loans table and the total debt of the customer in the
        Customers table. It also updates the main account balance with the payment amount.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.

        Returns:
        None
        """
        payment_amount_str = self.txt_payLoan_Credit.text()

        try:
            # Convert payment amount to integer
            payment_amount = int(payment_amount_str)

            # Check if payment amount is valid
            if payment_amount <= 0:
                self.messageBox(QMessageBox.Warning, "Warning", "Payment amount must be greater than zero.")
                return

            # Get the selected loan number and customer ID
            loan_number = self.creditNumber_chose.currentText()
            customer_id = self.getCustomerID()

            # Fetch the loan details
            loan_data = self.cursor.execute('SELECT * FROM Loans WHERE loan_number = ? AND customer_id = ?', (loan_number, customer_id)).fetchone()

            # Check if loan data exists
            if not loan_data:
                self.messageBox(QMessageBox.Warning, "Warning", "Loan not found.")
                return

            # Extract the current loan debt
            loan_debt = loan_data[4]

            # Check if payment amount exceeds loan debt
            if payment_amount > loan_debt:
                self.messageBox(QMessageBox.Warning, "Warning", "Payment amount exceeds total loan debt.")
                return

            # Calculate the new loan debt
            new_loan_debt = loan_debt - payment_amount

            # Update the loan debt in Loans table
            self.cursor.execute('UPDATE Loans SET loan_debt = ? WHERE loan_number = ? AND customer_id = ?', 
                                (new_loan_debt, loan_number, customer_id))

            # Update total debt of the customer
            current_total_debt = self.cursor.execute('SELECT debt FROM Customers WHERE id = ?', (customer_id,)).fetchone()[0]
            
            # Check if payment amount exceeds total debt
            if payment_amount > current_total_debt:
                self.messageBox(QMessageBox.Warning, "Warning", "Payment amount exceeds total debt.")
                return
            
            # Calculate new total debt
            new_total_debt = current_total_debt - payment_amount

            # Update the total debt in Customers table
            self.cursor.execute('UPDATE Customers SET debt = ? WHERE id = ?', (new_total_debt, customer_id))

            # Update main account balance
            current_mainAccount_balance = self.cursor.execute('SELECT balance FROM Accounts WHERE id = ?', (customer_id,)).fetchone()[0]
            new_mainAccount_balance = current_mainAccount_balance - payment_amount
            mainAccount_name = "Main Account"

            self.cursor.execute('UPDATE Accounts SET balance = ? WHERE customer_id = ? AND account_name = ?',
                                (new_mainAccount_balance, customer_id, mainAccount_name))

            # Commit the changes to the database
            self.connect.commit()

            # Display success message
            self.messageBox(QMessageBox.Information, "Success", f"Payment successful. New loan debt: {new_loan_debt}")

            # Clear the payment amount input field
            self.txt_payLoan_Credit.setText("")

        except ValueError:
            # Handle invalid payment amount input
            self.messageBox(QMessageBox.Warning, "Warning", "Invalid payment amount. Please enter a valid number.")

        except Exception as e:
            # Handle other exceptions
            self.messageBox(QMessageBox.Warning, "Error", f"An error occurred: {str(e)}")

    def getLoanNumbers(self):
        """
        Retrieve and populate the loan numbers associated with the current customer.

        This method fetches the loan numbers from the Loans table for the current customer
        and populates the creditNumber_chose combo box with these numbers.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.

        Returns:
        None
        """
        try:
            # Clear the combo box
            self.creditNumber_chose.clear()
            
            # Get the current customer's ID
            customer_id = self.getCustomerID()

            # Fetch loan numbers associated with the customer
            creditNumbers = self.cursor.execute('SELECT loan_number FROM Loans WHERE customer_id = ?', (customer_id,)).fetchall()

            # Extract loan numbers from the fetched rows
            credit_number_list = [str(row[0]) for row in creditNumbers]

            # Populate the combo box with the loan numbers
            self.creditNumber_chose.addItems(credit_number_list)

        except Exception as e:
            # Handle any exceptions and display a warning message
            self.messageBox(QMessageBox.Warning, "Error", f"An error occurred: {str(e)}")

    def showLoanDetails(self):
        """
        Display the details of the selected loan.

        This method fetches the loan details for the selected loan number and customer ID,
        and then displays these details in a message box.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.

        Returns:
        None
        """
        try:
            # Get the selected loan number from the combo box
            loan_number = self.creditNumber_chose.currentText()

            # Get the current customer's ID
            customer_id = self.getCustomerID()

            # Fetch the loan details from the Loans table
            loan_data = self.cursor.execute('SELECT * FROM Loans WHERE loan_number = ? AND customer_id = ?', (loan_number, customer_id)).fetchone()

            # Check if the loan data exists
            if not loan_data:
                self.messageBox(QMessageBox.Warning, "Warning", "Loan not found.")
                return

            # Extract loan details from the fetched data
            loan_limit = loan_data[2]
            loan_debt = loan_data[4]
            loan_take_date = loan_data[3]

            # Create the message to display
            message = (
                f"Loan Number: {loan_number}\n"
                f"Loan Limit: {loan_limit}\n"
                f"Loan Debt: {loan_debt}\n"
                f"Loan Take Date: {loan_take_date}"
            )

            # Display the loan details in a message box
            self.messageBox(QMessageBox.Information, "Loan Details", message)

        except Exception as e:
            # Handle any exceptions and display a warning message
            self.messageBox(QMessageBox.Warning, "Error", f"An error occurred: {str(e)}")


