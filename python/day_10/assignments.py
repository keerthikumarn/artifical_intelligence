# Iterate 0 to 10 using for loop, do the same using for loop.

for num in range(0, 11):
    print(num)
    
# Iterate 0 to 10 using for loop, do the same using while loop.
num = 0
while num <= 10:
    print(num)
    num+=1
    
for num in range(1, 8):
    print("#" * num)
    
for _ in range(8):
    print("# " * 8)
    
for num in range(0, 11):
    print(f"{num} x {num} = {num * num}")
