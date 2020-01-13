import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="contact")


"""
CREATE database contact;

USE contact;

CREATE TABLE `contact_book` (
	`mobile_no` INT(10),
	`name` VARCHAR(50),
	`address` VARCHAR(200),
	`email` VARCHAR(50)
);

"""




mycursor=mydb.cursor()



def add_contact():

    L=[]

    mobile_no=int(input("Enter Moobile number(10 Digits): "))

    L.append(mobile_no)

    name=input("Enter the Name : ")

    L.append(name)

    address=input("Enter address : ")

    L.append(address)

    email=input("Enter the email : ")

    L.append(email)

    cont=(L)

    sql="insert into contact_book(mobile_no,name,address,email) values (%s,%s,%s,%s)"

    mycursor.execute(sql,cont)

    mydb.commit()



def search_contact():

    print("Select the search criteria : ")

    print("1. Mobile_no")

    print("2. Name")
     
    print("3. Address")

    print("4. email")

    print("5. All contacts")

    ch=int(input("Enter the choice : "))

    if (ch==1):

        s=input("Enter mobile Nummber : ")

        rl=(s,)

        sql="select * from contact_book where mobile_no=%s"

        mycursor.execute(sql,rl)

    elif (ch==2):

        nm=input("Enter Name : ")

        rl=(nm,)

        sql="select * from contact_book where name='%s';"%nm
        mycursor.execute(sql)

    elif (ch==3):

        s=input("Enter address : ")

        rl=(s,)

        sql="select * from contact_book where address=%s;"

        mycursor.execute(sql,rl)

    elif (ch==4):

        s=input("Enter email : ")

        rl=(s,)

        sql="select * from contact_book where email=%s;"

        mycursor.execute(sql,rl)

    elif (ch==5):

        sql="select * from contact_book;"

        mycursor.execute(sql)

    res=mycursor.fetchall()

    print("The contact details are as follows : ")
     
    print("(mobile_no, name,  address,     email )")

     
    for x in res:

        print(x)

def view_contact():

    sql="select * from contact_book;"

    mycursor.execute(sql)
    
    res=mycursor.fetchall()

    print("The contact details are as follows : ")
     
    print("(mobile_no, name, address,email )")

     
    for x in res:

        print(x)



def del_contact():

    name=input("Enter the name to be deleted : ")

    rl=(name,)

    sql="delete from contact_book where name=%s"

    mycursor.execute(sql,rl)

    mydb.commit()





def Main_Menu():

    print("Enter 1 : TO ADD NEW CONTACT")

    print("Enter 2 : TO VIEW CONTACT ")

    print("Enter 3 : TO SEARCH CONTACT ")

    print("Enter 4 : TO DELETE CONTACT")

    try: #Using Exceptions For Validation

        userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    except ValueError:

        exit("\nHy! That's Not A Number") #Error Message
        



    else:

        print("\n") #Print New Line

    if(userInput==1):

        add_contact()

    elif (userInput==2):

        view_contact()

    elif (userInput==3):
        
        search_contact()

    elif (userInput==4):

        del_contact()

    else:

        print("Enter correct choice. . . ")



Main_Menu()



ch = input("\nwant to continue Y/N: ")

while(ch == 'Y' or ch=='y'):


    Main_Menu()

    ch = input("\nwant To Run Again Y/N: ")
