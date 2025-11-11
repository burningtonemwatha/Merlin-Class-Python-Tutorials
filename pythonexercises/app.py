# variables - named storage references for information
# variables will receive data types from the values they store
# Data types - categories of information that determine what can be done with that information
name = "Alice"          # string data type
age = 30                # integer data type
is_student = True       # boolean data type
height = 5.7           # float data type
courses = ["Math", "Science", "Art", 12]  # list data type
set_of_skills = {"Python", "Data Analysis", "Machine Learning"}  # set data type
person = {             # dictionary data type - collection of key-value pairs
    "name": name,
    "age": age,
    "is_student": is_student,
    "height": height,
    "courses": courses,
    "skills": set_of_skills
}
tuple_of_coordinates = (10.0, 20.0)  # tuple data type
none_value = None      # NoneType data type

# output by print()
print("Name:", name)
print("Age:", age)
print("Is Student:", is_student)
print("Height:", height)
print("Courses:", courses)
print("Skills:", set_of_skills)
print("Coordinates:", tuple_of_coordinates)
print("None Value:", none_value)

# input by input()
#user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
#user_is_student = input("Are you a student? (True/False): ")
#user_height = input("Enter your height: ")
#user_courses = input("Enter your courses (comma-separated): ").split(",")
#user_skills = input("Enter your skills (comma-separated): ").split(",")
#user_coordinates = tuple(map(float, input("Enter your coordinates (x,y): ").split(",")))

# formatted string output: we can attach statements dynamically with variables
#print(f"User Name: {user_name}, Age: {user_age}, Is Student: {user_is_student}, Height: {user_height}, Courses: {user_courses}, Skills: {user_skills}, Coordinates: {user_coordinates}")

# variable reassignment - changing the value stored in a variable
age = 100  # reassigning age variable
print("Updated Age:", age)
is_student = False  # reassigning is_student variable
print("Updated Is Student:", is_student)
height = 5.8  # reassigning height variable
print("Updated Height:", height)
courses.append("History")  # modifying courses list
print("Updated Courses:", courses)
set_of_skills.add("Communication")  # modifying skills set
print("Updated Skills:", set_of_skills)
tuple_of_coordinates = (15.0, 25.0)  # reassigning tuple_of_coordinates variable
print("Updated Coordinates:", tuple_of_coordinates)
person["age"] = age  # updating dictionary value
print("Updated Person Dictionary:", person)

# control flows

if is_student:
    print(f"{name} is a student.")
else:
    print(f"{name} is not a student.")

if user_age < 18:
    print(f"{name} is a minor.")
elif 18 <= user_age < 65:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a senior citizen.")

