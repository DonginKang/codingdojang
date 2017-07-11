#-*- coding:utf-8 -*-


"""
완전수 구하기  (take perfect numbers from natural numbers)

자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다. 예를 들면, 6과 28은 완전수이다. 6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14 // 1,2,4,7,14는 각각 28의 약수

입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하라.

"""

def Perfect_Number(N):

	for i in range(1,N+1):
		total = 0
		
		for j in range(1,i/2+1):

			if i % j == 0:
				total += j

		if total == i:
			yield i

print list(Perfect_Number(100))
