# Simple OpenAI API Demo

A minimal Python application that demonstrates sending a request to OpenAI's API and receiving a response.

## Features

- Initial hardcoded demo message request
- Interactive user input for up to 5 custom questions
- One-sentence responses for simplicity and speed
- 30-second timeout for each user input (auto-exits if no input)
- Uses OpenAI's GPT-3.5 Turbo model (legacy, cost-effective)
- Reads API key from Windows environment variables
- Clear console output showing request and response

## Prerequisites

- Python 3.7 or higher
- OpenAI API key set in Windows environment variables

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify your API key:**
   This application reads the `OPENAI_API_KEY` from your Windows user environment variables.
   Make sure you have already set it up in your Windows environment.

## Usage

Simply run the script:

```bash
python simple_openai_demo.py
```

The script will:
1. Load your API key from the environment variable
2. Send a hardcoded demo message to OpenAI's API
3. Display the response in the console
4. Prompt you to enter up to 5 custom questions (one at a time)
5. Each question has a 30-second timeout - if no input is received within 30 seconds, the program exits
6. After 5 questions or timeout/empty input, the program exits automatically

## Technical Details

- **Model:** gpt-3.5-turbo (legacy, most cost-effective)
- **API Key Source:** Windows user environment variable (`OPENAI_API_KEY`)
- **Interaction:** Initial hardcoded demo message, followed by up to 5 user questions
- **Response Format:** One sentence maximum (enforced via system message)
- **Input Timeout:** 30 seconds per question (uses threading for timeout handling)
- **Question Limit:** Maximum of 5 questions per session





