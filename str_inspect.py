# -*- coding: utf-8 -*-
"""
John Oates
CPSC 223P-01
1/25/2021
joates@fullerton.edu
"""
#read sys.argv[1]
import sys
sentence = sys.argv[1]
words = sentence.split()
#declared the initial value to start at 0
long_word_length = len(words[0])
short_word_length = len(words[0])

#loop the words array to and declaring if the variable current word could be either the shortest or longest 
for x in words:
  words_length = len(x)
  if words_length > long_word_length:
    long_word_length = words_length
    long_word = x
  if words_length < short_word_length:
    short_word_length = words_length
    short_word = x

#reads if the words have multiple characters or one and prints out
if short_word_length == 1:
  print("Shortest word:", short_word)
  print("It is", short_word_length,"character")
else:
  print("Shortest word:", short_word)
  print("It is", short_word_length,"characters")
if long_word_length == 1:
  print("Longest word:", long_word)
  print("It is", long_word_length,"character")
else:
  print("Longest word:", long_word)
  print("It is", long_word_length,"characters")

# This is my second Python program. It inspects strings.
