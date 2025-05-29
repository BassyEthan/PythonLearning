import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

number_of_friends = len(friends)
random = random.randint(0, number_of_friends - 1)
print(friends[random])
