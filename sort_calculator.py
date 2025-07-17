def bubble_sort(arr):
    len(arr)
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    try:
        input_str = input("Enter numbers: ").strip()
        if not input_str:
            print("Invalid input.")
            return

        parts = input_str.split()
        numbers = []
        print(parts)

        for part in parts:
            numbers.append(float(part))

        bubble_sort(numbers)

        formatted = " ".join(f"{num:.1f}" for num in numbers)
        print(f"Sorted: {formatted}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
