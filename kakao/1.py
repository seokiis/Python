def solution(friends, gifts):
    #send, receive graph
    graph=[[0 for i in range(len(friends))]for j in range(len(friends))]

    #gift send count, receive count, send-receive count
    send_count=[[0,0,0] for i in range(len(friends))]

    #gift send
    for gift in gifts:
        gift=gift.split()
        graph[friends.index(gift[0])][friends.index(gift[1])]+=1
        send_count[friends.index(gift[0])][0]+=1
        send_count[friends.index(gift[1])][1]+=1

    for i in range(len(friends)):
        send_count[i][2]=send_count[i][0]-send_count[i][1]


    #prediect receive count 
    answer=[0 for i in range(len(friends))]
    #graph traversal
    for a in range(len(friends)):
        for b in range(len(friends)):
            # 선물 받은 기록이 있고, 값이 같지 않다면 선물을 더 많이 준 사람 count +1
            if a!=b and graph[a][b]!=graph[b][a]:
                if graph[a][b]>graph[b][a]:
                    answer[a]+=1
                else:
                    answer[b]+=1
            #선물 받은 기록이 없거나, 같은 수로 선물을 주고 받았다면 선물 지수로 비교
            elif a!=b and graph[a][b]==graph[b][a]:
                if send_count[a][2]>send_count[b][2]:
                    answer[a]+=1
                elif send_count[a][2]<send_count[b][2]:
                    answer[b]+=1
    for i in range(len(answer)):
        answer[i]=answer[i]//2
    
    return(max(answer))


                
                


            
solution(["muzi","ryan","frodo","neo"],["muzi frodo","muzi frodo","ryan muzi","ryan muzi","ryan muzi","frodo muzi","frodo ryan","neo muzi"])