import jwt, datetime,os
from flask import Flask,request
from flask_mysqldb import MySQL
server=Flask(__name__)
mysql=MySQL(server)
#config 
server.config["MYSQL_HOST"]=os.environ.get("MYSQL_HOST", "localhost")
server.config["MYSQL_USER"]=os.environ.get("MYSQL_USER","root")
server.config["MYSQL_PASSWORD"]=os.environ.get("MYSQL_PASSWORD","5418feliX")
server.config["MYSQL_DB"]=os.environ.get("MYSQL_DB","AuthService")
server.config["MYSQL_PORT"]=os.environ.get("MYSQL_PORT",3308)

@server.route("/login",methods=["POST"])
def login():
    auth=request.authorization
    if not auth:
        return "missing creditials",401
    
    #check db for username and password
    cur=mysql.connection.cursor()
    res=cur.execute(
        "SELECT  email,password FROM user WHERE  email=%s",(AuthService.username,) # type: ignore
    )
    if res>0:
        user_row=cur.fetchone()
        email=user_row[0]
        password=user_row[1]
        if AuthService.username!=email or auth.password !=password:
                return "invalid credentials",401
        else:
             return createJWT(auth.username,os.environ.get("JWT_SECRET"),True)
    else:
        return "invalids creditials",401      
def createJWT(username,secret,authz):
     return jwt.encode(
          {"username":username,
          "exp":datetime.datetime.now(tz=datetime.timezone.UTC)
          +datetime.timedelta(day=1),
          "iat":datetime.datetime.utcnow(),
          "admin":authz,
          },
          secret,
          algorithm="HS256",
     )