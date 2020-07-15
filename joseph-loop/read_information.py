"""
    作者：LF
    功能：从存放玩家信息的txt文件中读取相关信息，并转化成相应的列表返回。
    版本：1.0
    日期：14/07/2020
"""
def read_player_information(file):
    with open(file) as player_information_file:            #使用with打开文件以避免关闭异常的情况
        player_information = []
        for line in player_information_file:
            player_information.append(line.strip("\n"))    #删除行尾的换行
        return player_information                          #txt中的每一行为列表的一个元素

if __name__ == "__main__":
    player_information = read_player_information("player_information.txt")
    print(player_information)
    