# python L2_Challenge4_Task2.py - Debugging


pets = [
    { "name": "Fluffy", "type": "dog" },
    { "name": "Parsley", "type": "dog" },
    { "name": "Ginger", "type": "cat" },
    { "name": "Biscuit", "type": "cat" },
    { "name": "Poppet", "type": "cow" }
]



def say_hello_to_pets(pets):
    for pet in pets:
        for key, value in pet.items():
            if pet["type"] == "dog":
                hello_message = "Woof"
                pet_name = pet["name"]
            elif pet["type"] == "cat":
                hello_message = "Meow"
                pet_name = pet["name"]
            else:
                raise Exception("Sorry, only cats and dogs")
        print(f"{hello_message}, {pet_name}!")

say_hello_to_pets(pets)




# Errors: L4 change list name "animals" --> "pets"; L14 is it needed? ;; removed ":"
# L17 and L20[pet.name --> pet[name]; L14 ";" to ":"; L18 "if" --> "elif";
# L21 "return instead of print?" L21 ";" not needed? L23 [?]
