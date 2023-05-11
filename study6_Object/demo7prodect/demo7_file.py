# 这边是抽象方法 去读取text本以及json文本的
import json
from typing import List

from demo7_date import Record


# 做一个顶层接口
# 抽象类 文件读取
class FileReader:
    def read_date(self) -> List[Record]:
        pass


class Text_read(FileReader):
    # 定义成员变量 路径
    def __init__(self, path):
        self.path = path

    def read_date(self) -> List[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: List[Record] = []
        for x in f.readlines():
            x = x.strip()
            date_list = x.split(",")
            record = Record(date_list[0], date_list[1], int(date_list[2]), date_list[3])
            record_list.append(record)
        f.close()
        return record_list


class Json_read(FileReader):
    # 路径
    def __init__(self, path):
        self.path = path

    def read_date(self) -> List[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: List[Record] = []
        for x in f.readlines():
            date_dict = json.loads(x)
            record = Record(date_dict["date"], date_dict["order_id"], int(date_dict["money"]), date_dict["province"])
            record_list.append(record)
        f.close()
        return record_list


if __name__ == '__main__':
    # text_read = Text_read("F:\workspace\python-study/2011年1月销售数据.txt")
    # list = text_read.read_date()
    # for x in list:
    #     print(x)

    json_read = Json_read("F:\workspace\python-study/2011年2月销售数据JSON.txt")
    j_list = json_read.read_date()
    for x in j_list:
        print(x)