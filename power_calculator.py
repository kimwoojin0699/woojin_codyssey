def main():
    try:
        a = float(input('Enter number: '))
    except ValueError:
        print('Invalid number input.')
        return

    try:
        b = int(input('Enter exponent: '))
    except ValueError:
        print('Invalid exponent input.')
        return

    result = 1
    for i in range(abs(b)):
        result *= a

    if b < 0:
        result = 1 / result

    print(f'Result: {result}')

if __name__ == "__main__":
    main()
