import os
from ollama import Client

client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY", "")},
)

MODEL = "gpt-oss:120b"

SYSTEM = """You are a gentle, calm helper for people who overthink.
Reply in this exact format, in simple words, under 150 words total:
1. Feeling: one kind sentence acknowledging how they feel.
2. In my control: 1-2 short bullets.
3. Not in my control: 1-2 short bullets.
4. Next 10 minutes: ONE small, easy action.
5. Breathe: a 30-second breathing exercise (in 4 seconds, hold 4, out 6).
The user is most likely a student, so do not assume they have a job.
Do not diagnose. Do not give medical advice. Do not be dramatic."""

CRISIS_WORDS = ["suicide", "kill myself", "end my life", "self harm", "hurt myself"]

CRISIS_MESSAGE = (
    "I'm really sorry you're feeling this much pain. This app can't help with this, "
    "but a real person can. In India you can call Tele-MANAS at 14416, "
    "or reach out to someone you trust right now."
)

def untangle(worry):
    reply = client.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": worry},
        ],
    )
    return reply["message"]["content"]

print("Overthink Untangler. Type your worry (or 'quit').")
while True:
    worry = input("\nWhat's looping in your head? > ").strip()
    if worry.lower() == "quit":
        break
    if any(word in worry.lower() for word in CRISIS_WORDS):
        print("\n" + CRISIS_MESSAGE)
        continue
    print("\n" + untangle(worry))