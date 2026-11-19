numbers = []

while True:
    number = input("Enter an integer or the 'Q'/'q' to exit: ")

    if number == "Q" or number == "q":
        break
    try:
        numbers.append(int(number)) # .appende is insert data to []
    except ValueError:
        print("only integer is allowed\n")

if len(numbers):
    numbers = numbers[::-1]

    print("\nIntegers in reversed order:", end = "")
    for num in numbers:
        print(num, end = " ")

else:
    print("No Integers.") 