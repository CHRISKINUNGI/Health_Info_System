# Basic Health Information System (HIS)

A simple web application simulating a basic Health Information System for managing clients and enrolling them into health programs.  
It demonstrates the integration of a **FastAPI** backend, a **React** frontend, and **Supabase** (PostgreSQL).

---

## 📚 Overview

- **Program Management:** Create and list health programs (e.g., TB, Malaria, HIV).
- **Client Registration:** Register new clients into the system.
- **Client Enrollment:** Enroll clients into one or more available health programs.
- **Client Search:** Find registered clients quickly.
- **Client Profiles:** View detailed client information and enrollment history.
- **RESTful API:** Exposes client data for external integrations.

---

## 🏗️ Architecture

| Layer        | Technology                         |
|:-------------|:-----------------------------------|
| Frontend     | React, Axios, React Router         |
| Backend      | FastAPI, Uvicorn                   |
| Database     | Supabase (PostgreSQL)              |
|              |                                    |

The **frontend** communicates with the **FastAPI backend**, which interacts with **Supabase** for persistent data storage.

---

## 🛠️ Tech Stack

- **Frontend:** React, Axios, React Router
- **Backend:** FastAPI, Uvicorn
- **Database:** Supabase (PostgreSQL)
- **Languages/Tools:** Python 3.9+, Node.js 18+, npm/yarn, Git

---

## 📁 Directory Structure

```txt
Health_info_system/
|
├── Health_api/     
│   ├── app/
│   ├── requirements.txt
│   └── README.md
├── frontend/      | FUTURE |
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
├── .gitignore       
└── README.md            
```

---

## 🚀 Getting Started

Each part of the project (backend and frontend) has its own detailed setup instructions.

- 🛠️ **Backend Setup:** See [Health_api/README.md](health_api/README.md)
- 🎨 **Frontend Setup:** See [frontend/README.md](frontend/README.md) | FUTURE

> In short, you will set up the database (Supabase), run the FastAPI backend, and start the React frontend.

---

## 📌 Notes

- **Supabase:** You'll need a Supabase project for database setup.
- **Environment Variables:** Both frontend and backend require `.env` files for API keys and URLs.
- **CORS:** Ensure CORS is properly handled on the backend during development (already configured via FastAPI middleware).
- **Row Level Security (RLS):** Can remain disabled for development; recommended to enable with proper policies before production.

---

## ✨ Future Enhancements (Optional)

- User authentication and role management
- Health records (visits, prescriptions)
- Notifications and appointment reminders
- Analytics dashboards (e.g., program enrollment statistics)

---

## 📬 Contact

For questions or collaboration ideas, feel free to reach out!
