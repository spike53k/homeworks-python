import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

def get_currency_rates():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()

    usd_rate = data["Valute"]["USD"]["Value"]
    eur_rate = data["Valute"]["EUR"]["Value"]

    return f"Курс доллара: {usd_rate} руб.\nКурс евро: {eur_rate} руб."

token = "vk1.a.fu3S7vYwp2lKIKTSsXC5tEzk4qzsxi0Dw3kn05kHW_K5ES0lf4tf1m4l2Zs3J2T7s3hddzIsF_KPVLKq-EPNCxHfsAOyeU3HKa0anmNVTKCck6eRTQ6TNBGppd7XdMqQ67t5TIwsSx1-yCC5lft5Bl_8Fd5nF1g5sf-41uwMTL6yU88KqUJjhmSEdmXls5QWBMQdwFXzxmKVh9QadehmTg"
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        user_id = event.user_id
        if message == "/course":
            rates = get_currency_rates()
            vk.messages.send(user_id=user_id, message=rates, random_id = 0)