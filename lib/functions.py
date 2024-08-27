#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print("Hello, " + name + "!")

def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2

# Test calls
greet_programmer()           # Output: Hello, programmer!
greet("Alice")               # Output: Hello, Alice!
greet_with_default()         # Output: Hello, programmer!
greet_with_default("Bob")    # Output: Hello, Bob!
print(add(45, 55))           # Output: 100
print(halve(20))             # Output: 10.0
print(halve(5.5))            # Output: 2.75
