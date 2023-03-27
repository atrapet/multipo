import random
import time

question_number = 10
sleep_time = 3
results = {}

for x in range(question_number):
    number_1=random.randint(0,10)
    number_2=random.randint(0,10)
    results[x] = number_1*number_2
    print(str(number_1)+" X "+str(number_2))
    time.sleep(sleep_time)  

print("Et voici les résultats!")

time.sleep(sleep_time)  

for x in range(question_number):
    print(results[x])
