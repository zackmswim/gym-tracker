##Workout Program
Exercise_Name = input("What is the name of exercise?")
Num_sets = int(input("How many sets?"))
reps_set = int(input("What are the number of reps per set?"))
weight_set = float(input("What weight was used?"))

total_volume = Num_sets * reps_set * weight_set

workout = {
    "exercise": Exercise_Name,
    "sets": Num_sets,
    "reps": reps_set,
    "weight": weight_set,
    "total_volume": total_volume
}

# Save the workout to a file
with open("workouts.txt", "a") as file:
    file.write(f"{workout}\n")  # Append the workout data to the file

# Print confirmation
print(f"✅ Workout Saved! Total Volume: {total_volume} lbs")