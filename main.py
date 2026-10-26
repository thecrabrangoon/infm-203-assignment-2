from mapreduce import map_reduce

'''
Please input your data into the transactions_data list

e.g.
transactions_data = [
    "Amber, 143",
    "Zachary, 68",
    "Amber, 27",
    "Rosie, 8"
]
'''
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



