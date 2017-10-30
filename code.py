from flask import Flask
from flask import request, Response
import urllib2, sys, time, MySQLdb
app = Flask(__name__)

@app.route("/service/publicXMLFeed")
def query():
    ''' This function will fetch the query string from the localServer and redirect it to the appropriate server'''

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
    '''This funtion will look up the MYSQL DB and return the slow querries and the count of each query, default will query slow queries for reponseTime>0.5s
    example: "http://localhost:5000/stats" , "http://localhost:5000/stats?responseTime>0.7"
    '''
    if request.query_string == "":
        query_str = 0.5
    else:
        query_str = request.query_string
    s = "Slow Response (greater than "+str(query_str)+"s):\n"
    DB_HANDLE.execute("select timeStamp, url, responseTime from stats where {0}".format(query_str))
    for row in DB_HANDLE.fetchall():
        s = s + str(row[1])+ " : " + str(row[2]) + "s\n"
    s = s +"\nNumber of queries:\n"
    DB_HANDLE.execute("select url, count(*) from stats group by url")
    for row in DB_HANDLE.fetchall():
        s = s + str(row[0]) + " : " + str(row[1]) + "\n"
    return Response(s,mimetype="text")


def setup_mysql_conn():
    global DB_HANDLE
    db = MySQLdb.connect(host="mysql_db", # your host, usually localhost
                     user="root",         # your username
                     passwd="mypassword", # your password
                     db="info")         # name of the data base
    DB_HANDLE = db.cursor()
    db.autocommit(True)

def main():
    setup_mysql_conn()
    app.run(host="0.0.0.0")

if __name__ == "__main__":
    main()
