# N = 10
# sum_squares = 0
# i = 1
# while i in range (11):
#     sum_squares = sum_squares + (i * i)
#     i = i + 1
# print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}")
# def function ():
#     print ('Hello world!')
# function () 
# def print_message(message):
#     print(message)
# print_message("Це повідомлення з функції.")
# message = "Hello world!"
# def function (message):
#     print (message)
# function(message)
# N = 10
# def function(N):
#     sum_squares = 0
#     i = 1
#     while i <= N:
#         sum_squares = sum_squares + i * i
#         i = i + 1
#     return sum_squares
# result = function(N)
# print(result)
# first_name = "John"
# last_name = "Doe"
# def get_fullname(first_name, last_name):
#     return first_name + " " + last_name   
# fullname = get_fullname(first_name, last_name)
# print (fullname)
# first_name = "John"
# last_name = "Doe"
# def get_initials(first_name, last_name):
#     return last_name + " " + first_name[-4] + "."
# formatted_name  = get_initials(first_name, last_name)
# print (formatted_name)
# first = "Python"
# second = "python"
# def compare(first, second):
# result = compare(first, second)
# print (result)
# first = "Python"
# second = "python"
# def compare(first, second):
#     return first.lower() == second.lower()
# result = compare(first, second) 
# # print (result)
# text = "Hello, world! Welcome to the world of Python."
# position = text.find("world")
# print (position)
# updated_text = text.replace("world", "planet")
# print (updated_text)
# product_name = "Coffee Maker"
# product_price = 7500.50
# product_quantity = 15
# def format_product_info(product_name, product_price, product_quantity):
#     return f"Product: {product_name}, Price: {product_price} UAH, Quantity: {product_quantity} pcs."
# product_info = format_product_info(product_name, product_price, product_quantity)
# print (product_info)
# class Car:
#    vehicle_type = "Automobile"
# def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
# class Car:
#     vehicle_type = "Automobile"

    # def __init__(self, make, model, year):
    #     self.make = make
#         self.model = model
#         self.year = year
#     def get_info(self):
#         return f"{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}"
# class Car:
#     vehicle_type = "Automobile"
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_info(self):
#         return f"{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}"
# car_ford = Car ("Ford", "Mustang", 2022)
# car_toyota = Car ("Toyota", "Corolla", 2021)
# print(car_ford.get_info())
# print(car_toyota.get_info())
# message = "Hello world!"
# def function (message):
#     print (message)
# function (message)
# n = 5000

# hours = n // (60 * 60)
# minutes = (n - hours * 60 * 60) // 60
# seconds = n - hours * 60 * 60 - minutes * 60
# time = f"{hours}g {minutes}m {seconds}s"
# print (time)
# condition = 7
# if condition == 6:
#     value = 10
# else:
#     value = 20
# print(value)
# sentence = "The quick brown fox jumps over the lazy dog"
# length = 0
# for i in sentence:
#     if i != ' ':
#         length = length + 1
#         print(length)
# summary = 0
# for i in range(1, 101):  # Додайте необхідні параметри до функції range
#     summary = summary + i
#     print(summary)
    # Вам потрібно дописати параметри до функції range() у циклі for, щоб код коректно обчислював суму всіх цілих чисел 
    # від 1 до 100 включно. 
    # Після виконання циклу значення змінної summary буде зберігати суму всіх чисел у заданому діапазоні: 5050.
#     N = 10
# sum_squares = 0
# i = 1
# while i in range (11):
#     sum_squares = sum_squares + (i * i)
#     i = i + 1
# print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}")
# first_name = "Олексій"
# last_name = "Гупало"
# full_name = first_name + " " + last_name
# print(len(full_name))
# first_name = "John"
# last_name = "Doe"
# def get_initials(first_name, last_name):
#     return last_name + " " + first_name[0] + "."
# formatted_name  = get_initials(first_name, last_name)
# print (formatted_name)
# my_list = [1, 2, 3, 4, 2, 2, 5, 2]
# count_2 = my_list.count(2)
# print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази
# words = ["banana", "apple", "cherry"]
# words.sorted(key=len)
# print(words)  # Виведе ['apple', 'banana', 'cherry']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reverse_numbers = numbers[::-1]
# # print(reverse_numbers)
# rate = 1.68
# value_day = 97
# value_night = 65
# payment = (rate * value_day) + (value_night * (rate / 2))
# print(payment)
# length = 2.75
# width = 1.75
# area = length * width
# show = f'With width {width} and length {length} of the room, its area is equal to {int(area)}'
# print(area)
# length = "2.75"
# width = "1.75"
# area = float(length) * float(width)
# show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# print(show)
# name = input("Your name? ")
# email = input("Your email? ")
# age = int(input("Your age? "))
# height = float(input("Your height? "))
# is_active = bool(input("Is active? "))
# print(type(name), type(email), type(age), type(height), type(is_active))
# length = float(input("Room length? "))
# width = float(input("Room width? "))
# area = length * width
# print(area)
# my_list = []
# my_list.insert(0, 2024)
# my_list.insert(1, 'Python')
# my_list.insert(2, 3.12)
# print(my_list)
# my_list = [2024, 3.12]
# some_data = ['Python']
# my_list.extend(some_data)
# my_list.reverse()
# print(my_list)
# data = {}
# data ["year"] = 2024
# data ["lang"] = 'Python'
# data ["version"] = 3.12
# # print(data)
# cat = {}
# info = {"status": "vaccinated", "breed": True}
# cat ["nick"] = "Simon"
# cat ["age"] = 7
# cat ["characteristics"] = ["лагідний, кусається"]
# age = cat.get("age")
# cat.update({"status": "vaccinated", "breed": True})
# print(cat)
#a = 3
#b = 4
#print("{a} + {b} = {a + b}")