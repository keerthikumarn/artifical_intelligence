import random
import string

def random_user_id():
  chars = string.ascii_lowercase + string.digits
  return ''.join(random.choice(chars) for _ in range(6))
  
print(random_user_id())


# print the rgb values
def generate_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


print(generate_rgb_color())
