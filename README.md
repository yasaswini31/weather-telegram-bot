# 🌦️ Telegram Weather Chatbot

A Python-based Telegram Weather Chatbot that provides users with real-time weather information based on their location. The bot integrates with a Weather API to deliver weather updates through a simple and interactive Telegram interface.

## 🚀 Features

- **Real-Time Weather Updates:** Get current weather information for any supported city.
- **Location-Based Search:** Retrieve weather details by entering a city name.
- **Temperature Details:** View current temperature and weather conditions.
- **Weather Information:** Get details such as humidity, wind speed and other weather parameters.
- **Interactive Chatbot:** Communicate with the bot through Telegram commands and messages.
- **API Integration:** Fetch live weather data using an external Weather API.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Bot Platform:** Telegram Bot API
- **Weather Data:** Weather API
- **Libraries:** python-telegram-bot, python-dotenv
- **Frontend:** HTML, CSS (if applicable)

## 📂 Project Structure

```text
weather-telegram-bot/
│
├── bot.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yasaswini31/weather-telegram-bot.git
```

### 2. Navigate to the Project Directory

```bash
cd weather-telegram-bot
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file and add your API credentials:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
WEATHER_API_KEY=your_weather_api_key
```

Never share your actual API keys or bot token publicly.

### 6. Run the Application

```bash
python bot.py
```

## 💡 How It Works

1. The user interacts with the chatbot through Telegram.
2. The user enters a city name.
3. The chatbot sends a request to the Weather API.
4. The API returns the latest available weather information.
5. The chatbot displays the weather details to the user.

## 🎯 Project Objective

The main objective of this project is to simplify access to real-time weather information through an interactive Telegram chatbot while demonstrating Python programming, API integration and chatbot development.

## 🔮 Future Enhancements

- Add multi-day weather forecasting.
- Implement automated severe-weather alerts.
- Integrate AI-powered natural-language conversations.
- Develop a weather analytics dashboard.

## 👩‍💻 Developer

**Yasaswini**

GitHub: https://github.com/yasaswini31

---

⭐ If you find this project interesting, feel free to explore the repository!
