from extentions import db

class Employees(db.Model):
    __tablename__ = "Employees"
    EmployeeID = db.Column(db.Integer, primary_key=True)
    EmployeeName = db.Column(db.String(100), nullable=False)
    PhoneNumber = db.Column(db.String(15), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    DesignationID = db.Column(db.Integer, db.ForeignKey("Designations.DesignationID"), nullable=False)

    payroll = db.relationship("Payroll", backref="employee", lazy=True)

class Designations(db.Model):
    __tablename__ = "Designations"
    DesignationID = db.Column(db.Integer, primary_key=True)
    DesignationName = db.Column(db.String(100), nullable=False)

class Payroll(db.Model):
    __tablename__ = "Payroll"
    PayrollID = db.Column(db.Integer, primary_key=True)
    EmployeeID = db.Column(db.Integer, db.ForeignKey("Employees.EmployeeID"), nullable=False)
    BasicPay = db.Column(db.Float, nullable=False)
    HouseRentAllowance = db.Column(db.Float, nullable=False)
    MedicalAllowance = db.Column(db.Float, nullable=False)
    SpecialAllowance = db.Column(db.Float, nullable=False)
    OtherEarnings = db.Column(db.Float, nullable=False)
    ProvidentFund = db.Column(db.Float, nullable=False)
    IncomeTax = db.Column(db.Float, nullable=False)
    ProfessionalTax = db.Column(db.Float, nullable=False)
    OtherDeductions = db.Column(db.Float, nullable=False)
    LeaveDeductionAmount = db.Column(db.Float, nullable=False)
