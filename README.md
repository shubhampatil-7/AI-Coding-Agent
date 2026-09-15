# AI Agent

A lightweight local AI coding assistant inspired by tools like Claude Code. This project is a small Python-based experiment for sending prompts to an LLM, retrieving a response, and extending the workflow toward file-aware, code-editing agent behavior.

The current version is intentionally simple: it exposes a CLI that sends a user prompt to an OpenAI-compatible API via OpenRouter and prints the response. The repository also includes a small calculator app used as a demo of a modular project structure and command-line tool patterns.

## Why this project exists

The goal is to explore the building blocks of an agentic coding environment:

- prompt-driven interaction from the terminal
- model access through a provider like OpenRouter
- easy extension to repository-aware tasks
- a foundation for file reading, code generation, validation, and iterative editing

This is not a full clone of Claude Code yet. Instead, it is a minimal starting point for a local coding agent that can grow into something more capable over time.

## Features

- Python CLI for sending natural-language prompts to an LLM
- OpenAI-compatible API integration through OpenRouter
- Optional verbose mode for debugging prompt and token usage
- Simple project layout for separating agent logic from example tools
- Calculator sample app with tests to demonstrate a realistic project structure

## Project structure

```text
ai-agent/
├── main.py                  # CLI entry point for the AI agent
├── pyproject.toml           # Python project metadata and dependencies
├── README.md                # Project documentation
├── .env                     # Local environment variables (not committed)
├── calculator/
│   ├── main.py              # Command-line calculator app
│   ├── tests.py             # Unit tests for calculator logic
│   └── pkg/
│       ├── calculator.py    # Expression evaluator
│       └── render.py        # JSON rendering helper
├── functions/
│   └── get_files_info.py    # Placeholder for future file-inspection helper
└── .venv/                   # Local virtual environment (optional)
```

## Architecture

At the moment, the core flow is very straightforward:

1. The user runs the CLI with a prompt.
2. The application loads the environment variable for the API key.
3. It creates an OpenAI client pointed at OpenRouter.
4. It sends the prompt to the model.
5. It prints the completion content to the terminal.

This gives the project a clear base to extend with agent-style capabilities such as:

- reading project files
- summarizing a repository
- making code changes
- running tests and validating outputs
- looping on errors until the task is complete

## Getting started

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -e .
```

### 3. Set your API key

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### 4. Run the agent

```bash
python main.py "Explain this repository in simple terms"
```

With verbose output:

```bash
python main.py "Summarize the project structure" --verbose
```

## Usage examples

```bash
python main.py "Write a Python function that sorts a list of numbers"
python main.py "Review this codebase and suggest improvements"
python main.py "Generate a README for a REST API project" --verbose
```

## Calculator example

The repository also contains a command-line calculator that can be used as a sample project for testing a local tool workflow:

```bash
cd calculator
python main.py "3 + 5 * 2"
```

This returns a JSON-style result with the expression and computed value.

## Roadmap

This project is intentionally a foundation rather than a finished product. A natural next step would be to turn it into a more capable agent with features like:

- repository scanning and file reading
- dependency-aware code analysis
- execution of shell commands in a controlled environment
- automatic patch generation and diffs
- test execution and verification loops
- chat history and context management
- multi-file editing workflows

## Notes

This project is designed as an educational and experimental agent framework. It is intentionally small, readable, and easy to extend, which makes it useful as a starting point for learning how coding assistants are built.

## License

This project does not currently specify a license. Add one if you plan to share or distribute it publicly.

## Contributing

Contributions are welcome. A good starting point would be:

- improving the agent interface
- adding file system awareness
- creating safer command execution patterns
- building a richer prompt and tool execution loop
- adding automated tests around the agent workflow
