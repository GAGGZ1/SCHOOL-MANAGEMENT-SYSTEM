
# ***************************************************************
#                   SCHOOL Management System
# ****************************************************************

# ***************************************************************
#                   Packages USED IN PROJECT
# ****************************************************************
import mysql.connector as a
con = a.connect(host="localhost", user="root", passwd="9907",)
c = con.cursor()
# TO BE RUN ONLY ONCE
# ***************************************************************
#                   Creating DATABASE/TABLES USED IN PROJECT
# ****************************************************************

c.execute("create database school")
c.execute("use school")

c.execute("create table student(name char(30),class int,roll_no int,address char(50),phone int)")
c.execute("create table teacher(name char(30),post char(30),salary int,address char(220),phone int,acno int)")
c.execute("create table cattendence(year int,month char(30),date varchar(30),class varchar(30),absent varchar(220))")
c.execute("create table tattendence(year int,month char(30),date varchar(30),absent varchar(220))")
c.execute("create table fees(name char(30),class int,roll_no int,Month varchar(22),fees int,date int)")
c.execute("create table salary(name char(30),month varchar(30),paid varchar(234))")
# CREATING DEAFULT TABLE


def deaf():
    c = con.cursor()
    c.execute("create table deafaultstudent(name char(30),class varchar(30),roll_no int,address varchar(220),phone int)")
    c.execute("insert into deafaultstudent(name,class,roll_no,address,phone) values('{}',{},{},'{}',{})".format(
        'raj kapoor', 12, 10, 'rdr', 233455))
    c.execute("insert into deafaultstudent(name,class,roll_no,address,phone) values('{}',{},{},'{}',{})".format(
        'jatin kalra', 12, 1, 'dineshpur', 238655))
    c.execute("select*from deafaultstudent")
    print("select from this table any student you want to remove")
    for i in c:
        print(i)
    l = int(input("class :"))
    r = int(input("Roll no:"))
    k = "delete from deafaultstudent where roll_no={} and class={}".format(
        r, l)
    c.execute(k)
    con.commit()
    print("STUDENT DETAILS DELETED SUCESSFULLY")
    print(">-------------------------<")
    main()
# TO STORE STUDENT DEATILS


def ast():
    n = int(input("class:"))
    m = input("names:")
    p = int(input("enter roll:"))
    ph = int(input("enter phone:"))
    d = input("enter address:")
    k = "insert into student(class,roll_no,phone,name,address) values({},{},{},'{}','{}')".format(
        n, p, ph, m, d)
    c = con.cursor()
    c.execute(k)
    con.commit()
    print("STUDENT ADDED sucessfully")
    print(">-------------------------<")
    main()

# TO REMOVE STUDENT


def rst():
    c = con.cursor()
    z = "select*from student"
    c.execute(z)
    for i in c:
        print(i)
    l = int(input("Class:"))
    r = int(input("Roll no:"))
    c = con.cursor()
    k = "delete from student where roll_no={} and class={}".format(r, l)
    c.execute(k)
    con.commit()
    print("STUDENT DELETED SUCCESSFULLY.")
    print(">-------------------------<")
    main()

# TO ADD TEACHER


def addt():
    n = input("teacher name:")
    c = input("post:")
    r = int(input("Salary:"))
    a = input("address:")
    p = int(input("phone:"))
    m = int(input("Account no:"))
    k = "insert into teacher(name,post,salary,address,phone,acno) values('{}','{}',{},'{}',{},{})".format(
        n, c, r, a, p, m)
    c = con.cursor()
    c.execute(k)
    con.commit()
    print("TEACHER ADDED sucesssfully")
    print(">-------------------------<")
    main()


# TO REMOVE TEACHER

def remt():
    c = con.cursor()
    z = "select*from teacher"
    c.execute(z)
    for i in c:
        print(i)
    m = input("name:")
    r = int(input("Ac no. :"))
    c = con.cursor()
    k = "delete from teacher where acno={}".format(r)

    c.execute(k)
    con.commit()
    print("TEACHER REMOVED")
    print(">-------------------------<")


