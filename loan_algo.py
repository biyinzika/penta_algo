'''
Created on 9 Aug 2019

@author: benjaminsenyonyi
'''

def get_days_of_power(R1, D1, R2, D2, R3, D3, K):
    '''
    Method to calculate days of power
    Takes
    D1, D2, D3 - Day 1, Day 2 and Day 3
    R1, R2, R3 - Rates for days 1, 2 and 3
    K - Payment made by user
    
    '''
#     Sort the days
    d1 = min(D1, D2, D3)
    d3 = max(D1, D2, D3)
    d2 = (D1 + D2 + D3) - d1 - d3
    
    #re-assign rates on all (3!) combinations 
    if ((d1 == D1) and (d2 == D2) and (d3 == D3)):
        r1 = R1 
        r2 = R2
        r3 = R3
    elif ((d1 == D1) and (d2 == D3) and (d3 == D2)):
        r1 = R1
        r2 = R3
        r3 = R2
    
    elif ((d1 == D2) and (d2 == D1) and (d3 == D3)):
        r1 = R2
        r2 = R1
        r3 = R3
    elif ((d1 == D2) and (d2 == D3) and (d3 == D2)):
        r1 = R1
        r2 = R3
        r3 = R2 
    
    elif ((d1 == D3) and (d2 == D2) and (d3 == D1)):
        r1 = R3
        r2 = R2
        r3 = R1 
    elif ((d1 == D3) and (d2 == D1) and (d3 == D2)):
        r1 = R3
        r2 = R1
        r3 = R2
#
#     print(d1, r1, d2, r2, d3, r3)
#     print(D1,R1,D2,R2,D3,R3)
    
    total_days = 0

#     Over the range of the first rates
    for value in range(d2-d1):
        if K > r1 :
            K -= R1
            total_days+=1    
#         print("First K : ", K)
    
    
    for value in range(d3-d2):
        if K > (r2+r1) :
            K -= (r2+r1)
            total_days +=1
#         print("Second K:", K)
    
    while (K > (r3+r2+r1)) :
        K -= (r3+r2+r1)
        total_days +=1
#         print("Third K:", K)
    
    print("Number of days : ", total_days)

    return total_days


if __name__ == '__main__':
    get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000)
    #141
    get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)
    #17
    get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000)
    #5
    get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)
    #1
    get_days_of_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000)
    #10
    pass







