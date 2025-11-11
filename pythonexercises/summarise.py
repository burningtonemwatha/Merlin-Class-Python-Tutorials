"""
Takes in a list and returns a dictionary of keye and value pairs for the following info:
"count":4,
"sum":10,
"min":1,
"max":4,
"average":2.5
"""


def summarise_data(user_input):

    # If numbers list is empty
    if not user_input:
        return "No data provided."
    print("Input List for summarisation:", user_input)

    # Reference Units
    total = 0.0
    count = 0
    smallest = float("inf")
    largest = float("-inf")

    # Loop list to calculate required values
    for num in user_input:
        total += num
        count += 1
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    average = total / count if count != 0 else 0

    summary = {
        "count": count,
        "sum": total,
        "min": smallest,
        "max": largest,
        "average": round(average, 2)
    }

    return summary


# In built variables __name__ and __main__
if __name__ == "__main__":
    # pick up the list from user
    numbers = input("Enter numbers separated by commas: ")
    # convert the string input to a list of floats
    # try (Try executing) and except (Graciously handles any error that arises without causing module crash): Error Handling
    try:
        # take users input and return a list
        # split inbuilt string method that truncates relative to symbol/char given
        # strip - removes any leading or trailing spaces, illegal chars
        # "10, 20, 30" -> ["10", "20", "30"] -> [10.0, 20.0, 30.0]
        user_input = [float(x.strip()) for x in numbers.split(",") if x.strip() != ""]
        result = summarise_data(user_input)

        print(result)
    except ValueError:
        print("Error: Please enter valid numbers separated by commas.")
        user_input = []
   