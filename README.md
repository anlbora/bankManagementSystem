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

- 'CreateBankAccount(self):' Creates a new bank account for the logged-in customer with the provided details.
- **Add Users**: Enables the addition of new user accounts.
- **Update Users**: Allows modification of existing user information.
- **Delete Users**: Facilitates the removal of user accounts after authentication.

### Director Management

- **View All Directors**: Presents a list of all registered directors.
- **Add Directors**: Allows the addition of new director profiles.
- **Update Directors**: Permits updates to existing director details.
- **Delete Directors**: Enables the deletion of director profiles from the database.

### Movie Management

- **View All Movies**: Displays a table containing information on all movies in the database.
- **Add Movies**: Facilitates the addition of new movie entries.
- **Update Movies**: Allows modifications to existing movie details.
- **Delete Movies**: Permits the removal of movies from the database

## Requirements

- Python
- PyQt5
- SQLite3

## Installation

1. Clone the repository:
  - git clone https://github.com/yourusername/movieLibrary.git
2. Navigate to the project directory:
  - cd movieLibrary
3. Install the required dependencies:
  - pip install -r requirements.txt
4. Run the application:
  - python main.py


## Usage

1. Launch the application by running `main.py`.
2. Sign up for a new account or log in with an existing account.
3. Use the respective buttons in the AdminPanel to manage movies, directors, and user accounts.
