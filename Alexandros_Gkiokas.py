import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hr"
)
cursor = conn.cursor()

class employee:
    #Create a Constructor
    def __init__(self, Employee_Code, Name, Surname, Email, Telephone, Address, Salary):
            self.Employee_Code = Employee_Code
            self.Name = Name
            self.Surname = Surname
            self.Email = Email
            self.Telephone = Telephone
            self.Address = Address
            self.Salary = Salary
#Add an employee function
def add_employee(employee, cursor, conn):
        Employee_Code = input("Enter Employee_Code: ")
        Name = input("Enter Name: ")
        Surname = input("Enter Surname: ")
        Email = input("Enter Email: ")
        Telephone = input("Enter Telephone: ")
        Address = input("Enter Address: ")
        Salary = float(input("Enter Salary: "))
        values = (Employee_Code, Name, Surname, Email, Telephone, Address, Salary)

        # create a cursor
        cursor = conn.cursor()
        # Add an employee in the employee table
        query = "INSERT INTO employee (Employee_Code, Name,Surname, Email, Telephone, Address, Salary) VALUES (%s, %s,%s, %s, %s, %s, %s)"
        cursor.execute(query, values)
        conn.commit()
        print("Employee added successfully!")
        conn.commit()
        cursor.close()
        conn.close()


#View all employees function
def view_employee(cursor):
    # create a cursor
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.commit()
    conn.close()

#Edit an employee function
def edit_employee(Employee_Code,column,value):
    # create a cursor
    cursor = conn.cursor()
    # Edit an employee from the employee table
    sql = "UPDATE employee SET {} = %s WHERE Employee_Code = %s" .format(column)
    values = (value,Employee_Code)

    cursor.execute(sql,values)

    print("Employee details updated successfully!")

    conn.commit()
    conn.close()
#Promote an employee function
def employee_promotion(Employee_Code, value):
    # create a cursor
    cursor = conn.cursor()
    # Promote an employee from the employee table
    sql = "UPDATE employee SET Salary = Salary + %s WHERE Employee_Code = %s"
    values = (value, Employee_Code)
    cursor.execute(sql, values)
    print("Employee promoted successfully!")
    conn.commit()
    conn.close()
#Delete an employee function
def delete_employee(Employee_Code):
    #crate a cursor
    cursor = conn.cursor()

    # Delete an employee from the employee table
    sql= ("DELETE FROM employee WHERE Employee_Code = %s" )
    values = (Employee_Code,)
    cursor.execute(sql,values)
    print("Employee deleted successfully")
    conn.commit()
    cursor.close()

#Search an employee function
def employee_search(Employee_Code):
    cursor = conn.cursor()
    # Search an employee from the employee table with their key (Employee_Code)
    sql= "SELECT * FROM employee WHERE Employee_Code = %s"
    values = (Employee_Code,)
    cursor.execute(sql,values)

    result = cursor.fetchone()

    print("Employee_Code: Name: Surname:       Email:             Telephone:        Address:        Salary:")
    print(result[0], "       ", result[1], "    " , result[2],"   ", result[3],"    ",result[4],"    ",result[5],"   ",result[6],"   ", )
    conn.commit()
    cursor.close()
#Exit
def exit_program():
            print("Exiting program...")
            quit()
#Menu to call the functions
def menu():
        while True:
            # Show the menu
            print("1. Add Employee")
            print("2. View Employees Details")
            print("3. Edit Employee")
            print("4. Employee Promotion")
            print("5. Delete Employee")
            print("6. Employee Search")
            print("7. Exit")

            # Get the user's choice
            choice = input("Enter your choice: ")

            # Execute the corresponding function
            if choice == "1":
                    add_employee(employee, cursor, conn)
            elif choice == "2":
                view_employee(cursor)
            elif choice == "3":
                  Employee_Code = int(input("Enter Employee Code to edit: "))
                  column = input("Enter column name to edit: ")
                  value = input("Enter new value: ")
                  edit_employee(Employee_Code,column,value)
            elif choice == "4":
                 Employee_Code = int(input("Enter Employee Code to promote: "))
                 value = float(input("Enter promotion value: "))
                 employee_promotion(Employee_Code, value)
            elif choice == "5":
                    Employee_Code = int(input("Enter Employee Code to delete: "))
                    delete_employee(Employee_Code)
            elif choice == "6":
                    Employee_Code = int(input("Enter Employee Code : "))
                    employee_search(Employee_Code)
            elif choice == "7":
                    exit_program()
            else:
                    print("Invalid choice.")
                    conn.commit()
menu()