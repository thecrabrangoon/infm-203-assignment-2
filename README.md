# INFM-203 Assignment 2: MapReduce Python Example

## Overview

Simple MapReduce implementation to sum transaction amounts per customer across transactions data.

## Getting Started

The MapReduce implementation can be run via main.py, or through your own python file using the mapreduce module.

### Using main.py

main.py is set up to run the MapReduce implementation. Simply open main.py, update the transaction_data list with
your desired transaction strings, then run `python main.py`.

### Calling the mapreduce module

If you'd like to call the mapreduce module directly, you can import the map_reduce() function and pass the
transaction list yourself.

For example:
```
from mapreduce import map_reduce

transactions = [ "Customer1, 5", "Customer2, 10", ...]

print(mapreduce(transactions))
```

## Running unit tests

Unit tests for the mapreduce module are written using pytest. To run the pytest suite:
```
# Create a virtual env
python -m venv venv

# Activate the venv (unix)
source ./venv/bin/activate

# Install test dependencies
python -m pip install -r requirements.txt

# Run the tests
pytest test_mapreduce.py

```



