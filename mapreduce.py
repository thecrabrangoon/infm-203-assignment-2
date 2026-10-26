```
Assumptions:
    "Amount" will always be a whole number
```

```
MapReduce Simulation

Input: List of transactions, each transaction is a string of "CustomerID, Amount"
Output: Dict mapping CustomerID to total amount spent across transactions

Pseudocode:

Handle input of transaction list
If no user input, return error
If at least one user input, ensure it is a list with strings in correct format

Map function
Input: list of transactions
Output: List of key-value pairs, key = user, value = specific transaction amount
For each input:
    Split string on comma, first part if customerID, second part is amount
    Cast amount string to int
    Append key value pair of customer and number amount to output of map function

Shuffle and sort function:
Input: mapped key value pairs list from map function
Output: default dict with key as customerID, value as list of transaction amounts
Create defaultdict(list)
for each key value pair in mapped data:
    add transaction value to key in grouped defaultdict

Reduce function:
Input: grouped data from shuffle and sort function
Output: map/dict of customer IDs to total transaction amounts
```



