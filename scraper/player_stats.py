import pandas as pd

def get_player_stats(date):
    return pd.DataFrame([
        {"Player": "Fernando Tatis Jr.", "Team": "San Diego Padres", "Opponent": "Dodgers", "Stadium": "Petco Park", "HR": 6, "G": 19},
        {"Player": "Peter Alonso", "Team": "New York Mets", "Opponent": "Giants", "Stadium": "Citi Field", "HR": 5, "G": 20},
        {"Player": "Tyler Soderstrom", "Team": "Oakland Athletics", "Opponent": "Angels", "Stadium": "Oakland Coliseum", "HR": 9, "G": 19},
        {"Player": "James Wood", "Team": "Washington Nationals", "Opponent": "Braves", "Stadium": "Nationals Park", "HR": 6, "G": 19},
        {"Player": "Spencer Torkelson", "Team": "Detroit Tigers", "Opponent": "White Sox", "Stadium": "Comerica Park", "HR": 6, "G": 20},
        {"Player": "Corbin Carroll", "Team": "Arizona Diamondbacks", "Opponent": "Rockies", "Stadium": "Chase Field", "HR": 6, "G": 20},
        {"Player": "Eugenio Suárez", "Team": "Arizona Diamondbacks", "Opponent": "Rockies", "Stadium": "Chase Field", "HR": 6, "G": 20},
        {"Player": "Juan Soto", "Team": "New York Mets", "Opponent": "Giants", "Stadium": "Citi Field", "HR": 3, "G": 20},
        {"Player": "Yordan Alvarez", "Team": "Houston Astros", "Opponent": "Rangers", "Stadium": "Minute Maid Park", "HR": 2, "G": 18},
        {"Player": "Wilmer Flores", "Team": "San Francisco Giants", "Opponent": "Mets", "Stadium": "Oracle Park", "HR": 6, "G": 20}
    ])
