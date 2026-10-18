import time

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds = seconds - 1
    print("Time's up!")

while True:
    try:
        seconds = int(input("How many seconds? "))
        if seconds <= 0:
            print("Please enter a positive number!")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number!")
countdown(seconds)
