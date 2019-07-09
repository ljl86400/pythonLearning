from nose.tools import *
import sys
sys.path.append('D:\python\pythonProj\pythonLearning\projectsFramework\demoForTestCaseUsing\computer')
import addModule

def test_addModule():
    check1 = addModule.addModule(1,6)
    assert_equal(check1,7)
    check1 = addModule.addModule(-1,6)
    assert_equal(check1,5)
    check1 = addModule.addModule(8,6)
    assert_equal(check1,14)
    check1 = addModule.addModule(10000000,60000000)
    assert_equal(check1,70000000)
    check1 = addModule.addModule(-10000000,60000000)
    assert_equal(check1,50000000)
    check1 = addModule.addModule(10000000000,60000000000)
    assert_equal(check1,70000000000)