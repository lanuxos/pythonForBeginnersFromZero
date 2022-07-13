# Python for beginners from zero
# ep.6

# Condition [if/elif/else] - 001220
# While loop - 014120
```
import time
while True:
    print('While Loop')
    time.sleep(5)
```
# for loop - 021100
```
friend = ['a', 'b', 'c', 'd', 'e']

for f in friend:
    print(f)

for i, f in enumerate(friend):
    print(i, f)

for i, f in enumerate(friend, start=2):
    print(i, f)

friends = {'a':'apple', 'b':'bird', 'c':'cat', 'd':'dog', 'e':'eye'}

for f in friends.items():
    print(f)

for k, v in friends.items():
    print(k, v)

for f in friends.keys():
    print(f)

for f in friends:
    print(f)

for i, f in enumerate(friends.items()):
    print(i, f)

for i, (k, v) in enumerate(friends.items()):
    print(i, k, v)
```