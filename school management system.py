class Student:
    school_name = 'XXXXX'     #classVariable
    student_Dictionary = {}   #class variable dictionary to store objects
    
    def __init__(self):                #To create student object
        self.roll_no = input('\n\tEnter the student Roll Number: ')
        self.name = input('\tEnter the Student Name: ')
        self.phone_number = input('\tEnter the student Phone Number: ')
        self.address = input('\tEnter the student Address: ')
        student_class = input('\tEnter the student class [Ex: 1 2 3 4 5 6 7 8 9 10]: ')
        
        if student_class in StudentClass.classes:       #checking whether the student_class is in classes dictionary
            StudentClass.classes[student_class].studentList.append(self)   #if it is in classes dictionary, we have to add this student to parituclar class
        else: #if no student_class is there
            new_class = StudentClass(student_class) #we need to create new StudentClass object
            new_class.studentList.append(self)           #next add this object to class object's student list.
            StudentClass.classes[student_class] = new_class      #adding class to the classes dictionary
            
        self.student_class = StudentClass.classes[student_class]    #adding class object to the student_class instance variable
        print('\nStudent Added Successfully')
        
        self.getStudent()        #to get the student details

    def getStudent(self):      #to get the student details
        print('\n---STUDENT DETAILS---\n')
        print('\tRoll Number : ', self.roll_no)        
        print('\tName : ', self.name)
        print('\tPhone Number : ', self.phone_number)
        print('\tAdress : ', self.address)
        print('\tClass : ', self.student_class.name)
        print('\tSchool Name : ', self.school_name)
        
    def updateStudent(self):      #to update the student details
        print('\t\tselect option to update student details\n')
        print('\t\t\t1) To Change Student Name')
        print('\t\t\t2) To Change Student Phone Number')
        print('\t\t\t3) To Change Student Address')
        print('\t\t\t4) To Change Student Class\n')
        option = input('\t\tEnter any above given option: ')
        print()
        
        if option in ['1','2','3','4']:
              
            if option=='1':
                self.name = input('\t\t\tEnter the Student New Name: ')
                print('\n\t\tStudent Name Changed Successfully\n')
      
            elif option == '2':
                self.phone_number = input('\t\t\tEnter the Student New Phone Number: ')
                print('\n\t\tStudent Phone Number Changed Successfully\n')
                
            elif option == '3':
                self.address = input('\t\t\tEnter the Student New Address: ')
                print('\n\t\tStudent Address Changed Successfully\n')
                
            elif option == '4':
                  new_class = input('\t\t\tEnter the Student New Class Name: ')
                  self.student_class.studentList.remove(self)
                  try:
                        self.student_class =  StudentClass.classes[new_class]
                        self.student_class.studentList.append(self)
                  except:
                        addClass = StudentClass(new_class)
                        self.student_class = addClass
                        addClass.studentList.append(self)
                  print('\n\t\tStudent Class Changed Successfully\n')
            self.getStudent()
            
        else:
            print('\n\t\t\tYou have choosen Wrong Option')

        
    @classmethod
    def getTotalStudentsCount(cls):
          return len(cls.student_Dictionary)
      
    @classmethod
    def updateSchoolName(cls, new_school_name):
          cls.school_name = new_school_name

class StudentClass:
    classes = {}
    def __init__(self, name):
        self.name = name
        StudentClass.classes[name] = self
        self.studentList = []


def main():
      
    print(f'---Welcome To {Student.school_name} School---\n')
    print('\t1) To Get Student Details')
    print('\t2) To Add New Student')
    print('\t3) To Remove Student')
    print('\t4) To Update Student Details')
    print('\t5) To Update School Name')
    print('\t6) To Get Number Of Students In School')
    print('\t7) To Get All Student Details')
    print('\t8) To Get Any Class Student Details\n')
    
    option = input('Enter any above given option: ')
    
    print()
    if option == '1':
        roll_no = input('\tEnter the Roll Number of a Student: ')
        try:
            Student.student_Dictionary[roll_no].getStudent()
        except:
            print('\t\tYou have Enter the Wrong roll number')
            
    elif option == '2':
        new_student = Student()
        Student.student_Dictionary[new_student.roll_no] = new_student
      
    elif option == '3':
        roll_no = input('\tEnter the Roll Number of a Student: ')
        try:
            student = Student.student_Dictionary.pop(roll_no)
            student.student_class.studentList.remove(student)
            print('\t\t', "'",roll_no, "'", 'Student Deleted Successfully')
        except:
            print('\t\tNo student there to delete')
            
    elif option == '4':
        roll_no = input('\tEnter the Roll Number of a Student: ')
        print()
        try:
            Student.student_Dictionary[roll_no].updateStudent()
        except:
            print('\n\t\tYou have Enter the Wrong roll number')
            
    elif option == '5':
        new_school_name = input('\tEnter the New School Name: ').upper()
        Student.updateSchoolName(new_school_name)
        print('School Name Changed Succesfully')
        
    elif option == '6':
        print('Total Number Of Students In School: ',Student.getTotalStudentsCount())
        
    elif option == '7':
        if Student.student_Dictionary:
              print('Total Number Of Students In School: ',Student.getTotalStudentsCount())
              print('\nTotal Student List with Details\n')
              for sNo, student in enumerate(Student.student_Dictionary.values()):
                    print('Student - ', sNo+1)
                    student.getStudent()
                    print()
        else:
              print('\tNo Students There')
              
    elif option == '8':
        try:
              students = StudentClass.classes[input('\tEnter the Class Name: ')]
              print('\nStudents of class - ', students.name)
              print(f'\nTotal Number Of Students In Class {students.name}: {len(students.studentList)}')
              print()
              for sNo, student in enumerate(students.studentList):
                    print('\tStudent - ',sNo+1)
                    print()
                    student.getStudent()
        except:
              print('\nYou Enter Wrong Class Name or No students There')


if __name__ == '__main__':
      option = 'y'
      while option == 'y':
            main()
            option = input('\nDo you want to Continue [y/n?]: ')
            print()
