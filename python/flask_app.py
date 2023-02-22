# Imports
import mysql.connector
import time
from flask import Flask, render_template, request, redirect, url_for
# --------------------------------------------------------------------------------
# Create Flask instance
app = Flask(__name__)
# --------------------------------------------------------------------------------
# Connecting to the mySQL Database
while True:
    try:
        connection = mysql.connector.connect(
            user = 'root',password = 'root',host='mysql',port="3306",database='db'
        ) 
        print("DB Connected")
        break
    except:
        print('MySQL server not yet available. Retrying in 5 seconds...')
        time.sleep(5)
# --------------------------------------------------------------------------------
# Gathering the student data from the table
def data_gather():  
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks')
    students = cursor.fetchall()

    return students
# --------------------------------------------------------------------------------
# Inserting the user's input into the table
def data_insert(task):
    cursor = connection.cursor()
    cursor.execute('SELECT MAX(taskNum) FROM tasks')
    max_id = cursor.fetchone()[0]
    new_id = max_id + 1 if max_id is not None else 1
    # Insert new data into the table
    sql = "INSERT INTO tasks (taskNum, task) VALUES (%s, %s)"
    val = (new_id, task)
    cursor.execute(sql, val)
    connection.commit()
# --------------------------------------------------------------------------------
# Removing element
def data_remove(task_id):
    cursor = connection.cursor()
    # Delete data from the table
    sql = "DELETE FROM tasks WHERE taskNum = %s"
    val = (task_id,)
    cursor.execute(sql, val)
    connection.commit()
# --------------------------------------------------------------------------------
def get_list_of_dict(keys, list_of_tuples):
     """
     This function will accept keys and list_of_tuples as args and return list of dicts
     """
     list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
     return list_of_dict

# --------------------------------------------------------------------------------
# URL Routing

# Home Page
@app.route('/')
def index():
    tasks = data_gather()
    keys = ("id", "task")
    tasks_json = get_list_of_dict(keys,tasks)
    return render_template('index.html',task_info = tasks_json)

# Insert Page
@app.route('/handle_data', methods=['POST'])
def handle_data():
    task = request.form['task_text']
    if len(task) < 1:
        
        return redirect(url_for('index'))
    else:
        data_insert(task)
        return redirect(url_for('index'))


@app.route('/remove_item')
def remove_item():
    item_id = request.args.get('id')
    print('Here is item_id: ',item_id)
    data_remove(item_id)
    tasks = data_gather()
    keys = ("id", "task")
    task_json = get_list_of_dict(keys,tasks)
    return render_template('index.html',task_info = task_json)
       
# -----------------------s---------------------------------------------------------
# Running the Flask Instance
if __name__ =='__main__':
    print('Website has RUN COME ON!')
    app.run(host='0.0.0.0',port='5000',debug=True)





