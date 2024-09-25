import random

#Charger les citations depuis un txt
def load_quotes(filename):
    with open(filename, 'r') as file:
        quotes = file.readlines()
    return [quote.strip() for quote in quotes] #enlève les espaces en trop

#Genère une citation aléatoire
def generate_quote(quotes):
    return random.choice(quotes)

#Application
try:
    quotes_loaded = load_quotes('citations.txt')
    print("Ta citation du jour:")
    print(generate_quote(quotes_loaded))
except FileNotFoundError:
    print("Le fichier 'citations.txt' est introuvable.")
except Exception as e:
    print(f"Une erreur s'est produite: {e}")
