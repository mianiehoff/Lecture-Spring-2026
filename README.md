# Lecture Spring 2026

Copyright 2026 Mia Greta Niehoff

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)

This project is released under the Apache License 2.0.

## Functions
- `find_best_combination_of_vehicles(passengers)`
This function takes an integer representing the number of passengers that need to be transported. It efficiently distributes the passengers across three types of vehicles: minibusses (13 people), minivans (7 people), and normal cars (5 people). The goal is to use as few vehicles as possible to transport all the passengers. If the passengers cannot be exactly distributed among the vehicles, the function returns an empty tuple.

- `list_passwd()`
This function generates and returns a list of all possible password combinations based on the following format: PetnameCalendardayStreetname. The combinations are generated using predefined options for each category.

- `prime(x)`
This function takes an integer x as input and determines whether it is a prime number. A prime number is a number greater than 1 that has no divisors other than 1 and itself.


- `xprime(x)`
This function takes an integer x as input and calculates the x-th prime number. It uses the prime() function to check if a number is prime while iterating through natural numbers until it finds the x-th prime.

- `interleave(x ,ys)`
The function takes two strings x (length 1), ys and returns a list of all possible ways to insert the character x into the string ys at different positions.

- `perms(xs)`
This function takes a string xs as input and returns a list of all possible permutations of the string. Each permutation is a rearrangement of the characters in xs.

## Tests
Tests are implemented in `test_functions`