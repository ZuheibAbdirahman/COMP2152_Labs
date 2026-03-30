"""
Author: Zuheib Abdirahman  
Assignment: #1
"""
gym_member = "Alex Alliton"  # str (string)
preferred_weight_kg = 20.5   # float
highest_reps = 25            # int
membership_active = True     # bool (boolean)

print("Hello!")  # Test print
workout_stats = {
    "Alex": (30, 45, 20),     # (yoga, running, weightlifting)
    "Jamie": (25, 30, 35),    # (yoga, running, weightlifting)
    "Taylor": (40, 25, 30)    # (yoga, running, weightlifting)
}
print("\nworkout_stats dictionary created:")
print(workout_stats)

totals = {}

for friend, minutes in workout_stats.items():
    total = sum(minutes)  # Calculate total minutes for each friend
    totals[friend] = total  # Store in temporary dictionary

# Now add the totals to the original dictionary
for friend, total in totals.items():
    workout_stats[f"{friend}_Total"] = total

print("\nDictionary after adding totals:")
for key, value in workout_stats.items():
    print(f"{key}: {value}")
    # Step e: Create a 2D nested list called workout_list
# This is a list of lists containing integer values (workout minutes)
workout_list = [
    list(workout_stats["Alex"]),      # Alex's minutes: [30, 45, 20]
    list(workout_stats["Jamie"]),     # Jamie's minutes: [25, 30, 35]
    list(workout_stats["Taylor"])     # Taylor's minutes: [40, 25, 30]
]

print("\n2D workout_list created:")
print("Row format: [yoga, running, weightlifting]")
for i, friend in enumerate(["Alex", "Jamie", "Taylor"]):
    print(f"{friend}: {workout_list[i]}")
    # Step f: Slice the workout_list

# Extract and print minutes for yoga and running for all friends (all rows, first two columns)
yoga_running = [row[:2] for row in workout_list]  # List comprehension to slice each row
print("\nYoga and Running minutes for all friends:")
print(f"Alex (yoga, running): {yoga_running[0]}")
print(f"Jamie (yoga, running): {yoga_running[1]}")
print(f"Taylor (yoga, running): {yoga_running[2]}")

# Extract and print minutes for weightlifting for the last two friends
# Last two friends are Jamie and Taylor (indices 1 and 2)
# Weightlifting is the third column (index 2)
weightlifting_last_two = [row[2] for row in workout_list[1:3]]  # Get column 2 for rows 1 and 2
print("\nWeightlifting minutes for the last two friends:")
print(f"Jamie: {weightlifting_last_two[0]} minutes")
print(f"Taylor: {weightlifting_last_two[1]} minutes")
# Step g: Check if any friend's total workout minutes >= 120
print("\n--- Step g: Checking for friends with 120+ total minutes ---")

# Loop through the friends to check their totals
friends = ["Alex", "Jamie", "Taylor"]
for friend in friends:
    total_key = f"{friend}_Total"
    if workout_stats[total_key] >= 120:
        print(f"Great job staying active, {friend}!")
    else:
        print(f"{friend}'s total is {workout_stats[total_key]} minutes (less than 120)")
        # Step h: User input to lookup a friend
print("\n--- Step h: Friend Lookup ---")

# Get user input
friend_name = input("Enter a friend's name to look up (Alex, Jamie, or Taylor): ")

# Check if the name exists in the dictionary (case-sensitive)
if friend_name in ["Alex", "Jamie", "Taylor"]:  # Check if it's one of our friends
    # Get the workout minutes for that friend
    minutes = workout_stats[friend_name]
    total = workout_stats[f"{friend_name}_Total"]
    
    # Print the friend's workout details
    print(f"\n{friend_name}'s workout minutes:")
    print(f"  Yoga: {minutes[0]} minutes")
    print(f"  Running: {minutes[1]} minutes")
    print(f"  Weightlifting: {minutes[2]} minutes")
    print(f"  Total: {total} minutes")
else:
    print(f"Friend '{friend_name}' not found in the records.")
    # Step i: Friend with highest and lowest total workout minutes
print("\n--- Step i: Highest and Lowest Totals ---")

# Find the friend with highest total
max_total = -1  # Start with a very low number
max_friend = ""

# Find the friend with lowest total
min_total = float('inf')  # Start with infinity (very high number)
min_friend = ""

# Loop through friends to find max and min
for friend in friends:
    total = workout_stats[f"{friend}_Total"]
    
    if total > max_total:
        max_total = total
        max_friend = friend
    
    if total < min_total:
        min_total = total
        min_friend = friend

# Print the results
print(f"Friend with highest total minutes: {max_friend} with {max_total} minutes")
print(f"Friend with lowest total minutes: {min_friend} with {min_total} minutes")

