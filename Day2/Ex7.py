import random

def get_random_temp(season=None):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "summer":
        return random.randint(24, 40)
    elif season == "autumn" or season == "fall":
        return random.randint(16, 23)
    elif season == "spring":
        return random.randint(16, 23)
    else:
        return random.randint(-10, 40)

def main():
    season = input("Enter the season (summer, autumn, winter, spring): ").lower()
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("It's a pleasant day.")
    elif 24 <= temp < 32:
        print("It's warm outside.")
    elif 32 <= temp <= 40:
        print("It's hot! Stay hydrated.")

# Call the main function
main()