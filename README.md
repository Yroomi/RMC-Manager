# RMC Manager - Resident Meal Choice Manager

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-5.0-green.svg)
![React](https://img.shields.io/badge/react-18-61dafb.svg)
![Status](https://img.shields.io/badge/status-in%20development-yellow.svg)

A multi-tenant, web-based meal management system for aged care facilities. Digitizes meal ordering, validates clinical dietary requirements (IDDSI compliance), generates production forecasts, and provides comprehensive audit trails.

---

## 🌟 Features

### Phase 1 (Production-Ready Internal Platform)
- ✅ **Multi-Tenant Architecture** - Isolated data per venue with strict tenant separation
- ✅ **Clinical Safety** - IDDSI validation, allergy blocking, fluid restriction tracking
- ✅ **Wing-Level Ordering** - Spreadsheet-style interface for efficient meal selection
- ✅ **Kitchen Production** - Automated forecasting, aggregation, and tray label generation
- ✅ **Audit Compliance** - Immutable audit logs with 7-year retention
- ✅ **Role-Based Access** - Super Admin, Venue Admin, Carer, Kitchen Staff, Dietitian, Auditor
- ✅ **Cut-off Time Enforcement** - Configurable meal ordering deadlines
- ✅ **Supplement Management** - Track and schedule nutritional supplements
- ✅ **Responsive UI** - Tablet and desktop optimized with offline capability

### Phase 2 (Future - SaaS Expansion)
- 🔄 Public API with rate limiting
- 🔄 OAuth2 & SSO authentication
- 🔄 Webhook integrations
- 🔄 Tenant self-service provisioning
- 🔄 Billing integration (Stripe)
- 🔄 White-labeling capability

---

## 🏗️ Architecture

### Tech Stack

**Backend:**
- Django 5.0 + Django REST Framework
- PostgreSQL 15 (Multi-AZ)
- Redis (ElastiCache)
- Celery for async tasks
- JWT authentication

**Frontend:**
- React 18 with TypeScript
- TailwindCSS for styling
- React Query for data fetching
- Redux Toolkit for state management
- PWA for offline capability

**Infrastructure:**
- AWS ECS Fargate (containerized deployment)
- AWS RDS PostgreSQL (Multi-AZ)
- AWS S3 (media storage)
- AWS CloudFront (CDN)
- AWS ALB (load balancing)
- CloudWatch (logging & monitoring)

### High-Level Architecture

```
┌─────────────┐
│   React     │
│  Frontend   │──────┐
└─────────────┘      │
                     │
                     ▼
              ┌─────────────┐
              │  CloudFront │
              │   (CDN)     │
              └─────────────┘
                     │
                     ▼
              ┌─────────────┐
              │     ALB     │
              └─────────────┘
                     │
          ┏━━━━━━━━━━┻━━━━━━━━━━┓
          ▼                     ▼
    ┌──────────┐         ┌──────────┐
    │   ECS    │────────>│   ECS    │
    │  Task 1  │         │  Task 2  │
    └──────────┘         └──────────┘
          │                     │
          └──────────┬──────────┘
                     │
          ┏━━━━━━━━━━┻━━━━━━━━━━┓
          ▼                     ▼
    ┌──────────┐         ┌──────────┐
    │   RDS    │         │  Redis   │
    │PostgreSQL│         │(ElastiCache)
    │(Multi-AZ)│         └──────────┘
    └──────────┘
          │
          ▼
    ┌──────────┐
    │    S3    │
    │  (PDFs)  │
    └──────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15
- Docker (optional, for local databases)
- AWS CLI (for deployment)

### Automated Setup

```bash
# Clone repository
git clone https://github.com/yourusername/rmc-manager.git
cd rmc-manager

# Run setup script (sets up everything automatically)
chmod +x setup.sh
./setup.sh

# Start application
./start-all.sh
```

The setup script will:
1. Create Python virtual environment
2. Install all dependencies
3. Set up PostgreSQL and Redis (Docker)
4. Run database migrations
5. Create startup scripts

### Manual Setup

If you prefer manual setup:

#### 1. Backend Setup

```bash
# Create and activate virtual environment
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements/development.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

#### 2. Frontend Setup

```bash
# Install dependencies
cd frontend
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with API URL

# Start development server
npm start
```

#### 3. Database Setup (Docker)

```bash
# Start PostgreSQL and Redis
docker-compose up -d

# Check status
docker-compose ps
```

### Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000/api/v1/
- **Django Admin:** http://localhost:8000/admin/

---

## 📂 Project Structure

```
rmc-manager/
├── backend/                    # Django backend
│   ├── config/                # Project configuration
│   │   ├── settings/          # Environment-specific settings
│   │   │   ├── base.py       # Shared settings
│   │   │   ├── development.py
│   │   │   ├── staging.py
│   │   │   └── production.py
│   │   ├── urls.py           # URL routing
│   │   └── wsgi.py
│   ├── apps/                  # Django applications
│   │   ├── tenants/          # Tenant management
│   │   ├── users/            # User authentication
│   │   ├── residents/        # Resident profiles
│   │   ├── menus/            # Menu management
│   │   ├── orders/           # Meal ordering
│   │   ├── kitchen/          # Kitchen production
│   │   ├── audit/            # Audit logging
│   │   └── core/             # Shared utilities
│   ├── middleware/            # Custom middleware
│   │   ├── tenant_isolation.py
│   │   └── audit_logging.py
│   ├── tests/                 # Test suite
│   │   ├── test_tenant_isolation.py
│   │   ├── test_authentication.py
│   │   ├── test_meal_ordering.py
│   │   └── ...
│   ├── requirements/          # Python dependencies
│   │   ├── base.txt
│   │   ├── development.txt
│   │   └── production.txt
│   ├── Dockerfile            # Backend container
│   ├── manage.py
│   └── pytest.ini
├── frontend/                  # React frontend
│   ├── public/
│   ├── src/
│   │   ├── api/              # API client
│   │   ├── components/       # React components
│   │   │   ├── common/       # Reusable components
│   │   │   ├── layout/       # Layout components
│   │   │   └── features/     # Feature components
│   │   │       ├── auth/
│   │   │       ├── residents/
│   │   │       ├── orders/
│   │   │       └── kitchen/
│   │   ├── hooks/            # Custom React hooks
│   │   ├── store/            # Redux store
│   │   ├── types/            # TypeScript types
│   │   ├── utils/            # Utility functions
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── package.json
│   └── tsconfig.json
├── infrastructure/            # Infrastructure as Code
│   ├── terraform/            # Terraform configurations
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── modules/
│   └── docker-compose.yml    # Local development
├── docs/                      # Documentation
│   ├── deployment-guide.md   # AWS deployment guide
│   ├── testing-checklist.md  # Testing procedures
│   ├── api-documentation.md  # API reference
│   ├── user-guide.md         # End-user documentation
│   └── architecture.md       # Architecture details
├── scripts/                   # Utility scripts
│   ├── setup.sh             # Automated setup
│   ├── deploy.sh            # Deployment script
│   └── backup.sh            # Backup script
├── .github/                   # GitHub Actions
│   └── workflows/
│       ├── ci.yml           # Continuous Integration
│       ├── deploy-staging.yml
│       └── deploy-production.yml
├── .gitignore
├── README.md                 # This file
└── LICENSE
```

---

## 🧪 Testing

### Run All Tests

```bash
# Backend tests
cd backend
source venv/bin/activate
pytest

# With coverage report
pytest --cov=. --cov-report=html

# Frontend tests
cd frontend
npm test

# E2E tests
npm run test:e2e
```

### Critical Test Suites

#### 1. Tenant Isolation Tests
```bash
pytest tests/test_tenant_isolation.py -v
```
**Critical:** Ensures no cross-tenant data access.

#### 2. Security Tests
```bash
pytest tests/test_security.py -v
```
Tests for SQL injection, XSS, CSRF, and authentication bypass.

#### 3. Clinical Validation Tests
```bash
pytest tests/test_iddsi_validation.py -v
pytest tests/test_allergy_validation.py -v
```
Ensures IDDSI and allergy validations work correctly.

### Load Testing

```bash
# Install locust
pip install locust

# Run load test
locust -f tests/load_test.py --host=http://localhost:8000
```

Open http://localhost:8089 and configure:
- **Users:** 100
- **Spawn rate:** 10 users/second
- **Duration:** 5 minutes

**Target:** 95th percentile response time < 2 seconds

---

## 🚢 Deployment

### AWS Deployment (Production)

Full deployment guide: [docs/deployment-guide.md](docs/deployment-guide.md)

#### Quick Deploy to AWS

```bash
# 1. Configure AWS credentials
aws configure

# 2. Build and push Docker image
cd backend
./scripts/build-and-push.sh

# 3. Deploy infrastructure (if using Terraform)
cd infrastructure/terraform
terraform init
terraform apply

# 4. Deploy application
cd ../..
./scripts/deploy.sh production

# 5. Run smoke tests
./scripts/smoke-test.sh https://your-domain.com
```

#### Infrastructure Components

- **ECS Fargate:** Auto-scaling containerized backend (2-10 tasks)
- **RDS PostgreSQL:** Multi-AZ deployment with automated backups
- **ElastiCache Redis:** Session storage and caching
- **ALB:** Load balancing with SSL termination
- **S3:** Static assets and PDF storage
- **CloudFront:** CDN for frontend
- **CloudWatch:** Logging and monitoring

### Environment Variables

#### Backend (.env)
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com

DB_NAME=rmc_manager
DB_USER=rmc_admin
DB_PASSWORD=secure-password
DB_HOST=your-rds-endpoint.rds.amazonaws.com
DB_PORT=5432

JWT_SECRET_KEY=your-jwt-secret

AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=rmc-manager-media
AWS_S3_REGION_NAME=us-east-1

REDIS_URL=redis://your-redis-endpoint:6379/0
```

#### Frontend (.env)
```env
REACT_APP_API_URL=https://api.yourdomain.com/api/v1
```

---

## 📊 Database Schema

### Core Entities

- **Tenant** - Multi-tenant isolation
- **User** - Authentication and roles
- **Resident** - Resident profiles with dietary requirements
- **Wing / Room** - Facility structure
- **Menu / MenuItem** - Daily menus with IDDSI tagging
- **MealOrder / MealOrderComponent** - Meal selections
- **Supplement** - Nutritional supplements
- **AuditLog** - Immutable audit trail
- **WingSubmission** - Meal sheet submissions

### Entity Relationship Diagram

Full ERD available in: [docs/architecture.md](docs/architecture.md)

**Key Relationships:**
- All entities have `tenant_id` for isolation
- Residents → Wings → Rooms (facility hierarchy)
- MealOrder → Resident (one order per meal per resident)
- MealOrderComponent → MenuItem (selected components)
- ResidentAllergy/Preference/Supplement → Resident

---

## 🔐 Security

### Authentication
- JWT-based authentication
- Token expiry: 1 hour (access), 7 days (refresh)
- Password hashing: Argon2
- Password complexity requirements enforced

### Authorization
- Role-based access control (RBAC)
- Tenant isolation enforced at middleware level
- Query-level filtering by tenant_id
- No cross-tenant data access possible

### Security Features
- ✅ HTTPS enforced (TLS 1.2+)
- ✅ CORS protection
- ✅ CSRF protection
- ✅ SQL injection prevention (ORM)
- ✅ XSS prevention (template escaping)
- ✅ Rate limiting (100 req/min per user)
- ✅ Account lockout after 5 failed attempts
- ✅ Encrypted database connections
- ✅ Encrypted data at rest (RDS/S3)

### Compliance
- **Audit Logs:** Immutable, 7-year retention
- **Data Isolation:** Automated tenant isolation tests
- **Clinical Safety:** IDDSI and allergy validation
- **Privacy:** GDPR/Privacy Act compliant architecture

---

## 📖 API Documentation

### Base URL
```
Production:  https://api.yourdomain.com/api/v1
Staging:     https://staging-api.yourdomain.com/api/v1
Development: http://localhost:8000/api/v1
```

### Authentication

All endpoints require JWT authentication except `/auth/login/` and `/auth/refresh/`.

**Login:**
```bash
POST /api/v1/auth/login/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Authenticated Request:**
```bash
GET /api/v1/residents/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

### Core Endpoints

#### Residents
```
GET    /api/v1/residents/              List residents
POST   /api/v1/residents/              Create resident
GET    /api/v1/residents/{id}/         Get resident details
PATCH  /api/v1/residents/{id}/         Update resident
DELETE /api/v1/residents/{id}/         Delete resident
GET    /api/v1/residents/{id}/allergies/  Get allergies
POST   /api/v1/residents/{id}/allergies/  Add allergy
```

#### Menus
```
GET    /api/v1/menus/                  List menus
POST   /api/v1/menus/                  Create menu
GET    /api/v1/menus/{id}/             Get menu details
PATCH  /api/v1/menus/{id}/             Update menu
GET    /api/v1/menus/{id}/items/       Get menu items
POST   /api/v1/menus/{id}/publish/     Publish menu
```

#### Orders
```
GET    /api/v1/orders/                 List orders
POST   /api/v1/orders/                 Create order
GET    /api/v1/orders/{id}/            Get order details
PATCH  /api/v1/orders/{id}/            Update order
POST   /api/v1/orders/validate/        Validate selection
```

#### Kitchen
```
GET    /api/v1/kitchen/production-summary/  Production summary
POST   /api/v1/kitchen/generate-labels/     Generate tray labels
GET    /api/v1/kitchen/production-report/   Detailed report
```

#### Audit
```
GET    /api/v1/audit-logs/             List audit logs
GET    /api/v1/audit-logs/?entity_type=meal_order  Filter logs
GET    /api/v1/audit-logs/?user={id}   Logs by user
```

Full API documentation: [docs/api-documentation.md](docs/api-documentation.md)

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Workflow

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Write/update tests**
5. **Ensure all tests pass**
   ```bash
   pytest
   npm test
   ```
6. **Commit with meaningful messages**
   ```bash
   git commit -m "feat: add IDDSI validation for beverages"
   ```
7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Open a Pull Request**

### Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Adding or updating tests
- `refactor:` Code refactoring
- `perf:` Performance improvements
- `chore:` Maintenance tasks

### Code Style

**Python:**
- Follow PEP 8
- Use Black for formatting: `black .`
- Use flake8 for linting: `flake8 .`
- Type hints where appropriate

**TypeScript/React:**
- Follow Airbnb style guide
- Use ESLint: `npm run lint`
- Use Prettier: `npm run format`

### Pull Request Checklist

- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] Code follows style guidelines
- [ ] No breaking changes (or clearly documented)
- [ ] Tenant isolation maintained (if touching core)
- [ ] Security implications considered

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

**Product Owner:** Yousuf Ali
**Technical Lead:** Ghazi Johar
**Backend Team:** Ghazi Johar
**Frontend Team:** Ghazi Johar
**DevOps:** Ghazi Johar


---

## 📞 Support

### Documentation
- [Deployment Guide](docs/deployment-guide.md)
- [Testing Guide](docs/testing-checklist.md)
- [API Documentation](docs/api-documentation.md)
- [User Guide](docs/user-guide.md)
- [Architecture Overview](docs/architecture.md)

### Contact
- **Email:** support@yourcompany.com
- **Issues:** [GitHub Issues](https://github.com/yourusername/rmc-manager/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/rmc-manager/discussions)

### Getting Help

1. Check the [documentation](docs/)
2. Search [existing issues](https://github.com/yourusername/rmc-manager/issues)
3. Ask in [discussions](https://github.com/yourusername/rmc-manager/discussions)
4. Open a new issue with detailed information

---

## 🗺️ Roadmap

### Phase 1: Production-Ready Internal Platform ✅
**Status:** In Development  
**Timeline:** Q1 2026

- [x] Multi-tenant architecture
- [x] Authentication & authorization
- [x] Resident management
- [x] Menu management
- [x] Meal ordering with validation
- [x] Kitchen production reports
- [x] Audit logging
- [ ] UAT and security testing
- [ ] Production deployment

### Phase 2: SaaS Expansion 🔄
**Status:** Planned  
**Timeline:** Q2-Q3 2026

- [ ] Public API with rate limiting
- [ ] OAuth2 & SSO
- [ ] Webhook integrations
- [ ] Tenant self-service portal
- [ ] Billing integration (Stripe)
- [ ] Advanced analytics dashboard
- [ ] Mobile app (React Native)

### Phase 3: Enterprise Features 📋
**Status:** Future  
**Timeline:** Q4 2026+

- [ ] White-labeling
- [ ] Multi-language support
- [ ] Integration marketplace
- [ ] Advanced reporting & BI
- [ ] AI-powered meal recommendations
- [ ] IoT kitchen equipment integration

---

## 🎯 Key Metrics

### Performance Targets
- API response time: < 2 seconds (p95)
- Page load time: < 3 seconds
- Uptime: 99.5%
- Database queries: < 100ms

### Scale Targets
- Venues: 200+
- Concurrent users: 500+
- Daily orders: 60,000+
- Database size: 500GB

---

## 📸 Screenshots

*Coming soon - screenshots will be added as the UI is developed*

---

## 🙏 Acknowledgments

- Django and Django REST Framework communities
- React and TypeScript communities
- All contributors and early adopters
- Aged care professionals who provided feedback

---

## ⚠️ Important Notes

### Security
- Never commit `.env` files
- Rotate secrets regularly
- Enable MFA for all admin accounts
- Review audit logs regularly

### Data Privacy
- Resident data is sensitive - treat accordingly
- Ensure GDPR/Privacy Act compliance
- Implement data retention policies
- Regular security audits required

### Clinical Safety
- IDDSI validation is critical - thoroughly test
- Allergy blocking must never fail
- All dietary restrictions must be enforced
- Production reports must be accurate

---

**Built with ❤️ for the aged care community**

Last Updated: February 16, 2026
