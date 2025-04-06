from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import SQLALCHEMY_TRACK_MODIFICATIONS, SQLALCHEMY_DATABASE_URI, SECRET_KEY
from extentions import db  
from flask import make_response
from flask import send_file
from reportlab.pdfgen import canvas
from services import get_employee_by_id, get_payroll_by_employee_id
import csv
import io
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY  
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)  
migrate = Migrate(app, db)

from model import Employees, Payroll, Designations 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project-display')
def project_display():
    return render_template('project_display.html')

@app.route('/workflow')
def workflow_database():
    return render_template('workflow_database.html')

@app.route('/etl')
def etl():
    return render_template('etl.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


@app.route('/employees')
def showEmployees():
    search_query = request.args.get('search', '')
    if search_query:
        employees = Employees.query.filter(
            Employees.EmployeeName.ilike(f'%{search_query}%')
        ).all()
    else:
        employees = Employees.query.all()
    
    designations = Designations.query.all()
    payroll_data = {p.EmployeeID: p for p in Payroll.query.all()}

    return render_template(
        'employees.html',
        employees=employees,
        search_query=search_query,
        designations=designations,
        payroll_data=payroll_data
    )


@app.route('/employee/<int:employee_id>')
def employeeDetails(employee_id):
    employee = Employees.query.get(employee_id)
    designation = Designations.query.get(employee.DesignationID)
    payroll = Payroll.query.filter_by(EmployeeID=employee_id).first()

    if payroll:
        net_salary = (
            payroll.BasicPay + payroll.HouseRentAllowance + payroll.MedicalAllowance +
            payroll.SpecialAllowance + payroll.OtherEarnings
        ) - (
            payroll.ProvidentFund + payroll.IncomeTax + payroll.ProfessionalTax +
            payroll.OtherDeductions + payroll.LeaveDeductionAmount
        )
    else:
        net_salary = None

    return render_template('employee_details.html', employee=employee, designation=designation, payroll=payroll, net_salary=net_salary)


@app.route("/designations")
def showDepartments():
    designations = Designations.query.all()
    return render_template('designations.html', designations=designations)


@app.route('/employee/<int:employee_id>/download_csv')
def download_employee_csv(employee_id):
    employee = Employees.query.get(employee_id)
    payroll = Payroll.query.filter_by(EmployeeID=employee_id).first()

    if not payroll:
        return "No payroll data found.", 404

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(['Field', 'Value'])
    writer.writerow(['Employee Name', employee.EmployeeName])
    writer.writerow(['Designation ID', employee.DesignationID])
    writer.writerow(['Basic Pay', payroll.BasicPay])
    writer.writerow(['HRA', payroll.HouseRentAllowance])
    writer.writerow(['Medical Allowance', payroll.MedicalAllowance])
    writer.writerow(['Special Allowance', payroll.SpecialAllowance])
    writer.writerow(['Other Earnings', payroll.OtherEarnings])
    writer.writerow(['Provident Fund', payroll.ProvidentFund])
    writer.writerow(['Income Tax', payroll.IncomeTax])
    writer.writerow(['Professional Tax', payroll.ProfessionalTax])
    writer.writerow(['Other Deductions', payroll.OtherDeductions])
    writer.writerow(['Leave Deduction Amount', payroll.LeaveDeductionAmount])

    net_salary = (
        payroll.BasicPay + payroll.HouseRentAllowance + payroll.MedicalAllowance +
        payroll.SpecialAllowance + payroll.OtherEarnings
    ) - (
        payroll.ProvidentFund + payroll.IncomeTax + payroll.ProfessionalTax +
        payroll.OtherDeductions + payroll.LeaveDeductionAmount
    )
    writer.writerow(['Net Salary', net_salary])

    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = f'attachment; filename=Payroll_{employee.EmployeeName}.csv'
    response.headers['Content-Type'] = 'text/csv'

    return response

@app.route('/employee/<int:employee_id>/pdf')
def download_employee_pdf(employee_id):
    employee = get_employee_by_id(employee_id)
    payroll = get_payroll_by_employee_id(employee_id)

    if not employee or not payroll:
        return "Employee or payroll data not found", 404

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    
    pdf.setFont("Helvetica", 16)
    pdf.drawString(50, 800, f"Employee Payroll Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 770, f"Name: {employee.EmployeeName}")
    pdf.drawString(50, 750, f"Email: {employee.Email}")
    pdf.drawString(50, 730, f"Phone: {employee.PhoneNumber}")

    pdf.drawString(50, 700, f"Basic Pay: ₹{payroll.BasicPay}")
    pdf.drawString(50, 680, f"HRA: ₹{payroll.HouseRentAllowance}")
    pdf.drawString(50, 660, f"Medical Allowance: ₹{payroll.MedicalAllowance}")
    pdf.drawString(50, 640, f"Special Allowance: ₹{payroll.SpecialAllowance}")
    pdf.drawString(50, 620, f"Other Earnings: ₹{payroll.OtherEarnings}")
    pdf.drawString(50, 600, f"Provident Fund: ₹{payroll.ProvidentFund}")
    pdf.drawString(50, 580, f"Income Tax: ₹{payroll.IncomeTax}")
    pdf.drawString(50, 560, f"Professional Tax: ₹{payroll.ProfessionalTax}")
    pdf.drawString(50, 540, f"Other Deductions: ₹{payroll.OtherDeductions}")
    pdf.drawString(50, 520, f"Leave Deduction: ₹{payroll.LeaveDeductionAmount}")

    pdf.save()

    buffer.seek(0)
    return make_response(buffer.read(), {
        'Content-Type': 'application/pdf',
        'Content-Disposition': f'attachment; filename=employee_{employee_id}_payroll.pdf'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
