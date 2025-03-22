
Joke = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs.'"
Sorry = "I Only Tell Jokes"

def bot():
    user_input = input("What Do You Want? ")

    if "Joke" in user_input:  # Fixed variable name
        print(Joke)
    else:
        print("I Don't Understand")

bot()
