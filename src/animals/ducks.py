from core.abc_animal import IAnimal


class Duck(IAnimal):

    def run(self):
        print(f"My name is {self.name} and i can't run")

    def swim(self):
        print(f"My name is {self.name} and i swimming")
        self.energy = self.energy - 10

    def fly(self):
        print(f"My name is {self.name} and i flying")
        self.energy = self.energy - 30