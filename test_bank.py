import bank

def test_value_starts_with_hello():
    assert bank.value("Здравствуйте") == 0

def test_value_starts_with_z():
    assert bank.value("Здрасте") == 20

def test_value_other_cases():
    assert bank.value("Добрый день") == 100
    assert bank.value("Привет") == 100