# My 10x Solution - Sanjara

## The problem

Manually checking bdjobs and LinkedIn daily for AI/ML-relevant roles in
Bangladesh is slow and unfocused -- no personalized filtering, no tracking
of what's been applied to, no sense of true fit before spending time on
an application.

## The solution

A personal web app that scrapes fresh listings daily, scores each one's
relevance against my actual resume using an LLM, emails a daily digest of
the best matches, tracks application status, and drafts a tailored cover
letter per job on request.

## How it implements the required concepts

- API endpoints -- FastAPI backend
- Database -- Postgres (users, jobs, matches, applications)
- Authentication -- JWT built from scratch (bcrypt hashing, signed tokens)
- Background/cron jobs -- scheduled daily scrape + digest email
- LLM integration -- resume-to-job relevance scoring, cover letter drafting
- Web scraping -- bdjobs (primary) + LinkedIn (best-effort)
- Reporting -- daily digest email via Gmail SMTP

## What I'd do with more time

(to be filled in at submission time)