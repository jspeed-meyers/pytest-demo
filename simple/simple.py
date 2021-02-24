"""A simple function to test"""

def add1(num):
	"""Add one to a number"""
	return num + 1

def test_add1():
	"""Unit test for add1()."""
	assert add1(2) == 3
	assert add1(5) == 6

def test_add1_failing():
	"""FAILING Unit test for add1()."""
	assert add1(2) == 4
	assert add1(5) == 4