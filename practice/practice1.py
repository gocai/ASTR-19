import numpy as numpy

def PrintTable():
    x = numpy.linspace(0,2*numpy.pi,2000)
    sinx = numpy.sin(x)
    print(x)
    print(sinx)
def main():
    PrintTable()
if __name__ == "__main__":
    main()