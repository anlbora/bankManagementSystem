# BANK MANAGEMENT PROGRAM

## Overview

The program serves as a comprehensive banking management system, allowing customers to manage their ***accounts, credit cards, and loans*** efficiently through a user-friendly interface. Each method corresponds to a specific banking operation, providing functionalities from ***account creation to money transfers and credit management***.

## Features

### Login Page

  The login page serves as the entry point to the banking management system. It provides a secure mechanism for users to authenticate themselves before accessing their accounts, credit cards, loans, and other banking functionalities. The login method is responsible for validating user credentials, ensuring that only authorized users can access the system.
- Log In
- Sign Up
- Reset Password
  
![1](https://github.com/anlbora/bankManagementSystem/assets/100442507/05cbf667-7e36-4aa9-8008-8bad0dcd5298)
![2](https://github.com/anlbora/bankManagementSystem/assets/100442507/07fe2271-1b32-4337-b67a-d1a859e17905)
![3](https://github.com/anlbora/bankManagementSystem/assets/100442507/2455c6e8-9268-4eab-a385-ef99756d514c)

### Main Window
  The main window provides a user-friendly interface to the banking management system, allowing customers to perform various banking operations conveniently. It integrates **account management, credit card functionalities, and loan management, enabling customers to manage their finances, accounts, and debts** effectively. The utility methods ensure consistent error handling and messaging throughout the application, enhancing user experience and system reliability. 

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
- `showCardDebt(self)` Displays the details of a selected credit card, including balance, debt, and limit.

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
