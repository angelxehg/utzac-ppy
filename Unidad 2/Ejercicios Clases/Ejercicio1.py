class Person():

    def __init__(self, first_name, last_name, age, address, phone):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__first_name

    def get_full_name(self):
        return self.__first_name + " " + self.__last_name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


name = input("Ingrese nombre: ")
last = input("Ingrese apellido: ")
age = int(input("Ingrese su edad: "))
addr = input("Ingrese su dirección: ")
phone = input("Ingrese su teléfono: ")

person = Person(name, last, age, addr, phone)

print("Datos de", person.get_name(), ":")
print("Nombre completo:", person.get_full_name())
print("Edad:", person.get_age())
print("Dirección:", person.get_address())
