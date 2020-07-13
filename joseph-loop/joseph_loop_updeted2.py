"""
    作者：LF
    功能：利用python解决约瑟夫环问题,面向对象编程
    版本：3.0
    日期：13/07/2020
    问题描述：N个人围成一圈，第一个人从1开始报数，报M的将被杀掉，下一个人接着从1开始报。
             如此反复，直至无人生还。
    新增条件：1.这N个人都具有姓名、性别、年龄等特征;
             2.这些信息保存在txt文件中。
"""


def joseph_circle(input_list, start_num=0, step=3):
    "约瑟夫环，返回出局人员列表"
    output_list = []
    for i in range(len(input_list)):
        start_num = (start_num + step - 1) % len(input_list)
        output_list.append(input_list[start_num])
        input_list.pop(start_num)
    return output_list


def read_player_information():
    player_information_file = open("player_information.txt")
    player_information = []
    for line in player_information_file:
        player_information.append(line.strip("\n"))
    player_information_file.close()
    return player_information


if __name__ == "__main__":
    player_information = read_player_information()
    start_num = int(input("请输入start_num的值："))
    step = int(input("请输入step的值："))
    palyer_out_list = joseph_circle(player_information, start_num, step)
    print("出局顺序为：")
    for i in palyer_out_list:
        print(str(i.split()[0]) + ": " + str(i.split()[1]) + ", " + str(i.split()[2]))