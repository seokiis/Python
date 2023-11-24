def solution(survey, choices):
    array=[{'R':0,'T':0},{'F':0,'C':0},{'M':0,'J':0},{'A':0,'N':0}]

    for i in range(len(survey)):
        if(survey[i]=="RT" or survey[i]=="TR"):
            if(choices[i]>4): #동의(두번째 원소)
                array[0][survey[i][1]]+=choices[i]-4
            else:
                array[0][survey[i][0]]+=4-choices[i]

        elif(survey[i]=="FC" or survey[i]=="CF"):
            if(choices[i]>4): #동의(두번째 원소)
                array[1][survey[i][1]]+=choices[i]-4
            else:
                array[1][survey[i][0]]+=4-choices[i]

        elif(survey[i]=="MJ" or survey[i]=="JM"):
            if(choices[i]>4): #동의(두번째 원소)
                array[2][survey[i][1]]+=choices[i]-4
            else:
                array[2][survey[i][0]]+=4-choices[i]

        elif(survey[i]=="AN" or survey[i]=="NA"):
            if(choices[i]>4): #동의(두번째 원소)
                array[3][survey[i][1]]+=choices[i]-4
            else:
                array[3][survey[i][0]]+=4-choices[i]
                
    answer=''
    answer+= 'T' if array[0]['T']>array[0]['R'] else 'R'
    answer+= 'F' if array[1]['F']>array[1]['C'] else 'C'
    answer+= 'M' if array[2]['M']>array[2]['J'] else 'J'
    answer+= 'N' if array[3]['N']>array[3]['A'] else 'A'
      
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))