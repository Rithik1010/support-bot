# Support Bot

## Overview

This project is an **AI-powered support bot** built with `Streamlit` and `OpenAI Assistants API`. The bot interacts with users by responding to their queries using knowledge provided through the OpenAI API. The bot allows for real-time streaming responses, providing a seamless chat experience.

## Features

-   Streamed chat-based interface powered by `Streamlit`.
-   Uses OpenAI API to fetch responses from a pre-configured assistant.
-   Stores the chat history for continuity across user interactions.
-   Cleans up responses to remove any unwanted source citations.

## Prerequisites

-   Python 3.12+
-   OpenAI API Key and Assistant ID stored in `Streamlit` secrets (`.streamlit/secrets.toml`).

## Installation

1. Clone the repository.
2. Install the required dependencies:

    ```bash
    pip install streamlit openai
    ```

3. Configure your OpenAI API key and Assistant ID in the `.streamlit/secrets.toml` file:

    ```toml
    api_key = "your-openai-api-key"
    assistant_id = "your-assistant-id"
    ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

-   The bot will start running locally on `http://localhost:8501`.
-   Users can input their queries, and the bot will respond using OpenAI’s assistant API in real time.
