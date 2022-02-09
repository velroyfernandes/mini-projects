import random 
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbol = "_*()[]{}<>@!#-?+$₩"

ans = lower_case + upper_case + numbers + symbol

length = 9
password="".join(random.sample(ans, length))
print("your password is", password)