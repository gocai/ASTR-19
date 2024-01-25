import numpy as np

def main():
    for i in range(1001):
        x = i / 500.0 * np.pi
        y = np.sin(x)
        print(f"sin(x) = {y} x = {x} i = {i}")
if __name__=="__main__":
    main()