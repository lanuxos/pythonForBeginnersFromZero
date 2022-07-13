# ep6
# while loop

# import time
# while True:
#     print('While Loop')
#     time.sleep(5)

money = 1000
transfer = 10000

print('Check:', money < transfer)

while money < transfer:
    print('Please check your transfer value and input again')
    transfer = int(input('New transfer value: '))
    if transfer > 100000:
        print('Call out the manager for authorization')
        break

print('You can transfer if you are a VIP membership')

