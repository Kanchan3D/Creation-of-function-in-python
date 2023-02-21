def factorial(value):
    if value==0:
        return 1
    else:
        return factorial(value-1)*value
value=int(input())
print(factorial(value))
