
import random

code_list = []

for i in range(4):
  statu = random.randint(1,3)
	if statu == 1:
		a = random.randint(65,90)
		random_uppercase = chr(a)
		code_list.append(random_uppercase)

	elif statu == 2:
		b = random.randint(97,122)
		random_lowercase = chr(b)
		code_list.append(random_lowercase)

	elif statu == 3:
		random_num = random.randint(0,9)
		code_list.append(str(random_num))

verification_code = ''.join(code_list)
print(verification_code)
