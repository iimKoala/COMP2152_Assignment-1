"""
Author: RJ Haye
Assignment: #1
"""

# Step b: Create 4 variables
friend1 = "Alex"
friend2 = "Jordan"
friend3 = "Taylor"
friend4 = "Morgan"

minutes1 = [30, 40, 50]
minutes2 = [20, 25, 30]
minutes3 = [60, 45, 30]
minutes4 = [15, 20, 25]

# Step c: Create a dictionary named workout_stats
workout_stats = {}

# Step d: Calculate total workout minutes using a loop and add to dictionary
friends = [friend1, friend2, friend3, friend4]
minutes_lists = [minutes1, minutes2, minutes3, minutes4]

for i in range(len(friends)):
    total = 0
    for m in minutes_lists[i]:
        total += m
    workout_stats[friends[i]] = total

print("Workout totals:", workout_stats)

# Step e: Create a 2D nested list called workout_list
workout_list = [minutes1, minutes2, minutes3, minutes4]

# Step f: Slice the workout_list
print("First two friends' workouts:", workout_list[:2])

# Step g: Check if any friend's total >= 120
for name, total in workout_stats.items():
    if total >= 120:
        print(name, "worked out at least 120 minutes")

# Step h: User input to look up a friend
search = input("Enter a friend's name to look up: ")

if search in workout_stats:
    print(search, "worked out", workout_stats[search], "minutes")
else:
    print("Friend not found")

# Step i: Friend with highest and lowest total workout minutes
highest = max(workout_stats, key=workout_stats.get)
lowest = min(workout_stats, key=workout_stats.get)

print("Highest workout:", highest, workout_stats[highest], "minutes")
print("Lowest workout:", lowest, workout_stats[lowest], "minutes")
