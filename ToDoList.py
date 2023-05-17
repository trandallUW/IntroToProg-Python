# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# trandallUW, 05/14/23,Added code to start assignment 5
# trandallUW, 05/16/23,Added final code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None  # An object that represents a file
strFile = "ToDoList.txt"
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "Task"  # Key - Task
strPriority = "Priority"  # Value - Priority
strUserTask = ""  # User choice for Task
strUserPriority = "" # User choice for Priority


# -- Processing -- #
# Step 1 - When the program starts, load any data that is
# in a text file called ToDoList.txt into a python list of dictionaries rows
objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {strTask: strData[0], strPriority: strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
strMenu = ("""                
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

# Begin loop based on user menu choice
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # add a line space for formatting

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("{:<20} {:<20}".format('TASK', 'PRIORITY'))   # Header
        print("{:<20} {:<20}".format('____', '________'))   # Separator
        for row in lstTable:
            print("{:<20} {:<20}".format(row[strTask], row[strPriority]))
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strUserTask = input("Enter a task: ")
        strUserPriority = input("Enter a priority: ")
        dicRow = {strTask:strUserTask, strPriority:strUserPriority}
        lstTable.append(dicRow)
        print("Task added to list! ") # User confirmation message
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemove = input("What task would you like to remove?: ")
        for row in lstTable:
            if row[strTask].lower() == strRemove.lower():
                lstTable.remove(row)
                print(strRemove + " - Task removed!")  # User confirmation message
            else:
                print("Task not found") # User message that item was not found
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row[strTask])+","+str(row[strPriority]+"\n"))
        objFile.close()
        print("Data saved to " + strFile + "!")  # User confirmation message
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print ("Exit program is complete")  # Display to user that program has ended
        break  # and Exit the program

