#!/usr/bin/env python3

def happy_new_year():
    i = 10

    while i > 0:
        print(i)
        i -= 1
    print('Happy New Year!')

def square_integers(int_list):
   squared_list = [x ** 2 for x in int_list if isinstance(x, int)]
   return squared_list

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Fizz")
        else:
            print(i)