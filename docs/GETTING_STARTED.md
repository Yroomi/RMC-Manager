```markdown
# Getting Started with RMC Manager

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15
- Git

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/rmc-manager.git
cd rmc-manager
```

### 2. Set Up Database
```bash
# Using Docker
docker run --name rmc-postgres \
  -e POSTGRES_DB=rmc_manager \
  -e POSTGRES_USER=rmc_user \
  -e POSTGRES_PASSWORD=password \
  -p 5432:5432 \
  -d postgres:15
```

### 3. Set Up Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 4. Set Up Frontend
```bash
cd frontend
npm install
npm start
```

### 5. Access Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/v1/
- Admin: http://localhost:8000/admin/

## Next Steps

Follow the Implementation Roadmap to add:
- Menu management
- Meal ordering
- Kitchen production
- Audit logging
```

---
