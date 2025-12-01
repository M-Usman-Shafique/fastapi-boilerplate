# ⚡ FastAPI Boilerplate

A production-ready FastAPI + UV boilerplate designed for fast, secure, and scalable web API development.

## 🧩 Features

- **FastAPI** — Modern async Python API framework
- **LangChain** — LLM orchestration framework
- **LangGraph** — Graph orchestration for complex workflows
- **OpenAI, Gemini** — Cloud LLM providers
- **MongoDB Atlas** — Cloud database
- **Beanie + PyMongo** — ODM for MongoDB
- **Sqlite Saver** — Checkpointer storage
- **Redis Saver** — Checkpointer storage
- **MongoDB Saver** — Checkpointer storage

## 🛠️ Install Dependencies

```bash
uv sync
```

## ✏️ Install New Dependency

```bash
uv add <dependency-name>
```

## 🗑️ Remove Dependency

```bash
uv remove <dependency-name>
```

## ⚙️ Environment Configuration

Use the provided `.env.example` file as a reference template.

1. Duplicate it and rename to `.env.dev` and `.env.prod`.

2. Replace the placeholder values with actual configuration values.

## 🧑‍💻 Development

Start dev server without auto-reload:

```bash
make dev-start
```

Start dev server with auto-reload:

```bash
make dev-run
```

## 🐞 Debugging

Start dev server in debug mode:

```bash
make dev-debug
```

- Open **Run and Debug** pannel (Cmd + Shift + D)
- Select **Python Debugger: FastAPI** in the dropdown
- Click the green Play button or press F5

## 🏗️ Production

Start production server:

```bash
make prod-start
```

## Note

- Open `Makefile` to see all the available scripts.
- Run, `make <script-name>` to run any particular task.
