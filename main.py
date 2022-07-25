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
#print(next(I)) # Исключение StopIteration можно перехватить с помощью try
###
print("-" * 40)
N = Squares(1, 5) # Создать итерируемый объект с состоянием
aa = [n for n in N] # Израсходует элементы: __iter__ возвращает self
print(aa)
print([n for n in N]) # Теперь он пуст
bb = [n for n in Squares(1, 6)] # Создать новый итерируемый объект
print(bb)
vv = list(Squares(1, 7)) # Новый объект для каждого нового вызова __iter__
print(vv)
print(36 in Squares(1, 10)) # Другие итерационные контексты
a, b, c = Squares(1, 3) # Для каждого объекта вызывается __iter__ и затем __next__
print(a, b, c)
print(":".join(map(str, Squares(1, 5))))

ll = Squares(1, 5)
print(tuple(ll))
print(tuple(ll)) # Второй вызов tuple израсходует элементы в итераторе
gg = list(Squares(1, 5))
print(tuple(gg))
print(tuple(gg))
print(tuple(gg))