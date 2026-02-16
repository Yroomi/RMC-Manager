# GitHub Setup Guide - RMC Manager

**Step-by-step instructions for publishing your project to GitHub**

---

## 📋 Prerequisites

- GitHub account ([sign up here](https://github.com/join) if needed)
- Git installed on your computer
- Project files ready to upload

---

## 🚀 Quick Setup (Recommended)

### Step 1: Create GitHub Repository

1. **Go to GitHub**: https://github.com/new
2. **Repository name**: `rmc-manager`
3. **Description**: `Multi-tenant meal management system for aged care facilities`
4. **Visibility**: 
   - ✅ **Public** (if open source)
   - OR **Private** (if keeping internal initially)
5. **Initialize repository**: 
   - ❌ **DO NOT** add README (we have one)
   - ❌ **DO NOT** add .gitignore (we have one)
   - ❌ **DO NOT** add license (we have one)
6. **Click "Create repository"**

### Step 2: Prepare Your Local Project

```bash
# Navigate to your project directory
cd /path/to/your/rmc-manager

# If you used the setup.sh script, you already have these files
# If not, copy the files from the GitHub repo template:
# - README.md
# - .gitignore
# - LICENSE
# - CONTRIBUTING.md
# - CHANGELOG.md
# - .github/workflows/ci.yml

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "feat: initial project setup with documentation"
```

### Step 3: Connect and Push to GitHub

```bash
# Add GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/rmc-manager.git

# Verify remote was added
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

**That's it!** Your project is now on GitHub. 🎉

---

## 📂 What Gets Pushed to GitHub

### Files Included ✅

```
rmc-manager/
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD automation
├── backend/                    # Django backend code
│   ├── config/
│   ├── apps/
│   ├── middleware/
│   ├── tests/
│   ├── requirements/
│   ├── Dockerfile
│   └── manage.py
├── frontend/                   # React frontend code
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── tsconfig.json
├── infrastructure/             # Terraform/Docker configs
│   ├── terraform/
│   └── docker-compose.yml
├── docs/                       # All documentation
│   ├── deployment-guide.md
│   ├── testing-checklist.md
│   └── ...
├── scripts/                    # Utility scripts
│   ├── setup.sh
│   └── deploy.sh
├── .gitignore                  # Files to exclude
├── README.md                   # Main documentation
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Contribution guidelines
└── CHANGELOG.md                # Version history
```

### Files Excluded ❌

Thanks to `.gitignore`, these won't be pushed:

- ❌ `.env` files (secrets/passwords)
- ❌ `venv/` (Python virtual environment)
- ❌ `node_modules/` (npm packages)
- ❌ `__pycache__/` (Python cache)
- ❌ `build/`, `dist/` (build artifacts)
- ❌ Database files
- ❌ Log files
- ❌ IDE settings
- ❌ `.DS_Store` (macOS)

---

## 🔒 Important Security Checks

### Before Pushing, Verify:

```bash
# Check what will be committed
git status

# Review files to be pushed
git diff --cached

# Search for potential secrets
git grep -i "password"
git grep -i "api_key"
git grep -i "secret"

# Make sure .env is not staged
git status | grep ".env"
```

### If You Accidentally Committed Secrets:

**DO NOT PUSH!** Remove them first:

```bash
# If not yet pushed
git reset HEAD~1  # Undo last commit
# Remove the secret from files
# Commit again

# If already pushed
# 1. Immediately rotate all exposed secrets/passwords
# 2. Use git filter-branch or BFG Repo-Cleaner to remove from history
# 3. Force push (dangerous - coordinate with team)
```

---

## ⚙️ Configure GitHub Repository Settings

### 1. Enable Branch Protection

**Settings → Branches → Add rule:**

- **Branch name pattern**: `main`
- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass before merging
  - Select: `backend-tests`, `frontend-tests`, `tenant-isolation-tests`
- ✅ Require branches to be up to date before merging
- ✅ Include administrators (optional but recommended)
- **Save changes**

### 2. Configure GitHub Actions

**Settings → Actions → General:**

- ✅ Allow all actions and reusable workflows
- ✅ Read and write permissions (for CI/CD)

### 3. Enable Security Features

**Settings → Code security and analysis:**

- ✅ Dependency graph
- ✅ Dependabot alerts
- ✅ Dependabot security updates
- ✅ Code scanning (CodeQL)
- ✅ Secret scanning

### 4. Set Up Project Board (Optional)

**Projects → New project:**

- **Template**: Team backlog
- **Track**: Issues and pull requests
- **Views**: Table, Board, Roadmap

### 5. Create Issue Templates

**Settings → Issues → Set up templates:**

Create templates for:
- Bug reports
- Feature requests
- Documentation improvements

---

## 👥 Invite Collaborators

### For Private Repository:

1. **Settings → Collaborators**
2. **Add people**
3. Enter GitHub username or email
4. Choose permission level:
   - **Read**: View only
   - **Write**: Push to repo
   - **Admin**: Full access

### For Public Repository:

- Anyone can fork and submit PRs
- Only maintainers can push directly

---

## 🏷️ Create First Release

### When Ready for v1.0.0:

```bash
# Create and push a tag
git tag -a v1.0.0 -m "Phase 1: Production-ready internal platform"
git push origin v1.0.0
```

**On GitHub:**

1. Go to **Releases**
2. **Draft a new release**
3. **Choose tag**: v1.0.0
4. **Release title**: "v1.0.0 - Phase 1 Release"
5. **Description**: 
   ```markdown
   ## 🎉 Phase 1: Production-Ready Internal Platform
   
   First production release of RMC Manager.
   
   ### Features
   - Multi-tenant architecture
   - Clinical safety validations (IDDSI, allergies)
   - Kitchen production forecasting
   - Audit compliance
   
   ### Installation
   See [Deployment Guide](docs/deployment-guide.md)
   
   ### Breaking Changes
   None (initial release)
   ```
6. **Publish release**

---

## 📊 Set Up GitHub Insights

### Enable Useful Insights:

1. **Insights → Community Standards**
   - Ensure all green checkmarks
   
2. **Insights → Traffic**
   - Monitor views, clones, referrers

3. **Insights → Contributors**
   - Track contributions

---

## 🔔 Configure Notifications

### Personal Settings:

1. **Settings → Notifications**
2. Configure how you want to be notified:
   - ✅ Email for mentions
   - ✅ Email for pull requests
   - ✅ Web notifications

### Watch Repository:

- Click **Watch** button
- Choose notification level:
  - **All Activity** (recommended for maintainers)
  - **Releases only**
  - **Ignore**

---

## 📝 Create Initial Issues

### Suggested First Issues:

```bash
# You can create these via GitHub web interface or GitHub CLI

gh issue create --title "Set up development environment" \
  --body "Follow setup.sh instructions" \
  --label "documentation"

gh issue create --title "Deploy to AWS staging" \
  --body "Follow deployment guide" \
  --label "infrastructure"

gh issue create --title "Run comprehensive testing" \
  --body "Complete testing checklist" \
  --label "testing"
```

---

## 🌐 Make Repository Discoverable

### 1. Add Topics

**Settings → About:**

Add topics (tags for discovery):
- `django`
- `react`
- `typescript`
- `healthcare`
- `aged-care`
- `meal-management`
- `multi-tenant`
- `aws`
- `iddsi`

### 2. Write Good Description

**Settings → About:**

**Short description:**
```
Multi-tenant meal management system for aged care facilities with IDDSI compliance
```

**Website:** (when deployed)
```
https://rmc-manager.yourcompany.com
```

### 3. Add Badges to README

Already included in README.md:
- License badge
- Python version
- Django version
- React version
- Build status (will show after first CI run)

---

## 🤖 Automate with GitHub Apps

### Recommended Apps:

1. **Codecov** - Code coverage reports
   - Install from GitHub Marketplace
   - Displays coverage in PRs

2. **Dependabot** - Dependency updates
   - Already enabled (built-in)
   - Auto-creates PRs for updates

3. **Snyk** - Security scanning (optional)
   - Additional security layer
   - Scans dependencies

---

## 📱 GitHub Mobile App

Download GitHub mobile app:
- **iOS**: App Store
- **Android**: Google Play

**Benefits:**
- Review PRs on the go
- Respond to comments
- Merge PRs
- Get notifications

---

## 🔄 Workflow After Setup

### Daily Development:

```bash
# 1. Pull latest changes
git pull origin main

# 2. Create feature branch
git checkout -b feature/my-feature

# 3. Make changes and commit
git add .
git commit -m "feat: implement new feature"

# 4. Push to GitHub
git push origin feature/my-feature

# 5. Create Pull Request on GitHub
# 6. Wait for CI checks and reviews
# 7. Merge when approved
```

### Team Collaboration:

1. **Create issue** for feature/bug
2. **Assign to team member**
3. **Create branch** from issue
4. **Develop and test**
5. **Open PR** referencing issue
6. **Review and approve**
7. **Merge** and close issue
8. **Update CHANGELOG.md**

---

## 🆘 Troubleshooting

### "Authentication failed"

```bash
# Option 1: Use personal access token
# GitHub Settings → Developer settings → Personal access tokens → Generate new token
# Use token as password when pushing

# Option 2: Use SSH keys (recommended)
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to GitHub
# Settings → SSH and GPG keys → New SSH key

# Change remote to SSH
git remote set-url origin git@github.com:YOUR_USERNAME/rmc-manager.git
```

### "Large files rejected"

```bash
# Git rejects files > 100MB

# Remove large file
git rm --cached path/to/large/file

# Add to .gitignore
echo "path/to/large/file" >> .gitignore

# Commit
git add .gitignore
git commit -m "chore: remove large file"
```

### "Conflicts during push"

```bash
# Pull latest changes
git pull origin main --rebase

# Resolve conflicts
# Edit conflicting files
git add .
git rebase --continue

# Push
git push origin main
```

---

## 📚 Additional Resources

### Git/GitHub:
- [GitHub Docs](https://docs.github.com/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Learning Lab](https://lab.github.com/)

### CI/CD:
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [CI/CD Best Practices](https://github.com/marketplace?type=actions)

### Security:
- [GitHub Security Advisories](https://docs.github.com/en/code-security)
- [Secure Coding Practices](https://owasp.org/)

---

## ✅ Setup Checklist

Use this checklist to ensure everything is configured:

- [ ] Repository created on GitHub
- [ ] Local repository initialized
- [ ] All files committed
- [ ] Pushed to GitHub
- [ ] Branch protection enabled
- [ ] CI/CD pipeline working
- [ ] Security features enabled
- [ ] Collaborators invited
- [ ] Topics and description added
- [ ] Issue templates created
- [ ] README.md displays correctly
- [ ] License is correct
- [ ] .gitignore working (no secrets pushed)
- [ ] First issue created
- [ ] Documentation reviewed

---

## 🎉 You're All Set!

Your project is now on GitHub and ready for collaboration!

**Next steps:**
1. Share repository with team
2. Start development workflow
3. Deploy to staging environment
4. Begin testing phase

**Need help?**
- [GitHub Community Forum](https://github.community/)
- [GitHub Support](https://support.github.com/)

---

**Happy coding!** 🚀
