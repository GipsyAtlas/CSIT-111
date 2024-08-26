# My name is Oluwatimilehin Amoo from CSIT 111 CLW
# I wrote this program to help user to creaet a family playlist

# The menu for the choice to add or see or exit the playlist.
def menu():
    print ("Enter 'add' to add to the family playlist.")
    print ("Enter 'see' to see the family playlist.")
    print ("Enter 'exit' to exit the family playlist.")

# This part open the file and create a loop to enter the songs and exit the loop
def add_playlist():
    with open ("playlist.dat", "a") as familyplaylist_file:
        # To loop the add song question.
        while True:
            music = input ("Enter a song name or 'exit' to go back to the menu: ")
            
            # To exit out of the loop
            if music == "exit":
                break

            # The creation of the playlist.dat file.
            familyplaylist_file.write(music + "\n")
            print (music,"has been addedd to your Family Playlist")

# To view the playlist
def see_playlist():
    with open("playlist.dat", "r") as familyplaylist_file:
        songs = familyplaylist_file.readlines()

        # If there are songs in the playlist.
        if songs:
            print ("These are the Songs in your Family Playlist:")
            for music in songs:
                print (music.strip())

        # If the playlist is empty.
        else:
            print ("Your Family Playlist is Empty")

# To exit the playlist
def exit_playlist():
    print ("I really appriciate you for using my Family Playlist Creator.")

def main():
    # Welcome message
    print ("Welcome to The Family Playlist Creator :)")

    # The user choice and input validation loop
    while True:
        menu()
        userinput = input ("Please pick an option: ")
        while userinput not in ('add', 'see', 'exit'):
            print ("Invalid input Please enter add or see or exit.")
            userinput = input ("Please pick an option: ")
        # The options of the user    
        if userinput == 'add':
            add_playlist()
        elif userinput == 'see':
            see_playlist()
        elif userinput == 'exit':
            exit_playlist()
            break

main()