# TO STORE ABSENT STUDENT NAME
def abclass():
    y = int(input("year:"))
    m = input("month:")
    d = eval(input("date:"))
    cl = int(input("class:"))
    ab = input("name of absent students:")
    sql = "insert into cattendence values({},'{}','{}',{},'{}')".format(
        y, m, d, cl, ab)
    c = con.cursor()
    c.execute(sql)
    con.commit()
    print("ABSENT STUDENT ADDED SUCCESSFULLY.")
    print(">-------------------------<")
    main()


# TO STORE ABSENT TEACHER NAME
def abteacher():
    y = int(input("year:"))
    m = input("month:")
    d = int(input("date:"))
    ab = input("name of absent Teacher:")
    sql = "insert into tattendence values({},'{}','{}','{}')".format(
        y, m, d, ab)
    c = con.cursor()
    c.execute(sql)
    con.commit()
    print("ABSENT TEACHER ADDED SUCCESSFULLY.")
    print(">-------------------------<")
    main()

# TO STORE FEES OF STUDENT


def submitf():
    n = input("student name:")
    c = int(input("class :"))
    r = input("Roll no:")
    m = input("month")
    f = int(input("fees:"))
    d = int(input("date:"))
    sql = "insert into fees values('{}',{},'{}','{}',{},{})".format(
        n, c, r, m, f, d)
    c = con.cursor()
    c.execute(sql)
    con.commit()
    print("FEES SUBMITTED sucesssfully")
    print(">-------------------------<")
    main()

# TO STORE SALARY DEATILS


def pays():
    n = input("teacher name:")
    m = input("Month:")
    p = input("PAID Yes/No:")
    sql = "insert into salary values('{}','{}','{}')".format(n, m, p)
    c = con.cursor()
    c.execute(sql)
    con.commit()
    print("data entered sucesssfully")
    print(">-------------------------<")
    main()

# TO DISPLAY STUDENTS


def dclass():
    sql = "select*from student "
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("NAME:", i[0])
        print("CLASS:", i[1])
        print("ROLL NO:", i[2])
        print("ADDRESS:", i[3])
        print("PHONE:", i[4])
        print(">-------<")
    print(">-------------------------<")
    main()


# TO DISPLAY TEACHER
def dteacher():
    sql = "select*from teacher"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("NAME:", i[0])
        print("POST", i[1])
        print("SALARY:", i[2])
        print("ADDRESS:", i[3])
        print("PHONE:", i[4])
        print("ACNO:", i[5])
        print(">-------<")
    print(">-------------------------<")
    main()
# ***************************************************************
# THE MAIN FUNCTION OF PROGRAM
# ****************************************************************
# The Main()


def main():

    print("""                      JAYCEES PUBLIC SCHOOL

                      1. ADD STUDENT       2. REMOVE STUDENT

                      3. ADD TEACHER        4. REMOVE TEACHER

                      5. CLASS Attendence(ADD ABSENT STUDENTS)

                      6. TEACHER Attendence(ADD ABSENT TEACHERS)

                      7. SUBMIT FEES        8. PAY SALARY

                      9. dISPLAY CLASS      10. TEACHER LIST

        *for removing/displaying teacher first Add Teacher(use "3")*
                              # TO BE RUN ONLY ONCE
""")
    Choice = input("ENTER TASK NO:")
    if (Choice == "1"):
        ast()
    elif (Choice == "2"):
        n = input("you want to remove student from 'default stored table' or table you have 'created now' ??? enter 'd' for default or 'c' for created now: ")
        if n == "c":
            rst()
        else:
            deaf()
    elif (Choice == "3"):
        addt()
    elif (Choice == "4"):
        remt()
    elif (Choice == "5"):
        abclass()
    elif (Choice == "6"):
        abteacher()
    elif (Choice == "7"):
        submitf()
    elif (Choice == "8"):
        pays()
    elif (Choice == "9"):
        dclass()
    elif (Choice == "10"):
        dteacher()
    else:
        print("WRONG CHOICE!!!!!!!!")
        main()


def pasd():
    p = input("PASSWORD:")
    print("use  '1234' to access")

    if p == "1234":
        main()
    else:
        print("access denied!")
        print("Enter again:")
        pasd()


pasd()

# ***************************************************
# ****************  END OF PROJECT ***************
# ***************************************************
