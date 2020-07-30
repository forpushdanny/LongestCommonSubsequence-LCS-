# coding=utf-8

'''
    109 資訊學分班作業 
    1. 測試資料檔test4.txt輸入字串
    2. 設計一個程式，利用dynamic programming演算法找出兩個字串的LCS
    3. 輸入格式：
          從鍵盤輸入兩個字串
    4. 輸出LCS與表格
    5. 範例：
         bacad
         accbadcb
       螢幕輸出
         acad
'''

def input_data():
    input_data_1 = input('請輸入字串1：') 
    input_data_1.strip()
    print()
    input_data_2 = input('請輸入字串2：') 
    input_data_2.strip()
    return input_data_1, input_data_2
    

def lcs(data_1, data_2):
    len_a1= len(data_1)+1
    len_a2= len(data_2)+1
    #optiaml_array 紀錄lcs陣列的值 
    optiaml_array=[[0 for i in range(0, len_a2)] for j in range(0, len_a1)]
    #direction_array 紀錄 陣列值的方向
    direction_array=[[0 for i in range(0, len_a2)] for j in range(0, len_a1)]

    # LCS　開始
    for i in range(1, len_a1):
        for j in range(1, len_a2):
            if data_1[i-1]==data_2[j-1]:
                optiaml_array[i][j]=optiaml_array[i-1][j-1]+1
                direction_array[i][j]=0
            elif optiaml_array[i][j-1]>=optiaml_array[i-1][j]:
                optiaml_array[i][j]=optiaml_array[i][j-1]
                direction_array[i][j]=1
            else:
                optiaml_array[i][j]=optiaml_array[i-1][j]
                direction_array[i][j]=2
    i=len(data_1)
    j=len(data_2)
    lcs_result=''

    while i>0 and j>0:
        if direction_array[i][j]==0:
            lcs_result = data_1[i-1] + lcs_result
            i-=1
            j-=1
        elif direction_array[i][j]==2:
            i-=1
        else:
            j-=1
    
    return  lcs_result, optiaml_array

def lcs_test():
    data_1, data_2 = input_data()
    
    lcs_result, optiaml_array = lcs(data_1, data_2)
    
    output(data_1, data_2, lcs_result, optiaml_array)
    
def output(data_1, data_2, lcs_result, optiaml_array):
    print('你輸入的字串1：',data_1)
    print('你輸入的字串2：',data_2)
    print('LCS 字串：',lcs_result)
    print('LCS 陣列如下：')
    for i in range(1, len(data_1)+1):
        for j in range(1, len(data_2)+1):
            print('{}'.format(optiaml_array[i][j]), end=' ')
        print()
    


if __name__ == "__main__":
    lcs_test()
