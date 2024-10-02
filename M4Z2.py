#to jest pierwsza bardziej przystępna dla mnie wersja
operator = input("wybierz jedno z działań (+ - * /):  ")
num1 = float(input("wpisz pierwszą liczbę: "))
num2 = float(input("wpisz drugą liczbę: "))

if operator == "+":
    result = num1 + num2
    print("wynik: " ,round(result, 3))
elif operator == "-":
    result = num1 - num2
    print("wynik: " ,round(result, 3))
elif operator == "*":
    result = num1 * num2
    print("wynik: " ,round(result, 3))
elif operator == "/":
    result = num1 / num2
    print("wynik: " ,round(result, 3))
else:
    print(f"{operator} nie istnieje")

#wersja z import logging, cały proces bardzo długi i póki co dla mnie nie do powtórzenia bez podglądania, pomogłam sobie chatemgpt

import logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def suma(x, y):
    result = x + y
    logging.info(f"suma {x} + {y} = {result}")
    return result

def różnica(x, y):
    result = x - y
    logging.info(f"różnica {x} - {y} = {result}")
    return result

def mnożenie(x, y):
    result = x * y
    logging.info(f"mnożenie {x} * {y} = {result}")
    return result

def dzielenie(x, y):
    if y == 0:
        logging.error("Dzielenie przez 0 nie jest możliwe")
        return "Dzielenie przez 0 niemożliwe"
    result = x / y
    logging.info(f"dzielenie {x} / {y} = {result}")
    return result


def kalkulator():
    print("Kalkulator")
    print("1. Suma")
    print("2. Różnica")
    print("3. Mnożenie")
    print("4. Dzielenie")

    choice = input("wybierz jedną opcję (1/2/3/4): ")

    num1 = float(input("wpisz pierwszą liczbę: "))
    num2 = float(input("wpisz drugą liczbę: "))

    if choice == '1':
        print(f"wynik: {suma(num1, num2)}")
    elif choice == '2':
        print(f"wynik: {różnica(num1, num2)}")
    elif choice == '3':
        print(f"wynik: {mnożenie(num1, num2)}")
    elif choice == '4':
        print(f"wynik: {dzielenie(num1, num2)}")
    else:
        logging.warning("nie ma takiej opcji")

kalkulator()




