class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def modify_ingredient(self, index, new_ingredient):
        self.ingredients[index] = new_ingredient

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def modify_instruction(self, index, new_instruction):
        self.instructions[index] = new_instruction

    def print_recipe(self):
        print(f"Recipe for {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(ingredient)
        print("Instructions:")
        for i, instruction in enumerate(self.instructions):
            print(f"{i + 1}. {instruction}")


# Create a new recipe
my_recipe = Recipe("Spaghetti Bolognese", ["pasta", "ground beef", "tomato sauce"], ["Cook pasta according to package instructions.", "Brown ground beef in a pan.", "Add tomato sauce to the pan and simmer for 10 minutes.", "Serve sauce over pasta."])

# Modify an ingredient
my_recipe.modify_ingredient(1, "ground turkey")

# Add a new ingredient
my_recipe.add_ingredient("diced onion")

# Add a new instruction
my_recipe.add_instruction("Saute onion in a separate pan until translucent.")

# Print the recipe
my_recipe.print_recipe()
