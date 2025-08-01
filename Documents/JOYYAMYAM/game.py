# --- Number Guessing Game ---
# This is the template file for the collaborative Git tutorial.

def get_player_guess():
    """
    Task for Student 1:
    1. Prompt the user to enter a number between 1 and 100.
    2. Read the input from the user.
    3. Convert the input to an integer.
    4. Return the integer.
    5. Add error handling for invalid input (e.g., text instead of a number).
    """
    # Student 1: Add your code here
	print("Debug: This is feature-get-guess branch")  # แก้ไขใหม่
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("❗ Please enter a number between 1 and 100.")
        except ValueError:
            print("❗ Invalid input. Please enter a number.")

def check_guess(secret_number, player_guess):
    """
    เปรียบเทียบตัวเลขที่ผู้เล่นทายกับตัวเลขลับ
    และส่งผลลัพธ์กลับเป็นข้อความ

    Returns:
        result (str): "ต่ำไป", "สูงไป", หรือ "ถูกต้อง!"
        correct (bool): True ถ้าทายถูก, False ถ้ายังไม่ถูก
    """
    if player_guess < secret_number:
        return "ต่ำไป", False
    elif player_guess > secret_number:
        return "สูงไป", False
    else:
        return "ถูกต้อง!", True
    """
    Task for Student 2:
    1. Compare the player's guess with the secret number.
    2. If the guess is correct, return the string "correct".
    3. If the guess is too high, return the string "high".
    4. If the guess is too low, return the string "low".
    """
    # Student 2: Add your code here
    pass

def play_game():
    """
    The main function to run the game.
    This part is already complete.
    """
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    # This part will be uncommented after the tasks are complete
    # import random
    # secret_number = random.randint(1, 100)
    # attempts = 0
    #
    # while True:
    #     attempts += 1
    #     guess = get_player_guess()
    #     result = check_guess(secret_number, guess)
    #
    #     if result == "correct":
    #         print(f"Congratulations! You guessed the number in {attempts} attempts.")
    #         break
    #     elif result == "high":
    #         print("Too high! Try again.")
    #     elif result == "low":
    #         print("Too low! Try again.")

if __name__ == "__main__":
    play_game()

