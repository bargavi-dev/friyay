#take a number input and print out the range from the number 1 to that number input

given_num = int(input('What is the number? '))



#for any number input that can be divided by BOTH 3 and 5, print "fizzbuzz"

for number in range(1, given_num + 1):
    if number % 3 == 0 and given_num % 5 == 0:
        print(str(number) + ": fizz buzz")
#for any number input that can be divided by 3, print "fizz"

    elif number % 3 == 0:
        print(str(number) + ": fizz")

#for any number input that can be divided by 5, print "buzz"

    elif number % 5 == 0:
        print(str(number) + ": buzz")

#if number input is not divisible by any of the numbers, then:



   
    