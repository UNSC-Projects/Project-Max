import random
import string
import sys
import os
import uuid


binary = ""
letters = []


def __init__():
    global DebugMode
    DebugMode = True


def text_to_binary():
    global binary
    word = input("Enter a base plate of letters (can only be one word): ")
    len_word = len(word)
    for x in range(len_word):
        letters.append(word.upper()[x])
    len_letters = len(letters)

    for y in range(len_letters):
        if letters[y] == "A":
            binary += "01000001"
        if letters[y] == "B":
            binary += "01000010"
        if letters[y] == "C":
            binary += "01000011"
        if letters[y] == "D":
            binary += "01000100"
        if letters[y] == "E":
            binary += "01000101"
        if letters[y] == "F":
            binary += "01000110"
        if letters[y] == "G":
            binary += "01000111"
        if letters[y] == "H":
            binary += "01001000"
        if letters[y] == "I":
            binary += "01001001"
        if letters[y] == "J":
            binary += "01001010"
        if letters[y] == "K":
            binary += "01001011"
        if letters[y] == "L":
            binary += "01001100"
        if letters[y] == "M":
            binary += "01001101"
        if letters[y] == "N":
            binary += "01001110"
        if letters[y] == "O":
            binary += "01001111"
        if letters[y] == "P":
            binary += "01010000"
        if letters[y] == "Q":
            binary += "01010001"
        if letters[y] == "R":
            binary += "01010010"
        if letters[y] == "S":
            binary += "01010011"
        if letters[y] == "T":
            binary += "01010100"
        if letters[y] == "U":
            binary += "01010101"
        if letters[y] == "V":
            binary += "01010110"
        if letters[y] == "W":
            binary += "01010111"
        if letters[y] == "X":
            binary += "01011000"
        if letters[y] == "Y":
            binary += "01011001"
        if letters[y] == "Z":
            binary += "01011010"
        if letters[y] == " ":
            binary += "00100000"
        binary += "\n"

    print(f"The Given Word: {word}\tThe Binary Version,")
    print(binary)