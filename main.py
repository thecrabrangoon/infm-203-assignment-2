"""main module

main function for running MapReduce implementation found in the mapreduce module.

Input data should be stored in transactions_data list. This is a list of strings,
with each transaction string matching the format "Customer_ID, Amount". Please
see the mapreduce module for further details.

Example values for transactions_data:

transactions_data = [
    "Amber, 143",
    "Zachary, 68",
    "Amber, 27",
    "Rosie, 8"
]
"""

from mapreduce import map_reduce



transactions_data = [
    "Alice, 20",
    "Bob, 50",
    "Alice, 30",
    "Bob, 20",
    "Charlie, 40"
]

def main():
    print(map_reduce(transactions_data))

if __name__ == "__main__":
    main()



