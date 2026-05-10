# School Management System - Version 1
from abc import ABC , abstractmethod

class Person(ABC):
    def __init__(self,name,role):
        self.school="kcc"
        self.name=name
        self.role=role
    @abstractmethod
    def introduction(self):
        print(f"{self.name} ---> {self.role} ---> {self.school}")

class Principal(Person):
    def __init__(self, name, role):
        super().__init__(name,role)
    def introduction(self):
        return super().introduction()


class Teacher(Person):
    def __init__(self, name, role,subject,salary):
        super().__init__(name,role)
        self.subject=subject
        self.__salary=salary
    def introduction(self):
        return super().introduction()
    def Teacher_sub_change(self,new_sub):
        if new_sub==self.subject:
            print(f"{self.name} already teaches {new_sub}")
        else:
            self.subject=new_sub
            print("data updated succesfully")
            print(f"{self.name} teaches {self.subject} ")
    def salary_change(self,new_salary):
        if new_salary<0:
            print("invalid salary")
        else:
            self.__salary=new_salary
            print("salary updated succesfully")
    @property
    def Salary(self):
        return self.__salary
    def __str__(self):
        return f"{self.name} ---> {self.role}"
    
class Student(Person):
    s_id=[]
    def __init__(self, name, role,student_id):
        super().__init__(name, role)
        self.__studentid=student_id
        Student.s_id.append(student_id)
    def introduction(self):
        return super().introduction()
    def change_student_id(self,new_id):
        if new_id<0:
            print("invalid id")
        else:
            self.__studentid=new_id
    @property
    def student_id(self):
        return self.__studentid
    def __str__(self):
        return f"""Name---->{self.name}
        student Id---> {self.__studentid}"""


