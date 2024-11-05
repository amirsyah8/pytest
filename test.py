"""
ext = [1200, 500, 4090, 3200, 700]
rawM = 6100
bal = [rawM]

for i in range(len(ext)):
    n = 0
    while n < len(bal):
        last_balance = bal[n]

        if last_balance - ext[i] >= 0:
            new_balance = last_balance - ext[i]
            bal[n] = ext[i]  # Update the current entry in bal with ext[i]
            bal.append(new_balance)  # Add the new balance to bal
            print(bal)  # Print bal after each update
            break
        n += 1
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


