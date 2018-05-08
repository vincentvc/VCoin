class Test:
    share = 2

    def __init__(self,x):
        self.x = x

    def standard(self):
        print(self.x)

    @staticmethod
    def static():
        print(Test.share)

    @classmethod
    def classMethod(cls):
        classShare = 100
        print(Test.share)
        print(classShare)

test = Test(3)
test2 = Test(2)


test.standard()
test.classMethod()
test.static()

Test.share = Test.share + 1
Test.classSSSSSS



















