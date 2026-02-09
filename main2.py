# Alexandher Arauz and Leo Sanchez


# My Version
# Abstraction and first function
def option(prompt, valid_options):
    choice = input(prompt)
    while choice not in valid_options:
        print("Invalid choice. Try again.")
        # this is a added loop
        print("These are your valid options:")
        for item in valid_options:
            print("-", item)
        choice = input(prompt)
    return choice

# Second function
# add a for loop or while loop
# append or remove
def tell_joke(joke):
    print("Knock Knock ")
    input()

    chosen_joke = {
        "robbers": ["Calder"],
        "tanks": ["Tank "],
        "pencils": ["Broken pencil "]
    }

    for line in chosen_joke[joke]:
        input(line)

    if joke == "robbers":
        print("Calder police - I've been robbed!")
        
    elif joke == "tanks":
        print("You are welcome! ")
        
    elif joke == "pencils":
        print("Nevermind, it's pointless! ")
    
    jokes.remove(joke)
        


# Main program

# List of Jokes
jokes = ["robbers", "tanks", "pencils"]

# start of the programming
print("Welcome to the Knock Kncok Joke Game!")
play = option("Do you want to hear a joke?", ["yes", "no"])

if play == "no":
    print("Okay suit yourself!")
else:
    # need to put a function and have the list "jokes" changed by either adding or removing more jokes
    while play == "yes":
        print("Great, lets play")
        joke = option("Choose a topic (robbers, tanks, pencils): ", jokes)
        tell_joke(joke)
        play = option("Do you want to hear another joke or are you finished?: ", ["yes","finished"])
        if play== "finished":
# The aftermath

            rate = int(input("Please rate our game 1-10!: "))
            final_score = int(rate * 10)
            print(str(final_score) + " percent satisfaction rate")
    
            friend = option("Would you recommend this game to a friend?:", ["yes", "maybe", "no"])

            if friend in ["yes", "maybe"]:
                print("Thanks, we appreciate it. ")
            else:
                print("Sorry you did not enjoy it. ")
        




# def 1st
# then for or while 
# then if/elif on one of the def




























# # My Version
# # Abstraction and first function
# def option(prompt, valid_options):
#     choice = input(prompt)
#     while choice not in valid_options:
#         print("Invalid choice. Try again.")
#         # this is a added loop
#         print("These are your valid options:")
#         for item in valid_options:
#             print("-", item)
#         choice = input(prompt)
#     return choice

# # Second function
# # add a for loop or while loop
# # append or remove
# def tell_joke(joke):
#     print("Knock Knock ")
#     input()

#     chosen_joke = {
#         "robbers": ["Calder"],
#         "tanks": ["Tank "],
#         "pencils": ["Broken pencil "]
#     }

#     for line in chosen_joke[joke]:
#         input(line)


#     if joke == "robbers":
#         input("Calder")
#         print("Calder police - I've been robbed!")
        
    
#     elif joke == "tanks":
#         input("Tank ")
#         print("You are welcome! ")
        
        
#     elif joke == "pencils":
#         input("Broken pencil ")
#         print("Nevermind, it's pointless! ")
    
#     jokes.remove(joke)
        


# # Main program

# # List of Jokes
# jokes = ["robbers", "tanks", "pencils"]

# # start of the programming
# print("Welcome to the Knock Kncok Joke Game!")
# play = option("Do you want to hear a joke?", ["yes", "no"])

# if play == "no":
#     print("Okay suit yourself!")
# else:
#     # need to put a function and have the list "jokes" changed by either adding or removing more jokes
#     while play == "yes":
#         print("Great, lets play")
#         joke = option("Choose a topic (robbers, tanks, pencils): ", jokes)
#         tell_joke(joke)
#         play = option("Do you want to hear another joke or are you finished?: ", ["yes","finished"])
#         if play== "finished":
# # The aftermath

#             rate = int(input("Please rate our game 1-10!: "))
#             final_score = int(rate * 10)
#             print(str(final_score) + " percent satisfaction rate")
    
#             friend = option("Would you recommend this game to a friend?:", ["yes", "maybe", "no"])

#             if friend in ["yes", "maybe"]:
#                 print("Thanks, we appreciate it. ")
#             else:
#                 print("Sorry you did not enjoy it. ")
        























































# if play == "no":
#     print("Okay suit yourself!")
# else:
#     # need to put a function and have the list "jokes" changed by either adding or removing more jokes
#     while play == "yes":
#         print("Great, lets play")
#         joke = option("Choose a topic (robbers, tanks, pencils): ", jokes)
#         tell_joke(joke)
#         play = option("Do you want to hear another joke or are you finished?: ", ["yes","finished"])

#         if play== "finished":
# # The aftermath

#             rate = int(input("Please rate our game 1-10!: "))
#             final_score = int(rate * 10)
#             print(str(final_score) + " percent satisfaction rate")
    
#             friend = option("Would you recommend this game to a friend?:", ["yes", "maybe", "no"])

#             if friend in ["yes", "maybe"]:
#                 print("Thanks, we appreciate it. ")
#             else:
#                 print("Sorry you did not enjoy it. ")
        



















#         elif play == "add":
#             new_joke = input("Enter a new joke topic: ")
#             jokes.append(new_joke)
#             print(new_joke, "has been added!")
#             play = "yes"

#         elif play == "remove":
#             print("Here are the current jokes: ")
#             for item in jokes:
#                 print("-", item)
            
#             remove_joke = option("Which joke do you want to remove? ", jokes)
#             jokes.remove(remove_joke)
#             print(remove_joke, "has been removed!")
#             play = "yes"
        
# def edit_jokes(jokes): 
#     action = option("Do you want to add or remove a joke? ", ["add", "remove", "none"]) 
#     while action != "none": 
#         if action == "add": 
#             new_joke = input("Enter a new joke topic: ").lower() 
#             jokes.append(new_joke) 
#             print(new_joke, "has been added!") 
#             elif action == "remove": 
#             print("Here are the current jokes:") 
#             for item in jokes: 
#                 print("-", item) 
#                 remove_joke = option("Which joke do you want to remove? ", jokes) 
#                 jokes.remove(remove_joke) 
#                 print(remove_joke, "has been removed!") 
#                 action = option("Add, remove, or none? ", ["add", "remove", "none"]) 
#                 return jokes