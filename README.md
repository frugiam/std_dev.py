# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/14/2024
# Description: Project 6c

def __init__(self, name, age):
    self.__name = name
    self.__age = age


def get_age(self):
    return self.__age


def std_dev(person_list):
    total = 0
    for person in person_list:
        total += person.get_age()
    mean_age = total / len(person_list)

    square_sum = 0
    for person in person_list:
        square_sum += (mean_age - person.get_age()) ** 2

    return (square_sum / len(person_list)) ** 0.5
