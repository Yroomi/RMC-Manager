# Project Structure

Complete directory structure for RMC Manager repository.

## Overview

```
rmc-manager/
├── .github/                    # GitHub configuration
│   └── workflows/
│       └── ci.yml             # CI/CD pipeline
├── backend/                    # Django backend
├── frontend/                   # React frontend
├── infrastructure/             # IaC and deployment
├── docs/                       # Documentation
├── scripts/                    # Utility scripts
├── .gitignore                  # Git ignore rules
├── README.md                   # Main documentation
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Contribution guide
├── CHANGELOG.md                # Version history
├── GITHUB_SETUP.md            # GitHub setup guide
└── STRUCTURE.md               # This file
```

## Detailed Structure

### Backend (Django)

```
backend/
├── config/                     # Project configuration
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py            # Shared settings
│   │   ├── development.py     # Dev settings
│   │   ├── staging.py         # Staging settings
│   │   └── production.py      # Prod settings
│   ├── urls.py                # Main URL routing
│   ├── wsgi.py                # WSGI config
│   └── asgi.py                # ASGI config
├── apps/                       # Django applications
│   ├── tenants/               # Tenant management
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── tests/
│   ├── users/                 # User auth
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── tests/
│   ├── residents/             # Resident profiles
│   ├── menus/                 # Menu management
│   ├── orders/                # Meal ordering
│   ├── kitchen/               # Kitchen production
│   ├── audit/                 # Audit logging
│   └── core/                  # Shared utilities
├── middleware/                 # Custom middleware
│   ├── __init__.py
│   ├── tenant_isolation.py
│   └── audit_logging.py
├── tests/                      # Test suite
│   ├── conftest.py            # Pytest fixtures
│   ├── test_tenant_isolation.py
│   ├── test_authentication.py
│   ├── test_meal_ordering.py
│   ├── integration/
│   └── load_test.py
├── requirements/               # Python dependencies
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── Dockerfile                  # Backend container
├── .dockerignore
├── manage.py                   # Django management
├── pytest.ini                  # Pytest config
├── .env.example               # Example environment vars
└── README.md                   # Backend-specific docs
```

### Frontend (React)

```
frontend/
├── public/
│   ├── index.html
│   ├── manifest.json
│   └── robots.txt
├── src/
│   ├── api/                   # API client layer
│   │   ├── client.ts          # Axios instance
│   │   ├── auth.ts            # Auth endpoints
│   │   ├── residents.ts       # Resident endpoints
│   │   ├── orders.ts          # Order endpoints
│   │   └── kitchen.ts         # Kitchen endpoints
│   ├── components/            # React components
│   │   ├── common/            # Reusable components
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   ├── Table.tsx
│   │   │   └── Alert.tsx
│   │   ├── layout/            # Layout components
│   │   │   ├── Header.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   └── Layout.tsx
│   │   └── features/          # Feature components
│   │       ├── auth/
│   │       │   ├── LoginForm.tsx
│   │       │   └── LoginForm.test.tsx
│   │       ├── residents/
│   │       │   ├── ResidentList.tsx
│   │       │   └── ResidentForm.tsx
│   │       ├── orders/
│   │       │   ├── WingSheetView.tsx
│   │       │   └── MealOrderForm.tsx
│   │       └── kitchen/
│   │           ├── ProductionSummary.tsx
│   │           └── TrayLabels.tsx
│   ├── hooks/                 # Custom React hooks
│   │   ├── useAuth.ts
│   │   ├── useTenant.ts
│   │   └── useOrders.ts
│   ├── store/                 # Redux store
│   │   ├── store.ts
│   │   ├── authSlice.ts
│   │   └── ordersSlice.ts
│   ├── types/                 # TypeScript types
│   │   ├── resident.ts
│   │   ├── order.ts
│   │   ├── menu.ts
│   │   └── user.ts
│   ├── utils/                 # Utility functions
│   │   ├── validation.ts
│   │   ├── formatting.ts
│   │   └── constants.ts
│   ├── App.tsx                # Main App component
│   ├── App.test.tsx
│   ├── index.tsx              # Entry point
│   └── setupTests.ts
├── package.json                # npm dependencies
├── package-lock.json
├── tsconfig.json              # TypeScript config
├── tailwind.config.js         # Tailwind config
├── postcss.config.js
├── .env.example               # Example env vars
└── README.md                  # Frontend-specific docs
```

### Infrastructure

```
infrastructure/
├── terraform/                  # Terraform IaC
│   ├── main.tf                # Main config
│   ├── variables.tf           # Variables
│   ├── outputs.tf             # Outputs
│   ├── backend.tf             # State backend
│   ├── modules/               # Terraform modules
│   │   ├── vpc/
│   │   ├── rds/
│   │   ├── ecs/
│   │   └── s3/
│   └── environments/
│       ├── dev.tfvars
│       ├── staging.tfvars
│       └── production.tfvars
├── docker-compose.yml         # Local dev services
├── docker-compose.override.yml.example
└── kubernetes/                # K8s configs (future)
    ├── deployment.yaml
    └── service.yaml
```

### Documentation

