from pet_shop import*

if __name__ == '__main__':
    print("####### PETSHOP #######")
    pets = []
    pet_shop = Petshop("CJ's Petshop", "Upper Tawason, Mandaue City, Cebu")
    print("Welcome to " + str(pet_shop.name) + " !")
    print("Location: " + str(pet_shop.location))
    selection = 0
    while selection != 5:
        print("\nPet Shop Menu")
        print("(1) Add a new pet")
        print("(2) Adopt a pet")
        print("(3) View Pets")
        print("(4) Adoption records\n (5) Exit\n")
        selection = int(input("Enter selection: "))
        if selection == 1:
            end = 1
            while end != 2:
                pets.append(pet_shop.add_new_pet())
                print("(1) Add another\n(2) Done")
                end = int(input("Enter selection: "))
        elif selection == 2:
            pet_shop.adopt(pets)
        elif selection == 3:
            pet_shop.view_pets(pets)
        elif selection == 4:
            pet_shop.record()
        else:
            print("Exiting program...")

#Testing comment for git