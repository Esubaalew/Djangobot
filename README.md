# Djangobot - Python Telegram Bot with Django

This project is a template for deploying a Python Telegram bot using Django. It is designed to use webhooks for interaction between Telegram and Django, with the token and webhook URL stored in environment variables.

## Features
- Django as the backend framework
- Telegram bot integration using webhooks
- Easy deployment setup

## Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- Django
- Telegram Bot API token (from [BotFather](https://core.telegram.org/bots#botfather))
- Webhook URL (your server's endpoint)
- `python-telegram-bot` library

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Esubaalew/Djangobot.git
    cd Djangobot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - `TOKEN`: Your Telegram Bot token.
    - `webhook`: The webhook URL for your bot.

    You can create a `.env` file in the root directory of the project to store these values:
    ```bash
    TOKEN=<your-telegram-bot-token>
    webhook=<your-webhook-url>
    ```



### Deployment

To deploy this project, follow your preferred method (Vercel, local server etc.), ensuring that you properly configure the environment variables.
If you are hosting it on verce create `vercel.json` fine in the root directory add th ff code please replace the names with your own app names
``` json
{
  "builds": [
    {
      "src": "dbot/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "dbot/wsgi.py"
    }
  ]
}
```

### Setting Webhook

Once your bot is live, set the Telegram webhook by running the following command:

```bash
curl -X POST https://api.telegram.org/bot<your-telegram-bot-token>/setWebhook?url=<your-webhook-url>
