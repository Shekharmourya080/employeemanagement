from department.models import Department


class DepartmentDto:
    def __init__(self, department:Department):
        self.deptName = department.deptName
        self.deptContactPerson = department.deptContactPerson
