"""
    作者：LF
    功能：利用python解决约瑟夫环问题
    版本：1.0
    日期：10/07/2020
    问题描述：N个人围成一圈，第一个人从1开始报数，报M的将被杀掉，下一个人接着从1开始报。如此反复，直至无人生还。
"""


def joseph_circle(n, m):
    if n < 1:
        return -1
    k = 0
    for i in range(2, n + 1):
        k = (k + m) % i
    return k + 1


if __name__ == "__main__":
    total_num = int(input("Please enter the total number of people: "))
    killed_num = int(input("Please enter the number of the person you killed: "))
    final_num = joseph_circle(total_num, killed_num)
    print("The number of the last person killed was: " + str(final_num))
