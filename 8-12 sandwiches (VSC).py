def make_sandwich(*items):
    print("\nI'll make you a great sandwhich: ")
    for item in items:
        print(f" ....adding {item} to your sandwhich ")
    print(("Your sandwhich is ready! "))

make_sandwich('roast beef','cheddar cheese','lettuce','honey dijon')
make_sandwich('turkey','apple slices','hoeny mustard')
make_sandwich('penut butter','strawberry jam')

