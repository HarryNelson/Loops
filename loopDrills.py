'''
Created on Nov 2, 2019

@author: ITAUser
'''
#EX) Declare a variable set to 3. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 0.
i = 3;
while i > 0:
    print(i)
    i -= 1

'''
END OF EXAMPLE
'''

'''
START HERE
'''

'''While Loops'''
#1) Declare a variable set to 4. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 1.

i = 4;
while i > 0:
    print(i)
    i -= 1

#2) Declare a variable set to 14. Make a while loop that prints the variable 
#    you just created and increments the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 20.

i = 14;
while i > 1:
    print(i)
    i += 20

#3) Declare a variable set to 55. Make a while loop that prints the variable 
#   you just created. Then make an if statement that makes the loop break when
#   the variable is equal to 50. 

o = 55;
while o > 50:
    print(o)
    o -= 1
    if o == 50:
        break

'''For Loops'''
#4) Create a list named sports. Put three sports into the list. Create
#   a for loop that prints each sport in the list

sports = ["soccer", "basketball", "football"]
for sport in sports:
    print(sport)

#5) Create a for loop that loops through each letter in a string of one of your
#   favorite songs. Each iteration should print should a letter of the word. 

lewiscapaldi = [" ","s","o","m","e","o","o","n","e"," ","y","o","u"," ","l","o","v","e","d"]
for capaldi in lewiscapaldi:
    print(capaldi) 

#6) Create a list named movies. Put five of your favorite movies into the list.
#   However, make sure one of the movies is Avatar. 
#   Create a for loop that iterates over the list. In the loop print the movie
#   being looped over, but create an if statement that breaks out of the 
#   loop if it is Avatar.

movies = ["the lion king","avatar","big hero 6","black panther"]
for movie in movies:
    print(movie)
    if movie == "avatar":
        break
