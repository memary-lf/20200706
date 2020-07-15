"""
    作者：LF
    功能：存放（类）Player，运用私有属性
    版本：1.0
    日期：14/07/2020
    问题描述：Player类的属性包括：name、sex、age
"""


class Player:
    def __init__(self, name, sex, age):
        self._name = name               #属性私有化
        self._sex = sex
        self._age = age

    @property                           #实现对私有属性的调用
    def name(self):
        return self._name

    @property
    def sex(self):
        return self._sex

    @property
    def age(self):
        return self._age


if __name__ == "__main__":
    player_instance = Player(1, 2, 3)
    #测试name
    assert player_instance.name == 1
    #测试sex
    assert player_instance.sex == 2
    #测试age
    assert player_instance.age == 3
