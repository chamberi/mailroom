# Mailroom Madness

This repo contain an small implementation of a donation manager that runs in the command line.    
It allows the user to enter a new donation and generate a formatted thank you email.  
It also allows the user to print a report of all previous donations.
The mocked-up donations were generated using [*Faker*](http://faker.readthedocs.io/en/master/).

###Spec:

This script is compatible with both Python 2.7 and 3.7
We also use [*tabulate*](https://pypi.python.org/pypi/tabulate) to generate the donation report in a tabular format. It looks pretty!

###To start the script:

- Clone this repo
- Start a virtual environment
- Pip install .
- Run the script from your command line using `python3 donation_manage.py`



###Coverage:

```sh
---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                                 Stmts   Miss  Cover   Missing
------------------------------------------------------------------
src/donation_manager.py                 74     29    61%   16-24, 55-56, 61-73, 84-85, 94-97
src/tests/__init__.py                    0      0   100%
src/tests/test_donation_manager.py      24      0   100%
------------------------------------------------------------------
TOTAL                                   98     29    70%
```