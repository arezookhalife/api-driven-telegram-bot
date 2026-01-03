
FAQ = {
    "ساعت": "ساعات کاری ما 9 صبح تا 6 بعداز ظهر است.",
    "ساعات": "ساعات کاری ما 9 صبح تا 6 بعداز ظهر است.",
    "تماس": "شما می‌توانید از طریق ایمیل support@example.com با ما در تماس باشید.",
    "ایمیل": "شما می‌توانید از طریق ایمیل support@example.com با ما در تماس باشید.",
}


def generate_reply(message: str) -> str:
    """
    Generate reply for user message.
    This logic is shared between Telegram bot and Web UI.
    """
    text = message.lower()

    for key, reply in FAQ.items():
        if key in text:
            return reply

    return f"پیام شما دریافت شد: {message}"
