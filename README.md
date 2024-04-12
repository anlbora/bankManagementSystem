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
  
![1](https://github.com/anlbora/bankManagementSystem/assets/100442507/05cbf667-7e36-4aa9-8008-8bad0dcd5298)
![2](https://github.com/anlbora/bankManagementSystem/assets/100442507/07fe2271-1b32-4337-b67a-d1a859e17905)
![3](https://github.com/anlbora/bankManagementSystem/assets/100442507/2455c6e8-9268-4eab-a385-ef99756d514c)

### Main Window

The Main Window offers a user-friendly interface to perform various banking operations.

- **Account Management**: Manage your bank accounts.
- **Money Management**: Handle withdrawals, deposits, and transfers.
- **Credit Card Operations**: Manage credit cards and spending.
- **Loan Management**: Take new loans and manage repayments.

![4](https://github.com/anlbora/bankManagementSystem/assets/100442507/a7b7a07c-2f0e-4be3-9f84-a93599dac41f)

### Account Management

- **CreateBankAccount**: Create a new bank account.
- **getAccountID**: Retrieve account ID.
- **getAccountName**: Retrieve account name.
- **deleteBankAccount**: Delete a bank account.
- **updateBankAccount**: Update bank account details.
- **getAccountList**: Retrieve list of accounts.

![5](https://github.com/anlbora/bankManagementSystem/assets/100442507/e834bca2-3a57-4e5a-affd-9fee5dd5e4c4)
![6](https://github.com/anlbora/bankManagementSystem/assets/100442507/6fea360d-733a-4c3a-9534-1f1e99845d43)
![7](https://github.com/anlbora/bankManagementSystem/assets/100442507/cd98b90d-f38e-4de9-bd9e-8ca467fa2055)
![8](https://github.com/anlbora/bankManagementSystem/assets/100442507/7a0a9977-5101-4c01-acc9-17130d7b3f7b)

### Money Management

- **withdrawMoney**: Withdraw money from an account.
- **depositMoney**: Deposit money into an account.
- **transferMoney**: Transfer money between accounts.
- **getCustomerList**: Retrieve list of customers.
- **getCustomerAccountList**: Retrieve customer account list.
- **changeAccount**: Display account details.

![9](https://github.com/anlbora/bankManagementSystem/assets/100442507/10260bbf-e1ff-4465-9c96-a4fa24b9dc42)
![10](https://github.com/anlbora/bankManagementSystem/assets/100442507/6ef3dd06-131d-472a-a7b4-a382f12db25b)
![11](https://github.com/anlbora/bankManagementSystem/assets/100442507/714e5e61-9f93-4d18-9337-52c1c57c350c)

### Credit Card Operations

- **newCreditCard**: Create a new credit card.
- **useCreditCard**: Handle credit card spending.
- **getCreditCardNumbers**: Retrieve list of credit card numbers.
- **showCardDebt**: Display credit card details.

![12](https://github.com/anlbora/bankManagementSystem/assets/100442507/534f4434-f4c1-4449-8700-fcaf309d5e57)
![14](https://github.com/anlbora/bankManagementSystem/assets/100442507/dd965807-72bc-419c-bd16-e4f27e0ed163)
![15](https://github.com/anlbora/bankManagementSystem/assets/100442507/1db8d898-a65a-4885-81a4-ec5fd03d8f7b)
![16](https://github.com/anlbora/bankManagementSystem/assets/100442507/8fe6ad6a-6990-4cc6-a5df-b7f93f467f3c)

### Loan Management

- **takeCredit**: Take a new credit/loan.
- **payCreditLoan**: Repay a loan.
- **getLoanNumbers**: Retrieve list of loan numbers.
- **showLoanDetails**: Display loan details.

![17](https://github.com/anlbora/bankManagementSystem/assets/100442507/723744bc-4022-40e5-892a-31b84c306de4)
![18](https://github.com/anlbora/bankManagementSystem/assets/100442507/20a807d7-6829-4fa9-90c4-e618cb26a241)
![19](https://github.com/anlbora/bankManagementSystem/assets/100442507/081b7843-d183-477f-80c1-3726e776972f)

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
