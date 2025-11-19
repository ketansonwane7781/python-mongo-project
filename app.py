from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = "secret_key"  # Needed for flash messages

# MongoDB setup
mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
client = MongoClient(mongo_url)

db = client["schoolDB"]
collection = db["students"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        dept = request.form['dept']

        if not (name and email and age and dept):
            flash("All fields are required.")
            return redirect(url_for('add'))

        collection.insert_one({"name": name, "email": email, "age": int(age), "dept": dept})
        flash("Student added successfully!")
        return redirect(url_for('home'))

    return render_template('add.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    student = None
    if request.method == 'POST':
        name = request.form['name']
        student = collection.find_one({"name": name})
    return render_template('search.html', student=student)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        new_email = request.form['email']
        new_age = request.form['age']
        new_dept = request.form['dept']

        result = collection.update_one(
            {"name": name},
            {"$set": {"email": new_email, "age": int(new_age), "dept": new_dept}}
        )
        if result.matched_count:
            flash("Student updated successfully!")
        else:
            flash("No student found to update.")
        return redirect(url_for('home'))

    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        name = request.form['name']
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            flash("Student deleted successfully!")
        else:
            flash("No student found to delete.")
        return redirect(url_for('home'))

    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)
