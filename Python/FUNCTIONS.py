# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I wrote this program to help user convert pounds to Kilograms and Kilograms to pounds.

# Welcome message.
print ("Welcome to the weight converter for only Pounds and Kilogram :)")

# The user inputs their name.
name = input ("What is your name: ")

# These are the converting calculation for the pounds to Kilograms and Kilograms to pounds.
def poundtokilogram(poundsEntered):
    return round (poundsEntered * 0.453592, 2)

def kilogramtopound(kilogramsEntered):
    return round (kilogramsEntered * 2.20462, 2)

# The user input if they want to convert pounds to kilograms or Kilograms to Pounds. 
print ("Hey", name,"if you want to convert pounds to kilograms then input 'pk' but if you want to convert Kilograms to Pounds then input 'kp'.")
decision = input ("Enter here: ")

# The user input how much the pounds is, then it calculated, and then printed.
if decision == 'pk':
    pounds = float ( input ("What is the weight in pounds: ") )
    kilograms = poundtokilogram(pounds)
    print ("The", pounds,"pounds is equal to", kilograms,"kilograms.")

# The user input how much the kilograms is, then it calculated, and then printed.
elif decision == 'kp':
    kilograms = float ( input ("what is the weight in kilograms: ") )
    pounds = kilogramtopound(kilograms)
    print ("The", kilograms,"kilograms is equal to", pounds,"pounds.")

# If the user enters the wrong input.
else:
    print ("Wrong input please enter pk or kp.")
