# OfficePilot Architecture

OfficePilot is an AI-powered operating system for small businesses.

## Product Philosophy

OfficePilot should not behave like a chatbot. It should behave like an AI employee that understands the business and helps complete operational work.

## Version Strategy

### Version 0.1 — Manual Foundation
Users manually upload documents, add customers, create invoices, and ask AI questions.

### Version 0.2 — Connected Systems
OfficePilot connects to Gmail, Google Drive, Calendar, and other business tools.

### Version 0.3 — Business Brain
OfficePilot builds a live knowledge layer across customers, documents, invoices, emails, and meetings.

### Version 1.0 — Proactive AI Employee
OfficePilot recommends and completes business actions.

## High-Level System

```mermaid
flowchart LR
    User --> Frontend
    Frontend --> Backend
    Backend --> Database
    Backend --> FileStorage
    Backend --> AILayer
    AILayer --> LLM