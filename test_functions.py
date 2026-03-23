from utils import find_best_combination_of_vehicles, list_passwd, prime, xprime, interleave, perms

def test_calculate_vehicle_combination():
    assert find_best_combination_of_vehicles(40) == (0,2,2) 
    print("test_calculate_vehicle_combination erfolgreich ausgeführt")

def test_calculate_list_passwd():
    expected_result = ['Bella17Münzenhalde', 'Bella17Schillerstraße', 'Bella17Elsterweg', 'Bella17Johnsallee', 
     'Bella2Münzenhalde', 'Bella2Schillerstraße', 'Bella2Elsterweg', 'Bella2Johnsallee', 'Bella7Münzenhalde', 
     'Bella7Schillerstraße', 'Bella7Elsterweg', 'Bella7Johnsallee', 'Coco17Münzenhalde', 'Coco17Schillerstraße', 
     'Coco17Elsterweg', 'Coco17Johnsallee', 'Coco2Münzenhalde', 'Coco2Schillerstraße', 'Coco2Elsterweg', 
     'Coco2Johnsallee', 'Coco7Münzenhalde', 'Coco7Schillerstraße', 'Coco7Elsterweg', 'Coco7Johnsallee', 
     'Merlin17Münzenhalde', 'Merlin17Schillerstraße', 'Merlin17Elsterweg', 'Merlin17Johnsallee', 'Merlin2Münzenhalde', 
     'Merlin2Schillerstraße', 'Merlin2Elsterweg', 'Merlin2Johnsallee', 'Merlin7Münzenhalde', 'Merlin7Schillerstraße', 
     'Merlin7Elsterweg', 'Merlin7Johnsallee']
    assert list_passwd() == expected_result
    print("test_calculate_list_passwd erfolgreich ausgeführt")

def test_prime():
    assert prime(17) is True
    print("test_prime erfolgreich ausgeführt")

def test_xprime():
    assert xprime(5) == 11
    print("test_xprime erfolgreich ausgeführt")

def test_interleave():
    expected_result = ['are', 'rea', 'ear']
    assert interleave('e', 'ar') == expected_result
    print("test_interleave erfolgreich ausgeführt")

def test_perms():
    expected_result = ['earh', 'arhe', 'rhea', 'hear', 'hare', 'areh', 'reha', 'ehar', 'hera', 'erah', 'rahe', 'aher', 'hear', 'earh', 'arhe', 'rhea']
    assert perms('hear') == expected_result
    print("test_perms erfolgreich ausgeführt")

test_calculate_vehicle_combination()
test_calculate_list_passwd()
test_prime()
test_xprime()
test_interleave()
test_perms()