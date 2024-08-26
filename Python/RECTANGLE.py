# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I wrote this program to help elementary school kids to calculate a ractangle with the biggest area.

# Welcome message
print ("Welcome to measuring shapes.")
name = input ("What is your name?")
print ("Hello,", name, "we are going to be calculating the areas of two rectangles and find out which one has the bigger area.")

# Rectangle 1
print ("I'll need the Length and Width for rectangle 1")
reclength1 = float ( input ("Enter the length of rectangle 1:") )
recwidth1 = float ( input ("Enter the width of rectangle 1:") )

# Rectangle 2
print ("Now same thing for rectangle 2")
reclength2 = float ( input ("Enter the length of rectangle 2:") )
recwidth2 = float ( input ("Enter the width of rectangle 2:") )
                    
# Rectangle calculation
recarea1 = str (reclength1 * recwidth1)
recarea2 = str (reclength2 * recwidth2)

# Display message
if recarea1 > recarea2:
    print ("Hello again,", name, "Rectangle 1 has a larger area than Reactangle 2.")

elif recarea2 > recarea1:
    print ("Hello again,", name, "Rectangle 2 has a larger area than Reactangle 1.")

else:
    print ("Hello again,", name, "Rectangle 1 and Rectangle 2 both have equal areas.")

    

