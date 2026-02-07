# AIzaSyAelMLTGoBsNbsveWhbRYK05XDWWwJ0zbA

import pyautogui
import pyperclip
import time
from google import genai

# this is for finding position of targeted goal
# while True:
#     pos=pyautogui.position()
#     print(pos)

time.sleep(3)

# Gemini setup
client = genai.Client(api_key="AIzaSyAelMLTGoBsNbsveWhbRYK05XDWWwJ0zbA")
last_seen=""

def read_chat():

    pyautogui.click(762, 1044)
    time.sleep(1)
    pyautogui.moveTo(703 ,193)
    pyautogui.dragTo(718,1019 , duration=1 ,button="left")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl","c")
    time.sleep(0.5)
    return pyperclip.paste()

def get_Last_message(chat_text):
    lines = [l.strip() for l in chat_text.splitlines() if l.strip()]
    if not lines:
        return ""
    return lines[-1]   # take last visible message


def ask_gemini(msg):
    prompt = f"""
        Reply to this WhatsApp message in **1 short sentence**,
        friendly, funny, lightly roasted, and in Hinglish.
        Do not provide multiple options or list items.
        Be playful and teasing, but not rude or offensive.
        Message: {msg}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash" \
        "", # Note: Check current available model names
        contents=prompt
    )
    return response.text

def send_reply(text):
    pyperclip.copy(text)
    pyautogui.click(810,983)
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press('enter')

time.sleep(5)

def is_probably_friend_message(msg):
    # crude but effective filters
    blocked = ["You:", "Me:", "Sent", "Delivered"]
    return not any(b.lower() in msg.lower() for b in blocked)


while True:
    chat=read_chat()
    last_msg=get_Last_message(chat)

    if last_msg and last_msg != last_seen and is_probably_friend_message(last_msg):
        last_seen = last_msg
        reply = ask_gemini(last_msg)
        send_reply(reply)
    break
    time.sleep(2)

# copy_text=pyperclip.paste()
# print(copy_text)

# For returning to original window
# pyautogui.hotkey("alt","tab")