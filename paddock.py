#!/usr/bin/env python3

import random
import pyfiglet

QUOTES = [
    ("Through goes Hamilton", "David Croft"),
    ("Simply lovely", "Du Du Du Max Verstappen"),
    ("We are checking", "Ferrari Mechanics xD"),
    ("Must be the water", "The Prince of Monoco, Charles Leclerc"),
    ("Ki ki rahh!", "Daniel Ricciardo"),
    ("Smooth operator", "Carlos Sainz"),
    ("Multi 21 Seb.", "Mark Webber"),
    ("Leave me alone, I know what I'm doing!", "The Iceman, Kimi Räikkönen"),
    ("No, Michael, no, no! That was so not right!", "Toto Wolff"),
    ("Valteri, its James.", "James knows everything Vowels"),
    ("I am stupid.", "Charles Leclerc"),
    ("Is that Glock?! Slowing Down?", "James Allen"),
    ("GP2 engine, GP2... ARGH!", "Fernando Alonso"),
    ("Sebastian Vettel, YOU ARE THE WORLD CHAMPION!", "Christian Horner"),
    ("Everyone is a Ferrari fan. Even if they're not, they are Ferrari fans.",
     "Sebastian Vettel"),
    ("Ring-ding-ding-ding-ding!", "Mr. Vettel")
]

FONTS = [
    "ansi_shadow",
    "slant",
    "standard",
    "big",
    "banner3-D",
    "speed",
    "doom",
    "starwars",
    "small",
    "smslant",
]


def main():
    quote, author = random.choice(QUOTES)
    font = random.choice(FONTS)

    print()
    try:
        text = pyfiglet.figlet_format(quote, font=font, justify="center")

        print(text)
    except FileNotFoundError:
        print(f'  "{quote}"')

    print(f"\n    — {author}\n")


if __name__ == "__main__":
    main()
