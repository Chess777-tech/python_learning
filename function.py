#function with no arguments
def say_hello():
    print("hello")


#function with one parameter
def say_greeting(message):
    print(f"Hello {message} ")



#function with two parameters
def add_two_numbers(num1, num2):
    return num1 + num2

#a function two parameters where one is a default value 
def display_text(text, caps=False, add_dunder=False):
    if caps:
        if add_dunder:
            print(f"__{text.upper}__")
        else:
            print(f"{text.upper()}")
    else:
        if add_dunder:
            print(f"__{text}__")
        else:
            print(f"{text}")


def find_color(colors):
    if len[colors] > 0:
        for color in colors:
            if len[colors] > 4:
                print(color)




if __name__ == "__main__":
    say_hello()
    msg = "Python is fun"
    answer = add_two_numbers(4,9)
    print(answer)


    display_text('coding', caps=True)
    

    find_color(['yellow','blue','red'])