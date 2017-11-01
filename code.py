from flask import Flask
from flask import request, Response
import urllib2, sys, time, MySQLdb, argparse
from redis_cache import SimpleCache

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
        response_xml = REDIS_CACHE.get(uri)
    except:
        try:
            response_xml = urllib2.urlopen(url).read()
        except:
            DB_HANDLE.execute("insert into stats (timeStamp,url) values ('{0}','{1}')".format(time_stamp,uri))
            return Response("Request got timed out!\n", mimetype='text')
    REDIS_CACHE.store(uri,response_xml)
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
        query_str = "responseTime>0.5"
    else:
        query_str = request.query_string
    
    stats = "Slow Response ("+str(query_str)+"s):\n"
    DB_HANDLE.execute("select timeStamp, url, responseTime from stats where {0}".format(query_str))
    for row in DB_HANDLE.fetchall():
        stats = stats + str(row[1])+ " : " + str(row[2]) + "s\n"
    stats = stats +"\nNumber of queries:\n"
    DB_HANDLE.execute("select url, count(*) from stats group by url")
    for row in DB_HANDLE.fetchall():
        stats = stats + str(row[0]) + " : " + str(row[1]) + "\n"
    return Response(stats,mimetype="text")


def setup_mysql_conn(mysql_user,mysql_password):
    '''This function creates a sql connection to the mysql db container'''
    global DB_HANDLE
    err = True
    while err:
        try:
            db = MySQLdb.connect(host="mysql_db", # your host, usually localhost
                     user=mysql_user,         # your username
                     passwd=mysql_password, # your password
                     db="info")         # name of the data base
            err =  False
        except:
            time.sleep(5)
    DB_HANDLE = db.cursor()
    db.autocommit(True)

def setup_redis_conn(cache_timer):
    global REDIS_CACHE
    err = True
    while err: 
        try:
            REDIS_CACHE = SimpleCache(limit=1000, expire=cache_timer, host='redis_cache', port=6379, db=0)
            err = False
        except:
            time.sleep(2)

def main(mysql_user,mysql_password,cache_timer):
    '''The main function: setup MYSQLDB, REDISCACHE and start application'''
    setup_mysql_conn(mysql_user,mysql_password)
    setup_redis_conn(cache_timer)
    app.run(host="0.0.0.0")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cache_timer', dest='cache_timer', default="60", type=str, help='Cache Expiry Timer in seconds')
    parser.add_argument('-p', '--mysql_password', dest='mysql_password', default="mypassword", type=str, help='MYSQL password')
    parser.add_argument('-u', '--mysql_user',dest="mysql_user", default='root', type=str, help='MYSQL user')
    args = parser.parse_args()
    main(args.mysql_user, args.mysql_password, args.cache_timer)
