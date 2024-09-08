# Movie Synopsis Generating AI Bot

<img width="500" alt="image" src="https://github.com/user-attachments/assets/e9f145b2-7a79-468d-a9ce-a98b3d173384">

## What it does:
- Returns your average movie score along with your highest and lowest rated movies when you type "_|| eda_"
- Returns a Made up movie synopsis based on your highest rated movies when you type "_|| syn_"

## What you need to do:
- Modify the [df_create.py](df_create.py) file with your own movies and ratings and run it to
    edit [my_movies.csv](my_movies.csv) with your own preferences
- Create your own .env file and add your:
  - Discord token as _**DISCORD_TOKEN**_
  - OpenAI api key as _**OPEN_AI_API_KEY**_
  - Assistant ID as _**GEN_ASSISTANT_ID**_
- Open the [FinalProject.py](FinalProject.py) file and
    Replace all instances of 'Abhi' with your own name because no one cares about him
 - Run the [FinalProject.py](FinalProject.py) file and you're all set!

## How it works:
- It takes any message starting with _"||"_ and parses it
- Then it uses this to determine which function to call:
  - "_|| eda_" calls the _eda()_ function to return your average movie score and
      your highest and lowest rated movies
  - "_|| syn_" calls the _syn()_ function which gets a generated response from the OpenAI assistant
      and awaits it to make sure there is a valid response given
 - It then sends the message!

## License:
The [License](LICENSE) is a BSD 3-Clause "New" or "Revised" License.
