import random
import sys
from itertools import *
from employee import Employee

if __name__ == '__main__':
    emp_list = []

    for item in range(10):
        emp = Employee.get_employee_instance()
        emp_list.append(emp)


    # print(emp_list)
    def get_employees_by_dept(dept):
        #result = list(filter(lambda emp: emp.empDept == dept, emp_list))
        result=groupby(emp_list,lambda emp:emp.empDept==dept)
        for key,lst in result:
            print(key,list(lst))
        #return result


    def get_employee_by_role(role):
        return list(filter(lambda emp: emp.empRole == role, emp_list))


    def get_employee_max_salary(role):
        emps = get_employee_by_role(role)
        emps.sort(key=lambda emp: emp.empSalary)
        return emps[0]




    def get_rating_list():
        rating_list = []
        for item in emp_list:
            rating = item.empRating
            rating.append(item.empName)
            rating_list.append(item.empRating)
        ans = list(starmap(lambda r1, r2, r3, name: (r1 + r2 + r3, name), rating_list))
        print(ans)
        finalans = ans.sort(key=lambda record: record[0], reverse=True)
        print(ans)
        return rating_list


    def group_by_gender(gndr):
        gender_list = []
        for item in emp_list:
            if item.empGender == gndr:
                gender_list.append(item)
        print("Gender: ", gender_list)

    def get_max_skill():
        mxskill_list=[]
        for item in emp_list:
            mxskill=item.empSkill
            mxskill.append(item.empName)
            mxskill_list.append(item.empSkill)
        mxskiter=groupby(mxskill_list,lambda x:len(x))

        maxskillset=[]
        for key,val in mxskiter:
            print(key,list(val))
            maxskillset.append(key)

        print(mxskill_list)






    #print("-"*20,"FIND DEPARTMENT","-"*20)
    #print(get_employees_by_dept('JAVA'))
    # print("-"*20,"FIND EMPLOYEE ROLE","-"*20)
    # print(get_employee_by_role('MANAGER'))
    # print("-"*20,"FIND MAX SALARY","-"*20)
    # print(get_employee_max_salary('MANAGER'))
    print(get_max_skill())
    # print(get_rating_list())
    # print(group_by_gender(0))
