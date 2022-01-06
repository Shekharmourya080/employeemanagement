from designation.models import Designation

class DesignationDto:
    def __init__(self, designation: Designation):
        self.id = designation.id
        self.designationName = designation.designationName
