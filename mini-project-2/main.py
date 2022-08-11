weights_kg = []
heights_cm = []

nums_people = 4

for person in range(1, nums_people + 1):
    weight = float(input(f"Cân nặng của người {person}: "))
    weights_kg.append(weight)
    
    height = float(input(f"Chiều cao của người {person}: "))
    heights_cm.append(height)

for person in range(nums_people):
    bmi = weighs_kg[person] / heights_cm[person] ** heights_cm[person]
    print(f"BMI của người {person} {bmi}")
