import pymongo
import datetime

from flask import current_app, g
from werkzeug.local import LocalProxy

from pymongo import MongoClient, DESCENDING, ASCENDING
from pymongo.write_concern import WriteConcern
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo.read_concern import ReadConcern

now = datetime.datetime.now()
currentYear = now.year

def get_db():
    uri = "mongodb+srv://tempReader:tempPassword@cluster0-focx3.mongodb.net/test?retryWrites=true&w=majority"
    client = pymongo.MongoClient(uri)
    db = client.NBA
    return db

def getColumns():
    db = get_db();
    numberOfColumns = len(db.list_collection_names())
    return numberOfColumns

def getActiveTeams():
    db = get_db();
    dbTeams = db.Teams;
    count = dbTeams.find( { "last": currentYear } ).count()
    return count

def getDefunctTeams():
    db = get_db()
    dbTeams = db.Teams
    #Find the defunct teams that have are not active as of the current year
    count = dbTeams.find( { "last": {'$lt': currentYear} }).count()
    return count

def getAllTeams():
    db = get_db()
    dbTeams = db.Teams
    count = dbTeams.count()
    return count
    