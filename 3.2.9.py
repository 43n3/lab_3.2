passports = {
    1234567: True,
    2345678: False,
    3456789: True,
    9876543: False,
    1111111: True,
}

def check_passport(passport_number):
    if passport_number not in passports:
        return "Вылет запрещён (паспорт не найден)"
    elif passports[passport_number]:
        return "Вылет разрешён"
    else:
        return "Вылет запрещён"

try:
    number = int(input("Введите номер паспорта: "))
    print(check_passport(number))
except ValueError:
    print("Ошибка: введите корректный номер паспорта (7 цифр)")