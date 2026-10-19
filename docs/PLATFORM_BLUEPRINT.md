# Infinate360 platform blueprint (target state)

Status: design only. The live Academy site stays a static, validated Python build (`src/build.py`). Rebuild phases below move to Next.js/Postgres only when each phase is approved and tested.

## 1. Folder structure (target)
```
app/                 Next.js App Router: (marketing) (academy) (corporate) (portal) api/
components/          ui/ (shadcn), seo/, lms/, forms/
lib/                 db.ts auth.ts seo.ts payments/ (stripe.ts razorpay.ts) ai/ (claude.ts openai.ts)
content/             mdx/ (guides, blog, case-studies) data/ (verified-claims.json)
prisma/              schema.prisma migrations/
scripts/             validate-seo.ts generate-candidates.ts
n8n/                 lead-qualification, content-generation, publish-revalidate
docs/  tests/  public/
```

## 2. Database schema (Prisma, core tables)
User(id, email, name, role[STUDENT|INSTRUCTOR|ADMIN|CORP_ADMIN|RECRUITER], orgId?) · Organization(id, name, plan) · Course(id, slug, title, level, hours, status) · Module(id, courseId, order, title) · Lesson(id, moduleId, order, type, videoRef) · Enrollment(id, userId, courseId, status) · Progress(id, userId, lessonId, completedAt) · Assessment/Attempt · Order(id, userId, provider[STRIPE|RAZORPAY], providerRef, amount, currency, status) · Lead(id, source, utm, service, consent, status, crmId) · Post(id, type, slug, status, authorId, reviewedAt) · Faq(id, pageId, q, a, reviewed) · Job(id, company, title, url, status) · CommunityThread/Reply · AuditLog.
Rules: no card data stored; payment providers hold it. Consent and source captured on every Lead.

## 3. Sitemap (public)
/ · /about · /consulting (+services) · /corporate-training · /academy (+programs, courses, tracks) · /community · /blog · /case-studies · /success-stories (only with consent) · /contact · /legal/*
Silos: Adobe (AEP, RTCDP, AJO, CJA, Target, Analytics, Launch, AEM) · AI (Agentic AI, MCP, GenAI, LangChain, CrewAI, AutoGen) · Data engineering (Snowflake, Databricks, Spark, Kafka, Airflow, Python). Each silo: pillar page, 5-15 child guides, related use cases, one program.

## 4. Wireframes (text)
Home: hero + 3 journeys (Consulting, Corporate training, Academy) · proof (verified only) · programs · free demo CTA · FAQ · footer.
Program page: answer box · fees/format card · curriculum accordion · audience · FAQ · enquiry form.
Student dashboard: continue-learning · progress · assessments · recordings · community.
Admin: leads · courses · orders · content queue (quality gate) · users. Corporate portal: cohort progress, seats, reports. Job portal: curated listings, saved, applications (only genuine listings).

## 5. API architecture
`POST /api/leads` (validate, rate-limit, store, queue CRM) · `GET /api/courses` · `POST /api/enroll` · `POST /api/checkout` (Stripe or Razorpay, server-side keys) · `POST /api/webhooks/{stripe,razorpay}` (signature verified) · `POST /api/chat` (retrieval + Claude, server-side key) · `POST /api/revalidate` (secret header) · admin routes behind auth + role checks. Secrets only in environment variables.

## 6. Content and SEO policy
Schemas: Organization, Person, Course, Article, Breadcrumb, FAQ only where visible and eligible; no Review schema without real, consented reviews. Publish by quality gate (distinct intent, sourced facts, duplicate and cannibalization check, internal links). Targets such as 100+ courses or 1000+ FAQs are candidate-inventory capacity, not publish quotas.
