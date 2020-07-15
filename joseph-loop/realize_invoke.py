"""
    作者：LF
    功能：用于实现对约瑟夫环(类)、Player(类)、读取信息函数、玩家信息.txt等的调用
    版本：1.0
    日期：14/07/2020
    问题描述：1.约瑟夫环：N个人围成一圈，第一个人从1开始报数，报M的将被杀掉，下一个人接着从1开始报。
               如此反复，直至无人生还；（以玩家、出局等字样代替）。
             2.这N个人都具有姓名、性别、年龄等特征;使用类进行调用。
             3.这些信息保存在txt文件中。
"""

# 调用函数、类、玩家信息
from joseph_circle_class import Joseph_circle
from read_information import read_player_information
from palyer_class import Player

if __name__ == "__main__":
    try:
        player_information_list = read_player_information("player_information.txt")
    except IOError:
        print("Error:读取玩家信息失败")
    else:
        joseph_instance = Joseph_circle()
        player_list = joseph_instance.append(player_information_list)
        player_length = joseph_instance.get_length()
        print("玩家总数量为：" + str(player_length))

        start_num = int(input("请输入start_num的值(整数）："))
        step = int(input("请输入step的值（整数）："))
        palyer_out_list = joseph_instance.get_out_players(start_num, step)
        print("出局顺序依次为：")
        for i in palyer_out_list:
            player_name = i.split()[0]
            player_sex = i.split()[1]
            player_age = i.split()[2]
            player_information = Player(player_name, player_sex, player_age)
            print(
                str(player_information.name)
                + ": "
                + str(player_information.sex)
                + ", "
                + str(player_information.age)
            )

        last_player = joseph_instance.get_last_player()
        print("最后一名出局的玩家为："+str(last_player))