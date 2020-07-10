# 练习 4

"""
问题描述:
   计算斐波那契数列n=100的值
"""
a = 1
b = 1
n = 100

for i in range(n - 1):
    a, b = b, a + b
print(a)