import random

def choose_random_word():
  words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon"]
  return random.choice(words)

def display_word(word, guessed_letters):
  displayed_word = ""
  for letter in word:
    if letter in guessed_letters:
      displayed_word += letter
    else:
      displayed_word += "_"
  return displayed_word

def play_hangman():
  secret_word = choose_random_word()
  guessed_letters = []
  remaining_attempts = 6

  print("Welcome to Hangman!")
  print("Guess the word:", display_word(secret_word, guessed_letters))

  while remaining_attempts > 0:
    guess = input("Enter a letter (lowercase): ").lower()

    if not guess.isalpha():
      print("Invalid input. Please enter a letter.")
      continue

    if guess in guessed_letters:
      print("You already guessed that letter!")
      continue

    guessed_letters.append(guess)

    if guess in secret_word:
      print("Correct!")
    else:
      print("Incorrect!")
      remaining_attempts -= 1
      print("Tries left:", remaining_attempts)

    if remaining_attempts == 0:
      print("Game over. The word was:", secret_word)
      break

    displayed_word = display_word(secret_word, guessed_letters)
    print(displayed_word)

    if "_" not in displayed_word:
      print("Congratulations! You guessed the word:", secret_word)
      break

play_hangman()
