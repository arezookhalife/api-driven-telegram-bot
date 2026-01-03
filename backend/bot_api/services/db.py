from bot_api.models import MessageHistory


def save_message(user_id, username, user_message, bot_reply):
    MessageHistory.objects.create(
        user_id=user_id,
        username=username,
        user_message=user_message,
        bot_reply=bot_reply
    )