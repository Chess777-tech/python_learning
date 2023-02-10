"""
make a list called sandwich_orders fill it with a variety of sandwiches
make an empty list named finished_sandwiches 
loop through the list of sandwich orders and print a message for each order
such as i made your tuna sandwich
as each sandwhich is made move it to the list of finished sandwiches 
after all sandwiches have been made print a message listing each sandwich that was made 
"""
print("\nThe deli has ran out of pastrami for the day ")
print("-----------------------------------------------")
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef','pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print(f"I'm working on your {current_sandwich} sandwich")
        finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich")