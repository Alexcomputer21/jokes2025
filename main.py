


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes


# Original Version
# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")









































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
def tell_joke(joke):
    print("Knock Knock ")
    input()
    if joke == "robbers":
        input("Calder")
        print("Calder police - I've been robbed!")
    
    elif joke == "tanks":
        input("Tank ")
        print("You are welcome! ")
        
    elif joke == "pencils":
        input("Broken pencil ")
        print("Nevermind, it's pointless! ")


# Main program

# List of Jokes
jokes = ["robbers", "tanks", "pencils"]

# start of the programming
print("Welcome to the Knock Kncok Joke Game!")
play = option("Do you want to hear a joke?", ["yes", "no"])

if play == "no":
    print("Okay suit yourself!")
else:
    while play == "yes":
        print("Great, lets play")
        joke = option("Choose a topic (robbers, tanks, pencils): ", jokes)
        tell_joke(joke)
        play = option("Do you want to hear another joke or are you finished?: ", ["yes","finished" ])

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






























# My first version

# joke_topics = ["robbers", "tanks", "pencils"]
# print("Welcome to the Knock Knock Joke Game!")
# def tell_joke(joke):
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "no":
#         print("Okay suit yourself!")
#     while joke == "yes":
#         print("Great, Let's Play")
#         print(input("Choose a topic: ", joke_topics))
#         tell_joke(joke)
#         question = input("Do you want to hear another joke or are you finished? ")
       
#     if joke == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#     elif joke == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#     elif joke == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#     else:
#         input("Not register in my list of jokes")

#     if question == "finished":
#         rate = int(input("Please rate our game 1-10! "))
#         final_score = int(rate * 10)
#         print(str(final_score) + " percent satisfaction ")
#         friend = input("Would you recommend this game to a friend? ")
#         if friend == "yes" or friend == "maybe":
#             print("Thanks, we appreciate it. ")
#         else:
#             print("Sorry you did not enjoy it. ")
 






