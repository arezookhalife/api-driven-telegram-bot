from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .services.db import save_message
import json
from .services.reply_engine import generate_reply
from .services.logger import log_message


@csrf_exempt
def reply_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    
    data = json.loads(request.body)

    user_id = data.get("user_id")
    username = data.get("username", "")
    message = data.get("message", "")
    
    if not message:
        return JsonResponse({"error": "No input provided"}, status=400)
    
    reply = generate_reply(message)
    
    log_message(user_id, username, message, reply)
    
    save_message(
        user_id=user_id,
        username=username,
        user_message=message,
        bot_reply=reply
    )
    
    return JsonResponse({"reply": reply})




