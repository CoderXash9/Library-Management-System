<div align="center">

# 📚 Library Management System API

A modern RESTful Library Management System built with **Django REST Framework** featuring authentication, book issue/return workflows, search, filtering, pagination, and interactive API documentation.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.x-darkgreen?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/Django_REST_Framework-API-red?style=for-the-badge)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?style=for-the-badge&logo=sqlite)
![Swagger](https://img.shields.io/badge/API_Docs-Swagger-green?style=for-the-badge)

</div>

---

## ✨ Features

- 📖 Complete CRUD APIs for Authors, Members, Books & Issue Records
- 📚 Book Issue & Return System with inventory management
- 🔒 Authentication & Permission-based access
- 🔍 Search, Filtering & Ordering
- 📄 Pagination for scalable API responses
- 📑 Interactive Swagger API Documentation
- ✅ Serializer & Model Validation
- ⚡ Clean RESTful architecture
- 🛠️ Django Admin Dashboard

---

## 🏗️ Architecture

```text
Client
   │
   ▼
REST API (DRF)
   │
   ▼
Views / ViewSets
   │
   ▼
Serializers
   │
   ▼
Models
   │
   ▼
SQLite Database
```

---

## 🗃️ Database Models

- 👨‍💻 Author
- 📚 Book
- 👤 Member
- 📋 IssueRecord

---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET/POST | `/api/authors/` | Manage Authors |
| GET/POST | `/api/books/` | Manage Books |
| GET/POST | `/api/members/` | Manage Members |
| GET/POST | `/api/issue-records/` | Manage Issue Records |
| POST | `/api/issue-book/` | Issue a Book |
| POST | `/api/return-book/` | Return a Book |

---

## 📸 Screenshots

 ![image alt](https://github.com/CoderXash9/Library-Management-System/blob/8ab6580ed17187afb73f08d630b4746a24a84f43/Screenshot%202026-08-01%20235739.png)
 ![image alt](https://github.com/CoderXash9/Library-Management-System/blob/8ab6580ed17187afb73f08d630b4746a24a84f43/Screenshot%202026-08-02%20153758.png)

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Swagger (drf-spectacular)
- Git & GitHub

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/Library-Management-System.git

cd Library-Management-System

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## 📖 API Documentation

Interactive Swagger UI:

```text
http://127.0.0.1:8000/api/docs/
```

---

## 🌟 Future Improvements

- PostgreSQL Support
- JWT Authentication
- Docker Deployment
- Email Notifications
- Fine Calculation
- Redis Caching

---

## 👨‍💻 Author

**Ashwini Purohit**

🔗 GitHub: https://github.com/CoderXash9

💼 LinkedIn: www.linkedin.com/in/ashwinicodes

---

<div align="center">

### ⭐ If you found this project helpful, consider giving it a star!

Built with ❤️ using Django REST Framework

</div>
