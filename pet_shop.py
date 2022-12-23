from Pets import*
adoption_record = []

class Petshop:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def add_new_pet(self):
        print("####### ADD NEW PET #######")
        selection = int(input("Choose a pet to add\n(1) Dog (2) Cat (3) Fish\nEnter selection: "))
        name = input("Enter pet name: ")
        breed = input("Enter pet's breed: ")
        price = int(input("Enter price: "))
        if selection == 1:
            pet = Dog(name, "dog", price, breed, True)
            return pet
        elif selection == 2:
            pet = Cat(name, "cat", price, breed, True)
            return pet
        else:
            pet = Fish(name, "fish", price, breed, True)
            return pet

    def adopt(self, pets):
        print("############ ADOPT A PET ###########")
        petname = input("Enter name of pet to be adopted: ")
        present = False
        n = len(pets)
        for i in range(n):
            if pets[i].name == petname:
                adoption_record.append(pets[i])
                pets.pop(i)
                present = True
        if present is False:
            print("Pet not found!")

    def view_pets(self, pets):
        print("################# Pets #################")
        n = len(pets)
        for i in range(n):
            print("Pet " + str(i + 1) + "\n----------------")
            print("Name: " + str(pets[i].name))
            print("Specie: " + str(pets[i].species))
            print("Breed: " + str(pets[i].breed))
            print("Price: " + str(pets[i].price))
            print("\n")

    def record(self):
        print("############ Adoption Records ###########")
        n = len(adoption_record)
        for i in range(n):
            print("Pet " + str(i+1) + "\n----------------")
            print("Name: " + str(adoption_record[i].name))
            print("Specie: " + str(adoption_record[i].species))
            print("Breed: " + str(adoption_record[i].breed))
            print("Price: " + str(adoption_record[i].price))
            print("\n")
