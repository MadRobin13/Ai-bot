import discord
import openai
import dotenv
import os
import sklearn
import pandas as pd
import asyncio

pd.options.display.max_columns = None
pd.options.display.max_rows = None

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPEN_AI_API_KEY')
ai = openai.OpenAI(api_key=OPENAI_API_KEY)
GENAI_ID = os.getenv('GEN_ASSISTANT_ID')


df = pd.read_csv('my_movies.csv')

def eda():
    sorted_df = df.sort_values('Abhi')
    avg = round(sorted_df['Abhi'].mean(), 3)
    least = sorted_df['Movies'].iloc[0]
    greatest = sorted_df['Movies'].iloc[len(sorted_df) - 1]

    return avg, least, greatest

async def syn():
    filter_condition = df['Abhi'] > df['Abhi'].quantile(0.7)
    filtered_df = df[filter_condition]

    messageList = []
    message = {
        'role' : 'user',
        'content' : 'create a a movie synopsis based on these movies I like: ' + str(filtered_df)
    }

    thread = ai.beta.threads.create(
        messages=messageList
    )

    ai.beta.threads.runs.create(
        assistant_id=GENAI_ID,
        max_prompt_tokens=300,
        max_completion_tokens=300,
        thread_id=thread.id
    )

    for i in range(30):
        messages = await ai.beta.threads.messages.list(thread_id=thread.id)
        print(messages.data[0].content[0].text.value)
        if len(messages.data) > 1 and len(messages.data[0].content) > 0:
            return messages.data[0].content[0].text.value
        await asyncio.sleep(1)



    response = "can't do much right now"
    return response


@client.event
async def on_ready():
    print(f"{client.user} is ready")

@client.event
async def on_message(message):
    cont = str(message.content)
    msg = cont[3:].lower()
    output_message = ''
    if message.author.bot:
        return
    # await message.channel.send(str(message.content))
    # await message.channel.send(msg)
    # await message.channel.send('hi')
    if cont.lower().startswith('||'):
        if msg == 'eda':
            avg, least, greatest = eda()
            output_message = f"your average rating is {avg}, your least rated movie is {least}, and your highest rated movie is {greatest}"
            await message.channel.send(output_message)
        if msg == 'syn':
            await message.channel.send(str(await syn()))


def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()