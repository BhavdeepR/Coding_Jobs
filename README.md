# CodingJobs

A modern job portal built with Django and Bulma, supporting job seekers and employers.

## Features
- User authentication (job seeker & employer roles)
- Employers: add, edit, delete jobs
- Job seekers: apply for jobs with resume upload
- Dashboard for both user types
- Notifications for applications and messages
- Search for jobs by title, description, company, or city
- Responsive, modern UI
- Media file cleanup for deleted applications
- Local timezone support

## Setup Instructions

### 1. Clone the repository
```
git clone <your-repo-url>
cd Coding_Jobs
```

### 2. Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set up the database
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)
```
python manage.py createsuperuser
```

### 6. Collect static files
```
python manage.py collectstatic
```

### 7. Create a media directory for uploaded resumes
```
mkdir media
```

### 8. Run the development server
```
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage
- **Job Seekers:**
  - Sign up as a job seeker
  - Browse and search for jobs ("New Jobs" in navbar)
  - Apply for jobs by uploading a resume
  - View your applications and conversations
- **Employers:**
  - Sign up as an employer
  - Add, edit, and delete jobs
  - View applicants and their resumes
  - Receive notifications for new applications
- **Notifications:**
  - Bell icon in navbar shows notifications for new applications and messages
- **Search:**
  - Use the search page to find jobs by title, description, company, or city
  - Filter by company size

## Timezone
- All times are displayed in your local timezone (set in `settings.py` as `TIME_ZONE`).

## Notes
- Make sure to configure your production server to serve static and media files correctly.
- For any issues, check the Django logs or open an issue in the repository.