'''
@author: Team 5 (Eric, Khayyam, Roman, Taavi)
@system: Laboratory Information System for Mt. Sinai Hospital
'''

#Import regex, csv and unittest
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

#Error message handling
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
    save_db=email, password, firstname, lastname, role
    file=open('./users.csv','a')
    file.write(str(save_db))
    file.close
    print('Success you are now registered!')

#Registration form  
def register_form():
    print('Welcome to Mt. Sinai Hospital LIMS system registration page! Please fill in the form.')
    while True:
        email=input('Email:')
        if (emailcheck(email) == 0):
            break
        else:
            error_message(emailcheck(email))
    while True:
        firstname=input('Firstname:')
        if (emptycheck(firstname) == 0):
            break
        else:
            error_message(emptycheck(firstname))
    while True:
        lastname=input('Lastname:')
        if (emptycheck(lastname) == 0):
            break
        else:
            error_message(emptycheck(lastname))
    while True:
        password=input('Password: ')
        password2=input('Repeat password:')
        if (passwordcheck(password, password2, firstname, lastname) == 0):
            break
        else:
            error_message(passwordcheck(password, password2, firstname, lastname))
    while True:
        role=input('Role in the hospital:')
        if (emptycheck(role) != 0 or rolecheck(role) != 0):
            if (emptycheck(role) == 0):
                error_message(rolecheck(role))
            else:
                error_message(emptycheck(role))
        else:
            break
    register_user(email, password, password2, firstname, lastname, role)

if __name__ == "__main__":
    register_form()  