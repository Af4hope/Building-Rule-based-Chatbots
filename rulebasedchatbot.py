import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Destination & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Paris", "Tokyo", "New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]
# Helper functions to normalize user input (remove extra spaces, make lowercase)
def normalize_input(user_input):
    return re.sub(r'\s+', ' ', user_input.strip().lower())
# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "TravelBot : Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You:")
    preference = normalize_input(preference)
    if preference in destinations:
        suggestions = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot : How about {suggestions}?")
        print(Forse.CYAN + "TravelBot: Do you like it?(yes/no)")
        answer = input(Fore.YELLOW + "You:").lower()
        if answer == "yes":
            print(Fore.GREEN + "TravelBot : Awesome! Enjoy{suggestions}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot : Let's try another.")
            recommend()  # Recursive call for new suggestions
        else:
            print(Fore.RED + "TravelBot : I'll suggest again.")
            recommend()  # Recursive call for new suggestions
    else:
        print(Fore.RED + "TravelBot : Sorry, I don't have that type of destination.")
        recommend()  # Recursive call for valid input
def packing_tips():
    print(Fore.CYAN + "TravelBot : Where to?")
    location = normalize_input(input(Fore.YELLOW + "You:"))
    print(Fore.CYAN + "TravelBot : How many days?")
    days = input(Fore.YELLOW + "You:")

    print(Fore.GREEN + f"TravelBot : Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Don't forget chargers and adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")
# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "-Offer packing tips (say 'packing)")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Type 'exit' or 'bye' to end.\n")
# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.Yellow + "Your name?")
    print()