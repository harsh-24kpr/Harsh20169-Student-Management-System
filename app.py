from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'venv', 'students.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        roll TEXT NOT NULL,
                        course TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect('/')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/login')

@app.route('/')
@login_required
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=('GET','POST'))
@login_required
def add():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        course = request.form['course']

        conn = get_db_connection()
        conn.execute('INSERT INTO students (name, roll, course) VALUES (?,?,?)',
                     (name, roll, course))
        conn.commit()
        conn.close()

        flash('Student added successfully!', 'success')
        return redirect('/')

    return render_template('add.html')

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id=?', (id,))
    conn.commit()
    conn.close()
    flash('Student deleted successfully!', 'success')
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)