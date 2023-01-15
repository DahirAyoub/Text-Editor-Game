# Importing pygame
import pygame
pygame.init()
# #Loading the image of my map
image = pygame.image.load("Assignment_10_Map.jpg")
#Making a 500 by 500 screen
screen=pygame.display.set_mode((500,500))
#Setting caption of the screen to map
pygame.display.set_caption("Map")
#Scaling the the map to 500 by 500
map=pygame.transform.scale(image,(500,500))
#Bliting the map on to the screen and updating the display
# screen.blit(map,(0,0))
screen.blit(map,(0,0))
pygame.display.update()

# List of names of the places on my map.
names=["Main Hall","Master Bedroom","Master Closet","Master Bathroom","Loft","Laundry Room","Bedroom 2","Bedroom 2 Closet","Bedroom 3","Bedroom 3 Closet","Bathroom 1","Dining Room",
"Kitchen","Bathroom 2","Theatre","Living Room","Office","Garden","Shed","Pool","Conservatory","Library","Playroom","Gym"]
#Adjancency list for my map
adjancency_list=[[1,4,11,15],[0,2,16],[1,3],[2],[0,5,6,8],[4],[4,7],[6],[4,9,10],[8],[8,11],[0,10,12],[11,13,15],[12,14],[13,15,21,22],[0,12,14,16],[1,15,17,21],
[16,18,20],[17,19],[18,20],[17,19],[14,16,20],[14,23],[22]]
#Description for each location on my map.
description=["The main hall is the entrance to the estate. You will find the it connects to all the main places in the estate","The Master Bedroom is the biggest room in the house. It has a bed fitting for a king."
,"The master closet has more cloths that one can imagine. It also the only way to get to the Master Bathroom.","The master bathroom features a beautiful shower and jaccuzi. It also has a his and her's sinks.","The loft is where you could relax and get away from people. It's also the connecting room of the west wing of the estate.",
"The laundry room is where we do laundry! It's also the smallest room in the estate.","Bedroom 2 is the first guest bedroom of the estate. It has its very own walk in closet.",
"Closet 3 is unfortunatly empty. The estate has currently has no visiting guest.","Bedroom 3 is the second guest bedroom of the estate. It has its very own walk in closet aswell. Unlike bedroom 2, it has a bathroom."
,"Bedroom 3 closet is also empty unfortunatly.Once again, the estate dosen't have any guests.","Bathroom 1 is the connecting washroom between the kitchen and bedroom 3. It has a stand up a shower in it.",
"The Dining Room is where everyone enjoys there meal in this estate. We eat every meal here.","The kitchen is where the estate's chef cook for us. All the chef's went to Culinary School",
"Bathroom 2 is the second bathroom is the estate. Unfortunately, it dosen't have a shower.","The Theatre is the main attraction of the east wing of the estate. It has all the lastest movies.",
"The living room is where all the guess relax. It has a wood fire place.","The Office is where the anyone can get the word done. It a Herman Miller chair in it!",
"The garden has all types of plants and trees in it. On any given day, the chefs can make a meal with the foods grown in the garden.","The shed is where the fuse box is. It also stores most of the materials need for the garden."
,"The pool is in the estate is olympic sized. It also has a hottub.","The conservatory is the most peaceful place of the estate. It also is the main attraction of the south wing of the estate.",
"The library has more books than one can read in there lifetime. It has books from every genre.","The playroom has the lastest technology in it. It also has enough room for vr!",
"The gym every type of machinery and free weights one needs to meet the fitness goals. It also has trainers ready to help you out."]

#North function for when user enters north
def north(location):
    #List of places that go north
    north_list=["Main Hall","Master Bedroom","Master Closet","Master Bathroom","Loft","Bedroom 2","Bedroom 2 Closet","Bedroom 3","Theatre",
    "Living Room","Office","Garden","Shed","Pool","Conservatory","Library","Gym"] 
    #Corressponding north place.
    new_room=["Dining Room","Main Hall","Master Bedroom","Master Closet","Bedroom 3","Loft","Bedroom 2","Bedroom 3 Closet","Bathroom 2",
    "Kitchen","Living Room","Office","Garden","Conservatory","Library","Theatre","Playroom"]
    #Returining corresponding north location if the location has the option to go north.
    if location in north_list:
        return new_room[north_list.index(location)]
    #Returring error message if that location can't go north
    else:
        return "You can't go that way."

#South functions does the same thing as north function but checks for south instead.
def south(location):
    south_list=["Main Hall","Master Bedroom","Master Closet","Loft","Bedroom 2","Bedroom 3","Bedroom 3 Closet","Dining Room",
    "Kitchen","Bathroom 2","Theatre","Living Room","Office","Garden","Conservatory","Library","Playroom"]
    new_room=["Master Bedroom","Master Closet","Master Bathroom","Bedroom 2","Bedroom 2 Closet","Loft","Bedroom 3","Main Hall",
    "Living Room","Theatre","Library","Office","Garden","Shed","Pool","Conservatory","Gym"]
    if location in south_list:
        return new_room[south_list.index(location)]
    
    else:
        return "You can't go that way."

