import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

new_dict = {
    'Movies' : ['Pacific Rim', 'Avengers Endgame', 'Mall Cop', 'Titanic', 'It', 'Scary Stories to Tell in the Dark'],
    'Abhi' : [0.69, 0.84, 0.53, 0.79, 0.73, 0.75],
    'Fred' : [0.9, 0.85, 0.15, 0.1, 0.15, 0.1],
    'Sarah' : [0.05, 0.1, 0.6, 0.2, 0.7, 0.7]
}

my_movies = pd.DataFrame(new_dict)

my_movies.to_csv('my_movies.csv', index=False)