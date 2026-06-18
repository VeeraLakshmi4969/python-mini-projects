import time


my_time =  int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours}:{minutes}:{seconds}")
    # one hour contain 3600 seconds
    time.sleep(1)
    # If we want to include days also we use hours = (x/3600) % 24


print("Time is over!")

# for x in range(0,my_time):
# we may also use(reverse order) for x in reversed(range(0,my_time)):
# OR for x in range(my_time,0,-1):