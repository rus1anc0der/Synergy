class Kassa:
    
    def __init__(self, cash) -> None:
        self.cash = cash
            
    def top_up(self, x) -> None:
        self.cash += x
    
    def count_1000(self) -> int:
        return self.cash//1000
    
    def take_away(self, x):
        if self.cash - x >= 0:
            self.cash -= x
            return self.cash
        return "В кассе недостаточно денег"
    
    def __str__(self) -> str:
        return f'Остаток = {self.cash}'
    
    
class Turtle:
    
    def __init__(self, x:int, y:int, s:int) -> None:
        self.x = x
        self.y = y
        self.s = s
        
    def go_up(self) -> None:
        self.y += self.s
    
    def go_down(self) -> None:
        self.y -= self.s
        
    def go_left(self) -> None:
        self.x -= self.s
        
    def go_right(self) -> None:
        self.x += self.s
        
    def evolve(self) -> None:
        self.s += 1
        
    def degrade(self) -> None:
        if self.s - 1 > 0:
            self.s -= 1  
        else:
            print('Ошибка, количество ходов должно быть больше 0')
        
    def count_moves(self, x2, y2) -> None:
        ...


        
kassa = Kassa(10_000) # заводим кассу с 10 тыс рублями
print(kassa.count_1000()) # смотрим сколько тысяч
kassa.top_up(500) # прибавляем 500 руб
kassa.take_away(1000) # отнимаем 1000 руб
print(kassa)

