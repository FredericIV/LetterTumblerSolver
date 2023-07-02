#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filename = str(input("Enter the name of the dictionary file: "))
tumblers = list(range(0, int(input("Enter the number of tumblers: "))))
for i in tumblers:
    print ("Enter tumblerset ", i, ": ", sep="", end="")
    inputset = input()
    tumblers[i] = []
    for j in range(len(inputset)):
        if inputset[j].isalpha():
            tumblers[i].append(inputset[j].lower())

possible_words = [set() for x in range(len(tumblers)+1)]
with open(filename, "r") as f:
    dictionary = f.read().splitlines()
    for word in dictionary:
        if len(word) == len(tumblers):
            possible_words[0].add(word.lower())
    del dictionary
for i in range(len(possible_words)-1):
    for word in possible_words[i]:
        for letter in tumblers[i]:
            if letter == word[i]:
                possible_words[i+1].add(word)
                break
print(possible_words[len(tumblers)])