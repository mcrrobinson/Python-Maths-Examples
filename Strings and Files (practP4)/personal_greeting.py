# Write a personalGreeting function which, after asking for the user’s name, outputs a
# personalised greeting. E.g., for user input Sam, the function should output the 
# greeting Hello Sam, nice to see you! (note the details of the spaces and punctuation).

def personalGreeting():
    username = input("Enter a username: ")
    return "Hello "+username+", nice to meet you."

print(personalGreeting())