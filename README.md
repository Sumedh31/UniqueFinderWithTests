# UniqueFinderWithTests
This little project demonstrates that a random unsorted list if emails of over 100000 addresses is parsed to remove duplicates from it under 1 s.
There are several unit tests as well whcih ensures the integrity of the code.

# Installation
First, install the dependencies of this project with pip:

$ pip install -r requirements.txt

# Run:
UniqueFinder.py File creates the data of more than 100,000 entries of email addresses (Returned list of email addresses is unsorted) with half of them are duplicate and later it removes the duplicated entries ans create a new list with unique email addresses.

# Tests:
TestsForUniqueFinder.py has several tests that ensures that the UniqueFinder does exactly what it is supposed to do. There are total 8 tests for unique finder in file "TestsForUniqueFinder.py". Following you can see that all the test are passed.
![Alt text](/TestResults.PNG.PNG?raw=true "Test results")

# Peroformance of the script-

The function was able to remove entries of 100000 emails with half of them are duplicated in under 1 seconds. The function removeduplicates returns a list of Unique elements in their original order.

![Alt text](/Peroformance.PNG?raw=true "Processed in 1 s")
