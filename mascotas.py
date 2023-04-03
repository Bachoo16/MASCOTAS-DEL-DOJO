class Pet:

    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

 
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self


    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)



class Ninja:
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):

        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"alimentar {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! necesitas mas comida!")
        return self

    def bathe(self):
        self.pet.noise()

my_treats = ['Snausage','Bacon',"Trash Bag"]
my_pet_food = ['Pizzas','hamburguesas']

nibbles = Pet("Sr. Nibless","Horse",['nibbles on things','is invisible'],"Hey Hey")

teo = Ninja("Teo","Dion",my_treats,my_pet_food, nibbles)

teo.feed();
teo.feed();
teo.feed();
