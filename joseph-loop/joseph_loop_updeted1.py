"""
    作者：LF
    功能：利用python解决约瑟夫环问题,面向对象编程
    版本：2.0
    日期：13/07/2020
    问题描述：N个人围成一圈，第一个人从1开始报数，报M的将被杀掉，下一个人接着从1开始报。
             如此反复，直至无人生还。
    新增条件：这N个人都具有姓名、性别、年龄等特征。
"""
"""
    变量含义：
    input_list：输入列表/需要处理的列表
    start_num: 新一轮报数的起始位置 = 前一轮出局人的位置
    step: 步长
    output_list: 出局顺序存放处
"""


def joseph_circle(input_list, start_num=0, step=3):
    "约瑟夫环，返回出局人员列表"
    output_list = []
    for i in range(len(input_list)):
        start_num = (start_num + step - 1) % len(input_list)
        output_list.append(input_list[start_num])
        input_list.pop(start_num)
    return output_list


if __name__ == "__main__":

    class Player:
        def __init__(self, name):
            player_gender = {
                "google": "man",
                "facebook": "woman",
                "github": "man",
                "baidu": "woman",
                "alibaba": "woman",
            }
            player_age = {
                "google": 10,
                "facebook": 20,
                "github": 30,
                "baidu": 40,
                "alibaba": 50,
            }
            self.name = name
            self.gender = player_gender[name]
            self.age = player_age[name]

    player_name = ["google", "facebook", "github", "baidu", "alibaba"]
    start_num = int(input("请输入start_num的值："))
    step = int(input("请输入step的值："))
    palyer_out_list = joseph_circle(player_name, start_num, step)
    print("出局顺序为："+str(palyer_out_list))

    print("出局的玩家依次为：")
    for i in palyer_out_list:
        player_information = Player(i)
        print(
            str(player_information.name)
            + ": "
            + str(player_information.gender)
            + ", "
            + str(player_information.age)
        )
