"""
Author: RJ Haye
Assignment: #1
"""

# ii. Create 4 variables with comments for data types

gym_member = "Alex Alliton"      # string
preferred_weight_kg = 20.5       # float
highest_reps = 25                # integer
membership_active = True         # boolean


# iii. Create a dictionary named workout_stats
# Data type: dictionary (keys = strings, values = lists of integers)

workout_stats = {
    "Alex": [30, 45, 50],
    "Jamie": [20, 25, 30],
    "Taylor": [60, 40, 35],
    "Morgan": [15, 20, 25]
}


# iv. Calculate total workout minutes using a loop
for friend, minutes in workout_stats.items():
    total = sum(minutes)
    workout_stats[friend + "_Total"] = total


# v. Create a 2D nested list called workout_list
# Data type: list of lists (2D list)

workout_list = list(workout_stats.values())[:4]


# vi. Slice the workout_list

# Yoga and running for all friends (columns 0 and 1)
print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[:2])

# Weightlifting for the last two friends (column 2)
print("\nWeightlifting minutes for last two friends:")
for row in workout_list[-2:]:
    print(row[2])


# vii. Check if any friend's total >= 120
for friend in ["Alex", "Jamie", "Taylor", "Morgan"]:
    total = workout_stats[friend + "_Total"]
    if total >= 120:
        print("Great job staying active,", friend + "!")


# viii. User input to look up a friend
name = input("\nEnter a friend's name: ")

if name in workout_stats:
    print(name, "workout minutes:", workout_stats[name])
    print("Total minutes:", workout_stats[name + "_Total"])
else:
    print("Friend", name, "not found in the records.")


# ix. Friend with highest and lowest total workout minutes

totals = {k: v for k, v in workout_stats.items() if "_Total" in k}

highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print("\nFriend with highest total:", highest.replace("_Total", ""), totals[highest])
print("Friend with lowest total:", lowest.replace("_Total", ""), totals[lowest])
