from core.abc_animal import IAnimal


class Dog(IAnimal):

    def run(self):
        print(f"My name is {self.name} and i running")
        self.energy = self.energy - 10

    def swim(self):
        print(f"My name is {self.name} and i swimming")
        self.energy = self.energy - 30

    def fly(self):
        print(f"My name is {self.name} and i can't fly")


