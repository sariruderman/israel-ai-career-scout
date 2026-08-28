
# Product & Architecture

## 1. Product Vision

Israel AI Career Scout is being designed as an AI-powered job-intelligence platform focused on helping candidates discover relevant job opportunities in Israel.

The long-term product aims to move beyond simple job aggregation by building a reliable pipeline from:

```text
Job Discovery
    ↓
Acquisition
    ↓
Raw Data Preservation
    ↓
Parsing
    ↓
Normalization
    ↓
Deduplication
    ↓
Enrichment
    ↓
AI Matching
    ↓
Candidate Experience
```

The immediate goal is deliberately smaller:

> **Prove that the data-acquisition and processing pipeline works reliably with real job data before building the complete product.**

---

## 2. Current Status

**Phase 0 — Foundation / Data Acquisition Spike**

The project is not yet a complete job-matching product.

The immediate milestone is a small, reproducible experiment that validates whether the system can acquire and process useful job data reliably.

The spike will initially target:

* approximately 10–20 jobs
* then approximately 50 jobs
* eventually approximately 200 jobs

The experiment should provide evidence about:

* source accessibility
* acquisition reliability
* raw-data preservation
* parsing quality
* normalization quality
* duplicate detection
* missing fields
* processing performance
* error handling
* source provenance

---

## 3. Scope

### 3.1 In Scope — Phase 0

* Job data acquisition
* Raw response preservation
* Parsing
* Basic normalization
* Basic deduplication
* Source/provenance metadata
* Error handling
* Local snapshots for repeatable development
* Small-scale experiments
* Data-quality measurement

### 3.2 Planned for Later

* Candidate profile ingestion
* CV parsing
* Skill extraction
* Embeddings
* Semantic search
* AI-assisted enrichment
* Candidate/job matching
* Personalized ranking
* Candidate-facing API
* Web application
* Notifications
* Analytics
* Application tracking

### 3.3 Explicitly Out of Scope for Phase 0

The first spike will not attempt to build:

* a complete candidate scoring system
* an acceptance-probability model
* a production frontend
* billing
* production authentication
* a large distributed crawling platform
* complex autonomous agent orchestration
* infrastructure that is not justified by an observed requirement

---

## 4. Engineering Principles

### 4.1 Execution Over Documentation

Documentation exists to support implementation.

The project should not spend more time designing documentation than validating the actual system.

Each important assumption should eventually be validated through working code, measurable experiments, or real data.

### 4.2 Build Incrementally

The system should evolve through small, meaningful milestones.

Each milestone should produce something executable, measurable, or testable.

### 4.3 Evidence Over Assumptions

Job sources differ significantly in structure, availability, stability, and access requirements.

Do not design a large acquisition architecture based only on assumptions.

Test representative sources first.

### 4.4 Preserve Provenance

Every acquired job should retain enough information to answer:

* Where did this data come from?
* What was the source URL?
* When was it acquired?
* What acquisition method was used?
* What raw information was received?
* When was it last observed?

### 4.5 Separate Acquisition From Processing

The system should distinguish between:

```text
Fetch
  ↓
Raw Snapshot
  ↓
Parse
  ↓
Normalize
  ↓
Deduplicate
```

The fetch layer should not contain job-specific parsing logic.

### 4.6 Cache Raw Data During Development

External sources should not be requested repeatedly while debugging parsers or normalization logic.

The preferred development flow is:

```text
External Source
      ↓
    Fetch
      ↓
 Raw Snapshot
      ↓
 ┌────┼────┐
 ▼    ▼    ▼
P1    P2    P3
 └────┼────┘
      ▼
 Normalize
```

This allows parsing and normalization logic to be changed and tested repeatedly against the same source snapshot without unnecessary network requests.

### 4.7 Avoid Premature Complexity

Do not introduce infrastructure simply because it might be useful later.

Technologies such as:

* Redis
* message queues
* distributed workers
* Kafka
* Kubernetes
* complex agent orchestration

should be introduced only when an actual requirement justifies them.

---

## 5. Target Architecture

The following describes the intended direction of the system.

