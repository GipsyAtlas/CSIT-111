# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I wrote this program for 10 specific people to help the user find their birthday

# Welcome message
print ("Welcome to Birthday Search")

# 1st 1D array
people = ["Becket", "Fry", "Damon", "Klaus", "Hope", "Eren", "Amber", "Gianni", "Chloe", "Levi"]

# 2nd 1D array
birthdays = ["Aug 18", "Aug 26", "Feb 3", "Jun 22", "Mar 12", "Dec 25", "Nov 7", "Jan 16", "May 26", "Sep 13"]

# Boolean variable to act as a flag
found = False

# variable as a loop counter
index = 0

# srings of names to seach for
name = input ("What is the person name (or part of the name) that you want to search: ")

# step to search for a name on the string
while found == False and index < len(people):
    # .lower() was added to allow user to enter the first three letter of a name and get their result witout have to write the full name
    if name.lower() in people[index].lower():
        found = True
    else:
        index += 1

# Display searched name's birtchday
if found:
    print ("The name",people[index],"has their birthday on", birthdays[index])
    print ("Happy Birthday")

# Wrong name inputed
else:
    print ("The name you enterd was not found")
    print ("Run the program again")
