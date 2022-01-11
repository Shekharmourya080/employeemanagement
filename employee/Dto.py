from department.Dto import DepartmentDto
from designation.Dto import DesignationDto
from employee.models import EmployeeAdd


class EmployeeDto:
    def __init__(self, employee):
        self.id = employee.id
        self.firstName = employee.firstName
        self.lastName = employee.lastName
        self.middleName = employee.middleName
        self.salary = employee.salary
        self.dateOfJoining = employee.dateOfJoining
        self.department: DepartmentDto = DepartmentDto(employee.deptId)
        self.designation: DesignationDto = DesignationDto(employee.desId)

class EmployeeAddDto:

    def __init__(self, employee_add: EmployeeAdd):
        self.id = employee_add.id
        self.EmpState = employee_add.EmpState
        self.EmpDistrict = employee_add.EmpDistrict
        self.EmpContact = employee_add.EmpContact
        self.Employee = EmployeeDto(employee_add.empid)
