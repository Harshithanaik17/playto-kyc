# Playto KYC System

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/playto-kyc.git
cd playto-kyc
python -m venv venv
venv\Scripts\activate   # Windows

pip install django djangorestframework pillow
cd backend
python manage.py migrate
python manage.py runserver
```

---

## API Endpoints

* GET /api/v1/kyc/
* POST /api/v1/kyc/
* POST /api/v1/state/<id>/
* GET /api/v1/queue/

---

## Test Credentials

Pass in headers:

merchant → user_id: 1
reviewer → user_id: 2

---

## Notes

* State machine enforces transitions
* File validation ensures security
* SLA calculated dynamically
