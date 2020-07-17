"""
    作者：LF
    功能：存放（类）Player，运用私有属性
    版本：2.0
    日期：17/07/2020
    问题描述：1.Player类的属性包括：name、sex、age
             2.输入的性别应为male/female，输入的年龄应为大于0的正整数
"""


class Player:
    def __init__(self, name, sex, age):
        "输入的name、sex、age均为字符串形式"
        self._name = name
        if sex == "male" or sex == "female":
            self._sex = sex
        else:
            raise ValueError("性别输入错误(male/female)")
        if age.isdigit() is True:
            if int(age) > 0:
                self._age = age
            else:
                raise ValueError("年龄输入错误(非正整数)") 
        else:
            raise ValueError("年龄输入错误(非整数)")

    @property
    def name(self):
        return self._name

    @property
    def sex(self):
        return self._sex

    @property
    def age(self):
        return self._age

    def __str__(self):
        return "Name:{} Gender:{} Age:{}".format(self.name, self.sex, self.age)


if __name__ == "__main__":
    player_instance = Player(1, "female", "3")
    # 测试name
    assert player_instance.name == 1
    # 测试sex
    assert player_instance.sex == "female"
    # 测试age
    assert player_instance.age == "3"
