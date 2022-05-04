#!/usr/bin/python
import psycopg2
from config import config
from datetime import datetime


def execute_psql(sql_command, long_url="", short_url=""):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        if (sql_command == 'create'):
            result = create_short_url(cur, long_url, short_url)
            conn.commit()

        if (sql_command == 'fetch'):
            result = fetch_long_url(cur, short_url)
        
        if (sql_command == 'recent'):
            result = get_most_recent_short_url(cur)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    print(result)
    return result

def fetch_long_url(cursor, short_url: str):
    print('fetching long url')
    cursor.execute(f'''SELECT long_url FROM url WHERE short_url='{short_url}';''')
    matching_long_urls = cursor.fetchone()
    
    if matching_long_urls == None or len(matching_long_urls) == 0:
        raise Exception('No matching short url found')
    if len(matching_long_urls) > 1:
        raise Exception('More than one matching url found')
    return matching_long_urls[0]

def create_short_url(cursor, long_url: str, short_url: str):
    sql = '''INSERT INTO url (long_url, short_url)
             VALUES(%s, %s) RETURNING short_url;'''
    print('creating short url')
    cursor.execute(sql, (long_url, short_url))
    return cursor.fetchone()[0]

def get_most_recent_short_url(cursor):
    print('getting most recent url')
    sql = '''SELECT short_url FROM url ORDER BY date DESC LIMIT 1'''
    cursor.execute(sql)
    previous_url = cursor.fetchone()
    if previous_url == None or len(previous_url) == 0:
        return None
    return previous_url[0]

if __name__ == '__main__':
    execute_psql('recent')