p_data=[]
t_data=[]
s_data=[]
ch=input("who are you? (Principal/Teacher/Student)---> ").strip()
if ch.isalpha():
    if ch.lower()=="principal":
        while True:
            option=input("""want to add new principal?(add) 
                        want to check existing principal data (search) --> """).strip()
            if option.isalpha():
                if option.lower()=="add":
                    while True:
                        name=input("enter Principal name--> ").strip().title()
                        if name.isalpha():
                            role="Principal"
                            adding=Principal(name,role)
                            p_data.append(adding)
                        else:
                            print("invalid name dont use symbol or number!!")
                        option=input("want to add more? (yes/no)").strip().lower()
                        if option=="no":
                            break
                        if option!="yes" and option!="no":
                            print("enter yes or no terminated")
                            break
                elif option.lower()=="search":
                    name=input("enter name you want to search---> ").strip().title()
                    f=False
                    for i in p_data:
                        if i.name==name:
                            i.introduction()
                            f=True
                    if f==False:
                        print(f"{name} name principal doesn't exist")
                else:
                    print("entered a wrong input")
            else:
                print("enter a wronng input")
            ch2=input("want to do add or search again (yes/no)").strip().lower()
            if ch2=="no":
                print("program is off")
                break
            if ch2!="no" and ch2!="yes":
                print("enter the wrong input loop is terminating")
                break
    elif ch.lower()=="teacher":
        while True:
            option=input("""want to add Teacher data? (add)
                         want to find teacher data? (find)
                         want to change subjact? (subject)
                         want to change salary?   (change)
                         want to check salary?    (salary)
                         enter what you want?----------> """).strip().lower()
            
            if option=="add":
                while True:
                    name=input("enter teacher name---> ").strip().title()
                    if name.isalpha():
                        role="Teacher"
                        sub=input("enter subject---> ").strip().capitalize()
                        if sub.isalpha():
                            try:
                                salary=int(input("enter salary---> "))
                                teach=Teacher(name,role,sub,salary)
                                t_data.append(teach)
                                print("data added sucesfully")
                            except Exception:
                                print("invalid salary")
                        else:
                            print("invalid subject")
                    else:
                        print("invalid name")
                    ch=input("do you want to add more data? (yes/no)---> ").strip().lower()
                    if ch=="no":
                        print("adding data is off")
                        break
                    if ch!="yes":
                        print("enter wrong input program is off")
                        break
            
            elif option=="find":
                name=input("enter the teacher name---> ").strip().title()
                if name.isalpha():
                    sub=input("enter the subject---> ").strip().capitalize()
                    if sub.isalpha():
                        f=False
                        for i in t_data:
                            if i.name==name and i.subject==sub:
                                i.introduction()
                                f=True
                        if f==False:
                            print("there is no data")
                    else:
                        print("enter valid subject (dont use symbol or numbers)")
                else:
                    print("enter a valid name")

            elif option=="subject":
                new_sub=input("enter new subject---> ").strip().capitalize()
                if new_sub.isalpha():
                    name=input("enter your Teacher name--> ").strip().title()
                    if name.isalpha():
                        old_sub=input("enter old sub---> ")
                        while True:
                            i=0
                            f=False
                            for i in t_data:
                                if i.name==name and i.subject==old_sub:
                                    i.Teacher_sub_change(new_sub)
                                    print("subject updated")
                                    f=True
                                    break
                            if f==False:
                                print("no data found")
                            else:
                                break
                    else:
                        print("enter valid name")
                else:
                    print("enter valid subject")
            
            elif option=="change":
                name=input("enter name of the person whose salary you want to change:").strip().title()
                if name.isalpha():
                    sub=input("enter teacher subject: ").strip().capitalize()
                    if sub.isalpha():
                        try:
                            new_sal=int(input("enter new sal: "))
                            f=False
                            for i in t_data:
                                if i.name==name and i.subject==sub:
                                    i.salary_change(new_sal)
                                    f=True
                            if f==False:
                                print("no data found")
                        except:
                            print("enter a valid salary")
                    else:
                        print("enter a valid subject")
                else:
                    print("enter a valid name")
            
            elif option=="salary":
                name=input("enter name-->").strip().title()
                if name.isalpha():
                    sub=input("enter subject---> ").strip().capitalize()
                    if sub.isalpha():
                        f=False
                        for i in t_data:
                            if i.name==name and i.subject==sub:
                                print(i.Salary)
                                f=True
                                break
                        if f==False:
                            print("data not found")
                    else:
                        print("valid subject")
                else:
                    print("enter valid name")
            else:
                print("enter a valid input")
            
            ch1=input("want to do more operation? (yes/no)--->").strip().lower()
            if ch1.isalpha():
                if ch1=="no":
                    print("terimnationg the program")
                    break
                if ch1!="yes": 
                    print("enter a yes or no we are terminating program")
                    break
               
    elif ch.lower()=="student":
        while True:
            option3=input("""want to add student data--->(add) 
                        want to find student---------->(find)
                        want to change student id----->(change)
                        what do you want: """).strip().lower()
            if option3=="add":
                while True:
                    s_name=input("enter student name---> ").strip().title()
                    if s_name.isalpha():
                        role="Student"
                        try:
                            s_id=int(input("enter student id--> "))
                            st_data=Student(s_name,role,s_id)
                            s_data.append(st_data)
                            print("data added sucesfully")
                        except:
                            print("enter invalid id")
                    else:
                        print("enter invalid name")
                    ch4=input("want to add more data? (yes/no)---> ").strip().lower()
                    if ch4=="no":
                        print("we stoped adding data")
                        break
                    if ch4!="yes":
                        print("entered wrong input terminating the loop")
                        break
        
            elif option3=="find":
                name=input("enter student name:--> ").strip().title()
                if name.isalpha():
                    try:
                        f=False
                        s_id=int(input("enter student id---> "))
                        for i in s_data:
                            if i.name==name and i.student_id==s_id:
                                f=True
                                i.introduction()
                        if f==False:
                            print("there is no student")
                    except:
                        print("enter valid student id")
                else:
                    print("enter a valid name")
        
            elif option3=="change":
                Student_name=input("enter student name---> ").strip().title()
                if Student_name.isalpha():
                    try:
                        old_id=int(input("enter student id---> "))
                    except:
                        print("enter valid number")
                    try:
                        new_id=int(input("enter studnet new id---> "))
                    except:
                        print("enter valid new id")
                    f=False
                    for i in s_data:
                        if i.name==Student_name and i.student_id==old_id:
                            i.change_student_id(new_id)
                            f=True
                            print("id updated sucesfully")
                    if f==False:
                        print("student id didn't find")
                else:
                    print("enter valid student name")
            ch5=input("do you want to do more operation(yes/no)---> ").strip().lower()
            if ch5=="no":
                print("program off")
                break
            if ch5!="yes":
                print("wrong input program off")
                break
        
            else:
                print("enter a valid input")