from posixpath import split
from tkinter import N


def solution (N):
    N =bin(N)[2:]
    j = N.split("1")

    
    if j[-1]!= "":
        j.pop()
        max_num = 0
        for i in j:
            noOfZero= i.count("0")
            if noOfZero > max_num:
                max_num =noOfZero
        return max_num, N

print(solution(50))


