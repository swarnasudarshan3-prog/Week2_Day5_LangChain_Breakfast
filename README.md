
# Week 2 Day 5: LangChain Breakfast Ideas

## Project Overview

A Python application that uses LangChain and OpenAI to generate exactly five healthy breakfast ideas.

The application demonstrates how to call a language model using `ChatOpenAI`, retrieve the response using `invoke()`, and print only the message content.

## Technologies Used

- Python
- LangChain
- LangChain OpenAI
- OpenAI GPT-4o-mini

## Key Features

- Generates exactly five healthy breakfast ideas.
- Displays numbered suggestions, one per line.
- Uses LangChain's ChatOpenAI integration.
- Prints only `reply.content`.
- Reads the OpenAI API key from an environment variable.
- Supports comparing results across multiple executions.

## Installation

Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
python -m pip install langchain langchain-openai
```

## API Configuration

Set your OpenAI API key:

```powershell
$env:OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

Never upload your API key to GitHub.

## Run the Application

```powershell
python breakfast.py
```

Run the command twice and compare the results.

## Testing Results

**Run 1:** Generated five healthy Indian breakfast ideas.

**Run 2:** Generated five different breakfast ideas.

Both runs followed the required numbered, one-line format.

## Observation

The two executions produced different breakfast suggestions. The model was configured with `temperature=0.7`, allowing variation in its responses.

## Assignment Status

Successfully completed and tested with two executions.

## Author

Mohan Ramalingam

Week 2 Day 5 Python Assignment
