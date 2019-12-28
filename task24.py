text = input("Введите слово: ").lower()
if text == text[::-1]:
    print("True")
else:
    print("False")