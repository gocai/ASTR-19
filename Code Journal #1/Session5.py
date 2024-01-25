import numpy as np


def main():
    x = np.linspace(0,2*np.pi,1000)
    y = np.sin(x)
    for one,two in zip(x,y):
        print(f"x = {one}, sin(x) = {two}")
    
if __name__=="__main__":
    main()