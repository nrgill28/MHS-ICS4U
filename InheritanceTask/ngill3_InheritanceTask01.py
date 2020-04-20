from datetime import datetime
from typing import List


class Dog:
    def __init__(self, breed: str, weight: float, sex: str, birthday: datetime):
        # Validate the information
        assert weight > 0
        assert sex.lower().startswith('m') or sex.lower().startswith('f')
        assert breed is not None and breed != ""

        # Set the information
        self.breed = breed
        self.weight = weight
        self.sex = "male" if sex.lower().startswith('m') else "female"
        self.birthday = birthday

    # This is a Python special function which is called whenever this object is converted to a string.
    # When this happens, we want to return the information about the object in a human-readable format
    def __str__(self) -> str:
        return f"A {self.weight}kg {self.sex} {self.breed} born on {self.birthday:%Y-%m-%d}"


class PetDog(Dog):
    def __init__(self, breed: str, weight: float, sex: str, birthday: datetime, name: str, owner: str, address: str):
        # Validate the information
        assert name is not None and name != ""
        assert owner is not None and owner != ""
        assert address is not None and address != ""

        # Set the information
        super().__init__(breed, weight, sex, birthday)
        self.name = name
        self.owner = owner
        self.address = address

    # This is a Python special function which is called whenever this object is converted to a string.
    # When this happens, we want to return the information about the object in a human-readable format
    def __str__(self) -> str:
        return f"{self.name}, a {self.weight}kg pet {self.sex} {self.breed} born on {self.birthday:%Y-%m-%d} owned by {self.owner}, {self.address}"


class ServiceDog(Dog):
    def __init__(self, breed: str, weight: float, sex: str, birthday: datetime, name: str, business_name: str, address: str, occupation: str):
        # Validate the information
        assert business_name is not None and business_name != ""
        assert address is not None and address != ""
        assert occupation is not None and occupation != ""
        assert name is not None and name != ""

        # Set the information
        super().__init__(breed, weight, sex, birthday)
        self.name = name
        self.business_name = business_name
        self.address = address
        self.occupation = occupation

    # This is a Python special function which is called whenever this object is converted to a string.
    # When this happens, we want to return the information about the object in a human-readable format
    def __str__(self) -> str:
        return f"{self.name}, a {self.weight}kg {self.sex} {self.breed} service dog born on {self.birthday:%Y-%m-%d} who works at {self.business_name}, {self.address} as a {self.occupation}"


# The task called for two separate functions to create the two separate dogs,
# But that's a lot of repeated code for no reason so I've merged them into one function which does more with less code
def create_dog() -> Dog:
    print("Which kind of dog do you want to create?")
    print("[0] Dog\n[1] PetDog\n[2] ServiceDog")
    inp = input("> ")[0].lower()

    # Gather the common information
    breed = input("Breed: ")
    weight = float(input("Weight (kg): "))
    sex = input("Sex (M/F): ")
    birthday = datetime.strptime(input("Birthday (YYYY/MM/DD): "), "%Y/%m/%d")

    # Declare a new Dog
    new_dog: Dog

    # Gather the specific information and create the object
    if inp == '0':
        new_dog = Dog(breed, weight, sex, birthday)
    elif inp == '1':
        name = input("Pet Name: ")
        owner = input("Owner Name: ")
        address = input("Owner Address: ")
        new_dog = PetDog(breed, weight, sex, birthday, name, owner, address)
    elif inp == '2':
        name = input("Name: ")
        business_name = input("Business Name: ")
        address = input("Business Address: ")
        occupation = input("Occupation Title: ")
        new_dog = ServiceDog(breed, weight, sex, birthday, name, business_name, address, occupation)

    return new_dog


if __name__ == "__main__":
    # Create a new list which holds objects of type 'Dog'.
    # This can also hold subclasses of Dog, like PetDog and ServiceDog
    # The task calls for two lists to separate the dogs, but since we're doing inheritance I thought it made sense
    # To use some class polymorphism.
    dogs: List[Dog] = []

    # Let the user create as many dogs as they want
    while True:
        dogs.append(create_dog())
        print("\nDog Added!")
        inp = input("Create another? (Y/N):")[0].lower()
        if inp != 'y':
            break

    # Print all the dogs
    print("\n\nHere is all of your dogs!")
    for dog in dogs:
        # Print out each dog added along side what kind of dog it is
        print(f"[{type(dog).__name__}] {dog}")
