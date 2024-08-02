import sys 
import os 
import random 
import logging 
from colorama import Fore 
import time 
from itertools import permutations 
program_title='student logging system'
grades=['Poor','Acceptable','excellcent','outstanding']
computer_characters='+0123456789!£"$%^&*()@~#:;/,.|\\`¬[]?'        
capital_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase_letters=[]
for letter in capital_letters:
    lowercase_letters.append(letter.lower())
else:
    pass
subjects=['further maths',
          'further maths'.upper()
          ,'further maths'.title()
          ,'food studies','food studies'.upper()
          ,'food studies'.title()
          ,'art','art'.title(),'art'.upper(),
          'computer science',
          'computer science'.upper(),
          'computer science'.title(),
          'triple science'.upper(),
          'triple science',
          'triple science'.title(),
          'ict',
          'ict'.upper(),
          'ict'.title(),
          'music',
          'music'.title(),
          'music'.upper(),
          'dt'.title(),
          'dt'.upper(),
          'dt',
          'history',
          'history'.upper(),
          'history'.title(),
          'mfl',
          'mfl'.upper(),
          'mfl'.title()]
mysequence=list(range(1,100+1,1))
colors=[Fore.RED,Fore.BLUE,Fore.CYAN,Fore.YELLOW,Fore.GREEN,Fore.RESET]
def loop_over(sequence,delay_time,color):
    for n in sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{color}{n}')
    else:
        print(colors[-1]) 
#Creating a basic logger and configuring it.
student_info_logger=logging.basicConfig(filename='student_information.log',filemode='w',level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')
class Student:
    def __init__(self,student_name,home_address,phone_number,subjects,grade,age):
        self.student_name=student_name 
        self.home_address=home_address 
        self.phone_number=phone_number 
        self.subjects=subjects 
        self.grade=grade 
        self.age=age
    def log_student_name(self):
        logging.info(f'Student Name:{self.student_name}')
      
    def log_student_age(self):
        logging.info(f'Student\'s age:{self.age}')
    def log_home_address_of_student(self):
        logging.info(f'Student\'s home address:{self.home_address}')
        
    def log_phone_number_of_student(self):
        logging.info(f'Student\'s phone number:{self.phone_number}')
        
    def log_students_chosen_subjects(self):
        logging.info(f'Student\'s chosen subjects:{",".join(self.subjects)}')
        
    def assign_grade(self):
        if self.grade<=30:  
          logging.info(f'Grade:{grades[0]}')
        elif self.grade>=40 and self.grade<=70:
          logging.info(f'Grade:{grades[1]}')
        elif self.grade>=70:
          logging.info(f'Grade:{grades[2]}')
    
for text in program_title:
    random_color=random.choice(colors[0:-1])
    print(f'{random_color}{text.upper()}',end='\t')
    time.sleep(0.1)
else:
    print(colors[-1])
    time.sleep(1)
    os.system("cls")
    time.sleep(1)
    student=Student(student_name=None,home_address=None,phone_number=None,subjects=None,grade=None,age=None)
    student_name=input('Enter student name:')
    for ch in student_name:
        if ch in computer_characters:
         logging.error('User Entered an invalid name')
         loop_over(sequence='You entered an invalid name',delay_time=0.1,color=colors[0])
         break 
        else:
            pass
    else:
        student=Student(student_name=student_name,home_address=None,phone_number=None,subjects=None,grade=None,age=None)
        student.log_student_name()
        time.sleep(1)
        try:
            enter_age=int(input('Enter student\'s age:'))
            if enter_age<11 or enter_age>16:
                logging.error('Invalid age has been entered for a student attending high school')
                loop_over(sequence='Error, an invalid age has been entered',delay_time=0.1,color=colors[0])
            else:
                 student=Student(student_name=student_name,home_address=None,phone_number=None,subjects=None,grade=None,age=enter_age)
                 student.log_student_age()
                 time.sleep(1)
                 home_address=input('home_address:')
                 space=' '
                 if space not in home_address and home_address[3]!=space or len(home_address)>7:
                   logging.error('Error, not a valid home address')
                   loop_over(sequence='Error, an invalid home address as been entered.',delay_time=0.1,color=colors[0])
                 else:
                     student=Student(student_name=student_name,home_address=home_address,phone_number=None,subjects=None,grade=None,age=enter_age)
                     student.log_home_address_of_student()
                     time.sleep(1)
                     phone_number=int(input('Enter student\'s phone number:'))
                     if len(str(phone_number))>11 or len(str(phone_number))<11:
                         logging.error('Student\'s phone number does not contain 11 digits.')
                         loop_over(sequence='Error, the Student\'s phone number does not contain 11 digits',delay_time=0.1,color=colors[0])
                     else:
                         student=Student(student_name=student_name,home_address=home_address,phone_number=None,subjects=None,grade=None,age=enter_age)
                         student.log_phone_number_of_student()
                         time.sleep(1)
                         loop_over(sequence='This computer program will now take the name of the subjects the student took\n',delay_time=0.1,color=colors[2])
                         time.sleep(1)
                         subjects_1=[]
                         for x in range(3):
                             enter_subject_alias=input('Enter the name of the subject:')
                             if enter_subject_alias not in subjects:
                                 logging.error('An invalid subject name has been entered')
                                 loop_over(sequence='An invalid subject name has been entered',delay_time=0.1,color=colors[0])
                             else:
                                 subjects_1.append(enter_subject_alias)
                         else:
                             student=Student(student_name=student_name,home_address=home_address,phone_number=None,subjects=subjects_1,grade=None,age=enter_age)
                             student.log_students_chosen_subjects()
                             time.sleep(1)
                             grade=int(input('What was the grade the student got recently in their recent exam?:'))
                             student=Student(student_name=student_name,home_address=home_address,phone_number=None,subjects=subjects,grade=grade,age=enter_age)
                             student.assign_grade()
        except ValueError:
            logging.error('A ValueError occurred')
            loop_over(sequence='An error occurred due to an inappropiate value being entered',delay_time=0.1,color=colors[0])
