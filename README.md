# Telegram Bot Fly.io Starter

A starter repository for creating and deploying a Telegram bot on Fly.io. This template includes a simple bot that can respond to basic commands and tell jokes.

## Features

- Basic command handling (/start, /joke)
- Easy deployment to Fly.io
- Environment variable configuration
- Dad jokes integration

## Prerequisites

- Python 3.9 or higher
- A Telegram account
- A Fly.io account
- Fly CLI installed

## Getting Started

### 1. Create Your Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Start a chat with BotFather and send the `/newbot` command
3. Follow the prompts to:
   - Set a name for your bot
   - Choose a username (must end in 'bot')
4. BotFather will provide you with a token that looks like this: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
5. Save this token - you'll need it for configuration

### 2. Local Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/[yourusername]/telegram-bot-fly-io-starter.git
   cd telegram-bot-fly-io-starter
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a .env file in the project root:
   ```plaintext
   TELEGRAM_BOT_TOKEN=your_TELEGRAM_BOT_TOKEN_here
   ```

4. Test your bot locally:
   ```bash
   python main.py
   ```

### 3. Deploying to Fly.io

1. Install the Fly CLI if you haven't already:
   ```bash
   brew install flyctl
   ```

2. Login to Fly:
   ```bash
   fly auth login
   ```

3. Launch your app:
   ```bash
   fly launch
   ```

4. Set your Telegram token as a secret:
   ```bash
   fly secrets set TELEGRAM_BOT_TOKEN=your_TELEGRAM_BOT_TOKEN_here
   ```

5. Deploy your app:
   ```bash
   fly deploy
   ```

## Bot Commands

- /start - Display welcome message and available commands
- /joke - Get a random dad joke

## Configuration

The bot uses the following environment variables:

- TELEGRAM_BOT_TOKEN : Your Telegram bot token from BotFather