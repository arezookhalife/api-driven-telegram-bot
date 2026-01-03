def log_message(user_id: int, username: str, message: str, reply: str):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{user_id}.{username}: {message}\nBot: {reply}\n---\n")