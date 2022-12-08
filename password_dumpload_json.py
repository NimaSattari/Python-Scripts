# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 13:50:12 2022

@author: Nima
"""

import json

def show_saved_password():
    """Shows Saved Password"""
    file_name = 'password.json'
    try:
        with open(file_name) as f:
            password = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return password

def get_new_password():
    """Get new password from user"""
    password = input('Enter Password: ')
    file_name = 'password.json'
    with open(file_name, 'w') as f:
        json.dump(password, f)
        return password

def identify_password():
    """Identifies entered password"""
    password = show_saved_password()
    if password:
        print(f'Saved Password Is: {password}')
    else:
        password = get_new_password()
        print(f'New Password Is: {password}')
            
identify_password()