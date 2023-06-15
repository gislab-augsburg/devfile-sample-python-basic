from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World, this is me, check it out now! The Funk Soul Brother. Check Commit, Check connection"
def hello2():
    return "Hello again"

def dbconn():
    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='postgres', host='dzckank001.srv.muenchen.de', port= '5432'
    )
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    

    #Executing an MYSQL function using the execute() method
    cursor.execute("SELECT schemaname FROM pg_catalog.pg_tables WHERE tablename = 'pg_statistic';")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    
    #Closing the connection
    conn.close()
    
    #return "fetched: "
    return data



if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
