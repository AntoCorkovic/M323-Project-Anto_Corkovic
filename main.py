from flask import Flask
from functools import reduce

app = Flask(__name__)

class StartingEleven:
    def __init__(self, team_name, players):
        self.team_name = team_name
        self.players = players

    def get_starting_eleven(self):
        return f"{self.team_name} Starting Eleven: {', '.join(self.players)}"

barcelona_starting_eleven = StartingEleven("Barcelona", ("Ter Stegen", "Cancelo", "Balde", "Araujo", "Kounde", "Gavi", "Pedri", "De Jong", "Gündogan", "Torres", "Lewandowski"))
real_madrid_starting_eleven = StartingEleven("Real Madrid", ("Courtois", "Carvajal", "Militao", "Rüdiger", "Mendy", "Valverde", "Modric", "Bellingham", "Kroos", "Vinicius", "Rodrygo"))

def get_first_letters(players):
    return ', '.join(list(map(lambda player: player[0], players)))

get_starting_eleven_response = StartingEleven.get_starting_eleven
get_starting_eleven_response = staticmethod(get_starting_eleven_response)

@app.route('/')
def home():
    return "Welcome to the Football App!"

@app.route('/barcelona')
def barcelona():
    return get_starting_eleven_response(barcelona_starting_eleven)

@app.route('/real-madrid')
def real_madrid():
    return get_starting_eleven_response(real_madrid_starting_eleven)

def get_team_first_letters(team):
    first_letters = get_first_letters(team.players)
    return f"{team.team_name} First Letters: {first_letters}"

@app.route('/barcelona/first-letters')
def barcelona_first_letters():
    return get_team_first_letters(barcelona_starting_eleven)

@app.route('/real-madrid/first-letters')
def real_madrid_first_letters():
    return get_team_first_letters(real_madrid_starting_eleven)

@app.route('/players-starting-with-m')
def players_starting_with_m():
    all_players = barcelona_starting_eleven.players + real_madrid_starting_eleven.players
    m_players = sorted(filter(lambda player: player.startswith('M'), all_players), key=lambda player: len(player))
    return f"Players whose names start with 'M' and sorted by length: {', '.join(m_players)}"

@app.route('/all-players')
def all_players():
    all_players = list(map(str, barcelona_starting_eleven.players + real_madrid_starting_eleven.players))
    return f"All Players: {', '.join(all_players)}"

@app.route('/remove-players')
def remove_players():
    real_madrid_players = list(real_madrid_starting_eleven.players)
    reduced_players = reduce(lambda players, _ : players[:-3], range(3), real_madrid_players)
    return f"Real Madrid Players after removing 3 players: {', '.join(reduced_players)}"

@app.route('/real-madrid-players-by-name-length')
def real_madrid_players_by_name_length():
    real_madrid_players = real_madrid_starting_eleven.players
    filtered_players = filter(lambda player: len(player) >= 7, real_madrid_players)
    return f"Real Madrid Players with names of length 7 or more: {', '.join(filtered_players)}"

@app.route('/process-players')
def process_players():
    all_players = list(map(str, barcelona_starting_eleven.players + real_madrid_starting_eleven.players))
    filtered_players = list(filter(lambda player: len(player), all_players))
    sorted_players = sorted(filtered_players, key=lambda player: len(player))
    reduced_players = reduce(lambda players, _: players[:-3], range(3), sorted_players)
    return f"Processed Players: {', '.join(reduced_players)}"

if __name__ == '__main__':
    app.run(debug=True)