# 🐍 python-mongo

[![Python](https://img.shields.io/badge/python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.0%2B-green?logo=flask)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/mongodb-%3E%3D4.0-brightgreen?logo=mongodb)](https://www.mongodb.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-informational)](LICENSE)

A modern, beginner-friendly Flask web application for managing student records using MongoDB.  
Perform **Create, Read, Update, Delete (CRUD)** operations with a simple web interface!

---

## 🚀 Features

- ✏️ Add student records
- 🔍 Search students by name
- 📝 Update student information
- 🗑️ Delete student records
- ⚡ Flash notifications for user feedback
- 🎨 User-friendly HTML forms

---

## 📸 Demo

> _Add screenshots/gif here after running your app!_

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ketansonwane7781/python-mongo.git
   cd python-mongo
   ```

2. **Set up a virtual environment (optional, but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask pymongo
   ```

4. **Start MongoDB locally**

   Make sure [MongoDB](https://www.mongodb.com/try/download/community) is running on `mongodb://localhost:27017/`.

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser:**  
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🏗️ Project Structure

```
python-mongo/
│
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   ├── index.html
│   ├── add.html
│   ├── search.html
│   ├── update.html
│   └── delete.html
└── README.md
```

---

## 💡 Usage

- **Add Student:**  
  Navigate to `/add` and fill out the form.

- **Search Student:**  
  Visit `/search` and enter the student's name.

- **Update Student:**  
  Go to `/update` to modify details.

- **Delete Student:**  
  Use `/delete` to remove a student.

---

## ⚙️ Tech Stack

- [Python 3.7+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [MongoDB](https://www.mongodb.com/)
- [PyMongo](https://pymongo.readthedocs.io/)

---

## 🤝 Contributing

Contributions are welcome!  
1. Fork the repo  
2. Create a new branch (`git checkout -b feature/your-feature`)  
3. Commit your changes  
4. Open a pull request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

- [Ketan Sonwane](https://github.com/ketansonwane7781)

---

> _Feel free to ⭐️ this repo if you find it useful!_
