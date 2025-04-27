# 🏥 Health API Backend

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-8DE05F?style=for-the-badge&logo=uvicorn)](https://www.uvicorn.org/)

This directory houses the backend API for the Basic Health Information System, crafted with 🐍 Python and the 🚀 FastAPI framework.

---

## ⚙️ Overview

The Health API serves as a robust and efficient RESTful interface, enabling the management of vital healthcare data: programs, clients, and their enrollments.  
It communicates seamlessly with a 💾 Supabase PostgreSQL database, ensuring data integrity and scalability for our health information needs.

---

## 💻 Tech Stack

- 🐍 **Language:** Python 3.9+
- 🚀 **Framework:** [FastAPI](https://fastapi.tiangolo.com/) - A modern, high-performance web framework for building APIs with Python.
- ⚙️ **ASGI Server:** [Uvicorn](https://www.uvicorn.org/) - An ASGI web server implementation for running FastAPI applications.
- 💾 **Database Interaction:** Supabase PostgreSQL client libraries (update if specific one is used).
- 📦 **Dependency Management:** `pip`

---

## 📂 Directory Structure

```text

Health_api/
.
├── app
│   ├── auth
│   │   ├── api.py
│   │   ├── schemas.py
│   │   └── services.py
│   ├── clients
│   │   ├── api.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── services.py
│   ├── database.py
│   ├── enrollments
│   │   ├── api.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── services.py
│   ├── main.py
│   ├── programs
│   │   ├── api.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── services.py
│   ├── search
│   │   ├── api.py
│   │   └── services.py
│   └── tests
│       ├── test_auth.py
│       ├── test_clients.py
│       ├── test_programs.py
│       └── test_search.py
├── health_api_Documentation.json
├── pytest.ini
├── README.md
├── requirements.txt


```

## 🛠️ Setup and Installation

1.  **Prerequisites:**
    * 🐍 [Python](https://www.python.org/downloads/) 3.9 or higher must be installed.
    * `pip` (Python package installer) should be available in your environment.
    * 🔑 Access to your [Supabase](https://supabase.com/) project URL and the `anon` (public) API key is required.

2.  **Navigate to the Backend Directory:**
    ```bash
    cd Health_info_system/Health_api
    ```

3.  **Create and Activate a Virtual Environment (Highly Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate   # On Windows
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **🔑 Environment Configuration:**
    Securely manage your Supabase credentials using environment variables.

    * Create a `.env` file in the `Health_api` directory (ensure `.env` is in your project's root `.gitignore`).
    * Add your Supabase connection details to the `.env` file:
        ```
        SUPABASE_URL=YOUR_SUPABASE_PROJECT_URL
        SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_PUBLIC_API_KEY
        ```
    * You'll likely use a library like `python-dotenv` in your `app/database.py` or `app/main.py` to load these variables.

## ▶️ Running the API

1.  **Navigate to the Backend Directory:**
    ```bash
    cd Health_info_system/Health_api
    ```

2.  **Activate the Virtual Environment (if not active):**
    ```bash
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate   # On Windows
    ```

3.  **Start the FastAPI Application with Uvicorn:**
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```
    * `app.main`: Points to the `app` instance in the `main.py` module.
    * `--reload`: Enables hot reloading for a smoother development experience.
    * `--host 0.0.0.0`: Allows connections from other devices on your network (use `127.0.0.1` for local access only).
    * `--port 8000`: Sets the port for the API server.

## 📚 API Documentation

FastAPI provides auto-generated API documentation for easy exploration and testing:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs) - An interactive interface to explore and test your API endpoints directly in your browser.
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc) - An alternative API documentation view with a focus on readability.

Refer to these URLs when the API is running to understand the available endpoints and how to interact with them.
