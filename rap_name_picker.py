import time
""" Code structure
 
- welcome(): prints intro
- get_user_input(): collects answers based on mood
- creator(): builds the rap name using logic
- main(): runs the program with replay support
"""

def welcome():
    print("Welcome to the Rap Name Generator!")
    print("This program will generate a rap name for you based on your input.")
    print("Let's get started!\n")

def get_user_input():
    valid_moods = ["chill", "savage", "energetic", "bored"]
    
    # keep asking for mood until a valid mood is entered
    while True:
        mood = input("How's your vibe like? (choices: chill, savage, energetic, bored) \n: ").lower().strip()
        if mood in valid_moods:
            print("Great! Let's slide with it. \n")
            break
        else:
            print("Cap mood! Please choose from the given choices.")

    # initialise variables for the rap name generator
    current_tshirt = spent_money = dance_move = actual_name = None

    if mood in valid_moods[0:3]:
        if mood in ["chill", "energetic"]:
            current_tshirt = input("What's the colour of your current t-shirt? \n: ").title().strip()
        if mood in ["chill", "savage"]:
            spent_money = input("What is the last thing you spent $R money on? \n: ").lower().strip()
        if mood == "energetic":
            dance_move = input("What's your favourite dance move? \n: ").title().strip()
    elif mood == "bored":
        print("Oh, We will make it smooth for you! \n")  
        actual_name = input("What's your actual first name? \n: ").upper().strip()
    
    return valid_moods, mood, current_tshirt, spent_money, dance_move, actual_name

def alternate_case(word):
    # create alternating lower and upper case letters in the input word
    result = ""
    for i, char in enumerate(word):
        if i % 2 == 0:
            result += char.lower()
        else:
            result += char.upper()
    return result


def creator():
    valid_moods, mood, current_tshirt, spent_money, dance_move, actual_name = get_user_input()
    rap_name = ""
    
    if mood == valid_moods[0]: # "chill"
        rap_name += current_tshirt
        rap_name += " "
        rap_name += spent_money
        rap_name = "Lil" + " " + alternate_case(rap_name)
    elif mood == valid_moods[1]: # "savage"
        rap_name += valid_moods[1]
        rap_name += " "
        rap_name += spent_money
        rap_name += " "
        rap_name += str(len(spent_money))
    elif mood == valid_moods[2]: # "energetic"
        rap_name += "Dj"
        rap_name += " "
        rap_name += current_tshirt
        rap_name += " "
        rap_name += dance_move
    else: # "bored"
        rap_name += actual_name[0] + actual_name[-1] 
        rap_name += " "
        rap_name += (valid_moods[3][::-1] + actual_name[-1]).title()
    
    print("Drop the beat! 🎶")
    time.sleep(3)
    print(f"Your rap name is: {rap_name} \n")
    return rap_name
        
def main():
    welcome()
    
    while True:
        creator()
        print("Big ups my G for using the coolest Rap Name Picker! \n")

        while True:
            replay = input("Do you want to try again? (y/n) \n: ").lower().strip()
            if replay in ["y", "yes"]:
                print("Alright! Let's get it again. \n")
                break # goes back to creator()
            elif replay in ["n", "no"]:
                print("Stay real, peace out dawg!")
                return # exits entire programme
            else:
                print("Invalid input. Please enter 'y' or 'yes' to replay or 'n' or 'no' to exit.")


if __name__ == "__main__":
    main()