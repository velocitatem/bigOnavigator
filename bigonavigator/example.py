# import O from same dire __init__.py
from __init__ import O, show_complexity_table

@O["1"]
def hello_world():
    print("Hello World!")
    return "Hello World!"

@O["n"]
def hello_world_n(n : int):
    for i in range(n):
        print("Hello World!")

@O["n!"]
def hello_world_nfact(n : int):
    for i in range(n):
        for j in range(n):
            print("Hello World!")

print(hello_world())
show_complexity_table()
