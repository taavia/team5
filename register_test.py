'''
@author: Team 5 (Eric, Khayyam, Roman, Taavi)
@system: Laboratory Information System for Mt. Sinai Hospital
'''

#Import regex, csv and unittest
import re, csv, unittest

#import register.py
import register as r

#Testing functions emptycheck(input), passwordcheck(password, password2, firstname, lastname), emailcheck(email) and rolecheck(role)
class TestMethods(unittest.TestCase):
    def test_firstname1(self):
        self.assertEquals(r.emptycheck('Roman'), 0, 'FR001A - firstname is valid')
    def test_firstname2(self):
        self.assertEquals(r.emptycheck(''), 7, 'FR001A - firstname is empty')
    def test_lastname1(self):
        self.assertEquals(r.emptycheck('Jackson'), 0, 'FR001A - lastname is valid')
    def test_lastname2(self):
        self.assertEquals(r.emptycheck(''), 7, 'FR001A - lastname is empty')
    def test_password1(self):
        self.assertEquals(r.passwordcheck('KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson'), 0, 'FR001B, FR001C - password is valid')
    def test_password2(self):
        self.assertEquals(r.passwordcheck('Khayyam', 'Khayyam', 'Khayyam', 'Jackson'), 3, 'FR001C - Password is firstname')
    def test_password3(self):
        self.assertEquals(r.passwordcheck('Jackson', 'Jackson', 'Roman', 'Jackson'), 2, 'FR001B - Password is lastname')
    def test_password4(self):
        self.assertFalse(r.passwordcheck('1234', '1234', 'Roman', 'Jackson'), 'FR001C - password too short')
    def test_password4(self):
        self.assertEquals(r.passwordcheck('KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson'), 5, 'FR001D - Passwords match')
    def test_password5(self):
        self.assertEquals(r.passwordcheck('KhayyamPassword', 'Khayyam', 'Roman', 'Jackson'), 6, 'FR001D - Passwords do not match')
    def test_email1(self):
        self.assertEquals(r.emailcheck('taavi@taltech.ee'), 0, 'FR001E - email is valid')
    def test_email2(self):
        self.assertEquals(r.emailcheck('taavi@taltech@ee'), 1, 'FR001E - email is invalid')
    def test_role1(self):
        self.assertEquals(r.rolecheck('Doctor'), 0, 'FR001F - role is valid')
    def test_role2(self):
        self.assertEquals(r.rolecheck('Plumber'), 8, 'FR001F - role is invalid')

if __name__ == "__main__":
    unittest.main()