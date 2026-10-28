# Basic Banking System — Flask Web Application

A responsive educational web application built with Python, Flask, SQLite, HTML, CSS, and JavaScript.

## Features

- Dashboard with total account count and combined current balances
- Create account with automatically generated 10-digit account number
- Check balance by account number or unique holder name
- Deposit and withdraw money
- Prevent negative amounts and withdrawals beyond available balance
- View all accounts and filter the table
- Identify the highest-balance account
- View account transaction history
- SQLite database persistence across restarts
- Responsive layout for desktop and mobile screens

## Requirements

- Python 3.10+
- VS Code
- Python extension for VS Code (recommended)

## Run on Windows

Open this folder in VS Code, then open **Terminal > New Terminal**.

### 1. Create a virtual environment

```powershell
py -m venv .venv
```

### 2. Activate it

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this for the current terminal only, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

Alternatively, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the website

```powershell
python run.py
```

Open this address in your browser:

http://127.0.0.1:5000

Stop the server with `Ctrl+C` in the terminal.

## Database

The app creates `instance/banking.db` automatically on first run. Account and transaction data persist after the app is stopped.

To reset all demo data, stop the app and delete `instance/banking.db`. The database will be recreated next time you run it.

## Folder structure

```text
BasicBankingWebApp/
├── run.py
├── requirements.txt
├── README.md
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── create_account.html
│   │   ├── balance.html
│   │   ├── transaction.html
│   │   ├── accounts.html
│   │   ├── highest_balance.html
│   │   └── history.html
│   └── static/
│       ├── css/style.css
│       └── js/script.js
└── instance/
    └── banking.db  (created automatically)
```

## Important limitations and security

This is a local classroom demo, not a real banking system. It has no user authentication or role-based access control. Anyone who can access the app can operate on demo accounts. Do not expose it to the public internet or enter real customer or financial data. Before any real deployment, add authentication, authorization, CSRF protection, secure secret management, audit controls, and production hosting configuration.