#East function doing the same thing as north function but checks for east instead.
def east(location):
    east_list=["Main Hall","Master Bedroom","Loft","Laundry Room","Bedroom 3","Bathroom 1","Dining Room","Kitchen","Theatre","Living Room","Office","Garden","Shed"]
    new_room=["Living Room","Office","Main Hall","Loft","Bathroom 1","Dining Room","Kitchen","Bathroom 2","Playroom","Theatre","Library","Conservatory","Pool"]
    if location in east_list:
        return new_room[east_list.index(location)]
    
    else:
        return "You can't go that way."
#West function doing the same thing as north function but checks for west instead.
def west(location):
    west_list=["Main Hall","Loft","Bathroom 1","Dining Room","Kitchen","Bathroom 2","Theatre","Living Room","Office","Pool","Consevatory","Library","Playroom"]
    new_room=["Loft","Laundry Room","Bedroom 3","Bathroom 1","Dining Room","Kitchen","Living Room","Main Hall","Master Bedroom","Shed","Garden","Office","Theatre"]
    if location in west_list:
        return new_room[west_list.index(location)]
    else:
        return "You can't go that way."


print("Welcome to My Estate.The Estate currrently has no power.Your goal is to get the power up and running. The fuse box is in the shed however, the shed is locked. FIND THE KEY AND TURN THE POWER BACK ON! There are items all over the estate the will aid you in this adventure. GOOD LUCK!")

#While loop to keep the game going
event=True
#Empty inventory list to store the inventory the user picks up
inventory=[]
#Making the user start off in the main hall
curr_location = "Main Hall"
while event==True:
    #Updating the display and keeping screen of map open
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # else:
        #     pygame.event.clear()

    print()
    print("You are currently in ", curr_location, ".", sep = '')
    #Printing the decription for the current location
    print(description[names.index(curr_location)])
    print()

    #If the user enters the shed giving the option to end the game
    if curr_location=="Shed":
        question=input("Would you like to turn the power back on? (YES OR NO ANSWERS ONLY): ")
        if question.casefold()=="yes":    
            print("Congratulations. You've found the key and where able to turn the power back. You were a great help to the estate and we will always remember you!")
            print()
            print("THE END")
            exit()
    #Empty list to store all possible exits
    exits = []
    
    #Giving the user the option to add a flashlight to their inventory.
    if curr_location=="Main Hall" and "flashlight" not in inventory:
        flashlight=input("There's a flashlight on the floor. The flashlight will help you look for the key. Enter take in order to add it into your inventory. ")
        if flashlight.casefold()=="take":
            inventory.append("flashlight")
            print("Flashlight has been added into your inventory.")
            
    #Giving the user the option to add glasses to their inventory    
    if curr_location=="Laundry Room" and "glasses" not in inventory:
        glasses=input("There's glasses on the floor. These glasses will help you find a clue in the library. Enter take in order to add it into your inventory. ")
        if glasses.casefold()=="take":
            inventory.append("glasses")
            print("Flashlight has been added into your inventory")
            
    #Giving the user the option to add key to their inventory.
    if curr_location=="Gym" and "key" not in inventory:
        key=input("Congrats you found the key! In order to add it into your inventory enter take.")
        if key.casefold()=="take":
            inventory.append("key")
            print("Key has been added into your inventory.")

    print("From this location, you could go to any of the following:")
    #For loop to appending possible locations user could go to. 
    indx_location = names.index(curr_location)
    for i in adjancency_list[indx_location]:
        exits.append(names[i])
    #Printing possible exits.
    print()
    print("\t",exits)
    print()
    #Input function to ask the user which direction they want to go.
    next_location=input("Which direction would you like to go? ")
    
    #If user enters east, east function gets called to get the new location.
    if next_location.casefold()=="east":
        if east(curr_location) in names:
            curr_location=east(curr_location)
        #Else statment to print error message
        else:
            print(east(curr_location))
    #Elif statement to call west function if user enters west to get the new location.
    elif next_location.casefold()=="west":
        #If user tries to enter the shed without the key in there inventory, error message is displayed.
        if west(curr_location)=="Shed" and "key" not in inventory:
            print("The shed is currently locked, you need the key to enter.")
            curr_location=curr_location
        
        elif west(curr_location) in names:
            curr_location=west(curr_location)
        #Else statement to print error message
        else:
            print(west(curr_location))
    
    #Elif statement to call north function if user enters north to get the new location.
    elif next_location.casefold()=="north":
        if north(curr_location) in names:
            curr_location=north(curr_location)
        #Error message being displayed
        else:
            print(north(curr_location))
    
    #Elif statement to call south function if user enters south to get the new location.
    elif next_location.casefold()=="south":
        #If user tries to enter the shed without the key, error message is displayed.
        if south(curr_location)=="Shed" and "key" not in inventory:
            print("The shed is currently locked, you need the key to enter.")
            curr_location=curr_location
        
        elif south(curr_location) in names:
            curr_location=south(curr_location)
        
        #Errror message if south isn't a option
        else:
            print(south(curr_location))
    
    #If user enters stop the loop comes to the end.
    elif next_location.casefold()=="stop":
        event=False
    
    #If user enters inventory, their inventory is displayed.
    elif next_location.casefold()=="inventory":
        print(inventory)
    
    #If user enters something other than a direction or inventory or stop, error message is displayed.
    else:
        print("That is not a option")
    

# Loop to close the window when the user wants to.
