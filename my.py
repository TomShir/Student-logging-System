from colorama import Fore 
import time 
import sys 
import os 
import random 
import tqdm 
import logging 
program_title='student logger'
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW]
myformat='%(asctime)s-%(name)s-%(message)s'
random.shuffle(colors)
grades=['Poor','Acceptable','excellcent','outstanding']
student_logger=logging.getLogger('student_information_logger')
computer_characters=['<',',','#','@','{','}','[',']','!','"','*','&','^',')','(','-','=','+','/','~','1','2','3','4','5','6','7','9','0','\\','|','_']
subjects=['Further Maths','further maths','triple science','Triple Science','French','french','Music','music','Art','art','food studies','Food Studies','History','history','Geography','geography','Computer Science','ICT','Ict','computer science','combined science','Combined science']
student_information_handler=logging.FileHandler('Student_information.log')
student_information_handler.setLevel(logging.INFO)
logging_format=logging.Formatter(myformat)
student_information_handler.setFormatter(logging_format)
student_logger.addHandler(student_information_handler)
class Student:
    def __init__(self,name,age,phone_number,address,grade):
        self.name=name 
        self.age=age 
        self.phone_number=phone_number 
        self.address=address 
        self.grade=grade 
    
    def log_student_name(self):
        print(f'Student_name:{self.name}')
        student_logger.info(f'Student_name:{self.name}')
    def log_age(self):
        print(f'Student"s age:{self.age}')
        student_logger.info(f'Student"s age:{self.age}')
    def phone_number(self):
        print(f'Student"s Phone_number:{self.phone_number}')
        student_logger.info(f'Student"s Phone_number:{self.phone_number}')
        
    def assign_grade(self):
        if self.grade<=30:
            for num in  tqdm.tqdm(mysequence,total=self.grade,colour='RED'):
                time.sleep(0.01)
            else:
                student_logger.info(f'Grade:{grades[0]}')
                return f'Grade:{grades[0]}'
        elif self.grade>=40 and self.grade<=70:
             for num in  tqdm.tqdm(mysequence,total=self.grade,colour='#FFA500'):
                time.sleep(0.01)
             else:
                 student_logger.info(f'Grade:{grades[1]}')
                 return f'Grade:{grades[1]}'
        elif self.grade>=70 and self.grade<=89:
            for num in tqdm.tqdm(mysequence,total=self.grade,colour='YELLOW'):
                time.sleep(0.01)
            else:
                student_logger.info(f'Grade:{grades[2]}')
                return f'Grade:{grades[2]}'
        elif self.grade>=90 and self.grade<=100:
            for num in tqdm.tqdm(mysequence,total=self.grade,colour='GREEN'):
                time.sleep(0.01)
            else:
                student_logger.info(f'Grade:{grades[-1]}')
                return f'grade:{grades[-1]}'
    def log_phone_number(self):
        student_logger.info(f'Student"s phone_number:{self.phone_number}')
        return f'Student"s phone_number:{self.phone_number}'
    def log_number_of_subjects(self,student_subjects):
        print(f'The number of subjects the student is taking:{len(student_subjects)}')
        student_logger.info(f'The number of subjects the student is taking:{len(student_subjects)}')
        time.sleep(1)
        print(f'Name of subjects {self.name} is taking:\n\t')
        for subject in student_subjects:
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write(f'{colors[1]}{subject}\n')
        else:
            print(f'{Fore.RESET}')
