numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Numbers:", numbers)
print("Count:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)