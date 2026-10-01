import random
import math
import base64


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def random_prime():
    while True:
        random_number = random.randint(10000000, 100000000)

        if is_prime(random_number):
            return random_number


def key_to_base64(key_part, modulus):
    key_text = str(key_part) + str(modulus)

    key_bytes = key_text.encode()

    encoded_key = base64.b64encode(key_bytes).decode()

    return encoded_key


def generate_keys():

    first_prime = random_prime()
    second_prime = random_prime()

    while first_prime == second_prime:
        second_prime = random_prime()

    modulus = first_prime * second_prime

    euler_function = ((first_prime - 1) * (second_prime - 1))

    while True:
        public_exponent = random.randrange(3, euler_function, 2)

        if math.gcd(public_exponent, euler_function) == 1:
            break

    private_exponent = pow(public_exponent, -1, euler_function)

    public_key = key_to_base64(public_exponent, modulus)

    private_key = key_to_base64(private_exponent, modulus)

    return public_key, private_key


while True:

    print("\n--- Генератор RSA ключей ---")
    print("1 - Создать новую пару ключей")
    print("0 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":

        public_key, private_key = generate_keys()

        print("\nПубличный ключ:")
        print(public_key)

        print("\nПриватный ключ:")
        print(private_key)

    elif choice == "0":
        print("Программа завершена")
        break

    else:
        print("Такой команды нет")