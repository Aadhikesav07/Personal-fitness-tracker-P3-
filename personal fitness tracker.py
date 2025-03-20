import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import datetime
import random

st.set_page_config(page_title="Smart Fitness Tracker", layout="wide", page_icon="🔥")

if 'streak' not in st.session_state:
    st.session_state['streak'] = 0
if 'last_login' not in st.session_state:
    st.session_state['last_login'] = datetime.date.today()

def update_streak():
    today = datetime.date.today()
    if today - st.session_state['last_login'] == datetime.timedelta(days=1):
        st.session_state['streak'] += 1
    elif today - st.session_state['last_login'] > datetime.timedelta(days=1):
        st.session_state['streak'] = 1
    st.session_state['last_login'] = today

update_streak()

st.sidebar.header("🔹 User Input Parameters")
age = st.sidebar.slider("Age", 10, 100, 30)
bmi = st.sidebar.slider("BMI", 15.0, 40.0, 22.0)
duration = st.sidebar.slider("Workout Duration (min)", 0, 120, 30)
heart_rate = st.sidebar.slider("Heart Rate", 60, 180, 90)
body_temp = st.sidebar.slider("Body Temperature (°C)", 36.0, 42.0, 37.5)
gender = st.sidebar.radio("Gender", ["Male", "Female"])
gender_male = 1 if gender == "Male" else 0

workout_plan = random.choice([
    "🏋️‍♂️ Strength Training: Squats, Deadlifts, Bench Press",
    "🏃‍♂️ Cardio: HIIT, Jump Rope, Running",
    "🧘 Yoga & Stretching: Improve Flexibility & Recovery",
    "🚴 Cycling: Endurance & Lower Body Strength",
    "🏊 Swimming: Full Body Cardio & Strength"
])

diet_plan = random.choice([
    "🥗 High Protein Diet: Chicken, Eggs, Quinoa, Tofu",
    "🥑 Healthy Fats: Avocados, Nuts, Olive Oil",
    "🍎 Balanced Diet: Fruits, Vegetables, Lean Proteins",
    "🍣 Omega-3 Rich Foods: Salmon, Chia Seeds, Walnuts"
])

st.subheader("🎯 AI-Powered Fitness Plan")
st.info(f"**Workout Plan:** {workout_plan}")
st.info(f"**Diet Recommendation:** {diet_plan}")

data = {"Fat Burned": duration * 0.1, "Protein Intake": 40, "Carb Intake": 100, "Fats Intake": 30}
fig_pie = px.pie(names=data.keys(), values=data.values(), title="Daily Macronutrient & Fat Burn Split")
st.plotly_chart(fig_pie)

st.sidebar.subheader("🔥 Your Streak: ")
st.sidebar.success(f"{st.session_state['streak']} Days Active! Keep it up! 🏆")

st.subheader("📊 Weekly Workout Progress")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
calories_burned = [random.randint(200, 500) for _ in days]
fig_progress = px.bar(x=days, y=calories_burned, labels={'x': "Day", 'y': "Calories Burned"}, title="Calories Burned This Week", color=calories_burned, color_continuous_scale='viridis')
st.plotly_chart(fig_progress)

st.subheader("💬 Ask AI: Health & Fitness Tips")
user_query = st.text_input("Ask any fitness-related question:")
if user_query:
    st.write("🤖 AI Suggestion:")
    st.success(random.choice([
        "Stay consistent! Fitness is a marathon, not a sprint.",
        "Drink at least 2 liters of water daily for optimal hydration.",
        "Recovery is as important as workouts. Sleep 7-9 hours daily!",
        "Strength training boosts metabolism and burns fat effectively.",
        "Mix cardio and weight training for best results."
    ]))

st.markdown("---")
st.subheader("🚀 Stay Fit & Keep Hustling!")
