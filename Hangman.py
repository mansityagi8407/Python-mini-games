import random

# 1. Words ki ek simple list
words = ["apple", "mango", "banana", "python", "code"]
target_word = random.choice(words)

# 2. Khali jagah (underscores) dikhane ke liye string
guessed_word = "_" * len(target_word)
attempts = 5

print("--- Welcome to Hangman ---")

# 3. Game tab tak chalega jab tak attempts bache hain ya word guess nahi ho jata
while attempts > 0 and "_" in guessed_word:
    print(f"\nWord: {guessed_word}")
    print(f"Attempts left: {attempts}")
    
    guess = input("Guess a letter: ").lower()

    if guess in target_word:
        # Naya guessed_word banana logic
        new_guessed_word = ""
        for i in range(len(target_word)):
            if target_word[i] == guess:
                new_guessed_word += guess
            else:
                new_guessed_word += guessed_word[i]
        
        guessed_word = new_guessed_word
        print("Yes you are Right")
    else:
        attempts -= 1
        print("Oops Wrong! Try Again ")

# 4. Final Result
if "_" not in guessed_word:
    print(f"\nYou Win! Word is: {target_word}")
else:
    print(f"\nGame Over! Correct word is: {target_word}")
    