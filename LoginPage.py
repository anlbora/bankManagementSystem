import sqlite3
from datetime import datetime as dt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import *
import random


class Ui_logInPage(object):

    def __init__(self):
        """
        Initializes a new instance of the class and establishes a connection to the SQLite database.
        
        This method initializes a connection to an SQLite database named 'BankDatabase.db' and creates a cursor
        object to execute SQL queries. It also calls the create_tables method to ensure that the necessary
        database tables (Customers, Accounts, CreditCards, Loans) are created or exist before further operations.

        Parameters:
        - self: The instance of the class.

        Returns:
        None
        """
        
        # Establish a connection to the SQLite database
        self.connect = sqlite3.connect('BankDatabase.db')
        self.cursor = self.connect.cursor()
        
        # Call the create_tables method to ensure required tables are created or exist
        self.create_tables()

    def setupUi(self, logInPage):
        logInPage.setObjectName("logInPage")
        logInPage.setWindowModality(QtCore.Qt.ApplicationModal)
        logInPage.resize(800, 420)
        logInPage.setMinimumSize(QtCore.QSize(800, 420))
        logInPage.setMaximumSize(QtCore.QSize(800, 420))
        font = QtGui.QFont()
        font.setPointSize(12)
        logInPage.setFont(font)
        logInPage.setAutoFillBackground(True)
        self.groupBox = QtWidgets.QGroupBox(logInPage)
        self.groupBox.setGeometry(QtCore.QRect(410, 2, 381, 401))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.signup_name = QtWidgets.QLineEdit(self.groupBox)
        self.signup_name.setFrame(False)
        self.signup_name.setObjectName("signup_name")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.signup_name)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.signup_surname = QtWidgets.QLineEdit(self.groupBox)
        self.signup_surname.setFrame(False)
        self.signup_surname.setObjectName("signup_surname")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.signup_surname)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.signup_age = QtWidgets.QLineEdit(self.groupBox)
        self.signup_age.setFrame(False)
        self.signup_age.setObjectName("signup_age")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.signup_age)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.signup_username = QtWidgets.QLineEdit(self.groupBox)
        self.signup_username.setFrame(False)
        self.signup_username.setObjectName("signup_username")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.signup_username)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.signup_password = QtWidgets.QLineEdit(self.groupBox)
        self.signup_password.setFrame(False)
        self.signup_password.setObjectName("signup_password")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.signup_password)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.signup_email = QtWidgets.QLineEdit(self.groupBox)
        self.signup_email.setFrame(False)
        self.signup_email.setObjectName("signup_email")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.signup_email)
        self.signup_btn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.signup_btn)
        self.groupBox_2 = QtWidgets.QGroupBox(logInPage)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 391, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.login_username = QtWidgets.QLineEdit(self.groupBox_2)
        self.login_username.setFrame(False)
        self.login_username.setObjectName("login_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.login_username)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.login_password = QtWidgets.QLineEdit(self.groupBox_2)
        self.login_password.setFrame(False)
        self.login_password.setObjectName("login_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.login_password)
        self.login_btn = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.login_btn)
        self.groupBox_3 = QtWidgets.QGroupBox(logInPage)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 391, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.reset_username = QtWidgets.QLineEdit(self.groupBox_3)
        self.reset_username.setFrame(False)
        self.reset_username.setObjectName("reset_username")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reset_username)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.reset_email = QtWidgets.QLineEdit(self.groupBox_3)
        self.reset_email.setFrame(False)
        self.reset_email.setObjectName("reset_email")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reset_email)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.reset_newpassword = QtWidgets.QLineEdit(self.groupBox_3)
        self.reset_newpassword.setFrame(False)
        self.reset_newpassword.setObjectName("reset_newpassword")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.reset_newpassword)
        self.reset_btn = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.reset_btn)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.reset_password = QtWidgets.QLineEdit(self.groupBox_3)
        self.reset_password.setFrame(False)
        self.reset_password.setObjectName("reset_password")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.reset_password)

        self.retranslateUi(logInPage)
        QtCore.QMetaObject.connectSlotsByName(logInPage)

        # Connect the clicked signal of the signup_btn to the sign_up method
        self.signup_btn.clicked.connect(self.sign_up)

        # Connect the clicked signal of the login_btn to the log_in method
        self.login_btn.clicked.connect(self.log_in)

        # Connect the clicked signal of the reset_btn to the reset_password_2 method
        self.reset_btn.clicked.connect(self.reset_password_2)

    def retranslateUi(self, logInPage):
        _translate = QtCore.QCoreApplication.translate
        logInPage.setWindowTitle(_translate("logInPage", "Welcome to Bank System"))
        self.groupBox.setTitle(_translate("logInPage", "Sign Up"))
        self.label_10.setText(_translate("logInPage", "Name:"))
        self.label_11.setText(_translate("logInPage", "Surname:"))
        self.label_12.setText(_translate("logInPage", "Age:"))
        self.label_13.setText(_translate("logInPage", "Username:"))
        self.label_14.setText(_translate("logInPage", "Password:"))
        self.label_15.setText(_translate("logInPage", "Email:"))
        self.signup_btn.setText(_translate("logInPage", "Sign Up"))
        self.groupBox_2.setTitle(_translate("logInPage", "Log In"))
        self.label.setText(_translate("logInPage", "Username:"))
        self.label_2.setText(_translate("logInPage", "Password:"))
        self.login_btn.setText(_translate("logInPage", "Log In"))
        self.groupBox_3.setTitle(_translate("logInPage", "Reset Password"))
        self.label_3.setText(_translate("logInPage", "Username:"))
        self.label_4.setText(_translate("logInPage", "Email:"))
        self.label_5.setText(_translate("logInPage", "New Password:"))
        self.reset_btn.setText(_translate("logInPage", "Reset my Password"))
        self.label_6.setText(_translate("logInPage", "New Password:"))

    def create_tables(self):
        """
        Creates database tables for Customers, Accounts, CreditCards, and Loans if they do not already exist.
        
        This method executes SQL queries to create the Customers, Accounts, CreditCards, and Loans tables in the database,
        with the specified column names and data types. It also establishes foreign key constraints
        to maintain referential integrity between the tables.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        # Create the Customers table if it does not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100),
                surname VARCHAR(100),
                age INTEGER,
                username VARCHAR(100),
                password VARCHAR(100),
                email VARCHAR(100),
                account_quantity INTEGER,
                join_date DATETIME,
                card_quantity INTEGER,
                balance FLOAT,
                debt FLOAT
            )
        ''')

        # Create the Accounts table if it does not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_name VARCHAR(100),
                account_number BIGINT,
                balance FLOAT,
                currency VARCHAR(100),
                opening_date DATETIME,
                last_activity DATETIME,
                customer_id INTEGER,
                is_main BOOL,
                FOREIGN KEY (customer_id) REFERENCES Customers(id)
            )
        ''')

        # Create the CreditCards table if it does not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CreditCards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                card_number BIGINT,
                card_limit INTEGER,
                card_balance FLOAT,
                card_debt FLOAT,
                card_last_use DATETIME,
                customer_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES Customers(id)
            )
        ''')

        # Create the Loans table if it does not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                loan_number BIGINT,
                loan_limit INTEGER,
                loan_take_date DATETIME,
                loan_debt FLOAT,
                customer_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES Customers(id)
            )
        ''')

        # Commit the changes to the database
        self.connect.commit()

    def sign_up(self):
        """
        Registers a new user by validating the provided user details and inserting them into the database.
        
        This method retrieves the user details entered by the user from the UI,
        validates the provided details,
        creates a new Customer object with the validated details,
        inserts the new customer's details into the database,
        and displays an appropriate message based on the result of the sign-up operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        # Retrieve user details entered by the user from the UI
        name = self.signup_name.text()
        surname = self.signup_surname.text()
        age = self.signup_age.text()
        email = self.signup_email.text()
        username = self.signup_username.text()
        password = self.signup_password.text()

        # Validate if all fields are filled
        if not name or not surname or not age or not email or not username or not password:
            self.messageBox(QMessageBox.Warning, "Warning", "Please fill in all fields.")
            return

        # Validate the email format
        if not email.endswith("@gmail.com") and not email.endswith("@hotmail.com") and not email.endswith("@outlook.com"):
            self.messageBox(QMessageBox.Warning, "Warning", "Not a valid email")
            return
        
        try:
            # Validate age to ensure it's 18 or above
            if int(age) < 18:
                self.messageBox(QMessageBox.Warning, "Warning", "Age can't be smaller than 18")
                return
        except ValueError:
            # Handle non-numeric age input
            self.messageBox(QMessageBox.Warning, "Warning", "Please type numerical values for age.")
            return

        # Check if the user already exists in the database
        does_exist = self.cursor.execute('''
                SELECT id FROM Customers WHERE username = ? OR email = ?''', (username, email)).fetchone()

        if does_exist:
            self.messageBox(QMessageBox.Warning, "Warning", "User already exists")
            return

        # Insert the new customer's details into the Customers table
        self.cursor.execute('''
                INSERT INTO Customers (name, surname, age, username, password, email, account_quantity, join_date, card_quantity, balance, debt)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, surname, age, username, password, email, 1, dt.now(), 0, 0, 0))
        
        # Retrieve the customer ID for the newly inserted customer
        customer_id = self.getCustomerID(username)[0]
        
        # Insert a new main account for the customer into the Accounts table
        self.cursor.execute('''
                INSERT INTO Accounts (account_name, account_number, balance, currency, opening_date, last_activity, customer_id, is_main)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', ('Main Account', random.randint(10000000000, 999999999999), 0.0, 'USD', dt.now(), dt.now(), customer_id, 1))

        # Commit the changes to the database
        self.connect.commit()
        
        # Display a success message
        self.messageBox(QMessageBox.Information, "Success", "Sign-up successful.")

        # Clear the sign-up fields
        self.signup_name.setText("")
        self.signup_surname.setText("")
        self.signup_age.setText("")
        self.signup_password.setText("")
        self.signup_email.setText("")
        self.signup_username.setText("")

    def log_in(self):
        """
        Authenticates the user by checking the provided username and password against the database.
        
        This method retrieves the username and password entered by the user from the UI,
        executes an SQL query to find a matching user in the database,
        and displays an appropriate message based on the authentication result.
        If authentication is successful, it closes the current window and opens the admin page.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Retrieve username and password entered by the user from the UI
            username = self.login_username.text()
            password = self.login_password.text()

            # Execute the SQL query to find a matching user in the database
            self.cursor.execute('SELECT * FROM Customers WHERE username = ? AND password = ?', (username, password))
            
            # Fetch the first matching row from the executed query
            row = self.cursor.fetchone()

            # Check if a matching user was found
            if row:
                # Display a success message
                self.messageBox(QMessageBox.Information, "Success", "Log-in successful.")
                
                # Instantiate the admin page
                self.mainWindow = QMainWindow()

                # Setup and initialize the admin page
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.mainWindow)  # Assuming QMainWindow is the parent widget for adminPage

                self.ui.txt_username_User.setText(username)
                
                # Retrieve and display the customer's email on the admin page
                email = self.getCutomerEmail(username)
                self.ui.txt_email_User.setText(email[0])

                # Show the admin page
                self.mainWindow.show()
            else:
                # Display an error message
                self.messageBox(QMessageBox.Warning, "Warning", "Invalid Credentials.")
                
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def reset_password_2(self):
        """
        Resets the user's password by verifying the provided username and email and updating the password in the database.
        
        This method retrieves the email, username, and new password entered by the user from the UI,
        executes an SQL query to find a matching user in the database,
        updates the user's password in the database if a matching user is found,
        and displays an appropriate message based on the result of the password reset operation.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
            
        Returns:
        None
        """
        
        try:
            # Retrieve email, username, and new password entered by the user from the UI
            email = self.reset_email.text()
            username = self.reset_username.text()
            password = self.reset_newpassword.text()

            # Execute the SQL query to find a matching user in the database
            self.cursor.execute('SELECT * FROM Customers WHERE username = ? AND email = ?', (username, email))
            
            # Fetch the first matching row from the executed query
            row = self.cursor.fetchone()

            # Check if a matching user was found
            if row:
                # Update the user's password in the database
                self.cursor.execute('UPDATE Customers SET password = ? WHERE username = ? AND email = ?', (password, username, email))
                
                # Commit the changes to the database
                self.connect.commit()
                
                # Display a success message
                self.messageBox(QMessageBox.Information, "Success", "Password changed successfully.")
            else:
                # Display an error message
                self.messageBox(QMessageBox.Warning, "Error", "User not found or incorrect username/email.")
                
        except Exception as e:
            # Display an error message for any unexpected exceptions
            self.messageBox(QMessageBox.Critical, "Error", f"An error occurred: {str(e)}")

    def messageBox(self, icon, title, message):
        """
        Display a QMessageBox with the specified icon, title, and message.

        This method creates and displays a QMessageBox with the specified icon, title, and message.
        It sets the icon, title, and text of the QMessageBox based on the provided parameters
        and executes the QMessageBox to display it to the user.

        Parameters:
        - icon: QMessageBox.Icon (e.g., QMessageBox.Warning, QMessageBox.Information)
        - title: str - The title of the QMessageBox
        - message: str - The message to display in the QMessageBox
            
        Returns:
        None
        """
        
        # Create a new QMessageBox
        msg_box = QMessageBox()
        
        # Set the icon of the QMessageBox
        msg_box.setIcon(icon)
        
        # Set the title of the QMessageBox
        msg_box.setWindowTitle(title)
        
        # Set the text/message of the QMessageBox
        msg_box.setText(message)
        
        # Execute the QMessageBox to display it to the user
        msg_box.exec_()
    
    def getCutomerEmail(self, username):
        """
        Retrieve the email associated with the provided username from the database.
        
        This method executes an SQL query to retrieve the email associated with the provided username
        from the Customers table in the database and returns the retrieved email.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
        - username: str - The username for which the email is to be retrieved.
            
        Returns:
        str - The email associated with the provided username.
        """
        
        # Execute the SQL query to retrieve the email associated with the provided username
        email = self.cursor.execute('''
            SELECT email FROM Customers WHERE username = ?
        ''', (username,)).fetchone()
        
        # Return the retrieved email
        return email

    def getCustomerID(self, username):
        """
        Retrieve the customer ID associated with the provided username from the database.
        
        This method executes an SQL query to retrieve the customer ID associated with the provided username
        from the Customers table in the database and returns the retrieved customer ID.

        Parameters:
        - self: The instance of the class containing the cursor for database operations.
        - username: str - The username for which the customer ID is to be retrieved.
            
        Returns:
        int - The customer ID associated with the provided username.
        """
        
        # Execute the SQL query to retrieve the customer ID associated with the provided username
        customer_id = self.cursor.execute('''
            SELECT id FROM Customers WHERE username = ?
        ''', (username,)).fetchone()
        
        # Return the retrieved customer ID
        return customer_id
