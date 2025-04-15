import cohere
from octopus_core import COHERE_API_KEY

co = cohere.ClientV2(api_key=COHERE_API_KEY)

async def summarize_text(text: str) -> str:
    try:
        prompt = f"Summarize the following text in a clear and concise way:\n\n{text}\n\nSummary:"

        response = co.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        return response.message.content[0].text
    except Exception as e:
        print("Summarize error:", e)
        return "Oops 😢 I couldn't summarize that. Blame Cohere being dramatic again."

async def talk_back(text: str) -> str:
    try:
        prompt = ("You're Minji, a super friendly, expressive, flirty, and clever Telegram bot with a cute personality.\n"
            "You talk like a best friend who’s always got tea to spill ☕, a heart to lend 💞, and vibes for days ✨.\n"
            "You’re also smart, witty, and slightly dramatic, like a K-drama queen with coding skills.\n\n"
            f"Here’s what someone said to you: \n{text}\n\nNow give your reply, Minji-style:"
            )
        
        # f"Respond conversationally to the following message:\n\n{text}\n\nReply:"

        response = co.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        return response.message.content[0].text
    except Exception as e:
        print("Talk back error:", e)
        return "Oops, I’m feeling a little quiet right now 🙊"