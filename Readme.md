# 🧠 Django Q&A Platform

A simple Quora-style question-and-answer web application built with Django. Authenticated users can post questions, answer others, and like helpful answers.

---

## 🚀 Features

- ✅ User authentication (Signup, Login, Logout)
- 📋 Post questions with title and detailed body
- 📝 Answer any posted question
- ❤️ Like and Unlike answers
- 👥 View all questions on the homepage
- 🗂 Pagination for question list (10 per page)
- 📅 Sorted by newest first
- 🎨 Beautiful and responsive UI (Bootstrap-based)

---

## 🛠 Tech Stack

- **Backend:** Django 4.x (CBVs + FBVs)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite3 (default, easily swappable)
- **Authentication:** Django built-in user model
- **Forms:** Django Forms + `widget_tweaks` for enhanced styling

---


## ⚙️ Project Setup

1. **Clone the repository:**

```bash
git clone https://github.com/murari-py/quoraverse.git
cd quoraverse
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply the database migrations:**

```bash
python manage.py migrate
```

5. **Create a superuser (admin account):**

```bash
python manage.py createsuperuser
```

6. **Run the development server:**

```bash
python manage.py runserver
```

7. **Visit the application in your browser:**

```
http://127.0.0.1:8000/

## 🙋 Author

**Murari**  
[GitHub](https://github.com/murari-py)
```