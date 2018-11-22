import sys
import re


class A(object):
    def __init__(self):
        self.boyRefList = dict()
        self.girlRefList = dict()
        for i in range(0, 6,1):
            self.boyRefList[i] = set()
            self.girlRefList[i] = set()


    def judge(self, name):
        ret = 0
        s = self.features(name)

        # if s["first-letter"] in self.girlRefList[0]:
        #     ret -=1
        # if s["first-letter"] in self.boyRefList[0]:
        #     ret +=1

        if s["first2-letters"] in self.girlRefList[1]:
            ret -=1
        if s["first2-letters"] in self.boyRefList[1]:
            ret +=1

        if s["first3-letters"] in self.girlRefList[2]:
            ret -=1
        if s["first3-letters"] in self.boyRefList[2]:
            ret +=1

        # if s["last-letter"] in self.girlRefList[3]:
        #     ret -=1
        # if s["last-letter"] in self.boyRefList[3]:
        #     ret +=1

        if s["last2-letters"] in self.girlRefList[4]:
            ret -=1
        if s["last2-letters"] in self.boyRefList[4]:
            ret +=1

        if s["last3-letters"] in self.girlRefList[5]:
            ret -=1
        if s["last3-letters"] in self.boyRefList[5]:
            ret +=1

        print(ret)
        if(ret>0):
            return "male"
        elif(ret<0):
            return "female"
        else:
            return "unknow"

    def getListItemSize(self, K, listSet):
        for i in range(0, K, 1):
            print(len(listSet[i]))


    def readInput(self):
        with open(sys.argv[1], "r") as f:
            fileContent = f.readlines()
        return fileContent

    def split(self, line):
        name, gender= re.split(r",", line)
        # print(name, gender)
        return name, gender


    def train(self, gender, name):
        if gender == "female":
            # self.girlRefList[0].add(name[0])
            self.girlRefList[1].add(name[0:2])
            self.girlRefList[2].add(name[0:3])
            # self.girlRefList[3].add(name[-1])
            self.girlRefList[4].add(name[-2:])
            self.girlRefList[5].add(name[-3:])
        else:
            # self.boyRefList[0].add(name[0])
            self.boyRefList[1].add(name[0:2])
            self.boyRefList[2].add(name[0:3])
            # self.boyRefList[3].add(name[-1])
            self.boyRefList[4].add(name[-2:])
            self.boyRefList[5].add(name[-3:])

    def features(self, name):
        # name = name.lower()
        # self.boyRefList[0] = name[0]
        return {
            'first-letter': name[0],  # First letter
            'first2-letters': name[0:2],  # First 2 letters
            'first3-letters': name[0:3],  # First 3 letters
            'last-letter': name[-1],
            'last2-letters': name[-2:],
            'last3-letters': name[-3:],
        }

if __name__ == '__main__':
    Solve = A()
    print(Solve.boyRefList)
    print(Solve.girlRefList)
    content = Solve.readInput()
    # i = 1
    for line in content:
        name, gender = Solve.split(line)
        gender= gender.replace("\n", '')
        Solve.train(gender, name)
        # i+=1
        # print(Solve.getListItemSize(6, Solve.boyRefList))
        # print(Solve.boyRefList)
        # print(Solve.getListItemSize(6, Solve.girlRefList))
        # print(Solve.girlRefList)
    with open(sys.argv[2], "r") as f:
            fileContent = f.readlines()
    for name in fileContent:
        print(name,',' , Solve.judge(name))


