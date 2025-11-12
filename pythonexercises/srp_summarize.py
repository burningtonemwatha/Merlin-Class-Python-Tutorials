def parse_input(user_input):
    # convert the comma separated string to a list of float numbers
    try:
        numbers = [float(x.strip()) for x in user_input.split(",") if x.strip()]
        return numbers
    except ValueError:
        print("Error: Please enter valid numbers separated by commas.")
        return []

def summarize_data(numbers):
    #computr the count, min, max, sum, avarage
    if not numbers:
        return "No data provided."
    
    # pyhton math method - count, sum, min, max, avarege
    total = sum(numbers)
    count = len(numbers) # returns number of items in a list
    smallest = min(numbers) # returns the smallest number in the list
    largest = max(numbers) # returns the largest number in the list
    average = round(total / count, 2) if count != 0 else 0 # round returns a number rounded to specified decimal places

    return {
        "count": count,
        "sum": total,
        "min": smallest,
        "max": largest,
        "average": average
    }

def display_result(result):
    #Display the dictionary in a user friendly way
    print("Summary of the provided data:")
    for key,value in result.items():
        print(f"The {key.capitalize()} is {value}")
        
# First function, main entry function
def main():
    """Main function: handle input and output printing"""
    user_input = input("Enter numbers separated by commas: ")

    # pass user input to the modular function that handles cleaning of the input
    numbers = parse_input(user_input)
    print(numbers)
    result = summarize_data(numbers)
    print(result) # dictionary output
    display_result(result)

if __name__ == "__main__":
    main()