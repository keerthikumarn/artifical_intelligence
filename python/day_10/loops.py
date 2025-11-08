#while loop
print("starting with the basic while loop")
count = 0
while count < 5:
   print(count)
   count = count + 1
else:
    print(count)
    
    
# break statement
print("starting with break in while loop")
counter = 0
while counter < 5:
    print(counter)
    counter = counter + 1
    if counter == 2:
        print("break loop encountered")
        break
        
# continue statement
print("starting with continue in while loop")
counter1 = 0
while counter1 < 5:
    if counter1 == 3:
        counter1 = counter1 + 1
        continue
    print(counter1)
    counter1 = counter1 + 1
