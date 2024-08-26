# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I wrote this program to help a user know what generation they fall under.

# Welcome message
print ("Welcome to GenAge.")
print ("I'll be telling you what generation you belong to based on your birth years.")

# This part of the code is to accurately decide what generation the user fall under and if they are a sub generation or not.
yob = int ( input ("What year were you born on?") )


if yob <= 1945:
       print ("Hi there you are part of The Silent Generation.")

elif 1946 <= yob <= 1964:
       print ("Hi there you are part of theBaby Boomers generation.")

elif 1965 <= yob <= 1980:
       print ("Hi there you are part of the Gen X generation.")

       if 1975 <= yob <= 1983:
           print ("I also want to let you know that you are part of sub_generation Xennials.")

elif 1981 <= yob <= 1996:
       print ("Hi there you are part of the Millennials generation.")

       if 1977 <= yob <= 1983:
           print ("I also want to let you know that you are part of sub_generation Xennials.")

       if 1993 <= yob <= 1998:
           print ("I also want to let you know that you are part of sub_generation Zillennials.")

elif 1997 <= yob <= 2012:
       print ("Hi there you are part of the Gen Z generation.")

elif 2012 <= yob <= 2025:
       print ("Hi there you are part of the Gen Alpha generation.")

else:
       print ("Hi there the generation in which you belong to is Unknown.")
