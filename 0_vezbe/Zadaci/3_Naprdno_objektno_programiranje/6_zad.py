"""Napraviti generičku klasu Animal  sa metodom set_name u kojoj se postavlja vrednost za polje name.  
Definisati klase Cat I Dog koje nasleđuju klasu Animal I imaju definisanu metdu set_sound u kojoj se čuva vrednost za polje sound. 
Instancirati klase I pozvati metode nad objektima."""

from typing import TypeVar
import string

T = TypeVar("T", bound = "Animal")

class Animal:
    def set_name(self: T, name: string) -> T:
        self.name = name
        return self
    
class Cat(Animal):
    def set_sound(self, sound: string) -> "Cat":
        self.sound = sound
        return self
    
class Dog(Animal):
    def set_sound(self, sound: string) -> "Dog":
        self.sound = sound
        return self
    

snesko = Cat().set_sound("Mjau,mjau...").set_name("Snesko")
print(snesko.name)
print(snesko.sound)

gari = Dog().set_sound("Av.av...").set_name("Gari")
print(gari.name)
print(gari.sound)
