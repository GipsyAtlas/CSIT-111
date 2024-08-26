# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I wrote this program to help students calculate the tuituion for each year.

# Welcome message
print ("Welcome to Degree Audit.")

# Constance
tui = 25000

# Loop for 5 years 
for yt in range(1,6):

    # Yealy calculation to get the next increase
    increase = 0.03 * tui

    # Total tuition calculation 
    tottui = increase + tui

    # Rounding the increased numbers
    rincrease = round (increase, 2)
    rtottui = round (tottui, 2)

    # Display messages showing the answers of the calculation
    print ("For Year", yt,)
    print ("The tuition increase is", rincrease,)
    print ("The total tuition is", yt, ":", rtottui,)

    # next years tuition
    tui = tottui
