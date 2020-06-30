def main():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    total = num1 + num2
    print("What is " + str(num1) + " + " + str(num2) + "?")
    your_answer = int(input("Your answer: "))
    streak = 0
    while streak != 3:
        if your_answer == total:
            streak += 1
            print("Correct! You've gotten " + str(streak) + " in a row.")
        if your_answer != total:
            streak = 0
            print("Incorrect. The expected result is " + str(total))
        if streak == 3:
            print("Congratulations! You mastered addition.")
        else:
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            total = num1 + num2
            print("What is " + str(num1) + " + " + str(num2) + "?")
            your_answer = int(input("Your answer: "))

if __name__ == '__main__':
    main()
