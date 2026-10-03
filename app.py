import streamlit as st

st.set_page_config(
    page_title="StepUp",
    page_icon="👟",
    layout="centered"
)

# ---------- Session state ----------
if "steps" not in st.session_state:
    st.session_state.steps = 4283

GOAL = 8000
progress = min(st.session_state.steps / GOAL, 1.0)
percentage = int((st.session_state.steps / GOAL) * 100)

# ---------- Styling ----------
st.markdown("""
<style>
    .main {
        background-color: #f8faf9;
    }

    .block-container {
        max-width: 700px;
        padding-top: 3rem;
    }

    .title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }

    .step-card {
        background: white;
        padding: 2.5rem;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        margin-bottom: 1.5rem;
    }

    .steps {
        font-size: 4rem;
        font-weight: 700;
        color: #16a34a;
    }

    .label {
        color: #6b7280;
        font-size: 1rem;
    }

    .goal {
        color: #6b7280;
        margin-top: 10px;
    }

    .message {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 1.5rem 0;
    }

    .weekly {
        background: white;
        padding: 1.5rem;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    footer {
        text-align: center;
        color: #9ca3af;
        font-size: 0.75rem;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="title">👟 StepUp</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Small steps. Better days.</div>',
    unsafe_allow_html=True
)

# ---------- Main card ----------
st.markdown('<div class="step-card">', unsafe_allow_html=True)

st.markdown(
    f'<div class="steps">{st.session_state.steps:,}</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="label">steps today</div>',
    unsafe_allow_html=True
)

st.progress(progress)

st.markdown(
    f'<div class="goal">Daily goal: {GOAL:,} &nbsp; • &nbsp; {percentage}%</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Message ----------
if percentage >= 100:
    message = "🎉 Goal reached! Great job!"
elif percentage >= 50:
    message = "💪 You're getting there!"
else:
    message = "🚶 Keep moving!"

st.markdown(
    f'<div class="message">{message}</div>',
    unsafe_allow_html=True
)

# ---------- Buttons ----------
col1, col2 = st.columns(2)

with col1:
    if st.button("➕ 100 Steps", use_container_width=True):
        st.session_state.steps += 100
        st.rerun()

with col2:
    if st.button("➕ 500 Steps", use_container_width=True):
        st.session_state.steps += 500
        st.rerun()

if st.button("🔄 Reset Day", use_container_width=True):
    st.session_state.steps = 0
    st.rerun()

# ---------- Weekly progress ----------
st.markdown("### 📊 Weekly Progress")

weekly_data = {
    "Mon": 6200,
    "Tue": 4800,
    "Wed": 7500,
    "Thu": 3900,
    "Fri": 6800,
    "Sat": 8200,
    "Sun": st.session_state.steps
}

for day, steps in weekly_data.items():
    pct = min(steps / GOAL, 1.0)

    col1, col2 = st.columns([1, 5])

    with col1:
        st.write(f"**{day}**")

    with col2:
        st.progress(pct)

# ---------- Footer ----------
st.markdown(
    '<footer>StepUp is for general wellness tracking and is not medical advice.</footer>',
    unsafe_allow_html=True
)
