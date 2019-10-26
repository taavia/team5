'''
@author: Team 5 (Eric, Khayyam, Roman, Taavi)
@system: Laboratory Information System for Mt. Sinai Hospital
'''

#Import regex, csv and array
import re, csv

#Set email regex
regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

#Check email validity
def emailcheck(email):
    if not (re.search(regex, email)):
        return 1
    else:
        return 0

#Check password validity
def passwordcheck(password, password2, firstname, lastname):
    if(len(password) == 0):
        return 2
    elif(len(password) < 6):
        return 3
    elif(password != password2):
        return 4
    elif(password == firstname):
        return 5
    elif(password == lastname):
        return 6
    else: 
        return 0

#Check if field is empty
def emptycheck(input):
    if (len(input) == 0):
        return 7
    else:
        return 0

#Check if role is acceptable
def rolecheck(role):
    if(role == 'Doctor' or role == 'Assistant' or role == 'Nurse'):
        return 0
    else:
        return 8

#Print corresponding error message
def error_message(error):
    message = {
        1: 'Email is invalid!',
        2: 'Password cannot be empty',
        3: 'Password must be at least 6 characters',
        4: 'Passwords do not match',
        5: 'Password cannot be firstname',
        6: 'Passwords cannot be lastname',
        7: 'Fields cannot be empty',
        8: 'Role is incorrect',
        0: 'Success'
    }
    print(message.get(error))

#Register user
def register_user(email, password, password2, firstname, lastname, role):
    error = 0
    data = [email, password, password2, firstname, lastname, role]
    #check if any field is empty
    for i in data:
        result = emptycheck(i)
        if (result != 0):
            error_message(result)
            error = 1
    #check if email is valid
    if (emailcheck(email) != 0):
        error_message(emailcheck(email))
        error = 1
    #check if password is valid
    pcheck = passwordcheck(password, password2, firstname, lastname)
    if (pcheck != 0):
        error_message(pcheck)
        error = 1
    #check if role is valid
    rcheck = rolecheck(role)
    if (rcheck != 0):
        error_message(rcheck)
        error = 1

    if (error == 0):
        save_db=email, password, firstname, lastname, role
        file=open('./users.csv','a')
        file.write(str(save_db))
        file.close
        print('Success you are now registered!')
        return True
    else:
        return False

#Registration form  
def register_form():
    print('Welcome to Mt. Sinai Hospital LIMS system registration page! Please fill in the form.')
    email=input('Email:')
    firstname=input('Firstname:')
    lastname=input('Lastname:')
    password=input('Password: ')
    password2=input('Repeat password:')
    role=input('Role in the hospital:')
    register_user(email, password, password2, firstname, lastname, role)

if __name__ == "__main__":
    register_form()  