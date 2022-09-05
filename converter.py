import random
import string
import sys
import os
import uuid


binary = ""
word = ""
letters = []


def __init__():
    global DebugMode
    DebugMode = True


def text_to_binary():
    global binary
    word = input("Enter a sentence / word: ")
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
    print("Writing to Binary.txt")
    with open("Binary.txt", "w") as file:
        file.write(binary)

def binary_to_text():
    global word
    with open("Binary.txt", "r") as file:
        all_binary = file.read().splitlines()
    len_binary = len(all_binary)

    for y in range(len_binary):
        if all_binary[y] == "01000001":
            word += "A"
        if all_binary[y] == "01000010":
            word += "B"
        if all_binary[y] == "01000011":
            word += "C"
        if all_binary[y] == "01000100":
            word += "D"
        if all_binary[y] == "01000101":
            word += "E"
        if all_binary[y] == "01000110":
            word += "F"
        if all_binary[y] == "01000111":
            word += "G"
        if all_binary[y] == "01001000":
            word += "H"
        if all_binary[y] == "01001001":
            word += "I"
        if all_binary[y] == "01001010":
            word += "J"
        if all_binary[y] == "01001011":
            word += "K"
        if all_binary[y] == "01001100":
            word += "L"
        if all_binary[y] == "01001101":
            word += "M"
        if all_binary[y] == "01001110":
            word += "N"
        if all_binary[y] == "01001111":
            word += "O"
        if all_binary[y] == "01010000":
            word += "P"
        if all_binary[y] == "01010001":
            word += "Q"
        if all_binary[y] == "01010010":
            word += "R"
        if all_binary[y] == "01010011":
            word += "S"
        if all_binary[y] == "01010100":
            word += "T"
        if all_binary[y] == "01010101":
            word += "U"
        if all_binary[y] == "01010110":
            word += "V"
        if all_binary[y] == "01010111":
            word += "W"
        if all_binary[y] == "01011000":
            word += "X"
        if all_binary[y] == "01011001":
            word += "Y"
        if all_binary[y] == "01011010":
            word += "Z"
        if all_binary[y] == "00100000":
            word += " "

    print("Loading Binary.txt")
    print(f"The Word is: {word}")

trr = 2

if trr == 1:
    text_to_binary()

if trr == 2:
    binary_to_text()