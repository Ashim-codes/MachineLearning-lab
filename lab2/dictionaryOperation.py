# Original dictionary
student = {
    "name": "Ram",
    "age": 20,
    "faculty": "BCE"
}

print("Original Dictionary:", student)

# Access value
print("\nName:", student["name"])

# Use get()
print("Age:", student.get("age"))

# Add item
student["address"] = "Kathmandu"
print("\nAfter Adding Address:", student)

#  Update value
student["age"] = 21
print("After Updating Age:", student)

#  Remove item using del
del student["faculty"]
print("\nAfter del faculty:", student)

#  Remove item using pop()
removed = student.pop("address")
print("Removed:", removed)
print("After pop:", student)

#  Remove last item
student.popitem()
print("\nAfter popitem():", student)

#  Copy dictionary
student_copy = student.copy()
print("\nCopied Dictionary:", student_copy)

#  Get all keys
print("\nKeys:", student.keys())

#  Get all values
print("Values:", student.values())

#  Get all items
print("Items:", student.items())

#  Check if key exists
if "name" in student:
    print("\n'name' key exists")
else:
    print("\n'name' key does not exist")

#  Get length
print("Length:", len(student))

#  Loop through keys
print("\nLoop through keys:")
for key in student:
    print(key)

#  Loop through values
print("\nLoop through values:")
for value in student.values():
    print(value)

# Loop through items
print("\nLoop through items:")
for key, value in student.items():
    print(key, ":", value)

#  Clear dictionary
student.clear()
print("\nAfter clear():", student)