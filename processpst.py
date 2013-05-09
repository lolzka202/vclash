__author__ = 'User'

from PSTTool import PSTTool,NewTool

def main():
    print("We got started")

    tool = PSTTool.PSTTool("Kelvin")
    newtool = NewTool.NewTool("New Tool")
    tool.runme()

if __name__ == "__main__":

    main()
