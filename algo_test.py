'''
Created on 13 Aug 2019

@author: benjaminsenyonyi
'''
import unittest
from solar_power import loan_algo


class Payment_Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(loan_algo.get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000), 141, "Answer expected : 141")
    
    def test2(self):
        self.assertEqual(loan_algo.get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000), 17, "Answer expected : 17")
        
    def test3(self):
        self.assertEqual(loan_algo.get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000), 5, "Answer expected :  5")
    
    def test4(self):
        self.assertEqual(loan_algo.get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000), 1, "Answer expected :  1")
    
    def test5(self):
        self.assertEqual(loan_algo.get_days_of_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000), 10, "Answer expected :  10")
        
        
         

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()