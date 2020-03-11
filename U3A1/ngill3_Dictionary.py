"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_Dictionary.py
Description:
    This is a simple student management system
    There is some of the code here, some of it is in web/functions.js
History . .:
    3/9/2020 - Created File
"""
import json

# In this project I'm using Eel.
# Eel is a simple library for making HTML/CSS/JS GUIs by opening
# a web browser window and loading local web files, but it also provides
# a way to call Python functions from JavaScript and vice versa.
# So, from Python I have functions to load and modify data and it is displayed in JavaScript
# Try and import Eel. If it's not installed exit.
try:
    import eel
except ModuleNotFoundError:
    # Eel isn't installed.
    import sys
    print("Eel isn't installed! Please install Eel with 'python -m pip install eel'")
    sys.exit(0)

DB_LOC = "db.json"


# This function will return a list of users
@eel.expose
def get_users(limit, offset):
    # Load the database and return the users defined by limit, offset
    # Limit = how many users to return
    # Offset = Where to start
    users = json.load(open(DB_LOC, 'r'))
    if limit == -1: limit = len(users)
    return {"data": [x for _, x in users.items()][offset:offset + limit], "total": len(users)}


# This function returns one user
@eel.expose
def get_user(sid):
    # Load the database and return the user (None if not exists)
    users = json.load(open(DB_LOC, 'r'))
    return None if sid not in users else users[sid]


# This function sets the data for a user
@eel.expose
def set_user(sid, user):
    # Load the database
    users = json.load(open(DB_LOC, 'r'))

    # If the Student ID changed, delete the old key
    if sid != user['sid'] and sid in users:
        del(users[sid])

    # Set the data
    users[user['sid']] = user

    # Save the database
    with open(DB_LOC, 'w') as f:
        f.write(json.dumps(users))


# This function deletes a user
@eel.expose
def delete_user(sid):
    # Load the database
    users = json.load(open(DB_LOC, 'r'))

    # If the user exists delete it
    if sid in users:
        del(users[sid])

    # Save the database
    with open(DB_LOC, 'w') as f:
        f.write(json.dumps(users))


# Start Eel.
# Default mode is "chrome" to run as a desktop app
# For debugging set this to "firefox", "edge", etc
eel.init("web")
eel.start("index.html", mode="chrome")
