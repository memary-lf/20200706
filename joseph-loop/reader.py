"""
    作者：LF
    功能：存放（类）TxtReader、CsvReader、ZipReader以及函数reader
    版本：3.0
    日期：21/07/2020
    问题描述：1.TxtReader、CsvReader、ZipReader三种类
               可完成对txt、csv、zip文件中玩家信息的读取，输出每一行的信息
               其中ZipReader可完成对zip中包含的指定的txt/csv文件进行每一行信息的输出。
             2.函数reader通过对三个类（迭代器）的返回信息进行处理，实现对三种文件读取
               得到的玩家信息进行输出格式统一，均为list(name+空格+sex+空格+age)
             3.对该版本不支持处理的数据类型完成错误收集
    3.0改进部分：1.类的命名更换为帕斯卡式(TxtReader、CsvReader、ZipReader)
                2.判断文件名后缀由path[-4:]改用为endswith()函数
                3.zipfile.ZipFile.open()使用with打开，以便处理无法关闭的情况
                4.将ZipReader类中传入的参数file删除，只保留path，
                  从而实现与TxtReader、CsvReader的接口相统一
                5.修改命名instance为all_reader_instance
                6.增加了部分测试案例，以确保得到尽可能准确的测试结果
                7.增加了父类Reader，来实现继承与多态
"""
import zipfile


class Reader:
    ext = None


class TxtReader(Reader):
    ext = ".txt"

    # 构造函数
    def __init__(self, path):
        self.path = path
        if self.path.endswith(".txt"):
            self.file = open(self.path)
        else:
            ex = Exception("TxtReader仅支持对txt文件的读取，请检查所选路径是否为txt文件")
            raise ex

    # 迭代部分
    def __iter__(self):
        for line in self.file:
            yield line.split()

    # 析构函数
    def __del__(self):
        self.file.close()


class CsvReader(Reader):
    ext = ".csv"

    # 构造函数
    def __init__(self, path):
        self.path = path
        if path.endswith(".csv"):
            self.file = open(self.path)
        else:
            ex = Exception("CsvReader仅支持对csv文件的读取，请检查所选路径是否为scv文件")
            raise ex

    # 迭代部分
    def __iter__(self):
        for line in self.file:
            yield line.split()

    # 析构函数
    def __del__(self):
        self.file.close()


class ZipReader(Reader):
    ext = ".zip"

    # 构造函数
    def __init__(self, path):
        self.path = path
        self.zip_path = self.path.split("/")[0] + ".zip"
        self.zip_file = zipfile.ZipFile(self.zip_path)

    # 迭代部分
    def __iter__(self):
        if self.path.endswith(".txt") or self.path.endswith(".csv"):
            with self.zip_file.open(self.path) as self.file:
                for line in self.file:
                    yield line.decode(encoding="UTF-8", errors="strict").split()
        else:
            ex = Exception("该版本仅支持对zip中的txt及csv文件的读取，请检查是否符合版本功能")
            raise ex

    # 析构函数
    def __del__(self):
        self.zip_file.close()


def reader(path):
    player_list = []
    for x in Reader.__subclasses__():
        if path.endswith(x.ext):
            if "/" in path:
                all_reader_instance = ZipReader(path)
            else:
                all_reader_instance = x(path)
    for i in all_reader_instance:
        player_name = i[0].strip(",")
        player_sex = i[1].strip(",")
        player_age = i[2].strip(",")
        player_list.append(player_name + " " + player_sex + " " + player_age)
    del all_reader_instance
    return player_list


if __name__ == "__main__":
    # 查看txt文件是否可以读取成功
    player_list = reader("player_information.txt")
    # print(player_list)
    assert len(player_list) == 5
    assert player_list[0].split()[2] == "10"
    assert player_list[2].split()[1] == "male"

    # 查看csv文件是否可以读取成功
    player_list = reader("player_information.csv")
    # print(player_list)
    assert len(player_list) == 6
    assert player_list[0].split()[2] == "10"
    assert player_list[2].split()[1] == "male"

    # 查看zip文件中的txt是否可以读取成功
    player_list = reader("player_information/player_information.txt")
    # print(player_list)
    assert len(player_list) == 5
    assert player_list[0].split()[2] == "10"
    assert player_list[2].split()[1] == "male"

    # 查看zip文件中的csv是否可以读取成功
    player_list = reader("player_information/player_information.csv")
    assert len(player_list) == 6
    assert player_list[0].split()[2] == "10"
    assert player_list[2].split()[1] == "male"
