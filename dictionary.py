# Creating a dictionary
student_info = {
 "name": "John Doe",
 "age": 20,
 "major": "Computer Science",
 "gpa": 3.8
}
# Accessing dictionary elements
print("Name:", student_info["name"])
print("Age:", student_info["age"])
# Modifying dictionary elements
student_info["age"] = 21
print("\nModified:",student_info)
# Adding a new key-value pair to the dictionary
student_info["university"] = "XYZ University"
print("\nADDED PAIR:",student_info)
# Checking if a key exists in the dictionary
if "age" in student_info:
 print("Age is present in the dictionary.")
else:
 print("Age is not present in the dictionary.")
