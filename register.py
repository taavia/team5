'''
@author: Team 5 (Eric, Khayyam, Roman, Taavi)
@system: Laboratory Information System for Mt. Sinai Hospital
'''

#Import regex, csv
import re, csv

#Register user
def register_user(email, password, password2, firstname, lastname, role):
    save_db=email, password, firstname, lastname, role
    file=open('./users.csv','a')
    file.write(str(save_db))
    file.close
    print('Success you are now registered!')
    return True

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