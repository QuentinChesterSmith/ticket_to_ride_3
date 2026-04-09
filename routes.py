import numpy as np

routes = {
    "0": {
        "City1": "Vancouver",
        "City2": "Seattle",
        "Length": 1,
        "RawPoints": 1,
        "Color": "Gray" # gray
    },
    "1": {
        "City1": "Seattle",
        "City2": "Portland",
        "Length": 1,
        "RawPoints": 1,
        "Color": "Gray" # Gray
    },
    "2": {
        "City1": "Portland",
        "City2": "San Francisco",
        "Length": 5,
        "RawPoints": 10,
        "Color": "Pink" # And Green
    },
    "3": {
        "City1": "San Francisco",
        "City2": "Los Angeles",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Yellow" #Pink
    },
    "4": {
        "City1": "Los Angeles",
        "City2": "El Paso",
        "Length": 6,
        "RawPoints": 15,
        "Color": "Black"
    },
    "5": {
        "City1": "Los Angeles",
        "City2": "Phoenix",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Gray"
    },
    "6": {
        "City1": "Los Angeles",
        "City2": "Las Vegas",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "7": {
        "City1": "San Francisco",
        "City2": "Salt Lake City",
        "Length": 5,
        "RawPoints": 10,
        "Color": "Orange" # White
    },
    "8": {
        "City1": "Portland",
        "City2": "Salt Lake City",
        "Length": 6,
        "RawPoints": 15,
        "Color": "Blue"
    },
    "9": {
        "City1": "Seattle",
        "City2": "Helena",
        "Length": 6,
        "RawPoints": 15,
        "Color": "Yellow"
    },
    "10": {
        "City1": "Vancouver",
        "City2": "Calgary",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Gray"
    },
    "11": {
        "City1": "Calgary",
        "City2": "Winnipeg",
        "Length": 6,
        "RawPoints": 15,
        "Color": "White"
    },
    "12": {
        "City1": "Calgary",
        "City2": "Helena",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Gray"
    },
    "13": {
        "City1": "Helena",
        "City2": "Winnipeg",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Blue"
    },
    "14": {
        "City1": "Helena",
        "City2": "Salt Lake City",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Pink"
    },
    "15": {
        "City1": "Salt Lake City",
        "City2": "Denver",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Red" # Yellow
    },
    "16": {
        "City1": "Phoenix",
        "City2": "Denver",
        "Length": 5,
        "RawPoints": 10,
        "Color": "White"
    },
    "17": {
        "City1": "Santa Fe",
        "City2": "Phoenix",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Gray"
    },
    "18": {
        "City1": "Phoenix",
        "City2": "El Paso",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Gray"
    },
    "19": {
        "City1": "El Paso",
        "City2": "Santa Fe",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "20": {
        "City1": "Santa Fe",
        "City2": "Denver",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "21": {
        "City1": "Denver",
        "City2": "Helena",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Green"
    },
    "22": {
        "City1": "Helena",
        "City2": "Duluth",
        "Length": 6,
        "RawPoints": 15,
        "Color": "Orange"
    },
    "23": {
        "City1": "Helena",
        "City2": "Omaha",
        "Length": 5,
        "RawPoints": 10,
        "Color": "Red"
    },
    "24": {
        "City1": "Denver",
        "City2": "Omaha",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Pink"
    },
    "25": {
        "City1": "Denver",
        "City2": "Kansas City",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Black" # Orange
    },
    "26": {
        "City1": "Denver",
        "City2": "Oklahoma City",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Red"
    },
    "27": {
        "City1": "Santa Fe",
        "City2": "Oklahoma City",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Blue"
    },
    "28": {
        "City1": "El Paso",
        "City2": "Oklahoma City",
        "Length": 5,
        "RawPoints": 10,
        "Color": "Yellow"
    },
    "29": {
        "City1": "El Paso",
        "City2": "Dallas",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Red"
    },
    "30": {
        "City1": "El Paso",
        "City2": "Houston",
        "Length": 6,
        "RawPoints": 15,
        "Color": "Green"
    },
    "31": {
        "City1": "Houston",
        "City2": "Dallas",
        "Length": 1,
        "RawPoints": 1,
        "Color": "Gray" # Gray
    },
    "32": {
        "City1": "Dallas",
        "City2": "Oklahoma City",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "33": {
        "City1": "Oklahoma City",
        "City2": "Kansas City",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "34": {
        "City1": "Kansas City",
        "City2": "Omaha",
        "Length": 1,
        "RawPoints": 1,
        "Color": "Gray" # Gray
    },
    "35": {
        "City1": "Omaha",
        "City2": "Duluth",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "36": {
        "City1": "Duluth",
        "City2": "Winnipeg",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Black"
    },
    "37": {
        "City1": "Winnipeg",
        "City2": "Sault St. Marie",
        "Length": 6,
        "RawPoints": 15,
        "Color": "Gray"
    },
    "38": {
        "City1": "Duluth",
        "City2": "Sault St. Marie",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Gray"
    },
    "39": {
        "City1": "Duluth",
        "City2": "Toronto",
        "Length": 6,
        "RawPoints": 15,
        "Color": "Pink"
    },
    "40": {
        "City1": "Sault St. Marie",
        "City2": "Montreal",
        "Length": 5,
        "RawPoints": 10,
        "Color": "Black"
    },
    "41": {
        "City1": "Sault St. Marie",
        "City2": "Toronto",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "42": {
        "City1": "Montreal",
        "City2": "Boston",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "43": {
        "City1": "Montreal",
        "City2": "New York",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Blue"
    },
    "44": {
        "City1": "Boston",
        "City2": "New York",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Red" # Yellow
    },
    "45": {
        "City1": "Toronto",
        "City2": "Pittsburgh",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "46": {
        "City1": "Toronto",
        "City2": "Chicago",
        "Length": 4,
        "RawPoints": 7,
        "Color": "White"
    },
    "47": {
        "City1": "Duluth",
        "City2": "Chicago",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Red"
    },
    "48": {
        "City1": "Omaha",
        "City2": "Chicago",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Blue"
    },
    "49": {
        "City1": "Chicago",
        "City2": "St Louis",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Green" # White
    },
    "50": {
        "City1": "Kansas City",
        "City2": "St Louis",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Blue" # Pink 
    },
    "51": {
        "City1": "Oklahoma City",
        "City2": "Little Rock",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "52": {
        "City1": "Dallas",
        "City2": "Little Rock",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "53": {
        "City1": "Houston",
        "City2": "New Orleans",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "54": {
        "City1": "Little Rock",
        "City2": "New Orleans",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Green"
    },
    "55": {
        "City1": "Little Rock",
        "City2": "Nashville",
        "Length": 3,
        "RawPoints": 4,
        "Color": "White"
    },
    "56": {
        "City1": "Little Rock",
        "City2": "St Louis",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "57": {
        "City1": "St Louis",
        "City2": "Nashville",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "58": {
        "City1": "New Orleans",
        "City2": "Atlanta",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Yellow" # Orange
    },
    "59": {
        "City1": "New Orleans",
        "City2": "Miami",
        "Length": 6,
        "RawPoints": 15,
        "Color": "Red"
    },
    "60": {
        "City1": "Miami",
        "City2": "Atlanta",
        "Length": 5,
        "RawPoints": 10,
        "Color": "Blue"
    },
    "61": {
        "City1": "Miami",
        "City2": "Charleston",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Pink"
    },
    "62": {
        "City1": "Atlanta",
        "City2": "Charleston",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "63": {
        "City1": "Raleigh",
        "City2": "Charleston",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "64": {
        "City1": "Nashville",
        "City2": "Atlanta",
        "Length": 1,
        "RawPoints": 1,
        "Color": "Gray"
    },
    "65": {
        "City1": "Atlanta",
        "City2": "Raleigh",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "66": {
        "City1": "Raleigh",
        "City2": "Washington",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "67": {
        "City1": "Nashville",
        "City2": "Pittsburgh",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Yellow"
    },
    "68": {
        "City1": "Chicago",
        "City2": "Pittsburgh",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Orange" # Black
    },
    "69": {
        "City1": "St Louis",
        "City2": "Pittsburgh",
        "Length": 5,
        "RawPoints": 10,
        "Color": "Green"
    },
    "70": {
        "City1": "New York",
        "City2": "Pittsburgh",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Green" # White
    },
    "71": {
        "City1": "Washington",
        "City2": "Pittsburgh",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "72": {
        "City1": "Raleigh",
        "City2": "Pittsburgh",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray"
    },
    "73": {
        "City1": "Las Vegas",
        "City2": "Salt Lake City",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Orange"
    },
    "74": {
        "City1": "New York",
        "City2": "Washington",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Orange" # Black
    },
        "75": {
        "City1": "Vancouver",
        "City2": "Seattle",
        "Length": 1,
        "RawPoints": 1,
        "Color": "Gray" # gray
    },
    "76": {
        "City1": "Seattle",
        "City2": "Portland",
        "Length": 1,
        "RawPoints": 1,
        "Color": "Gray" # Gray
    },
    "77": {
        "City1": "Portland",
        "City2": "San Francisco",
        "Length": 5,
        "RawPoints": 10,
        "Color": "Green" # And Green
    },
    "78": {
        "City1": "San Francisco",
        "City2": "Los Angeles",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Pink" #Pink
    },
    "79": {
        "City1": "San Francisco",
        "City2": "Salt Lake City",
        "Length": 5,
        "RawPoints": 10,
        "Color": "White" # White
    },
    "80": {
        "City1": "Salt Lake City",
        "City2": "Denver",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Yellow" # Yellow
    },
    "81": {
        "City1": "Denver",
        "City2": "Kansas City",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Orange" # Orange
    },
    "82": {
        "City1": "Houston",
        "City2": "Dallas",
        "Length": 1,
        "RawPoints": 1,
        "Color": "Gray" # Gray
    },
    "83": {
        "City1": "Dallas",
        "City2": "Oklahoma City",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "84": {
        "City1": "Oklahoma City",
        "City2": "Kansas City",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "85": {
        "City1": "Kansas City",
        "City2": "Omaha",
        "Length": 1,
        "RawPoints": 1,
        "Color": "Gray" # Gray
    },
    "86": {
        "City1": "Omaha",
        "City2": "Duluth",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "87": {
        "City1": "Montreal",
        "City2": "Boston",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "88": {
        "City1": "Boston",
        "City2": "New York",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Yellow" # Yellow
    },
    "89": {
        "City1": "Chicago",
        "City2": "St Louis",
        "Length": 2,
        "RawPoints": 2,
        "Color": "White" # White
    },
    "90": {
        "City1": "Kansas City",
        "City2": "St Louis",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Pink" # Pink 
    },
    "91": {
        "City1": "New Orleans",
        "City2": "Atlanta",
        "Length": 4,
        "RawPoints": 7,
        "Color": "Orange" # Orange
    },
    "92": {
        "City1": "Atlanta",
        "City2": "Raleigh",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "93": {
        "City1": "Raleigh",
        "City2": "Washington",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Gray" # Gray
    },
    "94": {
        "City1": "Chicago",
        "City2": "Pittsburgh",
        "Length": 3,
        "RawPoints": 4,
        "Color": "Black" # Black
    },
    "95": {
        "City1": "New York",
        "City2": "Pittsburgh",
        "Length": 2,
        "RawPoints": 2,
        "Color": "White" # White
    },
    "96": {
        "City1": "New York",
        "City2": "Washington",
        "Length": 2,
        "RawPoints": 2,
        "Color": "Black" # Black
    },

}

# Your city order
city_order = [
    "Vancouver", "Calgary", "Seattle", "Portland", "San Francisco", "Los Angeles",
    "Salt Lake City", "Las Vegas", "Phoenix", "Santa Fe", "El Paso", "Helena",
    "Denver", "Winnipeg", "Duluth", "Omaha", "Kansas City", "Oklahoma City",
    "Dallas", "Houston", "New Orleans", "Little Rock", "St Louis", "Chicago",
    "Sault St. Marie", "Toronto", "Montreal", "Boston", "New York", "Pittsburgh",
    "Washington", "Raleigh", "Nashville", "Atlanta", "Charleston", "Miami"
]
def to_array():
    # Map city names to integer indices
    city_to_idx = {city: idx for idx, city in enumerate(city_order)}

    # Color mapping
    color_map = {
        "pink": 0, "white": 1, "blue": 2, "yellow": 3, "orange": 4,
        "black": 5, "red": 6, "green": 7, "gray": 8
    }

    # Initialize array
    arr = np.zeros((4, len(routes)), dtype=int)

    for i, route in routes.items():
        idx = int(i)
        arr[0, idx] = city_to_idx[route["City1"]]
        arr[1, idx] = city_to_idx[route["City2"]]
        arr[2, idx] = route["Length"]
        arr[3, idx] = color_map[route["Color"].lower()]

    return arr