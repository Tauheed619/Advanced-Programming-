import os
import random

# Get path to the jokes file
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'resources', 'randomJokes.txt')

# Load jokes from file
def load_jokes(filename):
    jokes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if '?' in line:
                    setup, punchline = line.strip().split('?', 1)
                    jokes.append((setup.strip() + '?', punchline.strip()))
    except FileNotFoundError:
        print("Error: jokes file not found!")
    return jokes

# Main program
def tell_jokes():
    jokes = load_jokes(file_path)
    if not jokes:
        return

    print("Say 'Alexa tell me a Joke' to start or 'quit' to exit.")

    while True:
        user_input = input(">>> ").strip().lower()
        if user_input == "quit":
            print("Goodbye!")
            break
        elif user_input == "alexa tell me a joke":
            setup, punchline = random.choice(jokes)
            print("\n" + setup)
            input("Press Enter to see the punchline...")
            print(punchline + "\n")
            print("Ask for another joke or type 'quit' to exit.")
        else:
            print("Say 'Alexa tell me a Joke' or 'quit'.")

if __name__ == "__main__":
    tell_jokes()
