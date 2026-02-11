import streamlit as st
from datetime import date

from utils import calculate_bmi
from workout import get_workout_plan
from progress import save_progress_to_csv, load_progress
from theme import apply_theme

apply_theme()

st.set_page_config(
    page_title="FORGE",
    page_icon="💪",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "profile" not in st.session_state:
    st.session_state.profile = {}

# ---------------- STEP 1: PROFILE ----------------
if st.session_state.step == 1:
    st.title("FORGE 🖤💛")
    st.subheader("Create Your Profile")

    name = st.text_input("Name")
    age = st.number_input("Age", 15, 60)
    height = st.number_input("Height (cm)")
    weight = st.number_input("Weight (kg)")
    goal = st.selectbox("Goal", ["Muscle Gain", "Fat Loss", "Maintenance"])

    if st.button("Save & Continue"):
        st.session_state.profile = {
            "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "goal": goal
        }
        st.session_state.step = 2

# ---------------- STEP 2: CHOICE ----------------
elif st.session_state.step == 2:
    st.subheader(f"Welcome, {st.session_state.profile['name']} 💪")

    choice = st.radio(
        "What do you want to do today?",
        [
            "📊 Calculate BMI",
            "🔥 Calculate Calories",
            "🏋️ Workout Planner",
            "📈 Progress Tracker"
        ]
    )

    if st.button("Proceed"):
        if "BMI" in choice:
            st.session_state.step = 3
        elif "Calories" in choice:
            st.session_state.step = 4
        elif "Workout" in choice:
            st.session_state.step = 5
        elif "Progress" in choice:
            st.session_state.step = 6

# ---------------- STEP 3: BMI ----------------
elif st.session_state.step == 3:
    st.subheader("📊 BMI Analysis")

    h = st.session_state.profile["height"]
    w = st.session_state.profile["weight"]

    bmi = calculate_bmi(w, h)
    st.metric("Your BMI", round(bmi, 2))

    if bmi < 18.5:
        st.warning("Underweight – focus on nutrition & strength")
    elif bmi < 25:
        st.success("Normal – maintain consistency")
    else:
        st.error("Overweight – calorie control needed")

    if st.button("⬅ Back"):
        st.session_state.step = 2

# ---------------- STEP 4: CALORIES ----------------
elif st.session_state.step == 4:
    st.subheader("🔥 Daily Calorie Estimate")

    weight = st.session_state.profile["weight"]
    calories = weight * 30

    st.metric("Estimated Calories", f"{calories} kcal/day")
    st.info("Adjust based on workout intensity")

    if st.button("⬅ Back"):
        st.session_state.step = 2

# ---------------- STEP 5: WORKOUT ----------------
elif st.session_state.step == 5:
    st.subheader("🏋️ Workout Planner")

    goal = st.session_state.profile["goal"]
    plan = get_workout_plan(goal)

    for day, exercises in plan.items():
        st.markdown(f"### {day}")
        for ex, reps in exercises:
            st.write(f"- **{ex}** → {reps}")

    st.success("Progressive overload. Stay disciplined 💪")

    if st.button("⬅ Back"):
        st.session_state.step = 2

# ---------------- STEP 6: PROGRESS ----------------
elif st.session_state.step == 6:
    st.subheader("📈 Progress Tracker")

    entry_date = st.date_input("Date", date.today())
    weight = st.number_input("Weight (kg)", 30.0, 200.0)
    workout_done = st.checkbox("Workout Completed")

    if st.button("Save Progress"):
        save_progress_to_csv({
            "date": entry_date,
            "weight": weight,
            "workout_done": workout_done
        })
        st.success("Progress saved 💪")

    df = load_progress()
    if not df.empty:
        st.line_chart(df.set_index("date")["weight"])

    if st.button("⬅ Back"):
        st.session_state.step = 2
