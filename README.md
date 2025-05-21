# JobMatchPro

*Connecting talent with opportunity through intelligent job matching*

![JobMatchPro Banner](/api/placeholder/900/300)

## Overview

JobMatchPro is a sophisticated job search platform that helps candidates find their ideal positions through an intelligent rating system. By analyzing multiple factors including job type, company fit, and keyword relevance, the platform delivers highly personalized job recommendations.

## Features

### Smart Filtering
Filter jobs by title, specialty, company, and more to narrow down your search to exactly what you're looking for.

### Intelligent Rating Engine
Our core algorithm dynamically scores job listings based on their relevance to your search parameters, ensuring the best matches appear first.

### Company Similarity Matching
When you search for positions at specific companies, we'll also show you opportunities at similar organizations that match your profile.

### Keyword-Based Relevance
The system identifies and prioritizes listings that align with your skills and interests, giving priority to positions that match your specified keywords.

### Clean Interface
A straightforward, intuitive interface that makes your job search experience efficient and frustration-free.

## Architecture

```
JobMatchPro/
├── cgi-bin/                # Backend processing 
│   ├── __init__.py         # Package initializer
│   ├── config.py           # Configuration settings
│   ├── db.py               # Database connection
│   ├── html_formatter.py   # Results presentation
│   ├── jobsearch.py        # Main CGI handler
│   ├── rating_engine.py    # Scoring algorithm
│   └── utils.py            # Helper functions
└── html/                   # Frontend interface
    └── job_search.html     # Search form
```

## The Rating Algorithm

Our rating system quantifies job relevance through a multi-factor approach:

**Base Score**: Every job starts with 100 points

**Job Type Analysis**:
- Exact Match: No deduction
- Partial Match: -10 points
- Mismatch: -30 points

**Company Relevance**:
- Exact Match: No deduction
- Similar Company: -15 points
- Different Company: -40 points

**Keyword Bonuses**:
- Keyword in Job Title: +10 points
- Keyword in Specialty: +8 points
- Keyword in Description: +6 points

Results are then sorted by descending score, delivering the most relevant matches first.

## Technology

- **Backend**: Python 3 with CGI
- **Database**: Oracle (via cx_Oracle)
- **Frontend**: HTML

## Setup

```bash
# Configure Oracle credentials
export ORACLE_USER="your_username"
export ORACLE_PASS="your_password"
export ORACLE_DSN="your_oracle_host/servicename"

# Install required dependencies
pip install cx_Oracle

# Deploy to your web server
cp -r JobMatchPro/cgi-bin/* /path/to/cgi-bin/
cp -r JobMatchPro/html/* /path/to/html/
```

## Example Search

When searching with these parameters:
```
Job Type: Regular
Job Title: Developer
Specialty: Web Development
Company: Google
Keyword: frontend
```

The algorithm works as follows:
1. Retrieves Developer positions in Web Development
2. Gives higher ratings to jobs at Google
3. Applies moderate ratings to jobs at similar companies (Microsoft, Meta)
4. Adds bonus points for mentions of "frontend" in the title, specialty, or description
5. Presents results sorted by relevance score

## Future Development

- User accounts with saved searches
- Mobile application 
- AI-powered recommendation engine
- Resume parsing and automatic matching
- Professional networking features

---

*JobMatchPro - Simplifying your job search through intelligent matching*
