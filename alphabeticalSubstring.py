s = 'dlhgdfaghsdfbngklzrsdcvsdycabcdefgbhuuiguigbpubipabcdefghijklmmmmnopdfuivifsvdjvbd'  #random s to test my code and make sure that it returns the longest alphabetical substring, which is:  'abcdefghijklmmmmnop'

import string
allTheLetters = string.lowercase  #Found the code for getting all the letters online; this particular example will contain all the letters in lowercase and capital letters are not needed
                                  #Tested to see if this code would work for getting the letters by asking the progra to print allTheLetters before I continued
#print allTheLetters              #the output was correct for allTheLetters:  abcdefghijklmnopqrstuvwxyz


#one idea on solving this problem is by implementing an algorithm that will select the first letter, then the second letter, test to see if it is in alphabetical order
#if in alphabetical order, the program now tests the third letter
#if the third letter is in alphabetical order too, the program will run a booleah
#if the length of the third letter added is longer than the previous alphabetical length, the program takes the new string as the longest answer
#this test will continue until the end of the program, where the only answer should be the longest alphabetical string
#print the longest alphaebtical string

#i still don't know how to code it, but I am working on it.