class UserAccount:
    def __init__(self, username, email, password):
        """Инициализация атрибутов аккаунта пользователя."""
        self.username = username
        self.email = email
        self.__password = password 

    def set_password(self, new_password):
        """Изменяет пароль аккаунта."""
        self.__password = new_password

    def check_password(self, password):
        """Проверяет, соответствует ли введённый пароль текущему паролю аккаунта."""
        return self.__password == password

user_account = UserAccount("user123", "user@example.com", "securePassword")
print(user_account.check_password("wrongPassword"))  
user_account.set_password("newSecurePassword")
print(user_account.check_password("newSecurePassword"))  

class Vehicle:
    def __init__(self, make, model):
        """Инициализация атрибутов транспортного средства."""
        self.make = make
        self.model = model

    def get_info(self):
        """Возвращает информацию о транспортном средстве."""
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        """Инициализация атрибутов автомобиля и вызов конструктора родительского класса."""
        super().__init__(make, model) 
        self.fuel_type = fuel_type

    def get_info(self):
        """Переопределяет метод для включения информации о типе топлива."""
        return f"{super().get_info()}, Тип топлива: {self.fuel_type}"

vehicle = Vehicle("Toyota", "Camry")
print(vehicle.get_info())

car = Car("Honda", "Civic", "Бензин")
print(car.get_info())
