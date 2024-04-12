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
![4](https://github.com/anlbora/bankManagementSystem/assets/100442507/a7b7a07c-2f0e-4be3-9f84-a93599dac41f)

### Account Management

- `CreateBankAccount(self)` Creates a new bank account for the logged-in customer with the provided details.
- `getAccountID(self)` Retrieves the account ID associated with the logged-in customer.
- `getAccountName(self, account_id)` Retrieves the account name based on the provided account ID.
- `deleteBankAccount(self)` Deletes a bank account based on the provided account name.
- `updateBankAccount(self)` Updates the details of a bank account based on the provided account name.
- `getAccountList(self)` Retrieves and populates the list of accounts associated with the logged-in customer.
  
![5](https://github.com/anlbora/bankManagementSystem/assets/100442507/e834bca2-3a57-4e5a-affd-9fee5dd5e4c4)
![6](https://github.com/anlbora/bankManagementSystem/assets/100442507/6fea360d-733a-4c3a-9534-1f1e99845d43)
![7](https://github.com/anlbora/bankManagementSystem/assets/100442507/cd98b90d-f38e-4de9-bd9e-8ca467fa2055)
![8](https://github.com/anlbora/bankManagementSystem/assets/100442507/7a0a9977-5101-4c01-acc9-17130d7b3f7b)

### Money Management

- `withdrawMoney(self)` Handles the withdrawal of money from a selected bank account, updating the account balance and total customer balance accordingly.
- `depositMoney(self)` Manages the deposit of money into a selected bank account, updating the account balance and total customer balance accordingly.
- `transferMoney(self)` Facilitates the transfer of money between two bank accounts, updating the balances of the sender and receiver accounts, as well as the total customer balance.
- `getCustomerList(self)` Retrieves and populates the list of customers for initiating a money transfer.
- `getCustomerAccountList(self)` Retrieves and populates the list of accounts associated with a selected customer for initiating a money transfer.
- `changeAccount(self)` Displays detailed information about a selected bank account, including balance, account number, and account holder details.

![9](https://github.com/anlbora/bankManagementSystem/assets/100442507/10260bbf-e1ff-4465-9c96-a4fa24b9dc42)
![10](https://github.com/anlbora/bankManagementSystem/assets/100442507/6ef3dd06-131d-472a-a7b4-a382f12db25b)
![11](https://github.com/anlbora/bankManagementSystem/assets/100442507/714e5e61-9f93-4d18-9337-52c1c57c350c)

### Credit Card Operations

- `newCreditCard(self)` Creates a new credit card for the logged-in customer with the provided credit limit.
- `useCreditCard(self)` Handles credit card spending, updating the card balance and user debt accordingly.
- `getCreditCardNumbers(self)` Retrieves and populates the list of credit card numbers associated with the logged-in customer.
- `showCardDebt(self)` Displays the details of a selected credit card, including balance, debt, and limit.

![12](https://github.com/anlbora/bankManagementSystem/assets/100442507/534f4434-f4c1-4449-8700-fcaf309d5e57)
![14](https://github.com/anlbora/bankManagementSystem/assets/100442507/dd965807-72bc-419c-bd16-e4f27e0ed163)
![15](https://github.com/anlbora/bankManagementSystem/assets/100442507/1db8d898-a65a-4885-81a4-ec5fd03d8f7b)
![16](https://github.com/anlbora/bankManagementSystem/assets/100442507/8fe6ad6a-6990-4cc6-a5df-b7f93f467f3c)

### Loan Management

- `takeCredit(self)` Allows the customer to take a new credit/loan and updates the total debt and balance accordingly.
- `payCreditLoan(self)` Handles loan repayment, updating the loan debt and total customer debt accordingly.
- `getLoanNumbers(self)` Retrieves and populates the list of loan numbers associated with the logged-in customer.
- `showLoanDetails(self)` Displays the details of a selected loan, including limit, debt, and take date.
  
![17](https://github.com/anlbora/bankManagementSystem/assets/100442507/723744bc-4022-40e5-892a-31b84c306de4)
![18](https://github.com/anlbora/bankManagementSystem/assets/100442507/20a807d7-6829-4fa9-90c4-e618cb26a241)
![19](https://github.com/anlbora/bankManagementSystem/assets/100442507/081b7843-d183-477f-80c1-3726e776972f)

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
