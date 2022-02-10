class Department:
    def __init__(self, did, dname):
        self.deptId = did
        self.deptName = dname

    def __str__(self):
        return "{} {}".format(self.deptId,self.deptName)

    def __repr__(self):
        return str(self)
