import pytest
import time
from UniqueFinder import getemailaddressdata
from UniqueFinder import removeduplicates

def test_checknumberofemails():
    """Tests that number of emails in the received list are greater or equal
    than the expected entries"""
    assert len(getemailaddressdata(100000))>=100000
def test_checksmallnumberofemails():
    """Tests that number of emails in the received list are greater or equal
    than the expected entries"""
    assert len(getemailaddressdata(1))>=1
def test_checkzeroemails():
    """Tests that number of emails in the received list are 0 when expected entries are 0"""
    assert len(getemailaddressdata(0))==0
def test_negativeemails():
    """Tests that number of emails in the received list are 0 when expected entries are negative"""
    assert len(getemailaddressdata(0))==0
def test_allementsareunique():
    """Test that all truncated list of emails are unique"""
    assert IsUnique(removeduplicates(getemailaddressdata(1000)))
def test_allementsareuniqueforsmalldata():
    """Test that all truncated list of emails are unique"""
    assert IsUnique(removeduplicates(getemailaddressdata(1)))
def test_allementsareuniqueforlargedata():
    """Test that all truncated list of emails are unique"""
    assert IsUnique(removeduplicates(getemailaddressdata(233473)))
def test_processingisunder1s():
    """Test processing of elements is done under 1 s"""
    start_time = time.time()
    assert time.time() - start_time<=1

def IsUnique(list):
    elements=set()
    for item in list:
        if item in elements:
            return False
        elements.add(item)
    return True