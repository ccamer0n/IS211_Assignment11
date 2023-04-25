from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)
to_do = []

@app.route('/')
def to_do_list():
    '''Shows the current list of to do items and provides a form for adding new items.'''
    return render_template('to_do.html', to_do=to_do)

@app.route('/submit', methods = ['POST'])
def add_to_list():
    '''Adds new tasks to the to do list.'''
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    pattern = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    if re.fullmatch(pattern, email):
        if priority == 'low' or 'medium' or 'high':
            line = [task, email, priority]
            to_do.append(line)
    else:
        pass
    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear_list():
    '''Clears all items from the to do list.'''
    global to_do
    to_do = []
    return redirect('/')

if __name__ == '__main__':
    app.run()
