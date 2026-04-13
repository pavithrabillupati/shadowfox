#i
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")

#ii
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]

city = input("Enter a city name: ")

if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print("City not found in list")

#iii
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

def find_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None

country1 = find_country(city1)
country2 = find_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities not found")


