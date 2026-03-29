age = float(input("Enter your age: "))

if age < 18:
    print("Not eligible to vote")
elif 18 <= age <= 60:
    print("Eligible to vote")
else:
    print("Senior citizen voter")