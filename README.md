# Telegram Video Watermark Bot

Welcome to the Telegram Video Watermark Bot! This bot allows users to add watermarks to videos. It integrates with MongoDB for user data storage, supports a progress indicator, and requires users to subscribe to a channel before using the bot.

## Features
- Add watermark to videos
- MongoDB integration for user data storage
- Progress indicator
- Force subscription to a channel for access

## How to Use
1. Start the bot by sending `/start` on Telegram.
2. Subscribe to the channel mentioned by the bot to access its features.
3. Send a video to the bot to add a watermark.

## Deployment on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

To deploy this bot on Heroku, click the "Deploy to Heroku" button above. Follow the instructions to create a new Heroku app and configure the required environment variables.

### Environment Variables
- `API_ID`: Your Telegram API ID
- `API_HASH`: Your Telegram API hash
- `BOT_TOKEN`: Your Telegram bot token
- `MONGODB_URL`: Your MongoDB URL
- `FORCE_SUB_CHANNEL`: Your force subscription channel username

### Scaling the Worker
In the Heroku dashboard, go to the "Resources" tab, and under the "Free Dynos" section, scale the worker to 1.

### Open the App
Run the following command to open your app in the default web browser:

```bash
heroku open
