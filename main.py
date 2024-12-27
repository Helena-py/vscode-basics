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
n = 5000

hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60
time = f"{hours}g {minutes}m {seconds}s"
print (time)