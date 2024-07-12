FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
def convert_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit=(celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return fahrenheit

def main():
    user_temp= input("Enter the temperature to convert:")
    unit= input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    match unit:
        case'C':
            converted_temp=convert_to_fahrenheit(user_temp)
        case 'F':
            cconverted_temp=convert_to_celsius(user_temp)
    print("invalid temperature and unit")


if __name__ == "__main__":
    main()