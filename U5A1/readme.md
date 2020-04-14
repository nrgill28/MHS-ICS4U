# ICS4U CLASSES ASSIGNMENT 1

Complete the following project using only ONE FILE.
Each activity should be contained in a function that is called from a main menu.
The function should share the same name as the exercise name (ie. Activity 1 should use function PetClass()
Save your file as YourName_Classes.py

## Pet Class
Write a class named Pet, which should have the following data attributes:
 - __name (for the name of a pet)
 - __animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’,
and ‘Bird’)
 - __age (for the pet’s age)

The Pet class should have an \_\_init\_\_ method that creates these attributes. It should also have the following methods:
 - set_name: This method assigns a value to the __name field.
 - set_animal_type: This method assigns a value to the __animal_type field.
 - set_age: This method assigns a value to the __age field.
 - get_name: This method returns the value of the __name field.
 - get_animal_type: This method returns the value of the __animal_type field.
 - get_age: This method returns the value of the __age field.

Once you have written the class, write a program that creates an object of the class and
prompts the user to enter the name, type, and age of his or her pet. This data should be stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name,
type, and age and display this data on the screen.

## Car Class
Write a class named Car that has the following data attributes:
 - __year_model (for the car’s year model)
 - __make (for the make of the car)
 - __speed (for the car’s current speed)

The Car class should have an \_\_init\_\_ method that accepts the car’s year model and make as arguments. These values should be assigned to the object’s __year_model and __make data attributes. It should also assign 0 to the __speed data attribute.  
The class should also have the following methods:
 - accelerate: The accelerate method should add 5 to the speed data attribute each time it is called.
 - brake: The brake method should subtract 5 from the speed data attribute each time it is called.
 - get_speed: The get_speed method should return the current speed. 
 
Next, design a program that creates a Car object and then calls the accelerate method
five times. After each call to the accelerate method, get the current speed of the car and
display it. Then call the brake method five times. After each call to the brake method, get
the current speed of the car and display it.


## Retail Item Class
Write a class named RetailItem that holds data about an item in a retail store. The class
should store the following data in attributes: item description, units in inventory, and price.

Once you have written the class, write a program that creates three RetailItem objects
and stores the following data in them:

| Item Number | Description     | Units in Inventory | Price |
| ----------- | --------------- | ------------------ | ----- |
| 1           | Jacket          | 12                 | 59.95 |
| 2           | Designer Jeans  | 40                 | 34.95 |
| 3           | Shirt           | 20                 | 24.95 |
