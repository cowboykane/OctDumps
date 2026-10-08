# pass_generator yarp

import string, random

letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

combined = letters + numbers + punctuation

password_list = random.sample(combined, k=20)
password = "".join(password_list)

print(password)