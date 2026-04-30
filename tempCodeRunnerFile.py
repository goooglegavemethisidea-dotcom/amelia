
print("i have eaten" +str(99)+"burritos.")
positive_count = 0
negative_count = 0

for i in range(10):
    number = int(input("Enter an integer: "))
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    # 0 is ignored

choice = input("Type p for positive or n for negative: ").lower()

if choice == "p":
    print("Positive numbers:", positive_count)
elif choice == "n":
    print("Negative numbers:", negative_count)
else:
    print("Invalid choice. Please type 'p' or 'n'.")
# Increasing part
for row in range(1, 5):
    print("#" * row)
# Decreasing part
for row in range(3, 0, -1):
    print("#" * row)