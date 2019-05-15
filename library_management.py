from pymysql import *


class Student:
    
    def __init__(self):
        
        self.con=connect(db="newdbProj",user="root",password="123456",host="localhost")
        self.cur=self.con.cursor()


    
    def Add_Student(self):
        
        stu_id=int (input('Enter the id no of student: '))
        name = input('Enter the name of the student: ')
        cls =int(input('Enter the class of the student: '))
        section = input('Enter the section of the student: ')
        self.cur.execute("insert into student values('%d','%s','%d','%s')"%(stu_id,name,cls,section))
        self.con.commit()

        print('Record Added')

    def showdetail(self):
    
        self.cur.execute("select * from student")
        result=self.cur.fetchall()
		
        print("==================================")
        print("ID\tName\tclass\tsection ")	
        print("==================================")
        for x in result:
                
            print("%d\t%s\t%d\t%s"%(x[0],x[1],x[2],x[3]))
        print("===================================")

    


    def deletestudent(self):
            
        stu_id = int(input("Enter ID :  "))
        self.cur.execute("delete from student where stu_id = %d"%(stu_id))
        self.con.commit()
        print("Record Deleted.")

    def updatestudent(self):
        
            
        stu_id = int(input("Enter Id : "))
        name = input("Enter Name  : ")
        cls = int(input("Enter Class: "))
        section=input("Enter section: ")
        self.cur.execute("update student set name='%s',cls='%d',section='%s' where stu_id = %d"%(name,cls,section,stu_id))
        self.con.commit()
        print('Record Updated')




obj=Student()        

class Book:

    def __init__(self):

        self.con=connect(db="newdbProj",user="root",password="123456",host="localhost")
        self.cur=self.con.cursor()
        
    def Add_Book(self):

        book_id=int(input('Enter id number of the book: '))
        Isbn=int(input('Enter the Isbn Number of Book: '))
        title=input('Enter the name of the Book: ')
        Writer=input('Enter the Writer name: ')
        
        self.cur.execute("insert into book values(%d,'%s','%s','%s')"%(book_id,Isbn,title,Writer))
        self.con.commit()
        print('Record Added')
        
        
    def Remove(self):

        book_id = int(input("Enter ID :  "))
        self.cur.execute("delete from book where book_id = %d"%(book_id))
        self.con.commit()
        print("Record Deleted.")


    def show_books(self):
        self.cur.execute("select * from book")
        result=self.cur.fetchall()
       
        print("==================================") 
        print("Book_id\tIsbn\tTitle\tWriter ")	
        print("==================================")
        for x in result:
                
            print("%d\t%s\t%s\t%s"%(x[0],x[1],x[2],x[3]))
        print("===================================")
       

        
        
obj1=Book()

import time
class Issued_Book:

    def __init__(self):

        self.con=connect(db="newdbProj",user="root",password="123456",host="localhost")
        self.cur=self.con.cursor()
    


    def requestBook(self):

         
        self.cur.execute("select * from book")
        result=self.cur.fetchall()
       
        print("==================================") 
        print("Book_id\tIsbn\tTitle\tWriter ")	
        print("==================================")
        for x in result:
                
            print("%d\t%s\t%s\t%s"%(x[0],x[1],x[2],x[3]))
        print("===================================")

        Book_Id=int(input('Enter Book Id: '))
        stu_id=int(input("Enter student Id: "))
        a=time.localtime()
        issue_date = f"{a.tm_year}-{a.tm_mon}-{a.tm_mday}"
        print("issue Date : ",issue_date)
        
        r_date = a.tm_mday+7
        return_date= f"{a.tm_year}-{a.tm_mon}-{r_date}"
        print("Your Return Date : ",return_date)

 
        self.cur.execute("insert into issue values(%d,%d,'%s','%s')"%(Book_Id,stu_id,issue_date,return_date))
        self.con.commit()
        print('Book issues to Student')

    def returnBook(self):

        Book_Id = int(input("Enter Book ID :  "))
        self.cur.execute("delete from issue where Book_Id = %d"%(Book_Id))
        self.con.commit()
        print("Book Returned.")

    def book_status(self):
        self.cur.execute("select * from issue")
        result=self.cur.fetchall()
       
        print("==================================") 
        print("Book_Id\tstu_id\tissue_date\treturn_date ")	
        print("==================================")
        for x in result:
                
            print("%d\t%d\t%s\t%s"%(x[0],x[1],x[2],x[3]))
        print("===================================")

obj2=Issued_Book()
    
        
while True:
    print('==========Library Management System==========')

    
    print('Press 1 for add student')
   # print('press 1 for add: ')
    print('press 2 for  show details: ')
    print('press 3 for update: ')
    print('press 4 for Remove Student: ')
    print('press 5 for Add a book:')
    print('press 6 for Remove Book:')
    print('press 7 for Show Books')
    print('press 8 for Request a book')
    print('press 9 for Return Book')
    print('press 10 for Book Status')
    print('press 0 for Exit')

    


    choice=int(input('Enter your choices: '))

    if choice==1:
        obj.Add_Student()
    elif choice==2:
        obj.showdetail()
    elif choice==3:
        obj.updatestudent()
    elif choice==4:
        obj.deletestudent()
    elif choice==5:
        obj1.Add_Book()
    elif choice==6:
        obj1.Remove()
    elif choice==7:
        obj1.show_books()
    elif choice==8:
        obj2.requestBook()
    elif choice==9:
        obj2.returnBook()
    elif choice==10:
        obj2.book_status()
    elif choice==0:    
        break
    else:
        print('invalid choice')

obj.con.close()




