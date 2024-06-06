# Bank Management System

## Table of Contents

- [Overview](#overview)
- [Features](#features)
  - [Login Page](#login-page)
  - [Main Window](#main-window)
  - [Account Management](#account-management)
  - [Money Management](#money-management)
  - [Credit Card Operations](#credit-card-operations)
  - [Loan Management](#loan-management)
  - [Utility Methods](#utility-methods)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Overview

The Bank Management System is a comprehensive banking management application designed to help customers manage their accounts, credit cards, and loans efficiently. It offers a user-friendly interface for performing various banking operations, from account creation to money transfers and credit management.

## Features

### Login Page

The Login Page serves as the entry point to the banking management system, providing a secure mechanism for users to authenticate themselves.

- **Log In**: Authenticate and access your account.
- **Sign Up**: Create a new account.
- **Reset Password**: Reset your password if forgotten.
  
![1](https://github.com/anlbora/bankManagementSystem/assets/100442507/aeb12b15-9ec6-47ea-989b-ec7cb3a862b2)

![2](https://github.com/anlbora/bankManagementSystem/assets/100442507/5a0a1c1e-583a-42f1-a1ff-1957e0f5b903)

![3](https://github.com/anlbora/bankManagementSystem/assets/100442507/603e610c-aed9-4a3b-874a-adc4e7c5541c)

![4](https://github.com/anlbora/bankManagementSystem/assets/100442507/600ca28e-d0c8-486d-b154-f66dd7821ede)

![5](https://github.com/anlbora/bankManagementSystem/assets/100442507/cac46b96-1b0e-4776-8456-5c191d0573ce)

### Main Window

The Main Window offers a user-friendly interface to perform various banking operations.

- **Account Management**: Manage your bank accounts.
- **Money Management**: Handle withdrawals, deposits, and transfers.
- **Credit Card Operations**: Manage credit cards and spending.
- **Loan Management**: Take new loans and manage repayments.

![6](https://github.com/anlbora/bankManagementSystem/assets/100442507/782f7a0e-c7c3-41c3-af1d-df7717c392f9)

### Account Management

- **CreateBankAccount**: Create a new bank account.
- **getAccountID**: Retrieve account ID.
- **getAccountName**: Retrieve account name.
- **deleteBankAccount**: Delete a bank account.
- **updateBankAccount**: Update bank account details.
- **getAccountList**: Retrieve list of accounts.

![7](https://github.com/anlbora/bankManagementSystem/assets/100442507/240faea7-f24b-42f0-955f-7581571accbf)

![8](https://github.com/anlbora/bankManagementSystem/assets/100442507/1c8c636a-69db-485d-bba8-9cd6c6e24c9e)

### Money Management

- **withdrawMoney**: Withdraw money from an account.
- **depositMoney**: Deposit money into an account.
- **transferMoney**: Transfer money between accounts.
- **getCustomerList**: Retrieve list of customers.
- **getCustomerAccountList**: Retrieve customer account list.
- **Account Details**: Display account details.

![9](https://github.com/anlbora/bankManagementSystem/assets/100442507/167ae6d2-f7e3-4a93-bf89-5ba640b2f416)

![10](https://github.com/anlbora/bankManagementSystem/assets/100442507/cbe1f247-3012-4e51-a4b4-88c123d554d1)

![11](https://github.com/anlbora/bankManagementSystem/assets/100442507/fca2924a-19b9-42d0-94a8-b62513104211)

![12](https://github.com/anlbora/bankManagementSystem/assets/100442507/dab55e97-8df2-4664-a518-9b6c4d49a8ff)

### Credit Card Operations

- **newCreditCard**: Create a new credit card.
- **useCreditCard**: Handle credit card spending.
- **getCreditCardNumbers**: Retrieve list of credit card numbers.
- **showCardDebt**: Display credit card details.

![14](https://github.com/anlbora/bankManagementSystem/assets/100442507/153a8e59-6c18-4268-a49d-ad8a1e50172e)

### Loan Management

- **takeCredit**: Take a new credit/loan.
- **payCreditLoan**: Repay a loan.
- **getLoanNumbers**: Retrieve list of loan numbers.
- **showLoanDetails**: Display loan details.

![13](https://github.com/anlbora/bankManagementSystem/assets/100442507/0cdcde4c-0158-4cac-ba3a-e4e9937d4a35)

### Utility Methods

- **messageBox**: Display a message box.
- **getCustomerID**: Retrieve customer ID.
- **getChosenCustomerID**: Retrieve customer ID based on username.

## Requirements

- Python
- PyQt5
- SQLite3

## Installation

1. Clone the repository:
   `bash git clone https://github.com/yourusername/bankManagementSystem.git`
2. Navigate to the project directory:
   `cd bankManagementSystem`
3. Install the required dependencies:
   `pip install -r requirements.txt`
4. Run the application:
   `python main.py`
## Usage

1. Launch the application by running `main.py`.
2. Sign up for a new account or log in with an existing account.
2. Use the respective buttons in the Main Window to manage accounts, transfers, credit cards, and loans


