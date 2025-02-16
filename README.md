# FP2
Segundo projeto da cadeira de fundamentos de programação - 1º ano de faculdade

Go Game in Python

This project implements the game of Go in Python. The objective is to create a program that simulates the gameplay, including board setup, piece placement, and rule enforcement.
Features

    Goban: A 19x19 board (can be resized to 13x13 or 9x9).
    Pieces: Black and white stones are placed alternately.
    Chain and Liberty System: Tracks stone chains and liberties.
    Territory: Identifies and calculates controlled areas.
    Capture Mechanism: Stones with no liberties are captured.
    Illegal Moves: Includes rules like Suicide and Ko.
    Scoring: Determines the winner based on territory and captured stones.

Rules

    Game Start: The board is empty, and Black goes first.
    Turns: Players alternate placing stones or passing.
    Legal Moves:
        Stones can be placed on empty intersections.
        Stones are captured when surrounded by the opponent’s stones.
        Suicide and Ko are illegal moves.
    End Game: The game ends when both players pass consecutively, and the player with the most controlled territory and captured stones wins.

Getting Started

To play, run the Python program, which provides a turn-based interface for both players to place stones and view the game status.
Requirements

    Python 3.x

Installation

    Clone the repository:

git clone <repository-url>

Run the game:

    python go_game.py


Grade

    Grade for the project: 17.62
