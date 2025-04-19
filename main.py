import pandas as pd
import datetime
import streamlit as st
from scraper.player_stats import get_player_stats
from scraper.weather import get_weather_data
from scraper.ballpark_factors import get_ballpark_factor
from scraper.odds_scraper import get_hr_odds
from scraper.pitcher_scraper import get_probable_pitchers
from models.rating_model import rate_player
from matchup.calculate_matchup_boost import calculate_matchup_boost

def generate_daily_projections(date=None):
    if date is None:
        date = datetime.datetime.now().strftime("%Y-%m-%d")

    stats_df = get_player_stats(date)
    odds_df = get_hr_odds(date)
    pitcher_dict = get_probable_pitchers(date)

    merged = stats_df.merge(odds_df, on="Player", how="left")

    projections = []
    for _, row in merged.iterrows():
        player = row['Player']
        team = row['Team']
        opponent = row['Opponent']
        stadium = row['Stadium']

        weather_boost = get_weather_data(stadium, date)
        park_boost = get_ballpark_factor(stadium)

        pitcher = pitcher_dict.get(opponent, {}).get("name")
        pitcher_hand = pitcher_dict.get(opponent, {}).get("hand", "R")

        matchup_boost = calculate_matchup_boost(player, pitcher, pitcher_hand)
        rating = rate_player(row, weather_boost, park_boost, matchup_boost)

        projections.append({
            "Player": player,
            "Team": team,
            "HR Odds": row.get("HR Odds", "N/A"),
            "2025 Stats": f"{row['HR']} HR in {row['G']} games",
            "AI Rating": rating
        })

    df = pd.DataFrame(projections)
    df = df.sort_values(by="AI Rating", ascending=False).reset_index(drop=True)
    df.index += 1
    return df

def main():
    st.set_page_config(page_title="MLB HR Predictor", layout="wide")
    st.title("🔮 Daily MLB Home Run Projections")

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    st.caption(f"Projections for {today}")

    try:
        df = generate_daily_projections(today)
        st.success("✅ Projections generated!")
        st.dataframe(df.head(10), use_container_width=True)
    except Exception as e:
        st.error(f"⚠️ Error generating projections: {e}")

if __name__ == "__main__":
    main()
