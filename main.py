class Squares:
    def __init__(self, start, stop): # Сохранить состояние при создании
        self.value = start - 1
        self.stop = stop
    def __iter__(self): # Получить объект итератора при вызове iter
        return self
    def __next__(self): # Возвратить квадрат на каждой итерации
        if self.value == self.stop: # Также вызывается встроенной функцией next
            raise StopIteration
        else:
            self.value += 1
            return self.value ** 2


for i in Squares(1, 7): # for вызывает встроенную функцию iter, которая вызвает __iter__
    print(i) # Каждая итерация вызывает __next__

print("-" * 40)

X = Squares(1, 3) # Итерация вручную(то, что делают циклы)
I = iter(X) # iter() вызывает __iter__
print(next(I)) # next() вызывает __next__
print(next(I))
print(next(I))
print(next(I)) # Исключение StopIteration можно перехватить с помощью try