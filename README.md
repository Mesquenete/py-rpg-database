# 🛡️ RPG Guild Manager

A professional CLI (Command Line Interface) application to manage an RPG Guild database. 
Built with **Python** and **PostgreSQL**, focusing on CRUD operations, security best practices, and a modern terminal UI.

## 🚀 Technologies

* **Python 3.x**
* **PostgreSQL** (Database)
* **Psycopg2** (Database Adapter)
* **Rich** (Terminal UI Library)
* **Python-Dotenv** (Environment Security)

## 📋 Features

* **Create:** Add new heroes with specific roles, levels, and gold.
* **Read:** View all guild members in a dynamic, auto-formatted table.
* **Update:** Edit hero details (Level up / Gold transaction).
* **Delete:** Remove members from the database securely.
* **Security:** Database credentials are protected using Environment Variables (`.env`).

## 📦 How to Run

### 1. Clone the repository
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd seu-repositorio
2. Create a Virtual Environment
Bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a file named .env in the root directory and add your database credentials:

Ini, TOML
DB_HOST=localhost
DB_NAME=rpg_db
DB_USER=postgres
DB_PASS=your_real_password
DB_PORT=5432
5. Run the Application
Bash
python main.py
🛠️ Project Structure
main.py: The entry point and UI logic (Menu/Rich integration).

db_manager.py: Handles database connections and CRUD operations using OOP.

.env: Stores sensitive information (excluded from version control).