```
docs/
├── deployment-guide.md        # AWS deployment
├── testing-checklist.md       # Testing procedures
├── api-documentation.md       # API reference
├── architecture.md            # Architecture details
├── user-guide/                # User documentation
│   ├── carer-guide.md
│   ├── kitchen-guide.md
│   └── admin-guide.md
├── developer-guide/           # Developer docs
│   ├── setup.md
│   ├── coding-standards.md
│   └── troubleshooting.md
└── images/                    # Documentation images
    ├── architecture-diagram.png
    └── screenshots/
```

### Scripts

```
scripts/
├── setup.sh                   # Automated setup
├── deploy.sh                  # Deployment script
├── backup.sh                  # Backup script
├── smoke-test.sh             # Smoke tests
├── build-and-push.sh         # Docker build/push
└── utils/
    ├── db-migrate.sh
    └── reset-dev-db.sh
```

## File Naming Conventions

### Python/Django
- **Models**: `models.py` (lowercase)
- **Views**: `views.py`
- **Tests**: `test_*.py`
- **Apps**: lowercase, plural (e.g., `residents/`)

### TypeScript/React
- **Components**: `PascalCase.tsx` (e.g., `ResidentForm.tsx`)
- **Hooks**: `camelCase.ts` with `use` prefix (e.g., `useAuth.ts`)
- **Utils**: `camelCase.ts` (e.g., `validation.ts`)
- **Tests**: `*.test.tsx` or `*.spec.tsx`

### Configuration
- **Environment**: `.env`, `.env.example`
- **Config files**: lowercase with extension (e.g., `tsconfig.json`)

### Documentation
- **All docs**: `kebab-case.md` (e.g., `deployment-guide.md`)

## Key Files Explained

### Root Level

- **README.md**: Main project documentation, first thing people see
- **LICENSE**: MIT License - defines usage terms
- **CONTRIBUTING.md**: How to contribute to the project
- **CHANGELOG.md**: Track changes between versions
- **.gitignore**: Files/folders to exclude from Git
- **GITHUB_SETUP.md**: Guide for setting up GitHub repo

### Backend

- **manage.py**: Django command-line utility
- **requirements/**: Separate dependencies per environment
- **Dockerfile**: Container definition for backend
- **pytest.ini**: Pytest configuration
- **.env.example**: Template for environment variables

### Frontend

- **package.json**: npm dependencies and scripts
- **tsconfig.json**: TypeScript compiler configuration
- **tailwind.config.js**: Tailwind CSS customization

### Infrastructure

- **terraform/**: Infrastructure as Code for AWS
- **docker-compose.yml**: Local development services

## Environment-Specific Files

Files that differ per environment:

| File | Dev | Staging | Prod | Example |
|------|-----|---------|------|---------|
| `.env` | ✓ | ✓ | ✓ | ✓ |
| `settings.py` | ✓ | ✓ | ✓ | - |
| `.tfvars` | ✓ | ✓ | ✓ | - |

**Note**: Never commit actual `.env` files - only `.env.example`

## Generated Files (Not in Git)

These are created during development/build:

```
# Backend
backend/venv/                  # Virtual environment
backend/__pycache__/           # Python cache
backend/staticfiles/           # Collected static files
backend/media/                 # User uploads
backend/.coverage              # Coverage data
backend/htmlcov/              # Coverage reports

# Frontend
frontend/node_modules/         # npm packages
frontend/build/                # Production build
frontend/coverage/             # Test coverage

# Database
*.sqlite3                      # SQLite databases
*.db

# Infrastructure
infrastructure/terraform/.terraform/  # Terraform cache
infrastructure/terraform/*.tfstate    # State files
```

## Adding New Files

### New Django App

```bash
cd backend
python manage.py startapp new_app
```

Creates:
```
new_app/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── views.py
├── tests.py
└── migrations/
    └── __init__.py
```

Then:
1. Add to `INSTALLED_APPS` in `settings/base.py`
2. Create `serializers.py` for API
3. Create `urls.py` for routing
4. Add `tests/` directory for tests

### New React Component

```bash
cd frontend/src/components/features
mkdir new_feature
```

Create:
```
new_feature/
├── NewFeature.tsx             # Main component
├── NewFeature.test.tsx        # Tests
├── NewFeature.module.css      # Styles (if not using Tailwind)
└── index.ts                   # Barrel export
```

## Directory Best Practices

1. **Keep it organized**: Group related files together
2. **Consistent naming**: Follow conventions
3. **Small modules**: Break large files into smaller ones
4. **Tests near code**: Keep tests close to what they test
5. **Shared code**: Put reusable code in `common/` or `utils/`
6. **Documentation**: Include README in complex directories

## Quick Reference

**Most Important Files:**
- `README.md` - Start here
- `GITHUB_SETUP.md` - Setup GitHub
- `docs/deployment-guide.md` - Deploy to AWS
- `docs/testing-checklist.md` - Test the system
- `scripts/setup.sh` - Automated setup

**Entry Points:**
- Backend: `backend/manage.py`
- Frontend: `frontend/src/index.tsx`
- Tests: `backend/pytest.ini`, `frontend/package.json`

**Configuration:**
- Backend: `backend/config/settings/`
- Frontend: `frontend/src/api/client.ts`
- Infrastructure: `infrastructure/terraform/`
