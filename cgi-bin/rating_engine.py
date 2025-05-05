# rating_engine.py

from utils import similar_companies, normalize_text

def apply_ratings(jobs, job_type=None, company=None, keyword=None):
    rated_jobs = []

    for job in jobs:
        rating = 100  # Start with full rating

        # Normalize fields for consistent comparison
        job_type_field = normalize_text(job.get("job_type", ""))
        company_field = normalize_text(job.get("company", ""))
        job_title = normalize_text(job.get("job_title", ""))
        specialty = normalize_text(job.get("specialty", ""))
        description = normalize_text(job.get("description", ""))

        # 1. Job Type Rating
        if job_type and job_type.lower() != "all":
            job_type_input = normalize_text(job_type)
            if job_type_input == job_type_field:
                rating += 0  # Full match
            elif job_type_input in job_type_field or job_type_field in job_type_input:
                rating -= 10  # Related but not exact
            else:
                rating -= 30  # Mismatch

        # 2. Company Rating
        if company:
            company_input = normalize_text(company)
            if company_input == company_field:
                rating += 0  # Exact match
            elif company_input in similar_companies:
                if company_field in similar_companies[company_input]:
                    rating -= 15  # Similar company
                else:
                    rating -= 40  # Not similar
            else:
                rating -= 40

        # 3. Keyword Relevance
        if keyword:
            keyword = normalize_text(keyword)
            if keyword in job_title:
                rating += 10
            if keyword in specialty:
                rating += 8
            if keyword in description:
                rating += 6

        # Clamp rating between 0 and 100
        rating = max(0, min(100, rating))
        job["rating"] = rating
        rated_jobs.append(job)

    # Sort by descending rating
    rated_jobs.sort(key=lambda j: j["rating"], reverse=True)
    return rated_jobs
