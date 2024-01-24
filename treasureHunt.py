# creating a treasure hunt game
# fetch the treasure highland code from ascii.co.ku/art(copy and paste) press ctr+f to search
from random import choices


print('''
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
 ejm97   /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /

''')
print("Welcome to treasure highland")
print("Your mission is to find the treasure")
choice1 = input('You\'re at a crossroad, where do you want to go?,Type "left" or "right" to proceed.').lower()
if choice1 == "left":
  choice2 = input('You\'ve to a lake, there is an island in the middle of the lake.Type "wait" to wait for a boat or type "swim" to swim accorss').lower()
  if choice2 == "wait":
    choice3 = input("You arrived at the island unharmed,there is a house with three doors, one red , one blue and the other one yellow, which door will you choose?").lower()
    if choice3 == "red":
      print("you entered a room full of beasts, GAME OVER!")
    elif choice3 == "yellow":
      print("You found the treasure,YOU WIN!")
    elif choice3 == "blue":
      print("You entered a room full of wasps, GAME OVER!")
    else:
      print("You chose the door that doesnt exist, GAME OVER!")    

  else:
    print("You got attacked by an andry traut, GAME OVER! ")  
else:
    print("You fell into a hole, GAME OVER!")


