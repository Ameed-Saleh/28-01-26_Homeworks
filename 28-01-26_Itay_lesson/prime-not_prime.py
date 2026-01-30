# check if number is prime using while True
i = 2
number = int(input('number?'))
while True:
    if number == 2 :
        print(number, "is prime")
        break
    if number <= 1 or number % i == 0:
        print(number, "is not prime")
        break
    if number % i != 0:
        i = i + 1
        if number == i:
          print(number, "is prime")
          break


