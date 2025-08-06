# Blackjack Game in Racket

This project is a simple implementation of the classic card game **Blackjack** written in the Racket programming language. The game allows a single player to play against a dealer.

## Features

- **Deck Creation**: Generates a standard 52-card deck.
    
- **Shuffling**: Shuffles the deck before each game.
    
- **Player Interaction**: Prompts the player to "hit" or "stand."
    
- **Game Logic**: Implements the core rules of Blackjack, including scoring, determining winners, and handling dealer turns.
    
- **Card Counting**: Properly handles the value of aces as either 1 or 11.
    

## How to Play

To run this game, you will need a Racket environment.

1. **Save the code**: Save the provided code into a file named `blackjack.rkt`.
    
2. **Open DrRacket**: Launch the DrRacket IDE.
    
3. **Run the file**: Open the `blackjack.rkt` file and click the "Run" button.
    
4. **Follow the prompts**: The game will start, and you will be asked to make decisions via the console.
    

## Code Overview

The code is structured into several key procedures:

- `create-deck`: Generates a full 52-card deck by combining card numbers and symbols.
    
- `shuffle-deck`: A custom procedure to randomize the order of the cards in the deck.
    
- `list-length`: A helper function to count the number of elements in a list.
    
- `ace-count`: Counts the number of aces in a hand to help with scoring.
    
- `count-total-21`: Calculates the total score for a player's hand, aiming for 21.
    
- `count-total-17`: Calculates the total score for the dealer's hand, where the dealer must stand on 17.
    
- `start-game`: The main procedure that initiates the game, deals cards, and manages the game flow.
    

## Acknowledgements

- Uses built-in Racket functions like `cartesian-product` and `shuffle` as alternative, more concise implementations.