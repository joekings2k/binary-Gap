
from posixpath import split


def solution(N):
    N = bin(N) [2:]
    print(N)
    gap = 0 
    maxgap =0
    for i in N:
        if int(i)== 0:
            gap+=1 
        elif int(i) == 1:
            maxgap = max(gap,maxgap)
            gap = 0
        
    return maxgap
   
    









print(solution(1))