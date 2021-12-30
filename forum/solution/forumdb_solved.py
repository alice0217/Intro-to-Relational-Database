# "Database code" for the DB Forum.

import psycopg2
import bleach
from datetime import datetime

# POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
    """Return all posts from the 'database', most recent first."""
    conn = psycopg2.connect("dbname=forum")
    cursor = conn.cursor()
    # cursor.execute(" UPDATE posts SET content ='cheese' WHERE content like '%spam%' ")
    cursor.execute("DELETE FROM posts WHERE content like '%spam%';")
    cursor.execute("SELECT content, time FROM posts ORDER BY time DESC")
    results = cursor.fetchall()
    POSTS = results
    conn.close()
    return POSTS
    # return reversed(POSTS)


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    conn = psycopg2.connect("dbname=forum")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts VALUES (%s, %s)', (bleach.clean(content), datetime.now()), )
    conn.commit()
    conn.close()
