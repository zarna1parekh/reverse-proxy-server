from flask import Flask
from flask import request, Response
import urllib2, sys, time, MySQLdb
app = Flask(__name__)

@app.route("/service/publicXMLFeed")
def query():
    start_time = time.time()
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
    #print request.args
    url = "http://webservices.nextbus.com/service/publicXMLFeed?"+request.query_string
    uri = "/service/publicXMLFeed?"+request.query_string
    try:
        response_xml = urllib2.urlopen(url).read()
    except:
        DB_HANDLE.execute("insert into stats (timeStamp,url) values ('{0}','{1}')".format(time_stamp,uri))
        return Response("Request got timed out!", mimetype='text')
    end_time =  time.time()
    response_time = end_time - start_time
    insert_command = "insert into stats (timeStamp,url,responseTime) values ('{0}','{1}',{2})".format(time_stamp,uri,response_time)
    DB_HANDLE.execute(insert_command)
    return Response(response_xml,mimetype='xml')


@app.route("/stats")
def get_stats():
    if request.query_string == "":
        query_str = 0.5
    else:
        query_str = request.query_string
    s = "Slow Response (greater than "+str(query_str)+"s):\n"
    DB_HANDLE.execute("select timeStamp, url, responseTime from stats where responseTime > {0}".format(float(query_str)))
    for row in DB_HANDLE.fetchall():
        s = s + str(row[1])+ " : " + str(row[2]) + "\n"
    s = s +"\nNumber of queries:\n"
    DB_HANDLE.execute("select url, count(*) from stats group by url")
    for row in DB_HANDLE.fetchall():
        s = s + str(row[0]) + " : " + str(row[1]) + "\n"
    return Response(s,mimetype="text")


if __name__ == "__main__":
    global DB_HANDLE
    db = MySQLdb.connect(host="mysql_db", # your host, usually localhost
                     user="root",         # your username
                     passwd="mypassword", # your password
                     db="info")         # name of the data base
    DB_HANDLE = db.cursor()
    db.autocommit(True)
    app.run(host="0.0.0.0")
