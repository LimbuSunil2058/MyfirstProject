import random
print(" \n")
print("        WELCOME TO WORD GUESSING GAME")
print("   YOU HAVE 5 CHANCES IF YOU GUESS WRONG ANSWER")
print("===============================================================================================")
# While loop for play next game
while True:
  Animals=['elephant' , 'tiger' , 'gorilla' , 'chimpanzee' , 'dolphin' , 'whale' , 'shark' , 'jellyfish' , 'squid' , 'snail' , 'spider' ,'ant' , 'bee' , 'butterfly' , 'lizard' , 'snake' , 'crocodile' , 'alligator' , 'hippopotamus' , 'rhinoceros' , 'zebra' , 'horse' , 'cow' , 'dog' , 'cat' , 'squirrel' , 'deer' , 'bear' , 'wolf' , 'fox' , 'skunk' , 'raccoon' , 'opossum' , 'hamster' ]
  Birds=['parrot','owl','falcon','baldeagle','sparrow','woodpecker','bluejay','robin','pigeon','cardinal','finch','hummingbird','oriole','swallow','cuckoo','osprey','eagle','vulture',' pelican','albatross','seagull','stork','heron']
  NaturalDisasters=['earthquake','hurricane','tsunami','flood','wildfire','tornado','drought','landslide','blizzard','heatwave','volcano']
  Philosophy=['mythology','enlightenment','ethics','epistemology','metaphysics','aesthetics','logic','political', 'philosophy','existentialism','pragmatism','feminism','objectivism','utilitarianism','nihilism','cynicism','stoicism','idealism','realism','humanism']
  Science=[' physics','chemistry','biology', 'astronomy','geology','meteorology','neuroscience','psychology','sociology','ecology','anthropology','internet','artificial','intelligence','robotics','biotechnology','nanotechnology','spacetechnology','renewableenergy','cryptography','blockchain','virtualreality','augmentedreality']

  All=[Animals,Birds,NaturalDisasters,Philosophy,Science]
  first_choose=random.choice(All)
  if(first_choose is Animals):
      print("Hints: Animal Name")
  elif(first_choose is NaturalDisasters):
    print("Hint: Related To Naturaldisaster")
  elif(first_choose is Birds):
    print("Hint: Birds Name")
  elif(first_choose is Philosophy):
      print("Hint: Related To Philoshopy")
  else:
      print("Hint: Related To Science And Technology")
  # print(first_choose)
  randon_animal=random.choice(first_choose)
  print("The length of the word is:  ",len(randon_animal))
  print(randon_animal)
  #Function to show first and last word and '_' in the middle
  def first():
   res=[]
   #n=random.randint(1,3)
   res.append(randon_animal[0])
   i=1
   for i in range(int(len(randon_animal))-2):
     res.append("_")
   res.append(randon_animal[-1])
   return (res)
 
  guess_word=first()
  print(guess_word)
 
  count=5

  while True:   
  
     if(count!=0):
     
      
      
       a = input("Enter the guess word: ")
       new_word = []
    
       if a in randon_animal[1:-1]:
      
         for j, k in zip(randon_animal, guess_word):
   
          
              if k == '_' and a == j:
                  new_word.append(a)
              else:
                 new_word.append(k)
            
         guess_word = new_word
         result=''.join(new_word)
        
         print(guess_word)
         print("-->",result)
     
         if(result==randon_animal):
             print("Congralution!!!! You win the game")
             break
       else:
           print("You'r input is wrong")
       
        
           count=count-1
           print(f"You have {count} chances")
           print("\n")
           print(guess_word)
        
     else:
      print("You MF Loose Simple Game Focus On Study")
      print("The correct answer is: ",randon_animal)
      break
  c=input("press Enter for play another game: ")
  print("\n")    
      
      
      
    