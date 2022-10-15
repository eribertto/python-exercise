#!/usr/bin/env python

# from book Python Class Course 2ed by Eric Matthes
# assignment to create Restaurant and User classes


class Restaurant:
    """class Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age attributes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Describe the traits of the restaurant"""
        print(f"{self.name} is serving {self.cuisine}\n")


restaurant = Restaurant("Teddys", "Spaghetti")
print(f"The restaurant is named {restaurant.name}.")
print(f"{restaurant.name} menu for today is {restaurant.cuisine}")
restaurant.describe_restaurant()

restaurant_one = Restaurant("Netongs", "Lapaz Batchoy")
restaurant_one.describe_restaurant()
restaurant_two = Restaurant("Dapli", "Kaldereta meat goat")
restaurant_two.describe_restaurant()
restaurant_three = Restaurant("Tatoys", "Seafoods Galore")
restaurant_three.describe_restaurant()
