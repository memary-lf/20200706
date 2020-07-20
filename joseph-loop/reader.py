"""
    作者：LF
    功能：存放（类）Txt_reader、Csv_reader、Zip_reader以及函数reader
    版本：2.0
    日期：19/07/2020
    问题描述：1.Txt_reader、Csv_reader、Zip_reader三种类
               可完成对txt、csv、zip文件中玩家信息的读取，输出每一行的信息
               其中Zip_reader可完成对zip中包含的指定的txt/csv文件进行每一行信息的输出。
             2.函数reader通过对三个类（迭代器）的返回信息进行处理，实现对三种文件读取
               得到的玩家信息进行输出格式统一，均为list(name+空格+sex+空格+age)
             3.对该版本不支持处理的数据类型完成错误收集
"""
import zipfile


class Txt_reader:
    # 构造函数
    def __init__(self, path):
        if path[-4:] == ".txt":
            self.path = path
            self.file = open(self.path)
        else:
            ex = Exception("Txt_reader仅支持对txt文件的读取，请检查所选路径是否为txt文件")
            raise ex

    # 迭代部分
    def __iter__(self):
        for line in self.file:
            yield line.split()

    # 析构函数
    def __del__(self):
        self.file.close()


class Csv_reader:
    # 构造函数
    def __init__(self, path):
        if path[-4:] == ".csv":
            self.path = path
            self.file = open(self.path)
        else:
            ex = Exception("Csv_reader仅支持对csv文件的读取，请检查所选路径是否为scv文件")
            raise ex

    # 迭代部分
    def __iter__(self):
        for line in self.file:
            yield line.split()

    # 析构函数
    def __del__(self):
        self.file.close()


class Zip_reader:
    # 构造函数
    def __init__(self, path, file):
        if path[-4:] == ".zip":
            self.path = path
            self.zip_file = zipfile.ZipFile(path)
            if file[-4:] == ".txt" or file[-4:] == ".csv":
                self.file = self.zip_file.open(file)
            else:
                ex = Exception("该版本仅支持对zip中的txt及csv文件的读取，请检查是否符合版本功能")
                raise ex
        else:
            ex = Exception("Zip_reader仅支持对zip文件的读取，请检查所选路径是否为zip文件")
            raise ex

    # 迭代部分
    def __iter__(self):
        for line in self.file:
            yield line.decode(encoding="UTF-8", errors="strict").split()

    # 析构函数
    def __del__(self):
        self.zip_file.close()


def reader(path):
    player_list = []
    if "/" in path:
        file = path
        path = path.split("/")[0] + ".zip"
        instance = Zip_reader(path, file)
    elif path[-4:] == ".txt":
        instance = Txt_reader(path)
    elif path[-4:] == ".csv":
        instance = Csv_reader(path)
    else:
        ex = Exception("reader函数仅支持对txt、csv及zip文件的读取")
        raise ex
    for i in instance:
        player_name = i[0].strip(",")
        player_sex = i[1].strip(",")
        player_age = i[2].strip(",")
        player_list.append(player_name + " " + player_sex + " " + player_age)
    del instance
    return player_list


if __name__ == "__main__":
    # 查看txt文件是否可以读取成功
    player_list = reader("player_information.txt")
    # print(player_list)
    assert len(player_list) == 5

    # 查看csv文件是否可以读取成功
    player_list = reader("player_information.csv")
    # print(player_list)
    assert len(player_list) == 6

    # 查看zip文件中的txt是否可以读取成功
    player_list = reader("player_information/player_information.txt")
    # print(player_list)
    assert len(player_list) == 5

    # 查看zip文件中的csv是否可以读取成功
    player_list = reader("player_information/player_information.csv")
    # print(player_list)
    assert len(player_list) == 6
