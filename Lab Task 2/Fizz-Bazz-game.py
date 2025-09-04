import random

def fizzbuzz_twist(rounds=20):
    print("Welcome to FizzBuzz Game!")
    print("Rule: First round -> number itself.")
    print("Next rounds -> (previous + current).")
    print("Write 'Fizz', 'Buzz', 'Fizz Buzz' or the number.\n")

    score = 0
    prev = None

    for r in range(1, rounds + 1):
        curr = random.randint(1, 30)   
        total = curr if prev is None else prev + curr

        if total % 15 == 0:
            correct = "Fizz Buzz"
        elif total % 3 == 0:
            correct = "Fizz"
        elif total % 5 == 0:
            correct = "Buzz"
        else:
            correct = str(total)

        print(f"Round {r} — Computer -> {curr}")
        user = input("Your answer: ").strip()

        if user.lower() == correct.lower():
            score += 1
            print("Correct! Score:", score, "\n")
            prev = curr
        else:
            print("Wrong! Correct was:", correct)
            print("Game Over! Final Score:", score)
            break

fizzbuzz_twist(30)
