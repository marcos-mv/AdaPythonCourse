class Horario:
    def __init__(self, hour, minute, second) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second
        pass
    
    def __repr__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    #
    def __str__(self) -> str:
        
        return f"O horário é: {self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    #soma dois horários
    
    def __add__(self, other):
        
        somaSegundos = self.second + other.second
        somaMinutos = self.minute + other.minute
        somaHora = self.hour + other.hour
        
        if somaSegundos >=60:
            somaMinutos += 1
            somaSegundos -= 60
        
        if somaMinutos >=60:
            somaHora += 1
            somaMinutos -= 60
            
        if somaHora >= 24:
            somaHora -= 24
            
        return Horario(somaHora,somaMinutos,somaSegundos)
    
    # Verifica se uma hora é maior que a outra
    def __gt__(self,other):
        
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour and self.minute > other.minute:
            return True
        elif self.hour == other.hour and self.minute == other.minute and self.second > other.second:
            return True
        else:
            return False
        
        
        
    
agora  = Horario(18,5,32)

h1 = Horario(10,11,55)
h2 = Horario(9,33,22)

maior = h1 > h2
menor = h1 < h2

print(maior)
print(menor)

h3 = h1+h2

print(h1, h2)

print(h3)

print(agora)
print(type(agora))

print(agora.hour)
print(agora.minute)
print(agora.second)

print(vars(agora))

print(f"{agora.hour}:{agora.minute}:{agora.second}")


print((5).__add__(9)) #Método magico __add__

print("marcos".__mul__(3))



class A:
    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y
        
    def __eq__(self, outro) -> bool:
        return self.x == outro.x
    
class B:
    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y
        
    def __eq__(self, outro) -> bool:
        return self.y == outro.y
    
a = A(x=1,y=2)
b = B(x=1,y=3)

print(a==b, b==a)
        
        
class Tolerancia:
    def _init_(self, x, tol_minima=3, tol_maxima=6):
        self.x = x
        self.tol_minima = tol_minima
        self.tol_maxima = tol_maxima
    def _eq_(self, outro):
        return abs(self.x - outro.x) <= self.tol_minima
    def _ne_(self, outro):
        return abs(self.x - outro.x) >= self.tol_maxima
a = Tolerancia(x=10)
b = Tolerancia(x=15)
print(a==b, a!=b)