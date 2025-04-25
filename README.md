# Basic Health Information System (HIS)

A simple web application simulating a basic Health Information System for managing clients and their enrollment in health programs/services. This project serves as a demonstration of integrating a FastAPI backend, a React frontend, and Supabase for database and backend-as-a-service features.

**Current Date:** Friday, April 25, 2025
**Location Context:** Athi River, Machakos County, Kenya

## Features

* **Program Management:** Create and list health programs (e.g., TB, Malaria, HIV).
* **Client Registration:** Register new clients into the system.
* **Client Enrollment:** Enroll clients into one or more available health programs.
* **Client Search:** Search for clients from the list of registered individuals.
* **Client Profile:** View detailed information about a client, including the programs they are currently enrolled in.
* **API Exposure:** Exposes client profile data via a RESTful API endpoint for potential integration with other systems.

## Tech Stack

* **Backend:** [Python](https://www.python.org/) 3.9+, [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/)
* **Frontend:** [Node.js](https://nodejs.org/), [React](https://reactjs.org/), [Axios](https://axios-http.com/), [React Router](https://reactrouter.com/)
* **Database:** [Supabase](https://supabase.com/) (PostgreSQL)
* **Package Managers:** `pip` (Python), `npm` or `yarn` (Node.js)

## Architecture Overview

This project follows a standard client-server architecture:

1.  **React Frontend (`frontend/`):** Provides the user interface for doctors/users to interact with the system. It makes HTTP requests to the backend API.
2.  **FastAPI Backend (`Health_api/`):** Exposes a RESTful API. It handles business logic, data validation, and communicates with the Supabase database.
3.  **Supabase:** Acts as the database (PostgreSQL) and provides backend services like authentication (though not explicitly used in this basic version's core logic, it's available) and auto-generated APIs (though we are building our own custom API with FastAPI).

## Project Directory Structure

Health_info_system/
├── Health_api/     # FastAPI Backend (See Health_api/README.md)
│   ├── app/
│   ├── requirements.txt
│   └── README.md   # Backend specific instructions
├── frontend/       # React Frontend (See frontend/README.md)
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md   # Frontend specific instructions
├── .gitignore      # Specifies intentionally untracked files that Git should ignore
└── README.md       # This file: Project overview and entry point


## Prerequisites

Before you begin, ensure you have the following installed:

* [Git](https://git-scm.com/)
* [Python](https://www.python.org/downloads/) (version 3.9 or higher recommended)
* [Node.js](https://nodejs.org/) (version 18.x or later recommended) and `npm` or `yarn`
* A [Supabase](https://supabase.com/) account (the free tier is sufficient)

## Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd Health_info_system
    ```

2.  **Supabase Setup:**
    * Go to [app.supabase.com](https://app.supabase.com/) and create a new project.
    * Navigate to the **SQL Editor** section. You'll need to create tables for `programs`, `clients`, and a linking table like `client_enrollments`.
        * **Example `programs` table:** `id` (uuid, pk), `created_at` (timestamptz), `program_name` (text, unique), `description` (text)
        * **Example `clients` table:** `id` (uuid, pk), `created_at` (timestamptz), `name` (text), `date_of_birth` (date), `contact_info` (text, optional)
        * **Example `client_enrollments` table:** `id` (uuid, pk), `created_at` (timestamptz), `client_id` (uuid, fk to clients.id), `program_id` (uuid, fk to programs.id), `enrollment_date` (date)
        * *(Make sure to enable Row Level Security (RLS) on your tables if needed for production, though it might be simpler to keep it disabled for initial development).*
    * Go to **Project Settings** (Gear icon) -> **API**.
    * Find your **Project URL** and the **`anon` public API Key**. You will need these for both the backend and potentially the frontend configuration.

3.  **Backend Setup (`Health_api/`):**
    * Navigate to the backend directory: `cd Health_api`
    * **Detailed instructions are in `Health_api/README.md`**.
    * *Key steps typically involve:*
        * Creating and activating a Python virtual environment.
        * Installing dependencies: `pip install -r requirements.txt`
        * Creating a `.env` file and adding your `SUPABASE_URL` and `SUPABASE_ANON_KEY`.

4.  **Frontend Setup (`frontend/`):**
    * Navigate to the frontend directory (from the root): `cd frontend`
    * **Detailed instructions are in `frontend/README.md`**.
    * *Key steps typically involve:*
        * Installing dependencies: `npm install` or `yarn install`
        * Creating a `.env` file and adding `REACT_APP_API_URL` pointing to your running backend (e.g., `REACT_APP_API_URL=http://localhost:8000/api/v1`).

## Running the Application

1.  **Start the Backend Server:**
    * In your terminal, navigate to the `Health_api/` directory.
    * Activate your virtual environment.
    * Run: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000` (or as specified in `Health_api/README.md`).

2.  **Start the Frontend Development Server:**
    * In a *separate* terminal, navigate to the `frontend/` directory.
    * Run: `npm start` or `yarn dev` (or as specified in `frontend/README.md`).

3.  **Access the Application:**
    * Open your web browser and navigate to the address provided by the frontend development server (usually `http://localhost:3000` for Create React App or `http://localhost:5173` for Vite).

## API Documentation

The backend API provides interactive documentation powered by Swagger UI. Once the backend server is running, you can access it at:

[http://localhost:8000/docs](http://localhost:8000/docs)