It is a **target architecture**, not a statement that all components already exist.

```text
                    ┌─────────────────────────┐
                    │      Job Sources        │
                    │                         │
                    │ Job boards              │
                    │ Career pages            │
                    │ Feeds / APIs             │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Data / AI Worker    │
                    │        Python           │
                    │                         │
                    │ Acquisition             │
                    │ Parsing                 │
                    │ Normalization           │
                    │ Deduplication           │
                    │ Enrichment              │
                    │ AI processing            │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       Core API          │
                    │       NestJS             │
                    │                         │
                    │ Business logic          │
                    │ Jobs                    │
                    │ Candidates              │
                    │ Authentication          │
                    │ Application API         │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       PostgreSQL        │
                    │                         │
                    │ Application data        │
                    │ Job data                │
                    │ Future vector search    │
                    └─────────────────────────┘
```

The architecture should evolve according to evidence collected during implementation.

---

## 6. Component Responsibilities

### 6.1 Data / AI Worker

The Python worker is responsible for data-heavy processing.

Expected responsibilities include:

* acquisition
* raw response handling
* parsing
* normalization
* deduplication
* text processing
* enrichment
* embeddings
* future AI workflows

The worker should maintain a clear boundary between external data acquisition and application business logic.

### 6.2 Core API

The future NestJS API will own application-facing business logic.

Expected responsibilities include:

* job operations
* candidate profiles
* authentication and authorization
* API contracts
* persistence
* application state
* communication with background workers

The API should not become responsible for heavy scraping or AI processing.

### 6.3 Database

PostgreSQL is the intended primary database.

Future vector-search capabilities may be added when semantic matching becomes an actual requirement.

The data model should distinguish between:

```text
Source / Raw Data
        ↓
Normalized Data
        ↓
Derived / Enriched Data
        ↓
AI / Matching Data
```

---

## 7. Data Acquisition Strategy

The first technical question is not:

> "How do we build the perfect scraper?"

It is:

> "Can we reliably acquire useful job data from representative sources?"

The spike should test a small number of representative acquisition approaches.

For each source, the experiment should measure:

* acquisition success rate
* parsing success rate
* useful-field coverage
* duplicate rate
* missing fields
* processing time
* source stability
* error types
* source URL preservation

The project should favor maintainable and permitted acquisition methods.

The system should not attempt to bypass authentication, paywalls, CAPTCHAs, or other technical access controls.

---

## 8. Raw Data and Snapshot Strategy

Raw source responses are valuable during development because they allow the parser to evolve independently from acquisition.

Conceptually:

```text
data/
├── raw/
├── normalized/
└── samples/
```

### `data/raw/`

Contains source snapshots captured during the acquisition spike.

Examples:

```text
raw/
├── source-a/
│   ├── job-001.html
│   └── job-002.html
└── source-b/
    ├── job-003.json
    └── job-004.json
```

### `data/normalized/`

Contains normalized output generated from the raw snapshots.

### `data/samples/`

Contains small representative datasets useful for local development.

### Tests

Test fixtures should remain separate:

```text
tests/
└── fixtures/
```

Test fixtures are intentionally small and stable. They should not be confused with the raw data collected during the spike.

---

## 9. Fetch ≠ Parse

The acquisition layer should have a narrow responsibility.

Conceptually:

```text
Fetcher
   ↓
RawResponse
   ↓
Parser
   ↓
ParsedJob
   ↓
Normalizer
   ↓
NormalizedJob
```

The fetcher should not know how to extract:

* title
* company
* location
* salary
* requirements

Those concerns belong to parsing and normalization.

This separation makes it possible to change parsing logic without repeatedly contacting external sources.

---

## 10. Data Model Direction

A future job entity should distinguish source information from normalized and derived information.

Conceptually:

```text
Job
├── identity
│   ├── internal_id
│   └── source identifiers
│
├── source
│   ├── source_name
│   ├── source_url
│   ├── acquired_at
│   └── acquisition_method
│
├── content
│   ├── title
│   ├── company
│   ├── location
│   ├── description
│   └── requirements
│
├── normalized
│   ├── skills
│   ├── employment_type
│   ├── seniority
│   └── salary
│
└── derived
    ├── embeddings
    ├── enrichment
    └── matching metadata
```

