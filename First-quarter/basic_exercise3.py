# 练习 3

"""
问题描述:
    如果将一句话作为一个字符串，那么这个字符串中必然会有空格（这里仅讨论英文），
比如"How are you."，但有的时候，会在两个单词之间多大一个空格。现在的任务是，
如果一个字符串中有连续的两个空格，请把它删除。
"""

string_two_spaces = "Life  is  short. I  use  python."
print(string_two_spaces)

string_lst = string_two_spaces.split(" ")
print(string_lst)

string_delete_extra_spaces = [x for x in string_lst if x != ""]
print(string_delete_extra_spaces)

string_one_spaces = " ".join(string_delete_extra_spaces)
print(string_one_spaces)