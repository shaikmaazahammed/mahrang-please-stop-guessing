import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Top Secret Portal 🔐",
    page_icon="💀",
    layout="centered"
)

# --- CSS STYLING ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Creepster&family=Bangers&family=Comic+Neue:wght@700&display=swap');

html, body, [class*="css"] {
    background-color: #0d0d0d;
}

.stApp {
    background: radial-gradient(ellipse at top, #1a0033 0%, #0d0d0d 70%);
    min-height: 100vh;
}

h1.title {
    font-family: 'Bangers', cursive;
    font-size: 3.2rem;
    color: #ff3cac;
    text-align: center;
    letter-spacing: 4px;
    text-shadow: 0 0 20px #ff3cac, 0 0 40px #ff006688;
    margin-bottom: 0;
}

p.subtitle {
    font-family: 'Comic Neue', cursive;
    color: #aaa;
    text-align: center;
    font-size: 0.95rem;
    margin-top: 4px;
}

.login-box {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255, 60, 172, 0.25);
    border-radius: 16px;
    padding: 36px 40px;
    box-shadow: 0 0 60px rgba(255, 60, 172, 0.08);
    margin-top: 20px;
}

.stTextInput > label {
    font-family: 'Comic Neue', cursive !important;
    color: #cc88ff !important;
    font-size: 0.9rem !important;
}

.stTextInput > div > div > input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,60,172,0.3) !important;
    border-radius: 8px !important;
    color: white !important;
    font-family: 'Comic Neue', cursive !important;
}

div.stButton > button {
    background: linear-gradient(135deg, #ff3cac, #784ba0, #2b86c5);
    color: white;
    font-family: 'Bangers', cursive;
    font-size: 1.3rem;
    letter-spacing: 2px;
    border: none;
    border-radius: 10px;
    padding: 12px 0;
    width: 100%;
    cursor: pointer;
    transition: transform 0.1s ease, box-shadow 0.2s ease;
    box-shadow: 0 4px 30px rgba(255,60,172,0.3);
}

div.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 6px 40px rgba(255,60,172,0.5);
}

.wrong-password {
    background: rgba(255, 50, 50, 0.12);
    border: 1px solid rgba(255,80,80,0.4);
    border-radius: 10px;
    padding: 14px 18px;
    color: #ff6b6b;
    font-family: 'Comic Neue', cursive;
    font-size: 1rem;
    text-align: center;
    margin-top: 12px;
}

.welcome-box {
    background: rgba(255, 60, 172, 0.07);
    border: 2px solid rgba(255,60,172,0.5);
    border-radius: 16px;
    padding: 30px;
    text-align: center;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { box-shadow: 0 0 20px rgba(255,60,172,0.2); }
    to   { box-shadow: 0 0 50px rgba(255,60,172,0.6); }
}

.welcome-title {
    font-family: 'Bangers', cursive;
    font-size: 2.5rem;
    color: #ff3cac;
    letter-spacing: 3px;
}

.bully-text {
    font-family: 'Creepster', cursive;
    font-size: 1.8rem;
    color: #ff6b6b;
    margin: 10px 0;
}

.chaos-text {
    font-family: 'Comic Neue', cursive;
    color: #ccaaff;
    font-size: 1rem;
    line-height: 1.7;
}

.hint-text {
    font-family: 'Comic Neue', cursive;
    color: #666;
    font-size: 0.78rem;
    text-align: center;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- APP LOGIC ---
CORRECT_USERNAME = "Mahrang"
CORRECT_PASSWORD = "Sheslays"

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "wrong_attempts" not in st.session_state:
    st.session_state.wrong_attempts = 0

# --- LOGGED IN VIEW ---
if st.session_state.logged_in:
    st.markdown("""
    <div class='welcome-box'>
        <div class='welcome-title'>👑 WELCOME BACK, QUEEN 👑</div>
        <div class='bully-text'>⚠️ Mahrang is a Bully ⚠️</div>
        <div class='chaos-text'>
            Congratulations on successfully logging in<br>
            to your own personal chaos portal.<br><br>
            🐍 Known facts about Mahrang:<br>
            • Will steal your fries without asking<br>
            • Has never returned a single borrowed item<br>
            • Calls you at 2am for "a quick question"<br>
            • The definition of a menace to society<br><br>
            <em>...but we love her anyway 💅</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚪 Log Out (Escape While You Can)"):
            st.session_state.logged_in = False
            st.session_state.wrong_attempts = 0
            st.rerun()

# --- LOGIN VIEW ---
else:
    st.markdown("<h1 class='title'>🔐 TOP SECRET PORTAL</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Authorized personnel only. Yes, that means you, Mahrang.</p>", unsafe_allow_html=True)

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    username = st.text_input("👤 Username", placeholder="Who dares enter?")
    password = st.text_input("🔑 Password", type="password", placeholder="Think carefully...")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        login_btn = st.button("⚡ ENTER THE VOID ⚡")

    if login_btn:
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            st.session_state.logged_in = True
            st.session_state.wrong_attempts = 0
            st.balloons()
            time.sleep(0.5)
            st.rerun()
        elif username != CORRECT_USERNAME and username != "":
            st.markdown(f"""
            <div class='wrong-password'>
                🤨 "{username}"?? Who even is that?<br>
                <small>That's not a real person. Try again.</small>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.wrong_attempts += 1
        elif username == CORRECT_USERNAME and password != CORRECT_PASSWORD:
            st.session_state.wrong_attempts += 1
            attempts = st.session_state.wrong_attempts

            if attempts == 1:
                msg = "❌ Wrong password! Don't be like Mahrang — she can't remember anything either. 🙄"
            elif attempts == 2:
                msg = "❌ Still wrong! Mahrang would've given up by now tbh 💀"
            elif attempts == 3:
                msg = "❌ THREE times?? You're literally being Mahrang right now. Embarrassing. 😭"
            else:
                msg = f"❌ Attempt #{attempts}... at this point you ARE Mahrang. Accept your fate. 🐸"

            st.markdown(f"<div class='wrong-password'>{msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class='wrong-password'>
                🫠 Please fill in both fields.<br>
                <small>Unless you're Mahrang, in which case — take your time, queen.</small>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<p class='hint-text'>💡 Hint: The password rhymes with 'she slays'... because she does. Allegedly.</p>", unsafe_allow_html=True)
