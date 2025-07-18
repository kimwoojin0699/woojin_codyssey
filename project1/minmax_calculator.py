def main():
    try:
        user_input = input("Enter numbers: ")
        
        numbers = [float(x) for x in user_input.split()]
        
        min = numbers[0]
        max = numbers[0]
        
        for num in numbers[1:]:
            if num < min:
                min = num
            if num > max:
                max = num
        
        print(f"Min: {min}, Max: {max}")
        
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
    