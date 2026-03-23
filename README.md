# Lecture Spring 2026

Copyright 2026 Mia Greta Niehoff

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)

##License
This project is released under the Apache License 2.0.

##Functions
The find_best_combination_of_vehicles(passengers) function:
The function takes a number of passengers that need to be transported. It then distributes the passengers among the cars.
There are minibusses that take 13 people, minivans that take 7 people and normal cars that take 5 people.
The passengers shall be distributed efficiently, the function should find the best combination of people. 
The goal is to have as few cars as possible. If the passengers can't be distributed exactly, the return ist empty.
To return the best combination and tolerate empty seats change the code to psum >= passengers...
The return tuple is (car, minivan, minibus).
example: a group of 40 people can be distributed on 8 normal cars (which makes 8 vehicles) OR on 2 minibusses, 2 minivans and 0 normal cars ("pkw") (which makes 4 vehicles). 

The list_passwd() function:
Die Funktion gibt eine Liste aller Passwort-Kombinationen nach dem Schema HaustiernameKalendertageStraßennamen (Bsp.: Bella17Schillerstraße) zurück. 
Optionen für den Haustiernamen, die Kalendertage und den Straßennamen sind in der Funktion bereits vorgegeben.

The prime(x) function:
Die Funktion bekommt eine Zahl x als Input und bestimmt, ob es eine Primzahl ist.
Bsp.: prime(5) -> True

Die xprime(x) fucntion:
Die Funktion bekommt eine Zahl x als Input und berechnet die x-te Primzahl. Die xprime()-Funktion nutzt die prime()-Funktion.
Bsp.: xteprime(5) -> 11

The interleave(x ,ys) function:
Sei x ein String der Länge 1 und ys ein String beliebiger Länge. Dann gibt interleave(x, ys) eine Liste zurück, die alle möglichen Arten enthält, 
das Element x in den String ys einzufügen. Die Funktion gibt die Liste zurück.
Bsp.: interleave("e", "ar") -> ['are', 'rea', 'ear']

The perms(xs) function.
Die Funktion gibt alle Permutationen vom string xs als Liste von Strings zurück.
-> Jede mögliche Buchstabenkombination eines Wortes
Bsp.: perms("hear") -> ['earh', 'arhe', 'rhea', 'hear', 'hare', 'areh', 'reha', 'ehar', 'hera', 'erah', 'rahe', 'aher', 'hear', 'earh', 'arhe', 'rhea']
