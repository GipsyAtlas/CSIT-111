# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I worte this program to help a user know how much credits they'll need in order to graduate.

# Constants needed
creditsneededtograduate = 60

# Welcome messsage
print ("Welcome to Degree Audit.")
print ("I am going to calculate how much credits you'll need to graduate.")

# Input user basic infomation
name = input ("Enter your name:")
major = input ("Enter you major:")
creditstaken = int ( input ("Enter the amount of credits you have taken so far:") )

# Calculation of the amount of credits needed
creditsneeded = (creditsneededtograduate - creditstaken)

# Display Happy/Sad message for the result.
happymessage = "CONGRATULATIONS, " + name + " you have reached the amount of credits needed to graduate with a major in " + major + " :)"
sadmessage = "Hello, " + name + " you'll need " + str(creditsneeded) + " credits in order to graduate with a major in " + major

if creditsneeded <= 0:
    print (happymessage)

else:
    print (sadmessage)
