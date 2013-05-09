__author__ = 'User'


class PSTTool(object):
    def __init__(self, pstfile):
        super(PSTTool, self).__init__()

        self.filename = pstfile
        self.someVar = 12


    def openFile(self):
        """
        Open the file specified in the constructor

        Use the python pst module to open the pst file
        """

        pass

    def getEmailAddress(self):
        """
        Comment block
        """
        pass


    def runme(self):
        print("Param 1 is %s" % self.p1)
        print("someVar is %d" % self.someVar)
        print("All vars are %s and %d" % (self.p1, self.someVar))


def testTool():
    print("Testing")

    tool = PSTTool("Kelvin")
    tool.runme()


if __name__ == "__main__":
    testTool()
