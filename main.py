import random, time

def renderGame():

  file = open("words.txt", "r")
  lines = file.readlines()
  
  userGuesslist = []
  userGuesses = []
  
  secretWord = random.choice(lines)[:-1]
  
  #menu 
  print("Welcome to Hangman!")
  time.sleep(1)
  userinput = input("Click enter when you want to play")
  
  if userinput == "":
    playGame = True
  
  #game
  if playGame:
      time.sleep(1)
      secretWordList = list(secretWord)
      attempts = (len(secretWord) + 2)
  
      def printGuessedLetter():
          print("Your Secret word is: " + ''.join(userGuesslist))
  
      for n in secretWordList:
          userGuesslist.append('_')
      printGuessedLetter()
  
      print("The number of allowed guesses for this word is:", attempts)
  
  while True:
    print("Guess a letter:")
    letter = input()
    if letter in userGuesses:
      print("You already guessed this letter, try something else.")
    else:
      
      attempts -= 1
      userGuesses.append(letter)
      if letter == secretWord:
        print("You guessed the word, well done!")
        print("The secret word: " + secretWord.upper())
        break
      elif letter != secretWord:
        print("Opps! Try again!")
      if letter in secretWordList:
        print("Nice guess!")
        if attempts > 0:
          print("You have ", attempts, 'guess left!')
          for i in range(len(secretWordList)):
            if letter == secretWordList[i]:
              letterIndex = i
              userGuesslist[letterIndex] = letter.upper()
          printGuessedLetter()
        else:
            print("Oops! Try again.")
            if attempts > 0:
              print("You have ", attempts, 'guess left!')
            printGuessedLetter()
  
      joinedList = ''.join(userGuesslist)
      print(joinedList)
      if joinedList.upper() == secretWord.upper():
        print("Yay! you won.")
        break
      elif attempts == 0:
        print("Too many Guesses!, Sorry better luck next time.")
        print("The secret word was: " + secretWord.upper())
        break
  
renderGame()
