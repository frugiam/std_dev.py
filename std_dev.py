# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/14/2024
# Description: Project 6c

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def std_dev(person_list):
    # Compute the mean age
    sum_ages = 0
    for person in person_list:
        sum_ages += person.age
    mean_age = sum_ages / len(person_list)

    # Compute the standard deviation
    sum_squared_differences = 0
    for person in person_list:
        sum_squared_differences += (person.age - mean_age)**2
    variance = sum_squared_differences / len(person_list)
    return (variance ** 0.5)