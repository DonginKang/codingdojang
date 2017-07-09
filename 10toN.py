#-*- coding:utf-8 -*-

"""
라이브러리를 사용하지 말고 10진수를 n진수로 변환하는 프로그램을 작성하시오.. (단, n의 범위는 2 <= n <= 16)


2진수로 변환 : 23310 --> 111010012
8진수로 변환 : 23310 --> 3518
16진수로 변환 : 23310 --> E916

"""


#d_num = decimal number
#t_num = target number

def DecimalTo(d_num,t_num):

	dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
	s = ''

	if t_num > d_num:
		return d_num

 	while(d_num):

 		remainder = (d_num % t_num)
 		
 		if remainder >=10:
 			s = dic[remainder] + s 
 		else: 
			s = str(d_num%t_num) + s

		d_num = d_num/t_num

		if t_num > d_num:
			if d_num >=10:
				return dic[d_num] + s
			else:
				return str(d_num) + s

	return 0

print DecimalTo(10,3)