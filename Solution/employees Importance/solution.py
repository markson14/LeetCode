"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    
    def dfs(self, employee):
            self.value += employee.importance
            if not employee.subordinates: return
            for i in employee.subordinates:
                for j in self.employees:
                    if j.id == i:
                        self.dfs(j)
                        
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.employees = employees
        self.value = 0
        for employee in employees:
            if id == employee.id:
                self.dfs(employee)
        return self.value
            