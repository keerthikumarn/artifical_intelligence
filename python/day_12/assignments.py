import random
import string

def random_user_id():
  chars = string.ascii_lowercase + string.digits
  return ''.join(random.choice(chars) for _ in range(6))
  
print(random_user_id())
