'''
@author: Team 5 (Eric, Khayyam, Roman, Taavi)
@system: Laboratory Information System for Mt. Sinai Hospital
'''

#Import regex and unittest
import re, unittest

#import register.py
import register as r

#Testing function for registering users: register_user(email, password, password2, firstname, lastname, role)
class TestMethods(unittest.TestCase):
    def test_firstname1(self):
        self.assertTrue(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson', 'Doctor'), 'FR001A - firstname is valid')
    def test_firstname2(self):
        self.assertFalse(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'KhayyamPassword', '', 'Jackson', 'Doctor'), 'FR001A - firstname is empty')
    def test_lastname1(self):
        self.assertTrue(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson', 'Doctor'), 'FR001A - lastname is valid')
    def test_lastname2(self):
        self.assertFalse(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'KhayyamPassword', 'Roman', '', 'Doctor'), 'FR001A - lastname is empty')
    def test_password1(self):
        self.assertTrue(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson', 'Doctor'), 'FR001B, FR001C - password is valid')
    def test_password2(self):
        self.assertFalse(r.register_user('taavi@taltech.ee', 'Khayyam', 'Khayyam', 'Khayyam', 'Jackson', 'Doctor'), 'FR001B - Password is firstname')
    def test_password3(self):
        self.assertFalse(r.register_user('taavi@taltech.ee', 'Jackson', 'Jackson', 'Roman', 'Jackson', 'Doctor'), 'FR001B - Password is lastname')
    def test_password4(self):
        self.assertFalse(r.register_user('taavi@taltech.ee', '1234', '1234', 'Khayyam', 'Jackson', 'Doctor'), 'FR001C - Password too short')
    def test_password5(self):
        self.assertTrue(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson', 'Doctor'), 'FR001D - Passwords match')
    def test_password6(self):
        self.assertFalse(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'Khayyam', 'Roman', 'Jackson', 'Doctor'), 'FR001D - Passwords do not match')
    def test_email1(self):
        self.assertTrue(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson', 'Doctor'), 'FR001E - email is valid')
    def test_email2(self):
        self.assertFalse(r.register_user('taavi@taltech@ee', 'KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson', 'Doctor'), 'FR001E - email is invalid')
    def test_role1(self):
       self.assertTrue(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson', 'Doctor'), 'FR001F - role is valid')
    def test_role2(self):
        self.assertFalse(r.register_user('taavi@taltech.ee', 'KhayyamPassword', 'KhayyamPassword', 'Roman', 'Jackson', 'Plumber'), 'FR001F - role is invalid')

if __name__ == "__main__":
    unittest.main()