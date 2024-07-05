     
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
