__author__ = 'User'


class PSTTool(object):

    def __init__(self,param1):
        super(PSTTool,self).__init__()

        self.someVar = 12
        self.p1 = param1

    def runme(self):

        print("Param 1 is %s" % self.p1)
        print("someVar is %d" % self.someVar)
        print("All vars are %s and %d" % (self.p1,self.someVar))
