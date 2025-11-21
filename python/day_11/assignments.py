import math

def area_of_circle(r):
  return math.pi * r * r
  
print(area_of_circle(5)) 


def add_all_nums(* args):
  total_sum = 0
  for value in args:
     if not isinstance(value, (int, float)):
        return f"Invalid input: '{value}' is not a number."
     total_sum+=value
  return total_sum
  
print(add_all_nums(11, 22, 33, 44.5))
print(add_all_nums(101, "k", 76)) 
