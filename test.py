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
