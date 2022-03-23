from core.abc_animal import IAnimal


class Cat(IAnimal):

    def run(self):
        self.energy = self.energy - 5
        print(f"My name is {self.name} and i running")

    def swim(self):
        print(f"My name is {self.name} and i can't swim")

    def fly(self):
        print(f"My name is {self.name} and i can't fly")


class Tiger(Cat):
    def __init__(self, name, energy=200):
        super(Tiger, self).__init__(name=name, energy=energy)

    def run(self):
        print(f"My name is {self.name} and i running")
        self.energy = self.energy - 20

    def swim(self):
        print(f"My name is {self.name} and i swimming")
        self.energy = self.energy - 40
