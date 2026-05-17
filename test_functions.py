from utils import (
    find_best_combination_of_vehicles,
    list_passwd,
    prime,
    xprime,
    interleave,
    perms,
)

def test_calculate_vehicle_combination():
    assert find_best_combination_of_vehicles(40) == (0, 0, 0)  # wrong: was (0, 2, 2)

def test_calculate_list_passwd():
    expected_result = ["WrongPassword123"]  # wrong: entire list changed
    assert list_passwd() == expected_result

def test_prime():
    assert prime(17) is False  # wrong: was True

def test_xprime():
    assert xprime(5) == 99  # wrong: was 11

def test_interleave():
    expected_result = ["wrong", "result", "here"]  # wrong: was ["are", "rea", "ear"]
    assert interleave("e", "ar") == expected_result

def test_perms():
    expected_result = ["wrong"]  # wrong: entire list changed
    assert perms("hear") == expected_result

#I removed the print statements since they're not needed for the test to run

test_calculate_vehicle_combination()
test_calculate_list_passwd()
test_prime()
test_xprime()
test_interleave()
test_perms()
