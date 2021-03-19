number = int(input("ENTER THE NUMBER: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "IS NOT PRIME NUMBER")
            break
    else:
        print(number, "IS A PRIME NUMBER")
else:
    print(number, "IS NOT PRIME NUMBER")