def check_validity_of_name(sample_string):
    if computer_characters[0] in sample_string or computer_characters[1] in sample_string or computer_characters[2] in sample_string or computer_characters[3] in sample_string or computer_characters[4] in sample_string or computer_characters[5] in sample_string or computer_characters[6] in sample_string or computer_characters[7] in sample_string or computer_characters[8] in sample_string or computer_characters[9] in sample_string or computer_characters[10] in sample_string or computer_characters[11] in sample_string or computer_characters[12] in sample_string or computer_characters[13] in sample_string or computer_characters[14] in sample_string or computer_characters[15] in sample_string or computer_characters[16] in sample_string or computer_characters[17] in sample_string or computer_characters[18] in sample_string or computer_characters[19] in sample_string or computer_characters[20] in sample_string or computer_characters[21] in sample_string or computer_characters[22] in sample_string or computer_characters[23] in sample_string or computer_characters[24] in sample_string or computer_characters[25] in sample_string or computer_characters[26] in sample_string or computer_characters[27] in sample_string or computer_characters[28] in sample_string or computer_characters[29] in sample_string or computer_characters[30] in sample_string or computer_characters[31] in sample_string :
       error_msg(text='Error,this is not a real name')
    else:
       pass
#Creating a logger object that handles errors that might occur in the Python program
mylogger=logging.getLogger('Error_logger:')
#Creating a function that loops over a sequence and prints it horizontally 
def loop_over(text_color,text,delay_time):
    if text==f'{program_title}\n\n\t':
        for txt in text:
            sys.stdout.flush()
            time.sleep(delay_time)
            sys.stdout.write(f'\t{random.choice(colors)}{txt.upper()}')
        else:
            print(f'{Fore.RESET}')
    else:
        for n in text:
            sys.stdout.flush()
            time.sleep(delay_time)
            sys.stdout.write(f'{text_color}{n}')
        else: 
         print(f'{Fore.RESET}')
def error_msg(text):
    #Creating a filehandler to handle errors
    file_handler=logging.FileHandler('error.log')
    logging_format=logging.Formatter(myformat)
    file_handler.setFormatter(logging_format)
    file_handler.setLevel(logging.ERROR)
    mylogger.addHandler(file_handler)
    mylogger.error(f'{text}')
    loop_over(text_color=colors[0],text=text,delay_time=0.01)
#Creating a progress bar
mysequence=list(range(1,100+1,1))
for num in tqdm.tqdm(mysequence,desc='Loading Student System',colour='GREEN',ncols=100):
    time.sleep(0.01)
else:
    try:
     time.sleep(1)
     print('\n\t\tStudent Logging System loaded...')
     time.sleep(1)
     print('\n\t\tIniating...')
     time.sleep(1)
     os.system("cls")
     time.sleep(1)
     loop_over(text_color=random.choice(colors),text=f'{program_title}\n\n\t',delay_time=0.1)
     time.sleep(1)
     student_name=input('Student_name:')
     check_validity_of_name(sample_string=student_name)
     time.sleep(1)
     student_age=int(input('student"s age:'))
     if student_age<11 or student_age>16:
         error_msg(text='Error,that student cannot be in this school with that age')
     else:
         time.sleep(1)
         phone_number=int(input('phone_number:'))
         #Converting the variable phone_number into a str using typecastings in order to use the len() function 
         strphone_number=str(phone_number)
         if len(strphone_number)<11:
             error_msg(text='Error,this is an invalid phone number as it should be 11 characters or more')
         else:
             time.sleep(1)
             mark=int(input('Mark for recent exam: '))
             time.sleep(1)
             home_address=input('home_address:')
             space=' '
             if space not in home_address and home_address[3]!=space or len(home_address)>7:
                 error_msg('Error,not a valid home address')
             else:
                 courses=[]
                 number_of_subjects_student_is_taking=int(input(f'How many subjects is {student_name} taking?:'))
                 for subject in range(number_of_subjects_student_is_taking):
                     subject_name=input('Subject_name:')
                     courses.append(subject_name)
                 else:
                     default_student=Student(name=student_name,age=student_age,grade=mark,address=home_address,phone_number=phone_number)
                     default_student.log_student_name()
                     time.sleep(1)
                     default_student.log_age()
                     time.sleep(1)
                     print(default_student.log_phone_number())
                     time.sleep(1)
                     default_student.log_number_of_subjects(student_subjects=courses)
                     time.sleep(1)
                     print(default_student.assign_grade())
    except ValueError:
        error_msg(text='ValueError:You entered an inappropiate value')