# Initialize hash table
hash_table = {"mar1": 1, "mar2": 3, "mar3": 4, "mar4": 4}

# Access and print a specific item
print(f"Get item: {hash_table['mar1']}")

# Update a value in the hash table
hash_table["mar1"] = 3
print(f"Updated item value for 'mar1': {hash_table['mar1']}")

# Print all keys
print(f"Keys: {list(hash_table.keys())}")

# Print all values
print(f"Values: {list(hash_table.values())}")

# Iterate over and print all key-value pairs
print("All key-value pairs:")
for key, value in hash_table.items():
    print(f"Key: {key} --> Value: {value}")


# Initialize an empty dictionary to store weather data
weather = {}

# Path to the CSV file
file_path = "/Users/sabbir/work/hand-notes/DSA/hashTable/nyc_weather.csv"

# Open the file in read mode
with open(file_path, mode="r") as f:
    # Skip the header row if the file contains column names
    next(f)

    # Iterate through each line in the file
    for line in f:
        try:
            # Remove leading/trailing spaces and split the line into key (date) and value (temperature)
            key, value = line.strip().split(",")

            # Store the date and temperature in the dictionary
            # Convert the temperature value to an integer for further calculations
            weather[key] = int(value)
        except ValueError:
            # Skip lines that are not properly formatted (e.g., missing data or invalid numbers)
            continue

# Retrieve the first 10 days' temperature values
temperatures = list(weather.values())[:10]

# Find the maximum temperature in the first 10 days
max_temp = max(temperatures)

# Print the result
print("Max temperature -->", max_temp)
