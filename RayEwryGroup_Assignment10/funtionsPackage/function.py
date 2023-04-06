#function.py 

# Ray Ewry Group  
# Name: Ryan O'Connor, Graham Davis, Erin Herlihy, Catherine Dimbath
# email: oconnorp@mail.uc.edu, davisgh@mail.uc.edu, herlihej@mail.uc.edu, dimbatcs@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is an API that turn the entire thing into a dictionary and then only prints certain key/value pairs 
# Citations:
# Anything else that's relevant:


#function to iterate and turn data into a dictionary

def iterate_dictionary(myDictionary, keys_to_print=None):
    for k, v in myDictionary.items():
        if keys_to_print is None or k in keys_to_print:
            print("{0} : {1}".format(k, v))
        if isinstance(v, dict):
            iterate_dictionary(v, keys_to_print)
        elif isinstance(v, list):
            for vv in v:
                if isinstance(vv, dict):
                    iterate_dictionary(vv, keys_to_print)


