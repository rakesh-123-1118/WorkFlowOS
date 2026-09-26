# WorkFlowOS

AI-powered OS-level workflow automation platform for discovering, approving, and executing repetitive digital work.

## Overview

WorkFlowOS observes user activity across desktop applications, browser sessions, file operations, and messaging tools, then discovers recurring task patterns. It turns those patterns into structured workflows, asks for user approval, and automates the steps using the most reliable execution mechanism available.

## Architecture

- Backend API (Python/FastAPI)
- Desktop Activity Agent (Python)
- MongoDB data layer
- React frontend
- Workflow orchestration and automation service

## Tech Stack

- Backend: Python, FastAPI, Pydantic, Motor
- Desktop Agent: Python, PyAutoGUI, psutil, watchdog
- Database: MongoDB
- Frontend: React, Vite, TypeScript
- Containerization: Docker + Docker Compose

## Repository Structure

```text
backend/           # FastAPI backend
desktop_agent/     # Python desktop monitoring agent
frontend/          # React frontend
README.md
.dockerignore
.gitignore
docker-compose.yml
```

## Quick Start

### 1) Start infrastructure

```bash
docker compose up -d mongodb
```

### 2) Start backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3) Start frontend

```bash
cd frontend
npm install
npm run dev
```

### 4) Start desktop agent

```bash
cd desktop_agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Example Workflow

A support agent receives a customer request by email, downloads an attachment, updates the CRM record, and notifies Slack. WorkFlowOS learns this pattern and suggests an automated customer-request processing workflow.

## Current Scope

This repository is an initial scaffold for the platform. The next iterations can include:

- event ingestion and normalization
- repeated workflow detection
- AI intent mapping
- workflow approval UI
- automation execution engine
- browser and desktop integration adapters

## License

MIT
