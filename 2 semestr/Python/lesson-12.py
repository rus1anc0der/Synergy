class Transport:
    
    def __init__(self, name:str, max_speed:int, mileage:int) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def __str__(self) -> str:
        return f'{self.name} Скорость:{self.max_speed} Пробег: {self.mileage}'    
    
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
        
class Autobus(Transport):
    
    def __init__(self, name: str, max_speed: int, mileage: int) -> None:
        super().__init__(name, max_speed, mileage)
        
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


# autobus = Transport('Renaul Logan', 180, 12)
# print(autobus) #задание 1

reno = Autobus('Renaul Logan', 180, 12)
print(reno.seating_capacity())