class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return phone_number.isdigit() and len(phone_number) == 10

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            print(f"Error: номер {phone_number} не подходит")

class Library:
    def __init__(self, city, books=None):
        self.city = city
        self.books = books if books is not None else []

    def __str__(self):
        return f"<Library object, city: {self.city}, books: {len(self.books)}>"

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        print(f"Ищем книгу: {item}")
        return item in self.books

    def __bool__(self):
        return len(self.books) > 5

ContactList.add_contact("Владимир Путин", "0700100200")
ContactList.add_contact("Дональд Трамп", "0500123456")
ContactList.add_contact("Jeffrey Epstein", "5551234")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone)

lib = Library("Бишкек", books=["Война и мир", "1984", "Мастер и Маргарита"])
print(lib)
print(len(lib))
print("1984" in lib)
print("Гарри Поттер" in lib)

if lib:
    print("Библиотека большая (более 5 книг)")
else:
    print("Библиотека маленькая")