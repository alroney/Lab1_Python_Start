# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:05:43 2022

@author: Andrew
"""
import sys

def user_choice():
    """

    Returns
    -------
    bool
        Asks user to continue. Boolean determined by yes or no

    """
    while True:
        choice = input("Do you want to continue with voter registration: ")#User input
        choice = choice.lower()#Convert the input to be all lower-case for ease
        if choice == "yes": #If yes then continue
            return True
        if choice == "no":
            return False

print("Welcome to the Python Voter Registration Application.")

#DEFINING#

def is_alphabet(string):
    """

    Parameters
    ----------
    string : str
        Take a string analyze it.

    Returns
    -------
    bool
        If it contains a number it fails, otherwise it passes.

    """
    if string.isalpha():#Check if it contains only letter characters.
        return True
    return False

def get_f_name():
    """

    Returns
    -------
    f_name : str
        First name given by the user.

    """
    if not user_choice():
        input("Press ENTER to exit")
        sys.exit()

    while True:
        f_name = input("What is your First Name: ")
        if is_alphabet(f_name):
            return f_name

def get_l_name():
    """

    Returns
    -------
    l_name : str
        Last name given by the user.

    """
    if not user_choice():
        input("Press ENTER to exit")
        sys.exit()

    while True:
        l_name = input("What is your Last Name: ")
        if is_alphabet(l_name):
            return l_name

def get_age():
    """

    Returns
    -------
    int
        Get user age input, verify it qualifies and return the value.

    """
    if not user_choice():
        input("Press ENTER to exit")
        sys.exit()
    
    while True:
        try: 
            age = input("What is your age: ")
            age = int(age)
            if age < 18:
                is_of_age = input("Are you 18 years or older: ")
                if is_of_age == "no":
                    continue
            elif 18 <= age <= 120:
                return age
        except ValueError:
            #only except whole integer.
            print("Please enter a valid whole integer from 18 to 120")

def get_country():
    """

    Returns
    -------
    str
        Gets a 'yes' or 'no' input from user to set citizen status.

    """
    if not user_choice():
        input("Press ENTER to exit")
        sys.exit()

    while True:
        is_citizen = input("Are you a U.S Citizen: ")
        if is_alphabet(is_citizen):
            is_citizen = is_citizen.lower()#Convert all letters to lowercase.
            if is_citizen == "yes":
                return "yes"
            return "no"

def get_state():
    """

    Returns
    -------
    state : str
        Gets state value from user input, checks if it is an abbreviation.

    """
    if not user_choice():
        input("Press ENTER to exit")
        sys.exit()

    while True:
        state = input("What state do you live in: (abbreviate)")
        if is_alphabet(state):
            state = state.lower()
            if len(state) == 2:
                return state

def get_zipcode():
    """

    Returns
    -------
    int
        Gets zipcode value from user input, then checks validity and returns it.

    """
    if not user_choice():
        input("Press ENTER to exit")
        sys.exit()

    while True:
        try:
            zipcode = input("What is your Zipcode: ")
            if len(zipcode) == 5:
                return int(zipcode)

        except ValueError:
            pass




#ASSIGNING VALUES

VOTER = [] #Start list for application input data to be stored.

while True: #Infinite loop.
    FNAME = get_f_name()
    VOTER.append(FNAME)#Append to first name.

    LNAME = get_l_name()
    VOTER.append(LNAME)#Append to last name.

    AGE = get_age()
    if AGE == -1:
        break
    VOTER.append(AGE)#Append to age.

    COUNTRY = get_country()
    if COUNTRY == "no":
        break
    VOTER.append("yes")#Append yes for United States.

    STATE = get_state()
    VOTER.append(STATE.upper())#Append state with the first letter capitalized.

    ZIP = get_zipcode()
    VOTER.append(ZIP)

#DISPLAY RESULTS
    if len(VOTER) == 6: #If the length of the VOTER array is 6, then proceed
        print("=====================")

        print("Thanks for using the Python Registration Application")
        print("The following is submitted information:")
        #return value of arrays at [array position]
        print("Name (first last): ", VOTER[0], VOTER[1])
        print("Age: ", VOTER[2])
        print("U.S Citizen: ", VOTER[3])
        print("State: ", VOTER[4])
        print("Zipcode: ", VOTER[5])

        print("=====================")


input("Press ENTER to exit")
