from typing import TypeVar
#Python ima modul za tip string koji moramo importovati kako bismo mogli da definisamo tip podatka da bude string
import string


T = TypeVar('T', bound='Animal')

class Animal:
    def set_name(self: T,name: string) -> T:
        self.name = name
        return self

class Cat(Animal):
    def set_sound(self, s: string) -> 'Cat':
        self.sound = s
        return self

class Dog(Animal):
    def set_sound(self, s: string) -> 'Dog':
        self.sound = s
        return self

cica = Cat().set_sound('Mjau').set_name('Cica')
print(cica.name)
print(cica.sound)
zucko = Dog().set_sound('Av').set_name('Zucko')
print(zucko.name)
print(zucko.sound)

