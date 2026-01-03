from django.shortcuts import render
from django.conf import settings

def home(request):
    """
    Landing page for the Telegram Bot project.
    Shows project description and test interface.
    """
    return render(request, "web/index.html",  {"bot_link": settings.TELEGRAM_BOT_LINK})
