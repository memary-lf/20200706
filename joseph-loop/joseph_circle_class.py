"""
    作者：LF
    功能：存放（类）约瑟夫环
    版本：1.0
    日期：14/07/2020
"""
"""
    约瑟夫环（类），提供的方法有：
    1.获取类的名字
    2.增加玩家列表
    3.获取初始约瑟夫环长度
    4.删除指定位置玩家的数据
    5.获取出局玩家的顺序列表
    6.获取最后一个出局的玩家
    7.迭代玩家方法
"""


class Joseph_circle:
    def __init__(self):
        self._name = Joseph_circle
        self.input_players_list = []
        self.out_players_list = []

    @property
    def get_name(self):
        """获取类的名字"""
        return self._name

    def append(self, player_list):
        """增加玩家列表"""
        for i in player_list:
            self.input_players_list.append(i)
        return self.input_players_list

    def get_length(self):
        """获取初始约瑟夫环长度"""
        input_player_length = len(self.input_players_list)
        return input_player_length

    def pop(self, index):
        """删除指定位置玩家的数据"""
        if self.get_length() == 0:
            raise Exception("预删除列表为空，无法进行删除操作")
        else:
            self.input_players_list.pop(index)
        return self.input_players_list

    def get_out_players(self, start_num=0, step=1):
        """获取出局玩家的顺序列表"""
        if step < 0:
            raise IndexError("step < 0")
        else: 
            input_list = self.input_players_list
            for i in range(len(input_list)):
                start_num = (start_num + step - 1) % len(input_list)
                self.out_players_list.append(input_list[start_num])
                input_list.pop(start_num)
            return self.out_players_list

    def get_last_player(self):
        """获取最后一个出局的玩家"""
        last_player = self.out_players_list[-1]
        return last_player

    def __iter__(self):
        return self

    def __next__(self):
        if self.get_length > 0:
            return self.input_players_list
        else:
            raise StopIteration()

if __name__ == "__main__":
    # 测试get_name
    joseph_instance = Joseph_circle()
    assert joseph_instance.get_name == Joseph_circle

    # 测试append
    joseph_instance = Joseph_circle()
    test_list = [1, 2, 3]
    player_list = joseph_instance.append(test_list)
    assert player_list == test_list

    # 测试get_length
    joseph_instance = Joseph_circle()
    test_list = [1, 2, 3]
    player_list = joseph_instance.append(test_list)
    assert joseph_instance.get_length() == 3

    # 测试pop，length>0
    joseph_instance = Joseph_circle()
    test_list = [1, 2, 3]
    player_list = joseph_instance.append(test_list)
    input_player_length = joseph_instance.get_length()
    pop_player_list = joseph_instance.pop(1)
    assert pop_player_list == [1, 3]

    # 测试pop,length==0
    # joseph_instance = Joseph_circle()
    # test_list = []
    # player_list = joseph_instance.append(test_list)
    # input_player_length = joseph_instance.get_length()
    # pop_player_list = joseph_instance.pop(1)

    # 测试get_out_players
    joseph_instance = Joseph_circle()
    test_list = [1, 2, 3]
    start_num = 0
    step = 2
    expect_list = [2, 1, 3]
    input_list = joseph_instance.append(test_list)
    test_joseph_return = joseph_instance.get_out_players(start_num, step)
    assert test_joseph_return == expect_list

    # 测试get_last_player
    joseph_instance = Joseph_circle()
    test_list = [1, 2, 3]
    start_num = 0
    step = 2
    input_list = joseph_instance.append(test_list)
    test_joseph_return = joseph_instance.get_out_players(start_num, step)
    assert joseph_instance.get_last_player() == 3
