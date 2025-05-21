# ✨ JobMatchPro ✨

> *Connecting talent with opportunity through intelligent job matching*

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)

<div align="center">
  <img src="/api/placeholder/800/300" alt="JobMatchPro Banner" />
</div>

## 🚀 Overview

**JobMatchPro** is an advanced job search platform with intelligent rating and matching capabilities. The system helps job seekers find the perfect position by applying a sophisticated rating algorithm that considers multiple factors including job type, company preferences, and keyword relevance.

## ✨ Features

- **Smart Filtering** — Filter jobs by title, specialty, company, and more
- **Intelligent Rating Engine** — Jobs are automatically ranked based on relevance to your search
- **Company Similarity Matching** — Find jobs at companies similar to your preferred employers
- **Keyword-Based Relevance** — Prioritizes listings that match your skills and interests
- **Clean, User-Friendly Interface** — Simple yet powerful search options

## 🛠️ Architecture

JobMatchPro follows a clean, modular architecture:

```
JobMatchPro/
├── cgi-bin/               # Backend processing scripts
│   ├── __init__.py        # Package initializer
│   ├── config.py          # Configuration settings
│   ├── db.py              # Database connection and queries
│   ├── html_formatter.py  # HTML output generation
│   ├── jobsearch.py       # Main CGI handler
│   ├── rating_engine.py   # Job relevance algorithm
│   └── utils.py           # Utility functions
└── html/                  # Frontend files
    └── job_search.html    # Search form interface
```

## 💡 How It Works

1. **User Query** — Users input their job preferences through the search form
2. **Database Search** — System queries the Oracle database for matching positions
3. **Rating Application** — Each job is rated based on match quality:
   - Job type match (0 to -30 points)
   - Company match (0 to -40 points)
   - Keyword relevance (up to +24 bonus points)
4. **Results Rendering** — Jobs are displayed in order of relevance score

## ⚙️ Technology Stack

- **Backend**: Python 3 with CGI
- **Database**: Oracle (via cx_Oracle)
- **Frontend**: HTML

## 🚀 Getting Started

1. Configure your Oracle database credentials in the environment:
   ```bash
   export ORACLE_USER="your_username"
   export ORACLE_PASS="your_password"
   export ORACLE_DSN="your_oracle_host/servicename"
   ```

2. Ensure Python and required packages are installed:
   ```bash
   pip install cx_Oracle
   ```

3. Place the application files in your web server's CGI directory

4. Navigate to `job_search.html` in your browser to begin

## 🔍 Search Example

```
Job Type: Regular
Job Title: Developer
Specialty: Web Development
Company: Google
Keyword: frontend
```

This query will return web development positions with higher ratings for:
- Jobs that include "frontend" in the title, specialty, or description
- Exact matches at Google
- Similar matches at companies like Microsoft, Meta, etc.

## 🌟 Future Enhancements

- User accounts and saved searches
- Mobile application
- ML-based recommendation engine
- Integration with professional networking platforms
- Expanded similar companies database

---

<div align="center">
  <p>Developed with ❤️ by Your Team</p>
</div>