The final schema should be based on real source data rather than theoretical assumptions.

---

## 11. AI Strategy

AI should be introduced where it provides measurable value.

Potential future capabilities include:

* semantic job/candidate similarity
* CV information extraction
* skill normalization
* job-description enrichment
* semantic duplicate detection
* natural-language job search
* personalized recommendations

AI should not be introduced merely because the product is described as AI-powered.

If a deterministic solution is simpler, cheaper, and more reliable, it should be preferred.

---

## 12. Reliability and Trust

The system should make it possible to distinguish between:

```text
Observed Source Data
        ↓
Processed Data
        ↓
AI-Derived Data
```

Important principles:

* Preserve source provenance.
* Validate important fields.
* Log acquisition failures.
* Make processing failures visible.
* Avoid presenting inferred information as source fact.
* Keep raw data available for debugging where appropriate.
* Design for source failures.
* Measure data quality rather than assuming it.

The goal is a system that produces trustworthy information, not simply a large number of job records.

---

## 13. Privacy

Candidate data may contain personal information.

The production design should follow data-minimization principles:

* Store only information required by the product.
* Protect credentials and secrets.
* Separate candidate data from public job data.
* Define retention and deletion policies.
* Restrict access to candidate information.
* Avoid sending personal information to external AI services unless necessary and appropriately controlled.

Privacy requirements should become more concrete as candidate-facing functionality is implemented.

---

## 14. Roadmap

### Phase 0 — Foundation / Data Acquisition

**Goal:** Validate the acquisition and processing pipeline.

Initial deliverables:

* repository foundation
* documentation
* acquisition worker
* raw snapshots
* parsing
* normalization
* basic deduplication
* approximately 10–20 jobs
* expansion toward 50 jobs
* expansion toward approximately 200 jobs
* measurements and findings

### Phase 1 — Reliable Data Pipeline

**Goal:** Turn the spike into a repeatable pipeline.

Potential deliverables:

* source adapters
* validation
* stronger deduplication
* persistence
* scheduling
* retries
* monitoring
* error handling

### Phase 2 — AI Enrichment

**Goal:** Add useful intelligence to job data.

Potential deliverables:

* skill extraction
* normalization
* embeddings
* semantic search
* AI-assisted enrichment

### Phase 3 — Candidate Matching

**Goal:** Connect job opportunities with candidate profiles.

Potential deliverables:

* CV/profile ingestion
* candidate representation
* relevance scoring
* explainable matching
* personalized discovery

### Phase 4 — Candidate Product

**Goal:** Build the candidate-facing experience.

Potential deliverables:

* frontend
* authentication
* saved jobs
* alerts
* preferences
* application tracking
* analytics

The roadmap is intentionally directional. Evidence from each phase may change the priorities of the next phase.

---

## 15. Definition of Done — Phase 0

Phase 0 is successful when we can demonstrate:

1. A reproducible acquisition process.
2. Raw source data can be preserved locally.
3. The same raw snapshot can be processed repeatedly without another network request.
4. Job information can be parsed into a structured representation.
5. Basic normalization works.
6. Duplicate handling can be measured.
7. Acquisition and parsing failures are visible.
8. Source URLs and acquisition timestamps are preserved.
9. The pipeline can progress from approximately 10–20 jobs toward 50 and then approximately 200 jobs.
10. The experiment produces enough evidence to determine the next engineering step.

---

## 16. Engineering Decision Rule

> **Build the smallest system that can prove the next important assumption.**

The architecture described in this document is a direction and a set of boundaries—not a reason to postpone implementation.

The immediate next engineering step is:

```text
Create workers/ai-worker
        ↓
Implement acquisition
        ↓
Save raw snapshots
        ↓
Parse
        ↓
Normalize
        ↓
Test with 10–20 jobs
```

Only after the spike produces evidence should the project invest in additional infrastructure.
