#가장 거리가 먼 집부터 배달/수거를 하자!
#가는 방향으로 배달, 오는 방향에서 수거를 하면 배달과 수거가 분리된다.

def solution(cap,n,deliveries,pickups):
    current_delivery=0
    current_pickup=0
    total_distance=0
    last_stop=n

    for stop in range(last_stop-1,-1,-1):
        current_delivery+=deliveries[stop]
        current_pickup+=pickups[stop]

        while current_delivery>cap or current_pickup>cap:
            current_delivery-=cap
            current_pickup-=cap
            total_distance+=2*(last_stop)
            last_stop=stop+1
        
    if current_delivery>0 or current_pickup>0:
        total_distance+=2(last_stop)
       
    return total_distance
        
# print(solution(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]))
print(solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0]))