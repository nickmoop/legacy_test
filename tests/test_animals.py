import pytest
from src.core.abc_animal import IAnimal
from src.animals import Dog, Cat, Tiger, Duck, FlyingFish, FishSimple

DOG = {
    "name": "Bobik",
    "say": "Hello, i'm Dog and my name is Bobik",
    "run": "My name is Bobik and i running",
    "swim": "My name is Bobik and i swimming",
    "fly": "My name is Bobik and i can't fly",
}
CAT = {
    "name": "Barsik",
    "say": "Hello, i'm Cat and my name is Barsik",
    "run": "My name is Barsik and i running",
    "swim": "My name is Barsik and i can't swim",
    "fly": "My name is Barsik and i can't fly"
}
TIGER = {
    "name": "Kisik",
    "say": "Hello, i'm Tiger and my name is Kisik",
    "run": "My name is Kisik and i running",
    "swim": "My name is Kisik and i swimming",
    "fly": "My name is Kisik and i can't fly"
}
FISH_SIMPLE = {
    "name": "Boltun",
    "say": "Hello, i'm FishSimple and my name is Boltun",
    "run": "My name is Boltun and i can't run",
    "swim": "My name is Boltun and i swimming",
    "fly": "My name is Boltun and i can't fly"
}
FISH_FLYING = {
    "name": "Gagarin",
    "say": "Hello, i'm FlyingFish and my name is Gagarin",
    "run": "My name is Gagarin and i can't run",
    "swim": "My name is Gagarin and i swimming",
    "fly": "My name is Gagarin and i flying"
}
DUCK = {
    "name": "Krya",
    "say": "Hello, i'm Duck and my name is Krya",
    "run": "My name is Krya and i can't run",
    "swim": "My name is Krya and i swimming",
    "fly": "My name is Krya and i flying"
}


def act(animal: IAnimal, action: str):
    animal_actions = {
        'say': animal.say,
        'run': animal.run,
        'swim': animal.swim,
        'fly': animal.fly
    }
    action_run = animal_actions.get(action)
    if action_run:
        action_run()


@pytest.mark.parametrize('action, expected_energy, animal, animal_name', [
    ('say', 100, DOG, DOG["name"]),
    ('run', 90, DOG, DOG["name"]),
    ('swim', 70, DOG, DOG["name"]),
    ('fly', 100, DOG, DOG["name"])
])
def test_dog_instance(capfd, action, expected_energy, animal, animal_name):
    animal_instance = Dog(name=animal_name)
    act(animal_instance, action)
    out, err = capfd.readouterr()
    assert animal_instance.energy == expected_energy
    assert out.replace("\n", "") == animal[action]


@pytest.mark.parametrize('action, expected_energy, animal, animal_name', [
    ('say', 100, CAT, CAT["name"]),
    ('run', 95, CAT, CAT["name"]),
    ('swim', 100, CAT, CAT["name"]),
    ('fly', 100, CAT, CAT["name"])
])
def test_cat_instance(capfd, action, expected_energy, animal, animal_name):
    animal_instance = Cat(name=animal_name)
    act(animal_instance, action)
    out, err = capfd.readouterr()
    assert animal_instance.energy == expected_energy
    assert out.replace("\n", "") == animal[action]


@pytest.mark.parametrize('action, expected_energy, animal, animal_name', [
    ('say', 200, TIGER, TIGER["name"]),
    ('run', 180, TIGER, TIGER["name"]),
    ('swim', 160, TIGER, TIGER["name"]),
    ('fly', 200, TIGER, TIGER["name"])
])
def test_tiger_instance(capfd, action, expected_energy, animal, animal_name):
    animal_instance = Tiger(name=animal_name)
    act(animal_instance, action)
    out, err = capfd.readouterr()
    assert animal_instance.energy == expected_energy
    assert out.replace("\n", "") == animal[action]


@pytest.mark.parametrize('action, expected_energy, animal, animal_name', [
    ('say', 100, DUCK, DUCK["name"]),
    ('run', 100, DUCK, DUCK["name"]),
    ('swim', 90, DUCK, DUCK["name"]),
    ('fly', 70, DUCK, DUCK["name"]),
])
def test_duck_instance(capfd, action, expected_energy, animal, animal_name):
    animal_instance = Duck(name=animal_name)
    act(animal_instance, action)
    out, err = capfd.readouterr()
    assert animal_instance.energy == expected_energy
    assert out.replace("\n", "") == animal[action]


@pytest.mark.parametrize('action, expected_energy, animal, animal_name', [
    ('say', 100, DUCK, DUCK["name"]),
    ('run', 100, DUCK, DUCK["name"]),
    ('swim', 90, DUCK, DUCK["name"]),
    ('fly', 70, DUCK, DUCK["name"]),
])
def test_duck_instance(capfd, action, expected_energy, animal, animal_name):
    animal_instance = Duck(name=animal_name)
    act(animal_instance, action)
    out, err = capfd.readouterr()
    assert animal_instance.energy == expected_energy
    assert out.replace("\n", "") == animal[action]


@pytest.mark.parametrize('action, expected_energy, animal, animal_name', [
    ('say', 100, FISH_SIMPLE, FISH_SIMPLE["name"]),
    ('run', 100, FISH_SIMPLE, FISH_SIMPLE["name"]),
    ('swim', 95, FISH_SIMPLE, FISH_SIMPLE["name"]),
    ('fly', 100, FISH_SIMPLE, FISH_SIMPLE["name"]),
])
def test_fish_simple_instance(capfd, action, expected_energy, animal, animal_name):
    animal_instance = FishSimple(name=animal_name)
    act(animal_instance, action)
    out, err = capfd.readouterr()
    assert animal_instance.energy == expected_energy
    assert out.replace("\n", "") == animal[action]


@pytest.mark.parametrize('action, expected_energy, animal, animal_name', [
    ('say', 100, FISH_FLYING, FISH_FLYING["name"]),
    ('run', 100, FISH_FLYING, FISH_FLYING["name"]),
    ('swim', 95, FISH_FLYING, FISH_FLYING["name"]),
    ('fly', 80, FISH_FLYING, FISH_FLYING["name"]),
])
def test_fish_flying_instance(capfd, action, expected_energy, animal, animal_name):
    animal_instance = FlyingFish(name=animal_name)
    act(animal_instance, action)
    out, err = capfd.readouterr()
    assert animal_instance.energy == expected_energy
    assert out.replace("\n", "") == animal[action]
