from math import *
import numpy as np
import sys

def DTW(A, B, best, d = lambda x,y: abs(x-y)):
    # 전체 행렬 M X N 만들기 (각각의 값 max) 
    A, B = np.array(A), np.array(B)
    M, N = len(A), len(B)
    cost = sys.maxsize * np.ones((M, N))
    w=[0]

    # A에 대한 첫번째 줄 만들기
    cost[0, 0] = d(A[0], B[0])
    for i in range(1, M):
        cost[i, 0] = cost[i-1, 0] + d(A[i], B[0])

    # B에 대한 첫번째 줄 만들기
    for j in range(1, N):
        cost[0, j] = cost[0, j-1] + d(A[0], B[j])
    
    # 나머지 행렬 채우기
    for i in range(1, M): 
        if min(w) < best: 
            w=[] 
            for j in range(1, N):
                choices = cost[i - 1, j - 1], cost[i, j-1], cost[i-1, j]
                cost[i, j] = min(choices) + d(A[i], B[j])
                q = cost[i,j]
                w.append(q)
        else:           
            cost[-1,-1] = sys.maxsize
            return cost[-1,-1], best

    if best > cost[-1,-1]:
        best = cost[-1,-1]

    #마지막 값 출력
    return cost[-1, -1], best

