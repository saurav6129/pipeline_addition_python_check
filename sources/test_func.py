import calulator
import pytest
 
def test_addition():
    assert calulator.addition(10,5)==15
    assert calulator.addition(10,3)==13
    assert calulator.addition(10,100)==110
    print("testing build trigger ")
    print("testing again.")
    
def test_subtraction():
    assert calulator.subtraction(10,3)==7
    assert calulator.subtraction(30,10)==20
    assert calulator.subtraction(25,10)==15


