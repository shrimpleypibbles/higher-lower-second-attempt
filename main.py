# 1. display logo
# 2. Randomly select two people (ie, two dictionaries)
# 3. display their name:, description:, and country:
# 4. display vs. logo
# 6. compare follower_count: to determine correct answer
# 6. have user guess who has a higher follower count
# 7. if user is right, delete entry from dictionary and choose another
# 8. award user a point
# 9. move the correct answer to position A
# 10. clear the screen


from game_data import data
import art
import random
from replit import clear

def format_data(choice):
    """takes the choice_a or choice_b and formats the data into something readable"""
    account_name = choice['name']
    account_desc = choice['description']
    account_country = choice['country']
    return f"{account_name}, a {account_desc} from {account_country}."

def follower_compare(guess, a_followers, b_followers):
    """takes user's guess and the follower counts from the dictionary and checks if user guess is correct """
    if a_followers > b_followers:
        # When the correct answer is A, if user's guess == a, returns True, otherwise False.
        return guess == "a"
    else:
        return guess == "b"


# 1. display logo
print(art.logo)
score = 1
should_continue = True

choice_b = random.choice(data)
while should_continue:
    # 2. Randomly select two accounts (ie, two dictionaries)
    choice_a = choice_b
    choice_b = random.choice(data)
    #just in case we're returned the same answer from a previous round 
    while choice_a == choice_b:
        choice_b = random.choice(data)

    if choice_a == choice_b:
        choice_b = random.choice(data)


    # 3. display their name:, description:, and country:

    print(f"Compare A: {format_data(choice_a)}")
    print(art.vs)
    print(f"Compare B: {format_data(choice_b)}")


    # 6. have user guess who has a higher follower count
    guess = input("Who has more followers? A or B: ").lower()

    # 6. compare follower_count: to determine correct answer

    a_followers = choice_a["follower_count"]
    b_followers = choice_b["follower_count"]
    is_correct = follower_compare(guess, a_followers, b_followers)
   
    clear()
    
    if is_correct:
        print(f"You're right! Current score: {score}")
        score += 1  
    else:
        print("Sorry, that's wrong.")
        should_continue = False
        

