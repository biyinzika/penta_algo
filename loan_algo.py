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
    
    total_days = 0

#     Over the range of the first rates
    for x in range(d2-d1):
        if K > R1 :
            K -= R1
            total_days+=1    
#         print("First K : ", K)
    
    
    for y in range(d3-d2):
        if K > R2 :
            K -= R2
            total_days +=1
#         print("Second K:", K)
    
    while (K > R3) :
        K -= R3
        total_days +=1
        print("Third K:", K)
    
#     print("Number of days : ", total_days)

    return total_days


if __name__ == '__main__':
#     get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000)
    #464
    get_days_of_power(R1=1000, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)
    #41
#     get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000)
    #11
#     get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)
    #2
    
    pass







