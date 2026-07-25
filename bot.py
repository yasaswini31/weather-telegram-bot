import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def get_weather(city: str) -> dict[str, Any]:
    """
    Request current weather data from OpenWeatherMap.
    """

    response = requests.get(
        WEATHER_URL,
        params={
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric",
        },
        timeout=10,
    )

    if response.status_code == 404:
        raise ValueError("CITY_NOT_FOUND")

    response.raise_for_status()
    return response.json()


def format_weather(data: dict[str, Any]) -> str:
    """
    Convert weather data into a Telegram-friendly message.
    """

    city = data["name"]
    country = data["sys"]["country"]

    condition = data["weather"][0]["description"].title()

    temperature = round(data["main"]["temp"])
    feels_like = round(data["main"]["feels_like"])
    humidity = data["main"]["humidity"]

    wind = data["wind"].get("speed", 0)

    return (
        f"<b>📍 {city}, {country}</b>\n\n"
        f"🌤 <b>Condition:</b> {condition}\n"
        f"🌡 <b>Temperature:</b> {temperature}°C\n"
        f"🤗 <b>Feels Like:</b> {feels_like}°C\n"
        f"💧 <b>Humidity:</b> {humidity}%\n"
        f"💨 <b>Wind Speed:</b> {wind} m/s"
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /start command
    """

    await update.message.reply_text(
        "👋 Hello!\n\n"
        "I provide live weather updates.\n\n"
        "Use:\n"
        "<code>/weather City Name</code>\n\n"
        "Example:\n"
        "<code>/weather Delhi</code>",
        parse_mode=ParseMode.HTML,
    )


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /weather command
    """

    if not context.args:
        await update.message.reply_text(
            "Please provide a city name.\n\n"
            "Example:\n"
            "<code>/weather Mumbai</code>",
            parse_mode=ParseMode.HTML,
        )
        return

    city = " ".join(context.args)

    await update.message.reply_text("🔍 Checking live weather...")

    try:
        data = get_weather(city)

        await update.message.reply_text(
            format_weather(data),
            parse_mode=ParseMode.HTML,
        )

    except ValueError as error:

        if str(error) == "CITY_NOT_FOUND":
            await update.message.reply_text(
                "❌ City not found.\nPlease check the spelling and try again."
            )

        else:
            logger.exception("Unexpected value error")
            await update.message.reply_text(
                "Something went wrong while reading the weather data."
            )

    except requests.RequestException:
        logger.exception("Weather API request failed")
        await update.message.reply_text(
            "⚠️ Weather service is currently unavailable.\nPlease try again later."
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /help command
    """

    await update.message.reply_text(
        "<b>Available Commands</b>\n\n"
        "/start - Start the bot\n"
        "/weather City - Get weather information\n"
        "/help - Show help",
        parse_mode=ParseMode.HTML,
    )


def main() -> None:
    """
    Start the bot.
    """

    if not BOT_TOKEN or not WEATHER_API_KEY:
        raise RuntimeError(
            "Missing API keys.\n"
            "Create a .env file and add:\n"
            "TELEGRAM_BOT_TOKEN=your_token\n"
            "WEATHER_API_KEY=your_api_key"
        )

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("weather", weather))
    application.add_handler(CommandHandler("help", help_command))

    logger.info("Bot is starting...")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()