import math

def factorial(n):
    result = 1
    for n in range(2, n+1):
        result *= n
    return result

def deg2rad(deg):
    pi = 3.14159265358979323846264338
    return float(deg) * pi / 180

def sin(x, co):
    result = 0
    for i in range(int(co)):
        result += ((-1)**i) * (x ** (2*i+1)) / factorial(2*i+1)
    return result


def main():
    degree = input('degree: ')
    coefficient = input('coefficient for accuracy')
    rad = deg2rad(degree)
    result = sin(rad, coefficient)
    print(f'sin {degree} is {result}')

if __name__=="__main__":
    main()

