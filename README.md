## Project structure

```

agent-langchain-poc/           # Root directory
│
├── agent-langchain-frontend/   # Angular Frontend
│   ├── src/
│   ├── angular.json
│   ├── package.json
│   ├── tsconfig.json
│   └── (other Angular files)
│
└── agent-langchain-backend/    # Python FastAPI Backend
    ├── app/                     # Backend application folder
    │   ├── main.py               # Main FastAPI application (was app.py)
    │   ├── models/               # Pydantic models
    │   ├── services/             # Business logic (LangChain)
    │   ├── routes/               # API endpoints
    │   ├── config.py             # Configuration settings
    │   └── __init__.py           # Python package init file
    │
    ├── venv/                     # Virtual environment
    ├── requirements.txt          # Python dependencies
    ├── .env                      # Environment variables (API keys)
    ├── run.sh                    # Script to run the backend
    └── README.md                 # Documentation

```