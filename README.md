# 🔎 Telegram ID Generator Bot

A simple Telegram bot built with **Pyrogram** that helps you retrieve various Telegram IDs for development and debugging purposes.

This bot can generate:

* User ID
* Chat ID
* Message ID
* Replied User ID
* Forwarded User / Chat ID
* DC ID (Data Center ID)

It is especially useful for Telegram bot developers who need IDs for admin configuration, whitelisting, logging, or automation setup.

---

## 🚀 Features

### `/start`

Displays:

* Your User ID
* Current Chat ID

(Works in private chat)

---

### `/id`

Displays detailed ID information depending on chat type.

#### 📩 Private Chat

* Your User ID
* Chat ID

#### 👥 Group / Supergroup

Without reply:

* Your User ID
* Chat ID

With reply:

* Replied User ID
* Replied Message ID
* Chat ID
* Your User ID

#### 📢 Channel

Without reply:

* Chat ID

With reply:

* Chat ID
* Replied Message ID

---

### 🔁 Forwarded Message Detection (Private Only)

When you forward a message to the bot:

#### Forwarded from a User

* Forwarded User ID
* Forwarded DC ID
* Your User ID

#### Forwarded from a Channel / Group

* Forwarded Chat Title
* Forwarded Chat ID
* Forwarded Message ID
* Forwarded DC ID
* Your User ID

If the forward origin is hidden (privacy enabled):

```
Cannot get ID from hidden account 🥷🏻
```

---

## 🛠️ Tech Stack

* Python 3.9+
* Pyrogram
* TgCrypto (recommended for better performance)

---

## 📂 Project Structure

```
.
├── plugins/
│   ├── core/ (core of modules)
│   ├── modules/
│   ├── __init__.py
│   ├── __main__.py
│   └── config.py
├── .env
├── .gitignore
└── README.md
├── requirements.txt
├── sample_env
└── start
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/msdzulqurnain/genidsbot.git
cd genidsbot
```

### 2. Install Dependencies

Using requirements file:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

You need the following credentials:

* `API_ID`
* `API_HASH`
* `BOT_TOKEN` as `TOKEN`

Get them from:

* API_ID & API_HASH → [https://my.telegram.org](https://my.telegram.org)
* BOT_TOKEN → @BotFather

Example configuration inside your project:

```python
API_ID = 123456
API_HASH = "your_api_hash"
TOKEN = "your_bot_token"
```

For better security, it is recommended to use environment variables.

---

## ▶️ Running the Bot

```bash
bash start
```

If everything is configured correctly, the bot will start and respond to commands.

---

## 📌 Common Use Cases

* Getting Chat ID for admin bots
* Getting User ID for whitelist systems
* Debugging forwarded messages
* Retrieving DC ID information
* General Telegram bot development and testing

---

## 📜 License

Free to use, modify, and distribute.

---

## 👨‍💻 Author

- Built with 💻 + ☕ by ᴅᴢ </ ᴄᴏᴅᴇ> Dev Team
- Telegram: [ᴅᴢ </ᴄᴏᴅᴇ>](https://t.me/DZC0de)