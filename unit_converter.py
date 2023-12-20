def temperature_converter():
    print("Temperature Converter")
    try:
        value = float(input("Enter the temperature value: "))
        source_unit = input("Enter source unit (Celsius or Fahrenheit): ").lower()
        target_unit = input("Enter target unit (Celsius or Fahrenheit): ").lower()

        if source_unit == target_unit:
            result = value
        elif source_unit == "celsius" and target_unit == "fahrenheit":
            result = (value * 9/5) + 32
        elif source_unit == "fahrenheit" and target_unit == "celsius":
            result = (value - 32) * 5/9
        else:
            raise ValueError("Unsupported units for temperature conversion.")

        print(f"Result: {result} {target_unit}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def length_converter():
    print("Length Converter")
    try:
        value = float(input("Enter the length value: "))
        source_unit = input("Enter source unit (Meters or Feet): ").lower()
        target_unit = input("Enter target unit (Meters or Feet): ").lower()

        if source_unit == target_unit:
            result = value
        elif source_unit == "meters" and target_unit == "feet":
            result = value * 3.281
        elif source_unit == "feet" and target_unit == "meters":
            result = value / 3.281
        else:
            raise ValueError("Unsupported units for length conversion.")

        print(f"Result: {result} {target_unit}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def weight_converter():
    print("Weight Converter")
    try:
        value = float(input("Enter the weight value: "))
        source_unit = input("Enter source unit (Kilograms or Pounds): ").lower()
        target_unit = input("Enter target unit (Kilograms or Pounds): ").lower()

        if source_unit == target_unit:
            result = value
        elif source_unit == "kilograms" and target_unit == "pounds":
            result = value * 2.205
        elif source_unit == "pounds" and target_unit == "kilograms":
            result = value / 2.205
        else:
            raise ValueError("Unsupported units for weight conversion.")

        print(f"Result: {result} {target_unit}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Unit Converter")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")

    choice = input("Select an option (1, 2, or 3): ")

    if choice == "1":
        temperature_converter()
    elif choice == "2":
        length_converter()
    elif choice == "3":
        weight_converter()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
