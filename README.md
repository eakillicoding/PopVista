# PopVista

## Introduction
PopVista is a sophisticated full-stack application, leveraging Django for backend operations and React for the frontend. The backend is designed to securely store and manage data, which is retrieved by the frontend through React's Fetch API. This data is utilized to generate a detailed funnel chart of a country's population, which in this instance showcases the demographic of the United States in the year 2022 by age and gender.

## Getting Started

### Prerequisites
Python, Django, Node.js, npm, React

### Installation
A step-by-step guide that tells you how to get a development environment running.

### Backend (Django)
```bash
# Clone the repository
git clone <repo_url>
cd <cloned_repo>

# Setup virtual environment
python -m venv venv

# Run virtual environment
source venv/bin/activate #Mac/Linux
venv\Scripts\activate #Windows

# Install dependencies
pip install -r requirements.txt

# Backend directory
cd backend

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

### Frontend (React)
```bash
## Navigate to the frontend directory
cd <frontend>

## Install dependencies
npm install

## Start the development server
npm start
```