# Now I would like to bring the package structure to the next level by adding sub-packages.
from package.basic import add, subtract
from package.advance import multiply, divide
from package.my_tools import calculate

def main():
    a = 10
    b = 5

    sum_result = add(a, b)
    print(f"Addition of {a} and {b} is: {sum_result}")

    sub_result = subtract(a, b)
    print(f"Subtraction of {a} and {b} is: {sub_result}")

    mul_result = multiply(a, b)
    print(f"Multiplication of {a} and {b} is: {mul_result}")

    div_result = divide(a, b)
    print(f"Division of {a} by {b} is: {div_result}")

    calc_result = calculate()
    print(f"Calculation result from calculate function is: {calc_result}")

main()