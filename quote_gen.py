import random

#Liste de citations
quotes = [
    "L'amour, c'est offrir quelque chose à l'âme et au coeur de l'autre, un élan, une vie, une inspiration, afin que cet être-là s'épanouisse et avance dans la lumière et dans la joie. - Omraam Mikhaël Aïvanhov ",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Do not watch the clock. Do what it does. Keep going. - Sam Levenson",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "Believe you can and you're halfway there. - Theodore Roosevelt"
]

#Genère une citation aléatoire
def generate_quote():
    return random.choice(quotes)

#Affiche la citation
print("Ta citation du jour:")
print(generate_quote())