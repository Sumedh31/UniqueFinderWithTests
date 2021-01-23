import random
import time
import math


# This function receives number of email entries we want and create those entries
# and returns a list with emails , half of which are duplicate.
# If given number//2 does not give perfect square root then it would give a little more entries than desired entries.
# This is made generic to populate more than enough data.
def getemailaddressdata(requiredentries):
    iteration = int(math.sqrt(requiredentries // 2)) + 1 if requiredentries > 0 else 0
    names = []
    serverAddress = []
    emails = []
    for I in range(iteration):
        names.append("dummy_email_dummy_email_moreChar" + str(I))
        serverAddress.append("@testserver" + str(I) + ".com")
    for name in names:
        for domain in serverAddress:
            emails.append(name + domain)
    emails = emails + emails
    random.shuffle(emails)
    return emails


def removeduplicates(listtocheck):
    seen = {}
    #seen = set()
    unique = []
    for item in listtocheck:
        if (item not in seen):
            unique.append(item)
            # seen.add(item)
            seen[item] = item
    return unique


start_time = time.time()
originalList=getemailaddressdata(100000)
print("Lenghth of the Original List is %d"% len(originalList))
print("Lenghth of the Unique emails list is %d"% len(removeduplicates(originalList)))

print("------Porcessing took: %s" % (time.time() - start_time))
