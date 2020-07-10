# 练习 2

"""
问题描述:
 按照下面的要求实现对列表的操作：
    1.产生一个列表，其中有 40 个元素，每个元素是 0 到 100 的一个随机整数
    2.如果这个列表中的数据代表着某个班级 40 人的分数，请计算成绩低于平均分的学生人数，并输出
    3.对上面的列表元素从大到小排序
"""


def generating_scores(total_num, max_score=100):
    """
    This is a function used to generate a total_num number of grades.
    """
    return [random.randint(0, max_score) for i in range(total_num)]


def select_below_average(input_list):
    """
    This is a function used to select out below-average grades.
    """
    input_list_length = len(input_list)
    sum_up = float(sum(input_list))
    average = sum_up / input_list_length
    return [x for x in input_list if x < average]


import random

# total_num = input('The total number is: ')
total_num = 40

scores = generating_scores(total_num)
print("The randomly generated results are: " + str(scores))

scores_below_average = select_below_average(scores)
print("Below-average results are: " + str(scores_below_average))
numbers_below_average = len(scores_below_average)
print(
    "The number of students with below average scores is " + str(numbers_below_average)
)

ascending = True
scores_ascending = sorted(scores, reverse=ascending)
print(
    "The results produced in descending order of magnitude are " + str(scores_ascending)
)
