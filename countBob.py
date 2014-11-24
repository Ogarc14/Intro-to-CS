# -*- coding: utf-8 -*-
#Code one was created by Michael D. Salerno.  This code uses a loop with a 'while true' statement to search for the string:  'bob' within the code and increase the count of num by one for each bob found
#furthermore, the code will be instructed to break once it is done searching for bob and cannot find anymore instances of string 'bob' within the code.  This is done by knowing that the program will return a -1 find for when there are no more bobs within the function and instructing the program to break off from the code when count + 2 = positive 1.
#this will not interfere with 'bob' being counted, because since 'bob' is three characters long, the lowest possible count that could be returned for a 'bob' that is found within the string, even if 'bob' is the very beginning of the string, is 2, since 'bob' is three letters long, 'bob' in the beginning of the string would be 0, + 2, and return 2, ensuring the code loop continues to search for more bobs, this time starting from character 2, the b of the first 'bob'


s = 'azcbobobegghaklbob'       #random number of letters created by Michael to test out the code and see if it worked appropriately; notice the use of permuatations to test if the code acknowledges bobob as two bobs
num = 0                        #initial assignment of number is zero, since the counter will increase the number by one every time the loop statement for while true returns a true statement
start = 0                      #start is at zero to identify to the find function that its starting location will be zero, as in the first character in the string
while True:                   # just keep doing the loop forever until we assign a break to the loop
    start = s.find(‘bob’, start) + 2      #using the find function, the program is being instructed to find 'bob' within the random string of letters in s, its starting location will be character zero, and each time it runs, it must start from the previous location where it stopped and add plus two to the characters, this is done in order to ensure that once the string no longer contains 'bob' and the return is -1, adding two will bring the return to one, and it will cause the loop to break, since the loop is instructed to break when start = 1
         if start != 1:       #if start is not equal to one, then the statement will hold true, the loop will continue, and the counter for 'num' will go up by plus one           
              num += 1        #increase num by one
         else:               #the loop break with an else clause if start is equal to one instead of not equal to one as explained above in lines 4 and 5
              break          #the break clause to not contain an infinite loop and tell the program to break off the loop and print the num
print(num)                   #the instruction to print the num after the loop has broken








#code from user:  PabloRestrepoValencia within the EDX course
#this code will simply be copied and pasted to use for my analysis of its implementation, this code is not mine, and was originally submitted to the intro to computer science course on EDX by the username above
#an error occured when the code tried to run the string of s = 'bobbncobobobo' and it did not return 3, but it returned an error
#the code provided the proper return for all other occurences of s and found the accurate number of 'bob'

def count_bob(s):
'''(str) -> int

Devuelve el numero de veces que aparece la palabra bob en s.      #spanish instructions that state to return the number of times that bob appears in s

>>> count_bob('bobobobarte')                                      #simply asking the program to count bob within a random string would not yield the correct answer.  The correct answer should be three within that code, but the return was two.  The reason for this is because of the command's inability to count bob's that repeat from the previous bob's final b.  Example:  If I used, s=bobobobobob; the program would return three instead of 5

2

>>> count_bob('xtr')                                              #there is no bob here to count, so the return of zero is accurate

0

'''

word = 'bob'                                                     #defining 'bob' as word to use word within the code; 'bob' can be assigned to almost anything, including a single letter by making x = 'bob', etc.

num = 0                                                          # assigning zero for the intiial number



for i in range(len(s) - 1):

    if s[i] == word[0] and s[i + 1] == word[1] and s[i + 2] == word[2]:  #the implementation here is asking the code to search within the string of s for 'bob' and if it finds 'bob' to begin 2 characters down the line from when it found 'bob', and then to increase the num + 1

            num += 1                                            #increase the count of num plus one while the for loop holds true

print num                                                      #return the count for number