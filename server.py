import jwt, datetime,os
from flask import Flask,request
from flask_mysqldb import MySQL
server=Flask(__name__)
mysql=MySQL(server)
#config 
server.config["MYSQL_HOST"]=os.environ.get("MYSQL_HOST", "localhost")
server.config["MYSQL_USER"]=os.environ.get("MYSQL_USER", "root")
server.config["MYSQL_PASSWORD"]=os.environ.get("MYSQL_PASSWORD", "5418feliX")
server.config["MYSQL_DB"]=os.environ.get("MYSQL_DB", "istream")
server.config["MYSQL_PORT"]=os.environ.get("MYSQL_PORT", "3308")
