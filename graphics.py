#!/usr/bin/env python
# coding: utf-8

hangman_graphics = [
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
GAME OVER !""",
]


def update_status(fails):
    """update hangman graphics"""
    print(hangman_graphics[fails])
    print("\n")


if __name__ == "__main__":
    for item in hangman_graphics:
        print(item)
