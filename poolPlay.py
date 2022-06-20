from math import *
import numpy as np
import sys
import os
import multiprocessing
from multiprocessing import Pool
from DTW_up import*
import time

# 허밍 파일의 데이터 읽어오기
def selectHum(num):
    if num == 1:
        f = open("C:/Algorithm/humming_data/1782_humming1.txt","r")

        Hum_lines = f.readlines()
        Hum = list(map(int,Hum_lines))

        f.close()   

        return Hum

    elif num == 2:
        f = open("C:/Algorithm/humming_data/1197_humming2.txt","r")

        Hum_lines = f.readlines()
        Hum = list(map(int,Hum_lines))

        f.close()   

        return Hum

    elif num == 3:

        Hum = []

        f = open("C:/Algorithm/humming_data/0714_humming3.txt","r")

        Hum_lines = f.readlines()
        for i in range(0,len(Hum_lines)):
            try:
                Hum.append(int(Hum_lines[i]))
            except ValueError:
                pass
        f.close()

        return Hum 

    elif num == 4:
        f = open("C:/Algorithm/humming_data/0362_humming4.txt","r")

        Hum_lines = f.readlines()
        Hum = list(map(int,Hum_lines))

        f.close() 

        return Hum

        
# 노래 파일 비교하기

def musicCompare(Hum, result_dict, music):
    folderpath = r"C:/Algorithm/music_data" 
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    best = sys.maxsize
    with open(filepaths[music], 'r') as f:
        data_lines = f.readlines()
        one_dataResult_list=[]
        if len(data_lines) >= len(Hum):
            for k in range(0,len(data_lines)-len(Hum)+1,10):
                one_part = data_lines[k:k+len(Hum)]
                one_part = list(map(int,one_part))

                A, B = np.array(Hum), np.array(one_part)
                cost, best = DTW(A,B,best)
                
                print(filepaths[music])
                print(cost)
                print("베스트 : ",best)
                one_dataResult_list.append(cost)

            one_dataResult = min(one_dataResult_list)
            result_dict[one_dataResult] = filepaths[music]
        else:
            pass      

def main(Hum):
    manager = multiprocessing.Manager()
    result_dict=manager.dict()
    pool = multiprocessing.Pool(processes=10)
    pool.starmap(musicCompare, [(Hum, result_dict, music) for music in range(0,100)])
    pool.close()
    pool.join()

    return result_dict


if __name__ == '__main__':    
    num = int(input("허밍을 고르세요. (1~4) "))
    Hum = selectHum(num)
    start = time.time()

    result = main(Hum)
    min_distance = min(result.keys())
    fileName = result[min_distance]
    print("가장 비슷한 노래 : {} / DTW : {} ".format(fileName,min_distance))

    simular=[]
    for _ in range(5):
        simular_distance = min(result.keys())
        fileName = result[simular_distance]
        simular.append(fileName)
        del result[simular_distance]
    print("비슷한 5 곡 : ", simular)

    print("걸린시간 : ",time.time()-start)