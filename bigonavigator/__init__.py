import enum as e

class Complexity(e.Enum):
    O_1 = "1"
    O_n = "n"
    O_n2 = "n^2"
    O_n3 = "n^3"
    O_logn = "log(n)"
    O_nlogn = "nlog(n)"
    O_nlogn2 = "nlog(n)^2"
    O_2n = "2^n"
    O_nfact = "n!"


# static tracker for all the methods
tracker = {}



import time
import inspect
from typing import List, Tuple

def estimate_complexity(function, max_input_size=100):
    """
    Estimate the complexity of a function by measuring execution time
    for progressively larger inputs.
    """
    # Extract the argument names and annotations of the function
    signature = inspect.signature(function)
    parameters = signature.parameters

    # Check if all arguments have type annotations
    if not all(param.annotation != param.empty for param in parameters.values()):
        raise ValueError("All function parameters must have type annotations")

    # Function to generate sample inputs based on type annotations
    def generate_input(annotation, size):
        if annotation == int:
            return size
        elif annotation == List[int]:
            return [i for i in range(size)]
        else:
            raise ValueError("Unsupported argument type")

    times = []
    for size in range(1, max_input_size + 1):
        args = [generate_input(param.annotation, size) for param in parameters.values()]

        # suppress output
        import sys
        stdout = sys.stdout
        sys.stdout = open("trash", "w")
        start_time = time.time()
        function(*args)
        end_time = time.time()
        sys.stdout = stdout

        times.append((size, end_time - start_time))



O = {}
# define a method for each enum
for complexity in Complexity:
    # define a decorator for each method
    c = complexity
    def decorator(func, comp=c):
        tracker[func.__name__] = comp
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper
    # create a copy of the decorator for each method
    O[complexity.value] = decorator

def show_complexity_table():
    print("Complexity\tMethod")
    print("---------\t------")
    for method, complexity in tracker.items():
        print(f"O({complexity.value})\t\t{method}")
