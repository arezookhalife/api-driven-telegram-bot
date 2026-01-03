# AI-Powered Telegram Bot with Django Backend

This project demonstrates a Telegram bot powered by a Django backend API.  
It is structured professionally for easy setup and deployment.

---

## 🎯 Features

- Telegram bot built with **Aiogram**  
- Django backend API to generate intelligent replies  
- Asynchronous communication between bot and backend  
- Separate virtual environments for bot and backend  
- Configurable via private settings  

---

## Requirements

- Python 3.12+
- Virtualenv (optional but recommended)
- Pip packages (see `requirements.txt` in bot and backend folders)

---

## 🛠️ Installation & Setup

### 1. Clone the repository:

```bash
git clone https://github.com/USERNAME/PROJECT_NAME.git
cd PROJECT_NAME
```

### 2. Create virtual environments:

```bash
# For backend
cd backend
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt

# For bot
cd ../aiogram_bot
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

### 3. Configure secrets:

Create a config.py (bot) and settings_private.py (backend) based on the examples:

- aiogram_bot/config.py
```bash
API_token = "YOUR_TELEGRAM_BOT_TOKEN"
API_URL = "http://127.0.0.1:8000/api/reply/"
proxy_port = None  # optional, if you use a proxy
```

- backend/config/settings_private.py
```bash
SECRET_KEY = "YOUR_DJANGO_SECRET_KEY"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1"]
```

Important: Do not commit these private files to git. They are ignored by .gitignore.

---

## Running the Project

### - backend API (Django):
```bash
cd backend
source venv/Scripts/activate  # Windows
python manage.py migrate
python manage.py runserver
```

### - Telegram bot:
```bash
cd aiogram_bot
source venv/Scripts/activate  # Windows
python main.py
```
Make sure the backend is running before starting the bot.

---

## Usage

- Start the Telegram bot and send /start

- The bot will interact with the backend API to generate intelligent replies

---

## 🔧 Project Structure

```arduino
aiogram_bot/    # Telegram bot code
    main.py
    config.py
backend/        # Django backend
    bot_api/
    config/
README.md    
```

---

## 📌 Professional Notes

- Fully documented and organized code

- Uses virtual environments for dependency management

- API returns standardized JSON responses

- Easy to extend for additional features

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first.