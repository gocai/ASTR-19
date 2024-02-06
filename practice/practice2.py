class Yes:
    def __init__(self,one,two,three):
        self.one = 0.0
        self.two = True
        self.three = False
def PrintVals(x):
    print(x.one)
    print(x.two)
    print(x.three)
def main():
    x = Yes(1,2,3)
    PrintVals(x)
if __name__ == "__main__":
    main()