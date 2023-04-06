#main.py 

# Ray Ewry Group 
# Name: Ryan O'Connor, Graham Davis, Erin Herlihy, Catherine Dimbath
# email: oconnorp@mail.uc.edu, davisgh@mail.uc.edu, herlihej@mail.uc.edu, dimbatcs@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is an API that turn the entire thing into a dictionary and then only prints certain key/value pairs 
# Citations:
# Anything else that's relevant:


import requests
import json
from funtionsPackage.function import *

#api landing page
# #https://www.ftc.gov/developer/api/v0/endpoints/hsr-early-termination-notices-api


#making a request to the API and storing encoded JSON data in json_string 


response = requests.get('https://api.ftc.gov/v0/hsr-early-termination-notices?api_key=2mrcMmjDKS4OHkWHQW2YvSUsxFDi74a11lARvKwM')
json_string = response.content

#storing encoded json string in variable called dictionary

dictionary = json.loads(json_string) 

#prints whatever key and its value that you want if you add the key below. We chose transaction number, title, and date.
keys_to_print = ["transaction-number", "title", "date"]

#prints transaction-number, title , and date.
iterate_dictionary(dictionary, keys_to_print)



