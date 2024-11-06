"""
ext = []  # Initialize the outer list to hold other lists
start = 1
#qty = 0

# Create 3 sublists, each with 5 consecutive numbers
for _ in range(3):  # Outer loop for creating 3 sublists
    sublist = []  # Start with an empty sublist
    count = 0  # Counter to track the number of elements in each sublist

    while count < 5:
        sublist.append(start)  # Add the current number to the sublist
        start += 1  # Increment start to the next number
        count += 1  # Increment count to track elements added

    ext.append(sublist)  # Append the completed sublist to ext

# Print the result
print(len(ext))
for sublist in ext:
    print(sublist)
"""

ext = [1200,500,600,2100]  # Initialize the outer list to hold other lists
rawMate = 6100
#start = 1
#qty = 0

# Create 3 sublists, each with 5 consecutive numbers
for _ in range(len(ext)):  # Outer loop for creating 3 sublists

    sublist = []  # Start with an empty sublist
    count = 0  # Counter to track the number of elements in each sublist

    while count < 5:
        sublist.append(start)  # Add the current number to the sublist
        start += 1  # Increment start to the next number
        count += 1  # Increment count to track elements added

    ext.append(sublist)  # Append the completed sublist to ext

# Print the result
print(len(ext))
for sublist in ext:
    print(sublist)