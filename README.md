# BANK MANAGEMENT PROGRAM

## Overview

The program serves as a comprehensive banking management system, allowing customers to manage their ***accounts, credit cards, and loans*** efficiently through a user-friendly interface. Each method corresponds to a specific banking operation, providing functionalities from ***account creation to money transfers and credit management***.

## Features

### Login Page
- Log In
- Sign Up
- Reset Password
- ![11](https://github.com/anlbora/movieLibrary/assets/100442507/b08e8b91-888f-4d84-93bc-a4040c316d2d)

  The login page serves as the entry point to the banking management system. It provides a secure mechanism for users to authenticate themselves before accessing their accounts, credit cards, loans, and other banking functionalities. The login method is responsible for validating user credentials, ensuring that only authorized users can access the system.

  ![12](https://github.com/anlbora/movieLibrary/assets/100442507/f43b8665-89c9-45d0-aa54-c6d041f23b04)

  ![13](https://github.com/anlbora/movieLibrary/assets/100442507/adb60437-a757-4b5c-a434-edb8e2e265a3)


### Main Window
The main window provides a user-friendly interface to the banking management system, allowing customers to perform various banking operations conveniently. It integrates **account management, credit card functionalities, and loan management, enabling customers to manage their finances, accounts, and debts** effectively. The utility methods ensure consistent error handling and messaging throughout the application, enhancing user experience and system reliability. 

![16](https://github.com/anlbora/movieLibrary/assets/100442507/3fcc1645-44ad-466b-bd76-0b37d5581c8f)

### Account Management

- `CreateBankAccount(self)` Creates a new bank account for the logged-in customer with the provided details.
- `getAccountID(self)` Retrieves the account ID associated with the logged-in customer.
- `getAccountName(self, account_id)` Retrieves the account name based on the provided account ID.
- `deleteBankAccount(self)` Deletes a bank account based on the provided account name.
- `updateBankAccount(self)` Updates the details of a bank account based on the provided account name.
- `getAccountList(self)` Retrieves and populates the list of accounts associated with the logged-in customer.

### Credit Card Operations

- `newCreditCard(self)` Creates a new credit card for the logged-in customer with the provided credit limit.
- `useCreditCard(self)` Handles credit card spending, updating the card balance and user debt accordingly.
- `getCreditCardNumbers(self)` Retrieves and populates the list of credit card numbers associated with the logged-in customer.
- `showCardDebt(self): Displays the details of a selected credit card, including balance, debt, and limit.`

### Loan Management

- `takeCredit(self)` Allows the customer to take a new credit/loan and updates the total debt and balance accordingly.
- `payCreditLoan(self)` Handles loan repayment, updating the loan debt and total customer debt accordingly.
- `getLoanNumbers(self)` Retrieves and populates the list of loan numbers associated with the logged-in customer.
- `showLoanDetails(self)` Displays the details of a selected loan, including limit, debt, and take date.

### Utility Methods

- `messageBox(self, icon, title, message)` Displays a message box with a specified icon, title, and message.
- `getCustomerID(self)` Retrieves the customer ID based on the current logged-in username.
- `getChosenCustomerID(self, username):` Retrieves the customer ID based on the provided username.

## Requirements

- Python
- PyQt5
- SQLite3

## Installation

1. Clone the repository:
  - git clone https://github.com/yourusername/bankManagementSystem.git
2. Navigate to the project directory:
  - cd bankManagementSystem
3. Install the required dependencies:
  - pip install -r requirements.txt
4. Run the application:
  - python main.py


## Usage

1. Launch the application by running `main.py`.
2. Sign up for a new account or log in with an existing account.
3. Use the respective buttons in the Main Window to manage accounts, transfers, credit cards and credits.
