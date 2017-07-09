#-*- coding:utf-8 -*-

"""
라이브러리를 사용하지 말고 10진수를 n진수로 변환하는 프로그램을 작성하시오.. (단, n의 범위는 2 <= n <= 16)


2진수로 변환 : 23310 --> 111010012
8진수로 변환 : 23310 --> 3518
16진수로 변환 : 23310 --> E916

"""

def DecimalTo(dec,base):

	T = '0123456789ABCDEF'
	s = ''

	if dec == 0:           # 처음 0 을 입력 받았을때
		return T[0]

	if base > dec:         # 처음 10진수 값이 base 보다 작을때  
		return T[dec]

 	while(dec):
		s = T[dec%base] + s
		
		dec = dec/base
		if base > dec:    
			return T[dec] + s


print DecimalTo(1500,16)