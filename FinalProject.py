import discord
import openai
import dotenv
import os
import sklearn
import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('future.no_silent_downcasting', True)

dotenv.load_dotenv()

intents = discord.Intents.default()

client = discord.Client(intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPEN_AI_API_KEY')
GENAI_ID = os.getenv('GEN_ASSISTANT_ID')


df = pd.read_csv('movies_metadata.csv')

links_small = pd.read_csv('links_small.csv')
df = df.drop([19730, 29503, 35587])
df['id'] = df['id'].astype('int')
links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')

small_df = df[df['id'].isin(links_small)].dropna(axis=0, how='all')

small_df['overview'].fillna('')
small_df['tagline'].fillna('')
small_df['description'] = small_df['overview'].fillna('') + small_df['tagline'].fillna('')

small_df.fillna(0)

print(small_df.shape)

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()