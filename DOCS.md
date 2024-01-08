# BigONavigator Documentation

Welcome to the documentation for BigONavigator, your comprehensive guide to analyzing computational complexity in Python.

## Introduction

BigONavigator is a Python package developed initially as a university project. It's designed to estimate and track the computational complexity of functions, providing a clear overview of performance in Big O notation.

## Installation

To install BigONavigator, run the following command in your terminal:

```bash
pip install BigONavigator
```

Ensure you have Python version 3.8 or higher installed. Ideally 3.11.

## Getting Started

To begin using BigONavigator, import the package and use the decorators on your functions.

Example:

```python
from bigonavigator import O

@O['n']
def sample_function(data):
    # Your code here
    pass
```

## Using BigONavigator

### Decorators

BigONavigator provides decorators corresponding to different complexity classes. Here's how to use them:

- `@O['1']`: For constant time complexity.
- `@O['n']`: For linear time complexity.
- `@O['n^2']`: For quadratic time complexity.
- `@O['log(n)']`: For logarithmic time complexity.
- `@O['nlog(n)']`: For linearithmic time complexity.
- `@O['nlog(n)^2']`: For linearithmic time complexity.
- `@O['2^n']`: For exponential time complexity.
- `@O['n!']`: For factorial time complexity.


### Tracking and Displaying Complexity

After decorating your functions, you can display their complexities:

```python
from bigonavigator import show_complexity
show_complexity_table() # tracked statically across all instances
```

This function prints a table showing each function's name and its estimated complexity.
