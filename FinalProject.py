import discord
import openai
import dotenv
import os
import sklearn
import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

dotenv.load_dotenv()

intents = discord.Intents.default()

client = discord.Client(intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPEN_AI_API_KEY')
GENAI_ID = os.getenv('GEN_ASSISTANT_ID')


df = pd.read_csv('my_movies.csv')

def eda():
    sorted_df = df.sort_values('Abhi')
    avg = sorted_df['Abhi'].mean()
    least = sorted_df['Movies'].iloc[0]
    greatest = sorted_df['Movies'].iloc[len(sorted_df) - 1]

    return avg, least, greatest

@client.event
async def on_ready():
    print(f"{client.user} is ready")

@client.event
async def on_message(message):
    cont = message.content.split()
    msg = ' '.join(cont[1:]).lower()
    output_message = ''
    if message.author.bot:
        return
    await message.channel.send('hi')
    if cont[0] == '||':
        await message.channel.send('hello')
        if msg == 'eda':
            avg, least, greatest = eda()
            output_message = f"your average is {avg}, your least rated movie is {least} and your highest rated movie is {greatest}"
        await message.channel.send(output_message)


def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()