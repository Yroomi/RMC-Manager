```markdown
# RMC Manager Backend

Django REST API for the RMC Manager application.

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Endpoints

- `POST /api/v1/auth/login/` - Login
- `POST /api/v1/auth/refresh/` - Refresh token
- `GET /api/v1/auth/me/` - Get current user
```

---
