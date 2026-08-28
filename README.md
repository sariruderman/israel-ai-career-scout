# Israel AI Career Scout

AI-powered career intelligence platform designed to discover, process, and eventually match relevant job opportunities in Israel.

> **🚧 Status: Phase 0 — Foundation / Data Acquisition Spike**
>
> The project is currently validating its data-acquisition pipeline. The production application, AI matching, and candidate-facing experience have not been implemented yet.

## What We're Building

Israel AI Career Scout is being built as a reliable job-intelligence platform that will help candidates discover relevant opportunities while reducing noise, duplication, and manual searching.

The long-term platform is designed to:

* Discover job opportunities from multiple sources
* Preserve source URLs and acquisition metadata
* Normalize and deduplicate job data
* Enrich job information where AI provides real value
* Match job opportunities to candidate profiles
* Deliver relevant and personalized job discovery

The current priority is intentionally smaller:

**Build and validate the data-acquisition pipeline before building the full product.**

## Current Milestone

### Data Acquisition Spike

The first engineering milestone is to build a small, reproducible pipeline that can:

1. Acquire real job postings
2. Preserve raw/source data
3. Parse job information
4. Normalize the extracted data
5. Detect duplicates
6. Measure failures and data quality
7. Scale the experiment from a small sample toward approximately 200 jobs

The spike will begin with approximately **10–20 jobs**. Once the pipeline proves reliable, it will expand to approximately **50 jobs** and then toward **200 jobs**.

## Repository Structure

```text
.
├── docs/
│   └── 00-product-and-architecture.md
│
├── workers/
│   └── ai-worker/              # Data acquisition & AI processing
│
├── .gitignore
└── README.md
```

> `workers/ai-worker/` represents the next implementation milestone and may not exist yet.

## Getting Started

The project is currently in the initial foundation phase.

Installation and run instructions will be added together with the first executable implementation of the **Data Acquisition Spike**.

No commands are documented yet that depend on files or scripts that do not exist.

## Documentation

* [Product & Architecture](docs/00-product-and-architecture.md) — product vision, scope, target architecture, engineering principles, data strategy, reliability, privacy, and roadmap.

## Engineering Principles

* **Build incrementally** — validate the next important assumption before expanding the system.
* **Evidence over assumptions** — use real data and measurable experiments to drive technical decisions.
* **Separate responsibilities** — acquisition, parsing, normalization, business logic, and AI processing should have clear boundaries.
* **Preserve provenance** — know where job data came from and when it was acquired.
* **Cache raw data during experiments** — separate network acquisition from parsing and normalization so the same snapshot can be processed repeatedly without unnecessary external requests.
* **Avoid premature complexity** — introduce infrastructure when a real requirement justifies it.
* **Execution over documentation** — documentation supports implementation; it does not replace it.

## Project Status

This repository is an active engineering project.

Architecture and implementation decisions may evolve as the Data Acquisition Spike produces real-world evidence.
