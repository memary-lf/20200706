"""
    作者：LF
    功能：存放（类）Reader
    版本：1.0
    日期：17/07/2020
    问题描述：1.Reader中包含txt_reader、csv_reader、zip_reader三种方法def，
               可完成对txt、csv、zip文件中玩家信息的读取，
               其中zip_reader可完成对zip中包含的第一个txt/csv文件进行玩家信息读取，且只对一个文件进行读取。
             2.对三种文件读取得到的玩家列表进行输出格式统一，均为list(name+空格+sex+空格+age)
             3.对该版本不支持处理的数据类型完成错误收集
"""
import csv
import zipfile


class Reader:
    def __init__(self):
        self.player_list = []

    def txt_reader(self, path):
        """完成对txt文件中玩家信息的读取"""
        if path[-4:] == ".txt":
            with open(path) as file_txt:
                for line in file_txt:
                    self.player_list.append(line.strip("\n"))
                return self.player_list
        else:
            ex = Exception("txt_reader仅支持对txt文件的读取，请检查所选路径是否为txt文件")
            raise ex

    def csv_reader(self, path):
        """完成对csv文件中玩家信息的读取"""
        if path[-4:] == ".csv":
            with open(path) as file_csv:
                file_csv_read = csv.reader(file_csv)
                for i in file_csv_read:
                    player_name = i[0]
                    player_sex = i[1]
                    player_age = i[2]
                    self.player_list.append(str(player_name + player_sex + player_age))
                return self.player_list
        else:
            ex = Exception("csv_reader仅支持对csv文件的读取，请检查所选路径是否为scv文件")
            raise ex

    def zip_reader(self, path):
        """完成对zip文件中玩家信息的读取"""
        if path[-4:] == ".zip":
            with zipfile.ZipFile(path) as file_zip:
                self.file_zip_list = file_zip.namelist()
                for k in self.file_zip_list:  # 只读取第一个（csv/txt）文件内容
                    if k[-3:] == "csv":
                        return self.csv_reader(k)
                    elif k[-3:] == "txt":
                        return self.txt_reader(k)
                ex = Exception("该版本仅支持对zip中的txt及csv文件的读取，请检查是否符合版本功能")
                raise ex
        else:
            ex = Exception("zip_reader仅支持对zip文件的读取，请检查所选路径是否为zip文件")
            raise ex


if __name__ == "__main__":
    # 查看txt文件是否可以读取成功
    reader_instance = Reader()
    out_player_information = reader_instance.txt_reader("player_information.txt")
    print("从txt文件中读取的玩家信息为：\n" + str(out_player_information))

    # 查看csv文件是否可以读取成功
    reader_instance = Reader()
    out_player_information = reader_instance.csv_reader("player_information.csv")
    # print("压缩文件中储存的文件分别为：\n"+str(reader_instance.file_zip_list))
    print("从csv中读取的玩家信息为：\n" + str(out_player_information))

    # 查看zip文件是否可以读取成功
    reader_instance = Reader()
    out_player_information = reader_instance.zip_reader("player_information.zip")
    print("压缩文件中储存的文件分别为：\n" + str(reader_instance.file_zip_list))
    print("从zip中读取的玩家信息为：\n" + str(out_player_information))