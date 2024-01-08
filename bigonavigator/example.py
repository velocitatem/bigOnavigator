from ohno import O, show_complexity_table

@O["1"]
def hello_world():
    print("Hello World!")

@O["n"]
def hello_world_n(n : int):
    for i in range(n):
        print("Hello World!")

@O["n!"]
def hello_world_nfact(n : int):
    for i in range(n):
        for j in range(n):
            print("Hello World!")

show_complexity_table()
