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

![4](https://github.com/anlbora/bankManagementSystem/assets/100442507/a7b7a07c-2f0e-4be3-9f84-a93599dac41f)

## Features

### Login Page

The Login Page serves as the entry point to the banking management system, providing a secure mechanism for users to authenticate themselves.

- **Log In**: Authenticate and access your account.
- **Sign Up**: Create a new account.
- **Reset Password**: Reset your password if forgotten.



### Main Window

The Main Window offers a user-friendly interface to perform various banking operations.

- **Account Management**: Manage your bank accounts.
- **Money Management**: Handle withdrawals, deposits, and transfers.
- **Credit Card Operations**: Manage credit cards and spending.
- **Loan Management**: Take new loans and manage repayments.

![Main Window](https://github.com/anlbora/bankManagementSystem/assets/100442507/a7b7a07c-2f0e-4be3-9f84-a93599dac41f)

### Account Management

- **CreateBankAccount**: Create a new bank account.
- **getAccountID**: Retrieve account ID.
- **getAccountName**: Retrieve account name.
- **deleteBankAccount**: Delete a bank account.
- **updateBankAccount**: Update bank account details.
- **getAccountList**: Retrieve list of accounts.

![Account Management Screenshots](https://github.com/anlbora/bankManagementSystem/assets/100442507/)

### Money Management

- **withdrawMoney**: Withdraw money from an account.
- **depositMoney**: Deposit money into an account.
- **transferMoney**: Transfer money between accounts.
- **getCustomerList**: Retrieve list of customers.
- **getCustomerAccountList**: Retrieve customer account list.
- **changeAccount**: Display account details.

![Money Management Screenshots](https://github.com/anlbora/bankManagementSystem/assets/100442507/)

### Credit Card Operations

- **newCreditCard**: Create a new credit card.
- **useCreditCard**: Handle credit card spending.
- **getCreditCardNumbers**: Retrieve list of credit card numbers.
- **showCardDebt**: Display credit card details.

![Credit Card Operations Screenshots](https://github.com/anlbora/bankManagementSystem/assets/100442507/)

### Loan Management

- **takeCredit**: Take a new credit/loan.
- **payCreditLoan**: Repay a loan.
- **getLoanNumbers**: Retrieve list of loan numbers.
- **showLoanDetails**: Display loan details.

![Loan Management Screenshots](https://github.com/anlbora/bankManagementSystem/assets/100442507/)

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
   ```bash
   git clone https://github.com/yourusername/bankManagementSystem.git
