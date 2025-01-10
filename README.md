
# Email Sender Script

This is a Python script for sending personalized email messages to a list of clients. It uses a SQLite database and environment variables for configuration.

## Features
- Sends personalized emails to clients based on a provided JSON file.
- Easy to configure with environment variables.
- Uses SQLite for storing and managing email data.

## Prerequisites
- Python 3.8 or higher
- Poetry package manager

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/email-sender.git
   cd email-sender
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Activate the Poetry shell:
   ```bash
   poetry shell
   ```

## Setup

### 1. Create `clients.json`
Create a file named `clients.json` in the project root with the following structure:
```json
[
  {
    "email": "oleksandr.o.nazarevych@gmail.com",
    "name": "Oleksandr"
  }
]
```

### 2. Create `.env` File
Create a file named `.env` in the project root and define the following variables:
```ini
SQLITE_DB_PATH=database.sqlite  # Path to SQLite database file
DATABASE_URL=sqlite:///database.sqlite  # SQLite connection string

EMAIL_SENDER=your-email@gmail.com       # Sender email address
EMAIL_PASSWORD=your-email-password      # Sender email password
EMAIL_RECIPIENT=recipient-email@gmail.com # Optional: default recipient email
```

### 3. Database Initialization
If the database is not already initialized, the script will handle its setup automatically during execution.

## Usage

Run the script with the following command:
```bash
python main.py
```

The script will:
1. Read the `clients.json` file for client information.
2. Use the `.env` file for email credentials and database configuration.
3. Send personalized emails to each client in the JSON file.

## Notes
- Make sure to use a secure app password for your email if your email provider enforces 2-factor authentication.
- The email content can be customized in the `main.py` script.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute to this project by opening issues or submitting pull requests.
