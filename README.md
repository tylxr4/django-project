- Guitar Song Suggester

An AI-powered web app that recommends songs to learn based on your guitar skill level and the chords you already know.

- Overview

I built this project as a tool to help guide me in my journey of learning guitar. Tell the app what chords you know and your skill level, and it returns personalized song recommendations with chord progressions you can start playing right away.

- Features

User registration, login, and logout. AI-generated song suggestions based on skill level and known chords. Practice history saved per user in MongoDB Atlas. Clean dark-themed responsive UI.

- Tech Stack

Backend: Django and Python. Database: MongoDB Atlas with PyMongo. AI: OpenAI API using GPT-3.5 Turbo. Authentication: Django built-in auth. Frontend: HTML, CSS, and JavaScript. Deployment: Docker, AWS Elastic Beanstalk, and Kubernetes on AWS EKS (in progress).

- Running Locally

Clone the repository and navigate into it. Create and activate a virtual environment using python3 -m venv venv and source venv/bin/activate. Install dependencies with pip install -r requirements.txt. Create a .env file in the project root with MONGO_PASSWORD and OPENAI_API_KEY set to your credentials. Run python manage.py migrate and then python manage.py runserver. Visit http://127.0.0.1:8000 in your browser.

- Author

Tyler Summerlin — github.com/tylxr4