"""utils"""

###############################################################################################
#The function takes a number of passengers that need to be transported. It then distributes the passengers among the cars.
#There are minibusses that take 13 people, minivans that take 7 people and normal cars that take 5 people.
#The passengers shall be distributed efficiently, the function should find the best combination of people. 
#The goal is to have as few cars as possible. If the passengers can't be distributed exactly, the return ist empty.
#To return the best combination and tolerate empty seats change the code to psum >= passengers...

#example: a group of 40 people can be distributed on 8 normal cars (which makes 8 vehicles) OR on 2 minibusses, 1 minivan and 1 normal car ("pkw") (which makes 4 vehicles). 
#(car, minivan, minibus)


def find_best_combination_of_vehicles(passengers):
    "Kombinationen"
    best_combination = ()
    least_counter = passengers
    for minibus in range(passengers // 13, -1, -1):
        for minivan in range((passengers - minibus*13) // 7, -1, -1):
            pkw = (passengers - minibus*13 - minivan*7) // 5
            psum = minibus*13 + minivan*7 + pkw*5
            if psum == passengers and pkw >= 0 and minivan >= 0 and minibus >= 0:
                vehicle_sum = pkw + minivan + minibus
                if vehicle_sum < least_counter:
                    best_combination = (pkw, minivan, minibus)
                    least_counter = vehicle_sum                
    return best_combination

print("(cars, minivans, minibusses):", find_best_combination_of_vehicles(26))



###############################################################################################
#Die Funktion gibt eine Liste aller Passwort-Kombinationen nach dem Schema HaustiernameKalendertageStraßennamen (Bsp.: Bella17Schillerstraße) zurück.

haustiernamen = ('Bella', 'Coco', 'Merlin')
kalendertage = ('17', '2', '7')
strassennamen = ('Münzenhalde', 'Schillerstraße', 'Elsterweg', 'Johnsallee')
def list_passwd():
    "Passwort-Liste"
    liste = []
    for i in haustiernamen:
        for j in kalendertage:
            for k in strassennamen:
                liste.append(i+j+k)
    return liste

print(list_passwd())


###############################################################################################
#Die Funktion bekommt eine Zahl x als Input und bestimmt, ob es eine Primzahl ist.
#Bsp.: prime(5) -> True

def prime(x):
    #Primzahlen
    i = 2
    j = 3
    if x == 0 or x == 1:
        return False 
    
    while i < x:
        if x%i == 0:
            return False
        i +=1
        
    return True


###############################################################################################
#Die Funktion bekommt eine Zahl x als Input und berechnet die x-te Primzahl.
#Bsp.: xteprime(5) -> 11

def xprime(x):
    "Primzahlen"
    a = 0
    i = 0
    while a < x: 
        i+=1 
        if prime(i) is True :
            a += 1
    return(i)

print(xprime(5))


###############################################################################################
#Sei x ein String der Länge 1 und ys ein String beliebiger Länge. Dann gibt interleave(x, ys) eine Liste zurück, die alle möglichen Arten enthält, 
#das Element x in den String ys einzufügen. Die Funktion gibt die Liste zurück.
#Bsp.: interleave("e", "ar") -> ['are', 'rea', 'ear']

def interleave(x, ys):
    "Permutation"
    list = []
    for i in range(len(ys)+1):
        word = ys[i:] + x + ys[:i]
        list.append(word)
    return list

print(interleave("e", "ar"))


###############################################################################################
#Die Funktion gibt alle Permutationen vom string xs als Liste von Strings zurück.
# -> Jede mögliche Buchstabenkombination eines Wortes
#Bsp.: perms("hear") -> ['earh', 'arhe', 'rhea', 'hear', 'hare', 'areh', 'reha', 'ehar', 'hera', 'erah', 'rahe', 'aher', 'hear', 'earh', 'arhe', 'rhea']

def perms(xs):
    "Permutation"
    list = []
    for j in range(len(xs)):
        word = interleave(xs[j], xs[:j]+xs[j+1:])
        
        if word not in list:
            list.extend(word)
    return list

print(perms("hear"))
