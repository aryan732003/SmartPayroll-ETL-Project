# helpers.py or services.py
from model import Employees, Payroll

def get_employee_by_id(employee_id):
    return Employees.query.get(employee_id)

def get_payroll_by_employee_id(employee_id):
    return Payroll.query.filter_by(EmployeeID=employee_id).first()
