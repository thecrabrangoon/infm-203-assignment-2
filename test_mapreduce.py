import pytest

from mapreduce import map_reduce



def test_non_list_transactions_input_raises_exception():
    transactions = ("tuple_value_1", "tuple_value_2", "tuple_value_3")
    with pytest.raises(RuntimeError):
        map_reduce(transactions)

def test_no_transactions_does_not_raise_exception():
    transactions = []
    map_reduce(transactions)

def test_no_transactions_results_in_empty_dict():
    transactions = []
    assert map_reduce(transactions) == {}

def test_non_string_transaction_raises_exception():
    transactions = [30, 35, 40, 45]
    with pytest.raises(TypeError):
        map_reduce(transactions)

def test_incorrectly_formatted_transaction_string_raises_exception():
    transactions = ["Marshall, 50", "Adrian75"]
    with pytest.raises(RuntimeError):
        map_reduce(transactions)

def test_non_integer_transaction_amount_raises_exception():
    transactions = ["Ren, 3.14"]
    with pytest.raises(RuntimeError):
        map_reduce(transactions)

def test_single_transaction_yields_correct_result():
    transactions = ["Ham, 27"]
    assert map_reduce(transactions) == {"Ham": 27}

def test_multiple_customers_transactions_yields_correct_result():
    transactions = ["Pepper, 2", "Sage, 700", "Pepper, 3"]
    assert map_reduce(transactions) == {"Pepper": 5, "Sage": 700}

def test_multiple_transactions_same_customer_yields_correct_result():
    transactions = ["Pickle, 1", "Pickle, 2", "Pickle, 3", "Pickle, 5", "Pickle, 8"]
    assert map_reduce(transactions) == {"Pickle": 19}



