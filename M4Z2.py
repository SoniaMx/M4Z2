#to jest pierwsza bardziej przystępna dla mnie wersja
operator = input("wybierz jedno z działań (+ - * /):  ")
num1 = float(input("wpisz pierwszą liczbę: "))
num2 = float(input("wpisz drugą liczbę: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator== "-":
    result = num1 - num2
    print(round(result, 3))
elif operator== "*":
    result = num1 * num2
    print(round(result, 3))
elif operator== "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} nie istnieje")

#wersja z import.logging nie jest to na razie dla mnie zbyt zrozumiałe, pomogłam sobie chatemgpt




