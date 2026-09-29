# PYTHON PROJECT

# COLLEGE TIME TABLE MANAGEMENT SYSYTEM 

# Time Table of the week

timetable ={"Monday":["English", "Maths"," Computer science"],
            "Tuesday":["Environmental studies", "Maths"," Computer science"],
            "Wednesday":["English", "Maths"," Computer science" , "Computer science"],
            "Thursday":["Environmental studies", "Maths"," Computer science"],
            "Friday":[ "Maths"," Computer science" ,"Maths"]}

#Count the number of days


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# DEFINING THE TIMETABLES

def show_timetable():
    print("\n========== COMPLETE TIME TABLE==================")

    for day in days:
        print("\n" + day)
        print("-" * 25)

    for i in range(len(timetable[day])):
        print("period" , i+1 ,":", timetable[day][i])

# defining the days 

def show_day():
    day = input("\nEnter day: ").capitalize()

    if day in timetable:
       print("\n ==========" + day + "==========")

       for i in range (len(timetable[day])):
           print("period " , i + 1 ," :" ,timetable[day][i])
    else:
        print("Invalid day !")



# DEFINING NUMBER OF SUBJECT IN A WEEK

def find_subject():
    subject = input("\nEnter subject : ").lower()
    found = False

    for day in days :
        for i in range (len(timetable[day])):
            if timetable[day][i].lower() == subject:
                print(subject.title(), "is on" , 
                      day ,
                      "- period " , i + 1 
                )
                found = True 


            if not found:
                print("Subject not found !")

    # DEFINING THE SUBJECT

def add_subject():
    day = input ("\n Enter day :").caitalize()

    if day in timetable:
        subject = input("Enter subject : ")
        timetable[day].append(subject)
        print("Subject added successfully !")
    else:
        print("Invalid day!")


while True:
    print("\n============ COLLEGE TIME TABLE MANAGER ====================")
    print("1. Show complete Timetable")
    print("2. show Time table for a day")
    print("3. find a subject")
    print("4. Add a subject")
    print("5. Exit")

    choice = input("\nEnter your choice :")


    if choice == "1":
        show_timetable()

    elif choice == "2":
        show_day()

    elif choice == "3":
        find_subject()

    elif choice == "4":
        add_subject()

    elif choice == "5":
        print("\nThank you for using Timetbale Manger!")
        break
    else:
        print("\=================SORRY FOR THE INCONVIENCE INVALID CHOICE PLEASE TRY AGAIN=========================")
        #end of the code
        
    

                    

        
 
