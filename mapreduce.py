"""mapreduce module -- MapReduce implementation for customer transactions.

The mapreduce module implements a simple MapReduce process with mapping 
parallelization.

Functions:
map_reduce() -- public function, runs entire MapReduce implementation given input list of transactions
and produces final output.
_map_func() -- first step of MapReduce, map transaction amounts by customer ID.
_shuffle_and_sort_func() -- second step of MapReduce, group mapped transaction amounds by customer ID.
_reduce_func() -- last step of MapReduce, process sum of transaction amounts per customer ID.

Assumptions:
Transaction amount is always a whole number and can be cast to an integer.
Customer ID is case sensitive.
Customer ID is unique to each individual customer.
"""

from collections import defaultdict
from multiprocessing import Pool
import re
import sys


transaction_format = re.compile(r"^(\w*)\, (\d*)$")
"""Regex for transaction string format.

Transaction format is expected as "Customer_ID, Amount"

Customer_ID must be alphanumeric word.
Amount must be numeric integer.
"""

def _map_func(transaction):
    """Map transaction amounts by customer ID.

    First step of MapReduce implementation.

    Transforms transaction amount from string to int for return value.

    Arguments:
    transaction -- required, transaction string containing customer ID and amount. Must match the format of regex
        transaction_format.

    Return Value:
    list containing the key, value pair of customer ID, transaction amount.

    Exceptions Raised:
    Raises RuntimeError if the transaction does not match the regex contained in transaction_format.
    Raises RuntimeError if the transaction amount cannot be cast from str to int.
    """
    transaction_match = re.fullmatch(transaction_format, transaction)
    try:
        customer_id, amount_str = transaction_match.group(1, 2)
    except Exception as e:
        raise RuntimeError("All transactions in input list must be in the string format \"CustomerID, Amount\"") from e
    try:
        amount = int(amount_str)
    except Exception as e:
        raise RuntimeError(f"Unable to cast amount to integer in transaction {transaction}") from e
    return [(customer_id, amount)]

def _shuffle_and_sort_func(mapped_data):
    """Group mapped transaction amount data based on customer ID.

    Second step of MapReduce implementation.

    Requirements:
    To be used in MapReduce implementation, map_func() must be run first.

    Arguments:
    mapped data -- required, mapped output from map_func(), list of key value pairs.

    Return Value:
    defaultdict where the keys are the customer ID string, and the values are a list containing all int transaction amounts
        for that customer.
    """
    grouped_data = defaultdict(list)
    for key, value in mapped_data:
        grouped_data[key].append(value)
    return grouped_data

def _reduce_func(grouped_data):
    """Process grouped data to sum total transaction amount per customer ID.

    Third and final step of MapReduce implementation.

    Requirements:
    To be used in MapReduce implementation, shuffle_and_sort_func() must be run first.

    Arguments:
    grouped_data -- required, defaultdict where key is customer ID str, and value is list of int transaction amounts
        for that customer.

    Return Value:
    dict where key is customer ID str, and value is int sum of transaction amount for that customer.
    """
    return {customer_id: sum(amounts) for customer_id, amounts in grouped_data.items()}

def map_reduce(transactions):
    """MapReduce implementation for customer transactions.

    Maps, Shuffles & Sorts, and Reduces transaction data to calculate transaction amounts by customer ID.

    Mapping function is parallelized via the builtin multiprocessing library.

    Arguments:
    transactions -- required, list of transaction strings. Should match the format of the regex stored in transaction_format,
        however the function that checks this formatting is map_func() (see function documentation).

    Return Value:
    Result of MapReduce implementation, dict where key is customer ID str, value is int sum of transaction amount for that customer.
    
    Exceptions Raised:
    Raises RuntimeError if transactions argument input is not type list.
    """
    if type(transactions) != list:
        raise RuntimeError("Input to map_reduce must be a list of transaction strings.")
    with Pool() as pool:
        mapped_data = pool.map(_map_func, transactions)
    flat_mapped_data = [pair for sublist in mapped_data for pair in sublist]
    grouped_data = _shuffle_and_sort_func(flat_mapped_data)
    return _reduce_func(grouped_data)



