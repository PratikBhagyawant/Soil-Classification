import streamlit as st
import pandas as pd

# ------------------------------------------
# Page Configuration
# ------------------------------------------
st.set_page_config(page_title="GreenPulse AI", page_icon="🌿", layout="wide")

# ------------------------------------------
# Custom CSS
# ------------------------------------------
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 100%;
    }
    h1, h2, h3, h4, h5 {
        text-align: center;
    }
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    .lang-select {
        position: fixed;
        top: 15px;
        right: 25px;
        z-index: 1000;
        background-color: #f5f5f5;
        padding: 4px 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    .login-box {
        background-color: #f0fdf4;
        border-radius: 15px;
        padding: 40px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        margin-top: 80px;
        width: 400px;
        margin-left: auto;
        margin-right: auto;
    }
    .login-title {
        font-size: 48px;
        color: #2E7D32;
        font-weight: bold;
        text-align: center;
    }
    .login-subtitle {
        font-size: 18px;
        color: #555;
        margin-bottom: 30px;
    }
    .logout-container {
        text-align: center;
        margin-top: 40px;
    }
    .logout-button {
        background-color: #e53935 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 30px;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------
# Session Initialization
# ------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "language" not in st.session_state:
    st.session_state.language = "English"

# ------------------------------------------
# LOGIN PAGE
# ------------------------------------------
if not st.session_state.logged_in:
    st.markdown("<h1 class='login-title'>🌿 GreenPulse AI</h1>", unsafe_allow_html=True)
    st.markdown("<h5 class='login-subtitle'>Smart Soil Health & Crop Recommendation System</h5>", unsafe_allow_html=True)

    username = st.text_input("👤 Username", "")
    password = st.text_input("🔒 Password", type="password")

    col1, col2, col3 = st.columns([1, 0.5, 1])
    with col2:
        if st.button("Login", use_container_width=True):
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("✅ Login successful! Redirecting...")
                st.rerun()
            else:
                st.error("❌ Invalid username or password")
    st.stop()

# ------------------------------------------
# MAIN APP (AFTER LOGIN)
# ------------------------------------------

st.set_page_config(page_title="Soil Health Card Generator", page_icon="🌱", layout="wide")

# ------------------------------------------
# Language Toggle (Top-Right)
# ------------------------------------------
def set_language(lang):
    st.session_state.language = lang

st.markdown('<div class="lang-select">🌐 Language:</div>', unsafe_allow_html=True)
col1, col2 = st.columns([0.9, 0.1])
with col2:
    lang_choice = st.radio("", ["English", "मराठी"], horizontal=False, label_visibility="collapsed")
    set_language(lang_choice)

lang = st.session_state.language

# ------------------------------------------
# Language Dictionary
# ------------------------------------------
T = {
    "English": {
        "title": "🌱 Soil Health Card Generator",
        "subtitle": "Upload soil data or enter manually to get crop recommendations based on Soil Fertility Index (SFI).",
        "choose_input": "📥 Choose Input Method",
        "upload": "📂 Upload CSV File",
        "manual": "✍️ Enter Data Manually",
        "enter_soil": "✍️ Enter Soil Parameters Manually",
        "check_health": "🔍 Check Soil Health",
        "check_fertility": "✅ Check Fertility",
        "recommend_fertilizer": "🌱 Recommend Organic Fertilizer",
        "recommend_crop": "🌾 Recommend Crops",
        "warning": "⚠️ Please upload a soil CSV file or enter data manually to proceed.",
        "footer": "© 2025 GreenPulse AI | Developed with ❤️ using Streamlit",
        "tabs": ["🧾 Soil Health Card", "🌿 Fertility Check", "🌾 Recommendations"],
        "health_report": "🧾 Soil Health Report",
        "fertile": "✅ Soil Health Status: Healthy (Fertile)",
        "non_fertile": "❌ Soil Health Status: Unhealthy (Non-Fertile)",
        "fertilizer_header": "🌱 Organic Fertilizer Recommendations",
        "fertilizer_text": """
- Apply FYM (10–15 tons/ha) or Vermicompost (2–4 tons/ha)  
- Add green manure crops before the main crop  
- Use compost enriched with rock phosphate + biofertilizers (Azotobacter, PSB, KSB)  
- Apply neem cake or oil cakes for N & S improvement  
""",
        "crop_header": "🌾 Recommended Crops",
        "crops": [
            {"name": "🍇 Grapes (Vitis vinifera)", "notes": "Prefers well-drained soils with good aeration."},
            {"name": "🫑 Capsicum (Bell Pepper)", "notes": "Needs fertile, well-drained soils with high organic matter."},
            {"name": "🥭 Passion Fruit", "notes": "Thrives in soils rich in organic matter with good drainage."},
            {"name": "🍬 Sugarcane", "notes": "Requires deep, fertile soils. Nitrogen and potassium are essential."},
            {"name": "🌱 Soybean", "notes": "Fixes atmospheric nitrogen, enriching soil fertility."},
            {"name": "🥜 Groundnut", "notes": "Best in sandy loam/loamy soils. Nitrogen-fixing improves fertility."},
            {"name": "🌿 Cowpea", "notes": "Drought-tolerant legume, improves soil nitrogen levels."},
            {"name": "🌾 Moth Bean", "notes": "Suited for arid regions, improves soil fertility."},
        ]
    },
    "मराठी": {
        "title": "🌱 मातीचे आरोग्य पत्रक जनरेटर",
        "subtitle": "मातीची माहिती अपलोड करा किंवा स्वहस्ते भरा आणि मातीचे सुपीकता निर्देशांक (SFI) वर आधारित पिकांच्या शिफारसी मिळवा.",
        "choose_input": "📥 इनपुट पद्धत निवडा",
        "upload": "📂 CSV फाइल अपलोड करा",
        "manual": "✍️ माहिती स्वतः भरा",
        "enter_soil": "✍️ मातीच्या घटकांची माहिती भरा",
        "check_health": "🔍 मातीचे आरोग्य तपासा",
        "check_fertility": "✅ सुपीकता तपासा",
        "recommend_fertilizer": "🌱 सेंद्रिय खत सुचवा",
        "recommend_crop": "🌾 पिके सुचवा",
        "warning": "⚠️ कृपया मातीचे CSV फाइल अपलोड करा किंवा माहिती स्वहस्ते भरा.",
        "footer": "© 2025 GreenPulse AI |",
        "tabs": ["🧾 मातीचे आरोग्य पत्रक", "🌿 सुपीकता तपासणी", "🌾 शिफारसी"],
        "health_report": "🧾 मृदा आरोग्य अहवाल",
        "fertile": "✅ मातीचे स्थिती: आरोग्यदायी (सुपीक)",
        "non_fertile": "❌ मातीचे स्थिती: अस्वस्थ (असुपीक)",
        "fertilizer_header": "🌱 सेंद्रिय खतांची शिफारस",
        "fertilizer_text": """
- शेणखत (१०–१५ टन/हे.) किंवा गांडूळखत (२–४ टन/हे.) वापरा  
- मुख्य पिकापूर्वी हिरवळीचे खत पिके घ्या  
- खडकातील फॉस्फेट + सूक्ष्मजीव खत (Azotobacter, PSB, KSB) वापरा  
- नीम केक / तेलबिया केक वापरून नायट्रोजन आणि गंधक वाढवा  
""",
        "crop_header": "🌾 शिफारस केलेली पिके",
        "crops": [
            {"name": "🍇 द्राक्षे", "notes": "पाण्याचा निचरा चांगला होणाऱ्या मातीमध्ये उत्तम वाढतात."},
            {"name": "🫑 ढोबळी मिरची", "notes": "सेंद्रिय घटकांनी समृद्ध सुपीक माती आवश्यक."},
            {"name": "🥭 कृष्णकमळ (पॅशन फ्रूट)", "notes": "सेंद्रिय पदार्थांनी भरपूर आणि चांगला निचरा असलेली माती योग्य."},
            {"name": "🍬 ऊस", "notes": "सखोल, सुपीक माती आवश्यक. नायट्रोजन आणि पोटॅशियम अत्यावश्यक."},
            {"name": "🌱 सोयाबीन", "notes": "वायुमधील नायट्रोजन बांधते, त्यामुळे मातीची सुपीकता वाढते."},
            {"name": "🥜 शेंगदाणा", "notes": "वालुकामय मातीमध्ये चांगले वाढतात. नायट्रोजन स्थिरीकरण करते."},
            {"name": "🌿 चवळी", "notes": "दुष्काळ प्रतिरोधक व नायट्रोजन वाढवणारे पीक."},
            {"name": "🌾 मटकी", "notes": "कोरड्या भागात चांगले वाढते, मातीची सुपीकता वाढवते."},
        ]
    }
}[lang]

# ------------------------------------------
# Title Section
# ------------------------------------------
st.markdown(f"<h1 style='color: #2E7D32;'>{T['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size:18px;'>{T['subtitle']}</p>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------------------------
# Session Step Control
# ------------------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0

# ------------------------------------------
# Thresholds & Weights
# ------------------------------------------
thresholds = {
    "pH": (5.5, 6.5, 7.5),
    "EC": (0, 1, 4),
    "OC": (0.5, 0.75, 1.0),
    "N": (280, 560, 700),
    "P": (10, 25, 50),
    "K": (140, 280, 500),
    "S": (22.5, 45, 70),
    "Zn": (0.6, 1.5, 3),
    "B": (0.5, 1.0, 2),
    "Fe": (2.5, 4.5, 8),
    "Mn": (1.0, 2.0, 5),
    "Cu": (0.1, 0.2, 0.5)
}
weights = {
    "pH": 0.1, "EC": 0.1, "OC": 0.1,
    "N": 0.15, "P": 0.15, "K": 0.15,
    "S": 0.05, "Zn": 0.05, "B": 0.05,
    "Fe": 0.025, "Mn": 0.025, "Cu": 0.025
}

# ------------------------------------------
# Normalization Function
# ------------------------------------------
def normalize(val, low, opt, high, reverse=False):
    try:
        val = float(val)
    except:
        return 0
    if reverse:
        if val <= opt:
            return 1
        elif val >= high:
            return 0
        else:
            return 1 - (val - opt) / (high - opt)
    else:
        if val <= low:
            return 0
        elif val >= opt:
            return 1
        else:
            return (val - low) / (opt - low)

# ------------------------------------------
# Input Section
# ------------------------------------------
st.subheader(T["choose_input"])
input_mode = st.radio("Select how you want to provide soil data:", [T["upload"], T["manual"]], horizontal=True)

df = None
if input_mode == T["upload"]:
    uploaded_file = st.file_uploader("Upload your soil data file (CSV required)", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
elif input_mode == T["manual"]:
    st.markdown(f"### {T['enter_soil']}")
    manual_data = {}
    cols = st.columns(4)
    for i, param in enumerate(thresholds.keys()):
        with cols[i % 4]:
            manual_data[param] = st.number_input(f"{param}", value=0.0, step=0.01)
    df = pd.DataFrame([manual_data])

# ------------------------------------------
# Processing & Tabs
# ------------------------------------------
if df is not None:
    if not all(col in df.columns for col in thresholds.keys()):
        st.error(f"❌ Missing required columns: {', '.join(thresholds.keys())}")
    else:
        norm_df = pd.DataFrame()
        for param in thresholds:
            low, opt, high = thresholds[param]
            reverse = param in ["EC", "pH"]
            norm_df[param + "_F"] = df[param].apply(lambda x: normalize(x, low, opt, high, reverse))

        df["SFI"] = sum(norm_df[param + "_F"] * weights[param] for param in thresholds.keys())
        soil_data = df.iloc[0]
        SFI = soil_data["SFI"]

        st.markdown("### 📊 Data Preview (with Computed SFI)")
        st.dataframe(df.head(), use_container_width=True)

        tabs = st.tabs(T["tabs"])

        # TAB 1 - Soil Health Card
        with tabs[0]:
            if st.button(T["check_health"], use_container_width=True):
                st.session_state.step = 1
            if st.session_state.step >= 1:
                st.markdown(f"## {T['health_report']}")
                st.dataframe(pd.DataFrame([soil_data]), use_container_width=True)
                st.markdown(f"<h3>🌍 SFI: <b>{SFI:.2f}</b></h3>", unsafe_allow_html=True)
                st.info("➡ Go to next tab")

        # TAB 2 - Fertility Check
        with tabs[1]:
            if st.session_state.step >= 1:
                if st.button(T["check_fertility"], use_container_width=True):
                    st.session_state.step = 2
            if st.session_state.step >= 2:
                if SFI < 0.2:
                    st.error(T["non_fertile"])
                    if st.button(T["recommend_fertilizer"], use_container_width=True):
                        st.session_state.step = 3
                else:
                    st.success(T["fertile"])
                    if st.button(T["recommend_crop"], use_container_width=True):
                        st.session_state.step = 3
                st.info("➡ Go to Recommendations tab")

        # TAB 3 - Recommendations
        with tabs[2]:
            if st.session_state.step == 3:
                if SFI < 0.2:
                    st.markdown(f"### {T['fertilizer_header']}")
                    st.markdown(T["fertilizer_text"])
                else:
                    st.markdown(f"### {T['crop_header']}")
                    for crop in T["crops"]:
                        with st.expander(crop["name"], expanded=False):
                            st.write(f"🪴 {crop['notes']}")

    st.markdown("---")
else:
    st.warning(T["warning"])

# ------------------------------------------
# LOGOUT BUTTON (Bottom Center)
# ------------------------------------------
st.markdown("<div class='logout-container'>", unsafe_allow_html=True)
logout_col = st.columns([1, 1, 1])[1]
with logout_col:
    if st.button("🚪 Logout", key="logout", use_container_width=True):
        st.session_state.clear()
        st.success("👋 Logged out successfully!")
        st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align:center; font-size:14px; color:gray;'>{T['footer']}</p>", unsafe_allow_html=True)
