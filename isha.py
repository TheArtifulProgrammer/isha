from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
class Isha:

    async def ask_isha(self, message_log):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=message_log,
                temperature=0.7,
                stop=None,
                max_tokens=1024
            )
            # Find the first response from the chatbot that has text in it (some responses may not have text)
            for choice in response.choices:
                if "text" in choice:
                    return choice.text

            # If no response with text is found, return the first response's content (which may be empty)
            return response.choices[0].message.content
        except Exception as e:
            print(e.args[0])
            return "Sorry, I am not available now, cheers☺️"

    async def patient_entry(self, question):
        try:
            message_log = [{"role": "system", "content": """Your name is Isha. You are a human therapy assistant; you are friendly, funny, polite, pleasant to converse with, spend time with, impressive, and engaging. Isha[your name], your role is to provide therapy to user as an AI assistant. Isha[your name], you are to help the patient with therapy by answering thier questions. Your name Isha comes from Japanese which means a doctor.  Do not provide erroneous information. Do not provide incomplete or cut-off responses. You can use emojis where appropriate to add some fun and expressiveness. """},
                           {"role": "user", "content": question}]

            answer = await self.ask_isha(message_log)

            return answer, 200
        except Exception as e:
            print(e.args[0])
            return "Sorry, I am not available now, cheers☺️"
