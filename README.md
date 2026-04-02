
# 🎓 Student Management System (Flask)

A simple and efficient **Student Management System** built using **Flask** and **SQLite**.  
This project allows users to manage student records with basic CRUD operations.

---

## 🚀 Features

- 🔐 Admin Login System
- ➕ Add Student
- 📋 View Student List
- ❌ Delete Student
- 💬 Flash Messages for actions
- 🗄️ SQLite Database Integration

---

## 🛠️ Tech Stack

- Python
- Flask
- SQLite
- HTML/CSS (Templates)

---

## 📂 Project Structure

```

Student Management System/
│── app.py
│── templates/
│   ├── login.html
│   ├── index.html
│   ├── add.html
│── static/
│── requirements.txt
│── .gitignore

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
````

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the application

```bash
python app.py
```

---

## 🔑 Login Credentials

```
Username: admin
Password: admin
```

👉 Defined in your code 

---

## 🗄️ Database

* Uses **SQLite**
* Automatically creates `students` table on first run 

---

## 📦 Requirements

All dependencies are listed in `requirements.txt` 

---

## ⚠️ Note

* Make sure `venv/` is ignored using `.gitignore`
* Do not upload virtual environment to GitHub

---

## 📸 Screenshots (Optional)

*Add screenshots of your app here for better presentation*

---

## 🙌 Author

* Your Name

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

````

---

## 🔥 Small improvement (IMPORTANT)

👉 In your `app.py`, you are storing DB inside `venv`:
```python
db_path = os.path.join(os.path.dirname(__file__), 'venv', 'students.db')
````

❌ Not recommended

👉 Better:

```python
db_path = os.path.join(os.path.dirname(__file__), 'students.db')
```

---

 
