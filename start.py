

# random_no= random.randint(1,10)
# print(random_no)

# random_float= random.random() *3
# print(random_float)

# random_range= random.randrange(1,10)
# print(random_range)

# s="1234567890"
# li= list(s)
# print(li)

# print(random.choice(li))

# love_score= random.randint(1,100)
# print(f"Your Love score is {love_score}.")

# user_inp=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

# # print(type(user_inp))

# if user_inp=='0':
#    print("Rock")
# elif user_inp=='1':
#    print("Paper")
# elif user_inp=='2':
#    print("Scissors")
# else:
#    print("Enter a correct number dummy")

# list=[0,1,2]
# comp_choice=random.choice(list)

# if comp_choice==0:
#    print("Rock")
# elif comp_choice==1:
#    print("Paper")
# elif comp_choice==2:
#    print("Scissors")

# if user_inp=='0' and comp_choice==1:
#    print("You chose ROCK but comp chose PAPER, COMp WON")
# elif user_inp=='0' and comp_choice==2:
#    print("You chose ROCK but comp chose SCISSOR, YOU WON")
# elif user_inp=='0' and comp_choice==0:
#    print("You chose ROCK and comp also chose ROCK, TIE")
# elif user_inp=='2' and comp_choice==1:
#    print("You chose SCISSORS but comp chose PAPER, YOU WON")
# elif user_inp=='2' and comp_choice==2:
#    print("You chose SCISSORS but comp chose SCISSOR, YOU TIE")
# elif user_inp=='2' and comp_choice==0:
#    print("You chose SCISSORS and comp also chose ROCK, COMP WON")
# elif user_inp=='1' and comp_choice==0:
#    print("You chose PAPER but comp chose ROCK, you WON")
# elif user_inp=='1' and comp_choice==1:
#    print("You chose PAPER but comp chose PAPER, TIE")
# elif user_inp=='1' and comp_choice==2:
#    print("You chose  PAPER and comp also chose SCISSOR, COMP WON")



# list=[1,2,3,4,5]
# list.reverse()

# for i in list:
#    print(i)


# target=int(input())
# total=0
# for i in range(0,target+1,2):
#    total=total+i

# print(total)




# import random
# import hang_words
# from hang_logo import stages 
# from hang_logo import logo


# word_list = hang_words.word_list
# chosen_word = random.choice(word_list)

# print(logo)


# # print(f'shhhh, the solution is {chosen_word}.')


# display=[]
# for i in chosen_word:
#    display+="_"
# print(display)

# game_over= False
# lives=6
# while not game_over:

#    guess = input("Guess a letter: ").lower()
#    letter=chosen_word
#    if letter not in display:
#        print(f"{guess} is already used. Try a different letter.")

#    for i in range(len(chosen_word)):
#          letter= chosen_word[i]
#          if letter==guess:
#             display[i]=letter

#    print(f"{' '.join(display)}")

#    if guess not in chosen_word:   

#       lives-=1
#       if lives==0:
#          print("YOU LOSE")
#          print(f'The chosen word was {chosen_word}')
#          game_over=True

#    print(stages[lives])
      
#    # print(display)

#    if "_" not in display:
#        print("You WON")
#        game_over=True
   




  
  
      
import random
import hang_words
from hang_logo import stages 
from hang_logo import logo


word_list = hang_words.word_list
chosen_word = random.choice(word_list)

print(logo)


# print(f'shhhh, the solution is {chosen_word}.')
  

display=[]
for i in chosen_word:
   display+="_"
print(display)

#introducing new elements for storing correct, missed and a history of already used words
correctletter=missedletter=Aguessed=''
game_over= False
lives=6
# alreadyguessed=''
while not game_over:

   guess = input("Guess a letter: ").lower()
   letter=chosen_word

   #checking if the guessed letter is already guessed before or not
   if guess in Aguessed:
        print(f"{guess} is already used. Try a different letter.")
   #if not previously guessed, is that letter present in the chosen word
   elif guess not in letter:
        print(f"{guess} is not correct try again.")
        missedletter=guess

   #if the letter is there in the word, display them
   for i in range(len(chosen_word)):
         letter= chosen_word[i]
         if letter==guess:
            display[i]=letter
            correctletter=letter

   print(f"{' '.join(display)}")

   #changing value of Aguessed(already guessed) letter with correct and incorrect letters we found above
   Aguessed=correctletter+missedletter
   
   
   if guess not in chosen_word:   

      lives-=1
      if lives==0:
         print("YOU LOSE")
         print(f'The chosen word was {chosen_word}')
         game_over=True

   print(stages[lives])
      
   # print(display)

   if "_" not in display:
       print("You WON")
       game_over=True
