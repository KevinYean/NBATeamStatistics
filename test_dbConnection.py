import pytest
import pymongo
from pymongo import MongoClient
from main import getColumns


uri = "mongodb+srv://kevin:kevinAdmin@cluster0-focx3.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)

def test_dbColumns():
    assert getColumns() == 4
