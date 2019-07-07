from nose.tools import *
import sys
sys.path.append('D:\python\pythonProj\pythonLearning\projectsFramework\skeleton\NAME')
import NAME

def setup():
    print("setup!")
    
def teardown():
    print("teardown!")
    
def test_basic():
    print("i ran!")