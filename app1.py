import streamlit as st
import pandas as pd
import pickle

st.title(" Women's T20 1st Innings Score Prediction")

teams = ['India', 'Australia', 'South Africa', 'England', 'Barbados',
         'New Zealand', 'Sri Lanka', 'Ireland', 'Bangladesh', 'Pakistan',
         'Scotland', 'Netherlands']

cities = ['Guwahati', 'Sydney', 'St Lucia', 'Galle', 'East London',
          'Trinidad', 'Wellington', 'Colombo', 'Guyana', 'Dublin', 'Sylhet',
          'Derby', 'Nagpur', 'Nottingham', 'Bangkok', 'Potchefstroom',
          'Melbourne', 'Utrecht', 'Birmingham', 'Delhi', 'Taunton',
          'North Sound', 'Grenada', 'Dundee', 'Kuala Lumpur', 'Dambulla',
          'Durban', 'Mirpur', 'Brisbane', 'Antigua', 'Chennai', 'Doha',
          'Canterbury', 'Brighton', 'Johannesburg', 'Nelson', 'Canberra',
          'Surat', 'Cardiff', 'Chelmsford', 'Murcia', 'Barbados',
          'Bridgetown', 'Chandigarh', 'Sharjah', 'Karachi', 'Hamilton',
          'Paarl', 'Mumbai', 'Belfast', 'Loughborough', 'Pietermaritzburg',
          'Mohali', 'Guanggong', 'Deventer', 'Coolidge', 'Dharamsala',
          'Arundel', 'Providence', 'New Plymouth', 'Manchester', 'Perth',
          'Lucknow', 'Amstelveen', 'Bangalore', 'Hove', 'Centurion',
          'Bristol', 'Carrara', 'Southampton', 'Cape Town', 'Victoria',
          'Worcester', 'Northampton', 'London', 'Bready', 'Bloemfontein',
          'Gros Islet', 'Benoni', 'Napier', 'Gold Coast', 'Queenstown',
          'Mount Maunganui', 'FTZ Sports Complex', 'Auckland',
          'Chester-le-Street', 'Pretoria', 'Kolkata', 'Lahore', 'Adelaide',
          'Arbroath', 'Londonderry']

pipe = pickle.load(open('my_pipeline1.pkl', 'rb'))

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting_team ", sorted(teams))

with col2:
    bowling_team = st.selectbox("Select Bowling_team ", sorted(teams))

city = st.selectbox("Select city ", sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input("current_score")
with col4:
    overs = st.number_input("Overs done(Work for over > 5)")
with col5:
    wickets = st.number_input("Wickets_out")

last_five = st.number_input("Runs Scored in last 5 overs")

if st.button('Predict Score'):
    ball_left = 120 - (overs * 6)

    wicket_left = 10 - wickets

    crr = current_score / overs
    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team],
                             'city': [city], 'current_score': [current_score],
                             'ball_left': [ball_left],'wicket_left': [wicket_left],
                             'crr': [crr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header('Predict Score' + str(int(result)))


