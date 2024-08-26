# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I wrote this program to help caculate the how many hotdogs a person will need for the amount of people at their party.

# Welcome message
print ("Welcome to HotDogs Calculator.")

# Users input for name, amount of people, and amount of hotdogs per person
name = input ("Enter your name: ")
amountofpeople = int ( input ("How many people are going to be at this cookout: ") )
hotdogsamountsperperson = int ( input ("How many hotdogs will each person be getting: ") )

# This is the constance, total hotdogs, calculation for the hotdogs and hotdogs buns
def calculations(amountofpeople, hotdogsamountsperperson):
    hotdogspack = 10
    hotdogsbunspack = 8
    tothotdogs = amountofpeople * hotdogsamountsperperson
    hotdogsneeded = (hotdogspack + tothotdogs - 1) // hotdogspack
    hotdogsleft = tothotdogs % hotdogspack
    hotdogsbunsneeded = (hotdogsbunspack + tothotdogs - 1) // hotdogsbunspack
    hotdogsbunsleft = (hotdogsbunspack * hotdogsbunsneeded) - tothotdogs
    return hotdogsneeded, hotdogsbunsneeded, hotdogsleft, hotdogsbunsleft

# Display messages, the minimum amount and left over of the hotdogs needed and hotdogs buns
def displaymessage():
    hotdogsneeded, hotdogsbunsneeded, hotdogsleft, hotdogsbunsleft = calculations(amountofpeople, hotdogsamountsperperson)

    print("Hey", name,)
    print("The minimum amount of hotdogs packages you'll need are:", hotdogsneeded,)
    print("The minimum amount of hotdogs buns packages you'll need are:", hotdogsbunsneeded,)
    print("The amount of hotdogs that will be left are:", hotdogsleft,)
    print("The amount of hotdogs buns that will be left are:", hotdogsbunsleft,)

displaymessage()
