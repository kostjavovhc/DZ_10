from collections import UserDict


class PhoneValueError(Exception):
    ...

class NoNameError(Exception):
    ...

class NoPhoneError(Exception):
    ...

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    ...

class Phone(Field):
    def __init__(self, value:str):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Invalid Phone. Phone must have 10 numbers")
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone:Phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == phone:
                self.phones[i] = Phone(new_phone)
                return None
        raise ValueError("This phone phone does not exist")
        
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            else:
                continue

    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, contact:Record):
        name_value = contact.name.value
        if name_value not in self.data:
            self.data[name_value] = [contact]
        else:
            self.data[name_value].append(contact)

    def find(self, name:str):
        records = self.data.get(name)
        if records:
            return records[0]
        else:
            return None
        

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            return ValueError(f"{name} is not exist")


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

if __name__ == '__main__':
    main()
