# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup
- Multi-tenant architecture with strict isolation
- JWT-based authentication system
- Resident management with dietary requirements
- Menu management with IDDSI tagging
- Meal ordering with clinical validation
- Kitchen production forecasting
- Tray label generation (PDF)
- Supplement management
- Audit logging system
- Cut-off time enforcement
- Wing-level meal sheet submission
- Role-based access control
- Responsive frontend (React + TypeScript)
- Comprehensive test suite
- CI/CD pipeline with GitHub Actions
- AWS deployment infrastructure (Terraform)
- Complete documentation

### Changed
- N/A (initial release)

### Deprecated
- N/A (initial release)

### Removed
- N/A (initial release)

### Fixed
- N/A (initial release)

### Security
- Implemented tenant isolation at all levels
- Added CSRF protection
- Implemented rate limiting
- Added input validation and sanitization
- Enabled HTTPS enforcement
- Configured secure headers

---

## [0.1.0] - 2026-02-16

### Added
- Project initialization
- Repository structure
- Documentation framework
- Development environment setup scripts

---

## Version History

- **v0.1.0** - Initial project setup and documentation
- **v1.0.0** (Planned) - Phase 1: Production-ready internal platform
- **v2.0.0** (Planned) - Phase 2: SaaS expansion with public API

---

## How to Update This Changelog

When making changes:

1. **Add entries under [Unreleased]** section
2. **Use these categories:**
   - `Added` - New features
   - `Changed` - Changes to existing functionality
   - `Deprecated` - Soon-to-be removed features
   - `Removed` - Removed features
   - `Fixed` - Bug fixes
   - `Security` - Security improvements

3. **Follow this format:**
   ```markdown
   ### Added
   - New feature description [#PR_NUMBER](link-to-pr)
   - Another feature [#PR_NUMBER](link-to-pr)
   ```

4. **When releasing a version:**
   - Move [Unreleased] items to a new version section
   - Add release date
   - Create new [Unreleased] section
   - Update version links at bottom

### Example Entry

```markdown
## [1.2.0] - 2026-03-15

### Added
- IDDSI validation for beverages [#123](https://github.com/user/repo/pull/123)
- Fluid restriction warnings in carer dashboard [#124](https://github.com/user/repo/pull/124)

### Fixed
- Resolved tenant isolation bug in audit logs [#125](https://github.com/user/repo/pull/125)
- Fixed PDF generation timeout for large orders [#126](https://github.com/user/repo/pull/126)

### Security
- Updated Django to 5.0.2 for security patches [#127](https://github.com/user/repo/pull/127)
```

---

[Unreleased]: https://github.com/yourusername/rmc-manager/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/yourusername/rmc-manager/releases/tag/v0.1.0
