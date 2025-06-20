import random
import time

def play_game():
    print("🌊🧜🏽‍♀️ Welcome to the Undersea Challenge! 🐚")
    print("✨ I'm Zyra Shell, your sea guide to secrets & surprises...\n")
    
    name = input("💬 What's your name, adventurer? ")
    print(f"👋 Nice to meet you {name}!")
    time.sleep(1)
    
    print("🤫 I'm thinking of a number between 1 and 100....")
    time.sleep(1)
    
    ready = input("💫 Can you guess it? (Yes/No): ").lower()
    if ready not in ['yes', 'y', 'sure', 'ok', 'yeah']:
        print("\n🧜🏽‍♀️ Zyra Shell whispers: \"No worries, the sea holds your magical treasure until you're ready... 🌊\"")
        print("💎 Come back when you're ready to discover it!")
        return

    print("\nGreat! 🎁 A magical reward awaits if you succeed!")
    print("\n🔮 Let the guessing begin!\n")
    time.sleep(1)

    secret = random.randint(1, 100)
    guess = None

    while guess != secret:
        try:
            guess = int(input("🔢 Enter your guess: "))
            if guess < secret:
                print("📉 Too low. Try again!\n")
            elif guess > secret:
                print("📈 Too high. Try again!\n")
        except ValueError:
            print("⚠️ Please enter a valid number.\n")

    # Correct guess
    print(f"\n🌟 You got it, {name}! The number was {secret}.")
    print("🎊 You're a SUPER STAR! Use Code: ZyCodes at checkout for a surprise discount at www.luxiriesarchv.com 💝")

    # Ask to play again
    again = input("\n🔁 Want to play again? (yes/no): ").lower()
    if again in ['yes', 'y', 'sure', 'ok', 'yeah']:
        print("\n🔄 Restarting the game...\n")
        time.sleep(1)
        play_game()
    else:
        print("👋 Thanks for playing! Visit luxiriesarchv.com 💅")

# Start the game
play_game()

