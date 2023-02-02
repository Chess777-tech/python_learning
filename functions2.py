def multiplied_nums(num1, num2):
    return num1 * num2



def describe_pet(pet_name, animal_type='K9'):
    print(f"The {animal_type}s name is {pet_name}")


def health_bar(current_health, damage_dealt, defense=5):
    """
    max health 20 
    death is 0 
    max defense is 5
    """
    dmg = damage_dealt - defense
    if dmg > 0:
        return current_health - dmg
    
    return current_health


if __name__ == "__main__":
    #print(multiplied_nums(5, 5))
    #describe_pet('ch', animal_type="rabbit")
    current_health = 20
    damage_taken = 5
    new_health = health_bar(current_health, damage_taken, defense=3)
    print(f"The Wizards current health is {current_health}... You have taken {damage_taken} damage. The wizards new health is {new_health}")
