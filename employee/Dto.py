from department.Dto import DepartmentDto
from designation.Dto import DesignationDto


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
