# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I wrote this program to help people know how many bottles they have recycled.

# Welcome messages
print ("Welcome to Bottles Counter.")

#totbot means Total Bottles
totbot = 0

#Loop for 7 days
for days in range(1,8):
    print ("Enter the amount of bottles you have recycled for day", days,".")
    bottlesrecycled = int ( input ("bottles you have recycled:") )
    totbot = bottlesrecycled + totbot

#The total amount of bottles
print ("The total amount of bottles you have collected is", totbot, "for this week.") 

# Display messages
if totbot > 7 and totbot <=50:
    print ("Congratulation, you have more than 7 bottles.")

elif totbot > 50:
    print ("Congratulation, you have even more than 50 bottles.")

else:
    print ("You suck you didn't even make it pass 7.")
