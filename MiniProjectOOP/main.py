class Person:
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 20  # устанавливаем возраст

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


class Employee(Person):
    def work(self):
        print(f"{self.name} works")


tom = Employee("Tom")
tom.work()
tom.display_info()
