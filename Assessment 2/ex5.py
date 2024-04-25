import json

# Step 1: Store the example 5 JSON data in a file named ex5.json
example_5_json = '''
{
    "id": "0005",
    "type": "donut",
    "name": "Old Fashioned",
    "ppu": 0.55,
    "batters": {
        "batter": [
            { "id": "1001", "type": "Regular" },
            { "id": "1002", "type": "Chocolate" },
            { "id": "1003", "type": "Blueberry" },
            { "id": "1004", "type": "Devil's Food" }
        ]
    },
    "topping": [
        { "id": "5001", "type": "None" },
        { "id": "5002", "type": "Glazed" },
        { "id": "5005", "type": "Sugar" },
        { "id": "5007", "type": "Powdered Sugar" },
        { "id": "5006", "type": "Chocolate with Sprinkles" },
        { "id": "5003", "type": "Chocolate" },
        { "id": "5004", "type": "Maple" }
    ]
}
'''

with open('ex5.json', 'w') as file:
    file.write(example_5_json)

# Step 2: Read the JSON data from the file and load it into a dictionary
with open('ex5.json', 'r') as file:
    ex5 = json.load(file)

# Step 3: Add a batter named "Tea" for the donut with the name "Old Fashioned"
ex5['batters']['batter'].append({"id": "1005", "type": "Tea"})

# Step 4: Update the ex5.json file with the modified dictionary
with open('ex5.json', 'w') as file:
    json.dump(ex5, file, indent=4)

print("JSON file updated successfully.")

