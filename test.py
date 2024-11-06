"""
ext = []  # Initialize the outer list to hold other lists
cutLi = []
start = 1

# Create 3 sublists, each with 5 consecutive numbers
for i in range(3):  # Outer loop for creating 3 sublists
    cutLi.append([])  # Append an empty sublist to ext

    count = 0  # Counter to track the number of elements in each sublist
    while count < 5:
        cutLi[i].append(start)  # Add the current number to the sublist at ext[i]
        start += 1  # Increment start to the next number
        count += 1  # Increment count to track elements added

# Print the result
print(len(cutLi))
for sublist in cutLi:
    print(sublist)

"""
ext = [1200, 500, 4090, 3200, 200,110,2900,120]  # Initialize the outer list to hold other lists
cutLi = []
start = 1
rawMate = 6100


for i in range(len(ext)):  # nak loop ext
    if len(cutLi) == 0: # check sekiranya cutlist  permulaan
        cutLi = [[rawMate]]  # tambah dulu 1 batang 6100

    count = 0  # Counter to track the number of elements in each sublist
    while count < len(cutLi):
        if cutLi[count][-1] - ext[i] >= 0:
            newBalance = cutLi[count][-1] - ext[i]
            cutLi[count][-1] = ext[i]
            if newBalance > 0:
                cutLi[count].append(newBalance)
            break
        else:
            count += 1
            if count == len(cutLi):
                cutLi.append([rawMate])

        #cutLi[i].append(start)   Add the current number to the sublist at ext[i]
        #start += 1  # Increment start to the next number
          # Increment count to track elements added

# Print the result
print(len(cutLi))
for sublist in cutLi:
    print(sublist)
