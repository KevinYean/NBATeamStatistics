import pytest
import pymongo
from pymongo import MongoClient
from main import getActiveTeams, getDefunctTeams, getAllTeams

def test_activeTeams():
    assert getActiveTeams() == 30
    
def test_defunctTeams():
    assert getDefunctTeams() == 23
    
def test_totalTeams():
    assert getAllTeams() == 53
