# Contributing to RMC Manager

Thank you for your interest in contributing to RMC Manager! This document provides guidelines and instructions for contributing.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Documentation](#documentation)
- [Security](#security)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards others

**Unacceptable behavior includes:**
- Harassment, trolling, or insulting comments
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

### Enforcement

Instances of unacceptable behavior may be reported to the project team at conduct@yourcompany.com. All complaints will be reviewed and investigated promptly and fairly.

---

## Getting Started

### Prerequisites

Before contributing, ensure you have:
- Python 3.11+
- Node.js 18+
- PostgreSQL 15
- Docker (optional)
- Git
- GitHub account

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/rmc-manager.git
   cd rmc-manager
   ```
3. **Add upstream remote:**
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/rmc-manager.git
   ```

### Setup Development Environment

Run the setup script:
```bash
chmod +x setup.sh
./setup.sh
```

Or follow manual setup in [README.md](README.md).

### Keep Your Fork Updated

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

---

## Development Process

### 1. Choose or Create an Issue

- Browse [existing issues](https://github.com/yourusername/rmc-manager/issues)
- Comment on an issue you'd like to work on
- Wait for assignment/approval
- Or create a new issue for discussion

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Branch naming conventions:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `test/` - Test additions/updates
- `refactor/` - Code refactoring
- `perf/` - Performance improvements
- `chore/` - Maintenance tasks

### 3. Make Your Changes

- Write clean, maintainable code
- Follow coding standards (see below)
- Add/update tests
- Update documentation

### 4. Test Your Changes

```bash
# Backend tests
cd backend
source venv/bin/activate
pytest

# Frontend tests
cd frontend
npm test

# Linting
cd backend
black .
flake8 .

cd frontend
npm run lint
npm run format
```

### 5. Commit Your Changes

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git commit -m "feat: add IDDSI validation for beverages"
git commit -m "fix: resolve tenant isolation in audit logs"
git commit -m "docs: update API documentation for orders endpoint"
git commit -m "test: add unit tests for meal ordering"
```

**Commit message format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style (formatting, no logic change)
- `refactor`: Code refactoring
- `perf`: Performance improvement
- `test`: Adding/updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes
- `build`: Build system changes

**Examples:**
```
feat(orders): add fluid restriction validation

Implement validation to check daily fluid intake against
resident's fluid restriction limit. Warns carers when 
approaching limit and blocks orders that exceed it.

Closes #123
```

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Open a Pull Request

- Go to your fork on GitHub
- Click "Compare & pull request"
- Fill out the PR template
- Link related issues

---

## Pull Request Process

### PR Template

When opening a PR, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Closes #123

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests pass locally
- [ ] Dependent changes merged
```

### Review Process

1. **Automated Checks** - CI/CD pipeline runs
   - Linting
   - Tests
   - Security scans
   - Build verification

2. **Code Review** - At least one approval required
   - Maintainer reviews code
   - Provides feedback
   - Requests changes if needed

3. **Updates** - Make requested changes
   ```bash
   git add .
   git commit -m "fix: address review comments"
   git push origin feature/your-feature-name
   ```

4. **Merge** - Once approved:
   - Squash and merge (preferred)
   - Or rebase and merge
   - Delete branch after merge

### PR Guidelines

**Do:**
- Keep PRs small and focused
- Write descriptive PR titles
- Include tests
- Update documentation
- Respond to feedback promptly
- Test changes thoroughly

**Don't:**
- Submit large PRs (>500 lines)
- Mix multiple features in one PR
- Include unrelated changes
- Leave TODO comments
- Ignore CI failures

---

## Coding Standards

### Python (Backend)

**Style Guide:** PEP 8

**Tools:**
- **Black** for formatting: `black .`
- **flake8** for linting: `flake8 .`
- **isort** for import sorting: `isort .`

**Key Guidelines:**
```python
# Good
def calculate_meal_cost(resident_id: str, meal_type: str) -> Decimal:
    """
    Calculate total cost for a resident's meal.
    
    Args:
        resident_id: UUID of the resident
        meal_type: Type of meal (breakfast, lunch, dinner)
        
    Returns:
        Total meal cost as Decimal
        
    Raises:
        ResidentNotFound: If resident doesn't exist
        InvalidMealType: If meal type is invalid
    """
    resident = Resident.objects.get(id=resident_id)
    # ... implementation
    return cost

# Bad
def calc(r, m):
    # Does something
    return x
```

**Django Specific:**
- Use class-based views or ViewSets
- Keep business logic in models/services, not views
- Use Django ORM, avoid raw SQL
- Always use `select_related()` and `prefetch_related()` appropriately
- Add indexes for foreign keys and commonly queried fields

**Security:**
- Never use `objects.all()` without tenant filtering
- Always validate user input
- Use parameterized queries
- Sanitize output
- Check permissions in views

### TypeScript/React (Frontend)

**Style Guide:** Airbnb + Prettier

**Tools:**
- **ESLint**: `npm run lint`
- **Prettier**: `npm run format`

**Key Guidelines:**
```typescript
// Good
interface ResidentFormProps {
  resident?: Resident;
  onSubmit: (data: ResidentFormData) => Promise<void>;
  onCancel: () => void;
}

const ResidentForm: React.FC<ResidentFormProps> = ({
  resident,
  onSubmit,
  onCancel
}) => {
  const [loading, setLoading] = useState(false);
  
  const handleSubmit = async (data: ResidentFormData) => {
    setLoading(true);
    try {
      await onSubmit(data);
    } catch (error) {
      console.error('Failed to submit:', error);
    } finally {
      setLoading(false);
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      {/* ... */}
    </form>
  );
};

// Bad
const Form = (props: any) => {
  // ... poorly typed, unclear props
};
```

**React Specific:**
- Use functional components with hooks
- Properly type all props and state
- Use custom hooks for reusable logic
- Memoize expensive computations
- Handle loading and error states
- Clean up effects properly

**State Management:**
- Use React Query for server state
- Use Redux only for complex client state
- Keep state as local as possible
- Avoid prop drilling (use context when needed)

---

## Testing Requirements

### Backend Tests

**Required test types:**
- Unit tests for all business logic
- Integration tests for API endpoints
- Tenant isolation tests
- Security tests

**Coverage requirement:** 80% minimum

**Example:**
```python
# tests/test_meal_ordering.py

import pytest
from django.contrib.auth import get_user_model
from residents.models import Resident
from orders.models import MealOrder

User = get_user_model()

@pytest.mark.django_db
class TestMealOrdering:
    def test_create_order_success(self, tenant, carer_user, resident):
        """Test successful meal order creation."""
        order = MealOrder.objects.create(
            tenant=tenant,
            resident=resident,
            meal_type='lunch',
            order_date='2026-03-01'
        )
        
        assert order.tenant == tenant
        assert order.resident == resident
        assert not order.is_submitted
    
    def test_cannot_order_for_other_tenant_resident(
        self, tenant1, tenant2, carer_user1, resident2
    ):
        """Test tenant isolation in meal ordering."""
        with pytest.raises(PermissionDenied):
            MealOrder.objects.create(
                tenant=tenant1,
                resident=resident2,  # resident2 belongs to tenant2
                meal_type='lunch',
                order_date='2026-03-01'
            )
```

### Frontend Tests

**Required test types:**
- Unit tests for utilities and helpers
- Component tests with React Testing Library
- Integration tests for user flows

**Example:**
```typescript
// components/ResidentForm.test.tsx

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { ResidentForm } from './ResidentForm';

describe('ResidentForm', () => {
  it('validates required fields', async () => {
    const onSubmit = jest.fn();
    
    render(<ResidentForm onSubmit={onSubmit} />);
    
    fireEvent.click(screen.getByRole('button', { name: /submit/i }));
    
    await waitFor(() => {
      expect(screen.getByText(/first name is required/i)).toBeInTheDocument();
    });
    
    expect(onSubmit).not.toHaveBeenCalled();
  });
  
  it('submits form with valid data', async () => {
    const onSubmit = jest.fn();
    
    render(<ResidentForm onSubmit={onSubmit} />);
    
    fireEvent.change(screen.getByLabelText(/first name/i), {
      target: { value: 'John' }
    });
    fireEvent.change(screen.getByLabelText(/last name/i), {
      target: { value: 'Doe' }
    });
    
    fireEvent.click(screen.getByRole('button', { name: /submit/i }));
    
    await waitFor(() => {
      expect(onSubmit).toHaveBeenCalledWith({
        firstName: 'John',
        lastName: 'Doe'
      });
    });
  });
});
```

### Critical Tests

**Must include tests for:**
1. Tenant isolation
2. Authentication/authorization
3. IDDSI validation
4. Allergy validation
5. Audit logging

---

## Documentation

### Code Documentation

**Python:**
```python
def calculate_iddsi_compatibility(
    resident_level: str,
    item_levels: List[str]
) -> Tuple[bool, str]:
    """
    Check if menu item is compatible with resident's IDDSI level.
    
    IDDSI (International Dysphagia Diet Standardisation Initiative) defines
    standardized texture levels for food. This function validates whether
    a menu item's texture levels are safe for a resident.
    
    Args:
        resident_level: Resident's IDDSI level (e.g., 'level_4')
        item_levels: List of IDDSI levels the item is suitable for
        
    Returns:
        Tuple of (is_compatible, message):
        - is_compatible: True if item is safe for resident
        - message: Explanation of compatibility or reason for incompatibility
        
    Examples:
        >>> calculate_iddsi_compatibility('level_4', ['level_4', 'level_5'])
        (True, 'IDDSI compatible')
        
        >>> calculate_iddsi_compatibility('level_4', ['level_7'])
        (False, 'Item texture too difficult for resident')
    """
    # Implementation...
```

**TypeScript:**
```typescript
/**
 * Validates meal selection against resident's dietary requirements.
 * 
 * Checks IDDSI compatibility, allergen conflicts, and fluid restrictions.
 * Returns validation result with severity level and user-friendly messages.
 * 
 * @param resident - Resident with dietary requirements
 * @param menuItem - Selected menu item
 * @param existingOrders - Today's existing orders for fluid calculation
 * @returns Validation result with warnings and errors
 * 
 * @example
 * ```typescript
 * const result = validateMealSelection(resident, menuItem, orders);
 * if (!result.isValid) {
 *   showError(result.errors);
 * }
 * ```
 */
export function validateMealSelection(
  resident: Resident,
  menuItem: MenuItem,
  existingOrders: MealOrder[]
): ValidationResult {
  // Implementation...
}
```

### API Documentation

Update API documentation for:
- New endpoints
- Changed request/response formats
- New query parameters
- Authentication requirements

### User Documentation

Update user guides when:
- Adding new features
- Changing workflows
- Modifying UI significantly

---

## Security

### Security Requirements

**Never commit:**
- API keys or secrets
- Passwords
- Private keys
- Personal data
- `.env` files

**Always:**
- Use environment variables for secrets
- Sanitize user input
- Validate all data
- Check permissions
- Use parameterized queries
- Encrypt sensitive data
- Log security events

### Reporting Security Issues

**DO NOT** open a public issue for security vulnerabilities.

Instead, email: security@yourcompany.com

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We will:
1. Acknowledge within 48 hours
2. Investigate and provide updates
3. Fix and release patch
4. Credit you in release notes (if desired)

---

## Questions?

- 💬 [Discussions](https://github.com/yourusername/rmc-manager/discussions)
- 📧 Email: dev@yourcompany.com
- 📖 [Documentation](docs/)

---

**Thank you for contributing to RMC Manager!** 🎉
