class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = color

    def get_model(self):
        return print("Модель:", self.__model)

    def get_horsepower(self):
        return print("Мощность двигателя:", self.__engine_power)

    def get_color(self):
        return print("Цвет:", self.__color)

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
            print(self.__color)
        else:
            print("Нельзя сменить цвет на", new_color)

    def print_info(self):
        return self.get_model(), self.get_horsepower(), self.get_color(), print("Владелец:", self.owner)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
