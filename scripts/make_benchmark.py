#!/usr/bin/env python3
"""Writes data/seo/ai_citation_benchmark.csv: 100 customer questions, results columns EMPTY.
Results are filled only from real, dated observations (see docs/AI_CITATION_BENCHMARK.md). Nothing here is a result."""
import csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = {
 "Adobe Experience Platform": ["What is Adobe Experience Platform and what does it do?", "How does Adobe Experience Platform differ from Real-Time CDP?", "How do XDM schemas work in Adobe Experience Platform?",
   "What is the difference between an AEP schema and a dataset?", "How does identity resolution work in Adobe Experience Platform?", "How do I ingest batch data into Adobe Experience Platform?",
   "What are AEP sandboxes and how should I use them?", "How do I troubleshoot a failed batch ingestion in AEP?", "What is the Real-Time Customer Profile?", "How do merge policies work in AEP?",
   "How should I design an identity namespace strategy for AEP?", "What is the AEP data lake used for?"],
 "Real-Time CDP": ["What is Adobe Real-Time CDP?", "How do I build an audience in Adobe Real-Time CDP?", "What is the difference between batch, streaming and edge segmentation?",
   "How do destinations work in Adobe Real-Time CDP?", "How do I activate an audience to an advertising platform?", "How do I measure audience match rates at a destination?",
   "What consent controls does Real-Time CDP support?", "How do data usage labels and policies work in Adobe Experience Platform?", "How do I test that a blocked data use is really blocked?", "How do I make sure opted-out people leave an audience and its destinations?"],
 "Adobe Journey Optimizer": ["What is Adobe Journey Optimizer used for?", "What is the difference between an AJO campaign and a journey?", "How do I design a journey with suppression rules?",
   "How do I measure the effect of a journey using a holdout?", "How do I prevent customers receiving duplicate messages across journeys?", "What events does a journey need to start correctly?", "How do I test an AJO journey before launch?", "How do I choose between email, push and SMS in a journey?"],
 "Customer Journey Analytics and Adobe Analytics": ["What is Customer Journey Analytics?", "What is the difference between Customer Journey Analytics and Adobe Analytics?",
   "How do I migrate from Adobe Analytics to Customer Journey Analytics?", "What is a data view in Customer Journey Analytics?", "How does a CJA connection stitch cross-device data?",
   "Why do Adobe Analytics and CJA numbers differ?", "What is the difference between eVars and props?", "How do I backfill historical data into Customer Journey Analytics?", "How do I reconcile a CJA backfill against the source?", "How do I learn Analysis Workspace in Customer Journey Analytics?"],
 "Web SDK and data collection": ["What is the Adobe Experience Platform Web SDK?", "How do I migrate from AppMeasurement to the Web SDK?", "What is a datastream in Adobe Experience Platform?",
   "How do I validate Web SDK events in the browser?", "How do I design a data layer for Adobe Tags?", "How does the Web SDK handle consent?", "What is an ECID and how is it set?", "How do I debug a missing Web SDK event?", "How do I set up separate datastreams for staging and production?"],
 "Agentic AI and MCP": ["What is the Model Context Protocol?", "What is the difference between MCP and a REST API for AI agents?", "How can an AI agent safely access a customer data platform?",
   "What is an enterprise AI coworker?", "How do I scope an AI coworker for a marketing operations team?", "How do I add human approval to an AI agent workflow?", "How do I test an agentic AI implementation?",
   "What are the security risks of connecting an AI agent to company data?", "How do I protect an MCP server against prompt injection?", "What is agentic AI in marketing technology?", "What does human-in-the-loop mean for AI agents?"],
 "Customer 360 and data engineering": ["What is a Customer 360 architecture?", "How do I design a customer data model with identity keys?", "How do I load data incrementally into Snowflake?",
   "How do I connect Snowflake or BigQuery to a marketing technology stack?", "What is the difference between a CDP and a data warehouse?", "How do I prevent wrong merges in an identity graph?", "What does a MarTech data engineer do?", "What is an identity graph?"],
 "Enterprise architecture and consulting": ["How do I evaluate a MarTech consulting engagement?", "What should a MarTech architecture review cover?", "How do I set up a MarTech centre of excellence?",
   "What does a MarTech operating model look like?", "How do I build a MarTech implementation backlog?", "How do I choose between building and buying a customer data platform?",
   "What does a fractional MarTech advisor do?", "How can a global capability centre take on product ownership?"],
 "Professional training and corporate enablement": ["What is the best way to learn Adobe Experience Platform?", "How long does it take to learn Adobe Experience Platform?",
   "What should a corporate Adobe training programme include?", "How do I plan technology training for a delivery team?", "How do I measure whether team training worked?",
   "What hands-on labs help learn Adobe Experience Platform?", "Is online instructor-led Adobe training worth it?", "How do I choose an Adobe MarTech training provider?"],
 "Technology careers and certifications": ["How do I start a career in Adobe MarTech?", "What skills does an AEP developer need?", "What does an Adobe Experience Platform architect do?",
   "What interview questions are asked for Adobe Experience Platform roles?", "How do I prepare a portfolio for a MarTech job?", "How do I move from analytics into Adobe Experience Platform?",
   "How should I prepare for an Adobe certification exam?", "What does a Customer Journey Analytics analyst do?", "How do I transition from a developer role to an AI engineer role?",
   "What jobs use Adobe Journey Optimizer skills?", "How do I write a resume for a MarTech architect role?"],
 "Enterprise platforms (SkillSurf topics)": ["How do I start learning SAP?", "What is Guidewire and what roles use it?", "How do I begin a career in SailPoint or CyberArk identity security?",
   "What is the difference between ServiceNow administration and development?", "How do I choose between learning Salesforce and learning Adobe?"],
}
rows = [(f"Q{i + 1:03d}", t, q) for i, (t, qs) in enumerate(Q.items()) for q in qs]
rows = [(f"Q{i + 1:03d}", t, q) for i, (_, t, q) in enumerate(rows)]
assert len(rows) == 100, len(rows)
assert len({r[2] for r in rows}) == 100
cols = ["id", "topic", "question", "platform", "test_date", "method", "observed_answer", "cited_domains", "cited_page_url", "our_domain_cited", "competitor_visibility", "recommended_improvement"]
out = os.path.join(ROOT, "data", "seo", "ai_citation_benchmark.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(cols)
    for r in rows:
        w.writerow([r[0], r[1], r[2]] + [""] * (len(cols) - 3))
print(len(rows), "questions ->", out)
