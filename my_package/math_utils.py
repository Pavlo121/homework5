def factorial(n):
    """Обчислює факторіал числа n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def gcd(a, b):
    """Знаходить найбільший спільний дільник (НСД) двох чисел a та b."""
    while  b:
        a, b = b, a % b
    return a



