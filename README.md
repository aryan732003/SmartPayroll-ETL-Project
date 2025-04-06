# 👨‍💼 SmartPayroll ETL Project

> A full-stack, production-ready Payroll Management system with an integrated ETL pipeline, data analysis, and interactive UI built using Flask, SQL Server, Python, and Pandas.

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)](https://flask.palletsprojects.com/)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-ETL%20Database-red?logo=microsoftsqlserver)](https://www.microsoft.com/en-us/sql-server/)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)

---

## 📌 Overview

**SmartPayroll ETL** is a complete end-to-end project designed for managing employee payrolls efficiently. It covers:

- ETL data pipeline from raw Excel to SQL Server.
- A beautiful and modern Flask-based UI to view, search, and filter employees.
- Net salary breakdown and department-wise filtering.
- CSV/PDF download and dark mode toggle.
- Exploratory data analysis using Jupyter Notebooks.

---

## 📸 Screenshots

| Dark Mode | Employee List | PDF Preview |
|----------|----------------|-------------|
| ![Dark Mode](screenshots/dark_mode.png) | ![List](screenshots/list.png) | ![PDF](screenshots/pdf.png) |

---

## 🔍 Features

- 🔄 ETL Pipeline with raw Excel ➡ SQL Server
- 🧠 Data Analysis using Pandas
- 📂 CSV & PDF payroll download
- 🌙 Dark Mode toggle
- 🔍 Employee search & filtering
- 🏢 Department overview page
- ➕ Add new employee from UI
- 📊 Responsive and modern design

---

## 🧰 Tech Stack

| Layer     | Tools                       |
|-----------|-----------------------------|
| Backend   | Python, Flask, SQLAlchemy   |
| Database  | SQL Server                  |
| ETL       | Pandas, Stored Procedures   |
| Frontend  | HTML, CSS (Custom), Jinja2  |
| Deployment| Localhost (Dev Ready)       |
| Others    | .env config, Dark Mode      |



## 🔄 ETL Workflow


Raw Excel (.xlsx)
        |
        v
[Pandas ETL Script]
        |
        v
SQL Server - [Staging → Processing → Final Tables]
        |
        v
SmartPayroll UI (Flask) → Data Access via SQLAlchemy


Stored procedures are used to transform and load clean data efficiently.



## 🗃️ Project Structure


SmartPayroll-ETL-Project/
│
├── app.py                   # Main Flask app
├── .env                     # Environment Variables (not pushed to GitHub)
├── templates/               # Jinja2 HTML templates
├── static/                  # CSS, JS, and assets
├── etl/                     # ETL scripts
├── analysis/                # Jupyter Notebooks
├── db/                      # SQL queries & structure
├── screenshots/             # Project screenshots
├── README.md
└── requirements.txt


---

## 🧪 Run Locally


# 1. Clone the repository
git clone https://github.com/aryan732003/SmartPayroll-ETL-Project.git
cd SmartPayroll-ETL-Project

# 2. Setup environment
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a `.env` file and add your DB credentials:
# Example:
DB_SERVER=YOUR_SERVER
DB_DATABASE=payrolldata
DB_USERNAME=your_username
DB_PASSWORD=your_password
SECRET_KEY=some_random_key

# 5. Run the app
python app.py




## 📊 Data Analysis

The analysis is performed in the `analysis/` folder using Jupyter Notebooks:
- Salary distributions
- Department-wise counts
- Monthly expenditure graphs
- Anomalies in payroll data

---

## 📸 UI Screenshots

### Employee Detail View (Dark Mode)  
![SmartPayroll UI - Dark Mode](https://github.com/aryan732003/SmartPayroll-ETL-Project/blob/main/static/images/SmartPayroll_UI.png)

---

## 🔄 Workflow Diagram

![ETL Workflow Diagram](https://github.com/aryan732003/SmartPayroll-ETL-Project/blob/main/static/images/Flow_Diagram.png)


---

## 🔄 Workflow Diagram

![Workflow Diagram](assets/workflow_diagram.png)

## 📁 Folder Highlights

| Folder       | Purpose                            |
|--------------|------------------------------------|
| `etl/`       | Contains ETL pipeline code         |
| `templates/` | Frontend HTML + Jinja2             |
| `analysis/`  | Notebooks for data exploration     |
| `static/`    | CSS, JS, assets                    |
| `db/`        | SQL scripts, stored procedures     |
| `screenshots/`| UI screenshots for README         |



## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

Made by Aryan Thombre

- GitHub: [@aryan732003](https://github.com/aryan732003)
- LinkedIn: [@aryan732003](https://www.linkedin.com/in/aryan732003)

---

> If you found this project helpful, feel free to ⭐ star the repo!
