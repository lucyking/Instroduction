import sys
import re

class Alpha(object):
    def __init__(self):
        self.count = 0
    def file_reader(self):
        ret = list()
        with open(sys.argv[1], "r") as f:
            file_content = f.readlines()
        for line in file_content:
            cur_line = [x for x in re.split(r"[\s,]", line) if x]
            # print(cur_line)
            ret.append(cur_line)
        return ret

    def fx(self):
        fileBuff = self.file_reader()
        line_num, usr_num = fileBuff.pop(0)
        line_num = int(line_num)
        usr_num = int(usr_num)
        # print("usr_num>> ", usr_num)
        allReadyVisted= set()

        tmp = list()
        # print("----")
        ret = self.recursive(usr_num, tmp, 0 , fileBuff, allReadyVisted)
        # print(">>", tmp)
        allReadyVisted.clear()

    def recursive(self, user_number= 100, retList = list(), usr_index = 1, itemList = list(), allReadyVisted = set()):
        if usr_index== user_number:
            # print("solve>", retList)
            self.count += 1
            # allReadyVisted.clear()
            return retList
        # curLine = itemList[usr_index]
        for item in itemList[usr_index]:
            # todo need cancel the 2rd
            # if (item not in allReadyVisted) and (item not in retList):
            if item not in retList:
                retList.append(item)
                # allReadyVisted.add(item)
                self.recursive(user_number, retList, usr_index + 1, itemList, allReadyVisted)
                retList.pop(-1)
                # break



if __name__ == "__main__":
    A = Alpha()
    fileBuff = A.file_reader()
    A.fx()
    print(A.count)