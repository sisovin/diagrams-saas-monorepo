# Diagrams SaaS Monorepo

This repository contains the code for the Diagrams SaaS project, which is structured as a monorepo using Turborepo.

## Project Setup Instructions

### Prerequisites

- Node.js (>=14.x)
- Python (>=3.8)
- Docker

### Initial Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Install dependencies:
   ```sh
   npm install
   ```

3. Set up the Python environment for the backend:
   ```sh
   cd apps/backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Start the development environment:
   ```sh
   docker-compose up
   ```

### Directory Structure

- `apps/backend/`: Backend service using FastAPI
- `apps/frontend/`: Frontend service using React
- `packages/`: Shared packages

### Development

- To start the development environment, run:
  ```sh
  docker-compose up
  ```

- To run individual services:
  - Backend:
    ```sh
    cd apps/backend
    uvicorn main:app --reload
    ```
  - Frontend:
    ```sh
    cd apps/frontend
    npm start
    ```

### Deployment

- Configure deployment targets (e.g., Vercel, Railway)
- Add CI/CD pipelines
- Enable production Docker configs
- Secure environment variables and secrets
