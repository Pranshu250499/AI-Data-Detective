import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================


st.markdown("""
<style>

/* FRONT DASHBOARD ANIMATIONS */

@keyframes dashboardFadeIn {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes ambientPulse {
    0%, 100% {
        opacity: .35;
        transform: scale(1);
    }
    50% {
        opacity: .65;
        transform: scale(1.08);
    }
}

@keyframes neonFloat {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-8px);
    }
}

@keyframes gridMove {
    from {
        background-position: 0 0;
    }
    to {
        background-position: 80px 80px;
    }
}

@keyframes glowPulse {
    0%, 100% {
        box-shadow: 0 0 8px rgba(34,211,238,.08);
    }
    50% {
        box-shadow: 0 0 24px rgba(34,211,238,.20);
    }
}

/* Main dashboard entrance */

[data-testid="stAppViewContainer"] {
    animation: dashboardFadeIn .8s ease-out;
}

/* Animated futuristic background */

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;

    background-image:
        linear-gradient(rgba(34,211,238,.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(34,211,238,.035) 1px, transparent 1px);

    background-size: 55px 55px;
    animation: gridMove 18s linear infinite;
}

/* Ambient glow */

[data-testid="stAppViewContainer"]::after {
    content: "";
    position: fixed;
    width: 420px;
    height: 420px;
    left: 50%;
    top: 25%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;

    background: radial-gradient(
        circle,
        rgba(34,211,238,.12),
        rgba(59,130,246,.05) 40%,
        transparent 72%
    );

    filter: blur(25px);
    animation: ambientPulse 5s ease-in-out infinite;
}

/* Dashboard content */

.block-container {
    position: relative;
    z-index: 1;
}

/* Headings */

h1, h2, h3 {
    animation: dashboardFadeIn .8s ease-out;
}

/* Streamlit metric cards */

[data-testid="stMetric"] {
    animation:
        dashboardFadeIn .7s ease-out,
        glowPulse 4s ease-in-out infinite;

    transition:
        transform .3s ease,
        border-color .3s ease,
        box-shadow .3s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-7px) scale(1.015);
    border-color: rgba(34,211,238,.55);
    box-shadow: 0 0 28px rgba(34,211,238,.16);
}

/* Buttons */

.stButton > button {
    transition:
        transform .25s ease,
        box-shadow .25s ease,
        border-color .25s ease;

    position: relative;
    overflow: hidden;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow:
        0 0 18px rgba(34,211,238,.20),
        0 8px 24px rgba(0,0,0,.20);
    border-color: rgba(34,211,238,.55);
}

.stButton > button:active {
    transform: scale(.97);
}

/* Button light sweep */

.stButton > button::before {
    content: "";
    position: absolute;
    top: 0;
    left: -120%;
    width: 70%;
    height: 100%;

    background: linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,.12),
        transparent
    );

    transform: skewX(-20deg);
    transition: left .55s ease;
}

.stButton > button:hover::before {
    left: 140%;
}

/* Containers / cards */

[data-testid="stVerticalBlockBorderWrapper"] {
    transition:
        transform .3s ease,
        box-shadow .3s ease,
        border-color .3s ease;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 25px rgba(34,211,238,.10);
    border-color: rgba(34,211,238,.35);
}

/* Images */

img {
    transition:
        transform .4s ease,
        filter .4s ease;
}

img:hover {
    transform: scale(1.025);
    filter: drop-shadow(0 0 16px rgba(34,211,238,.18));
}

/* Sidebar */

[data-testid="stSidebar"] {
    animation: dashboardFadeIn .6s ease-out;
}

/* Tabs */

button[data-baseweb="tab"] {
    transition:
        color .25s ease,
        transform .25s ease;
}

button[data-baseweb="tab"]:hover {
    transform: translateY(-2px);
}

/* Floating effect for common emoji/icon elements */

.dashboard-icon,
.hero-icon,
.feature-icon {
    animation: neonFloat 3s ease-in-out infinite;
}

</style>
""", unsafe_allow_html=True)


# AI LIVE ANALYSIS VISUAL
st.markdown("""
<style>

.ai-live-visual {
    position: relative;
    height: 210px;
    margin: 20px 0 30px 0;
    border-radius: 22px;
    overflow: hidden;
    border: 1px solid rgba(34,211,238,.30);
    background:
        radial-gradient(circle at 50% 50%,
        rgba(34,211,238,.13),
        rgba(15,23,42,.92) 45%,
        rgba(3,10,22,.98));
    display: flex;
    align-items: center;
    justify-content: center;
}

.ai-orb {
    position: relative;
    width: 82px;
    height: 82px;
    border-radius: 50%;
    background: radial-gradient(
        circle at 35% 30%,
        #ffffff,
        #67e8f9 18%,
        #06b6d4 42%,
        #2563eb 70%,
        transparent 72%
    );
    box-shadow:
        0 0 25px rgba(34,211,238,.65),
        0 0 70px rgba(37,99,235,.35);
    animation: aiOrbFloat 3s ease-in-out infinite;
    z-index: 3;
}

.ai-ring {
    position: absolute;
    width: 130px;
    height: 130px;
    border-radius: 50%;
    border: 1px solid rgba(34,211,238,.55);
    animation: aiRing 3s linear infinite;
}

.ai-ring.two {
    width: 175px;
    height: 175px;
    border-color: rgba(59,130,246,.30);
    animation-duration: 5s;
    animation-direction: reverse;
}

.ai-ring.three {
    width: 220px;
    height: 220px;
    border-color: rgba(34,211,238,.15);
    animation-duration: 7s;
}

.ai-scan {
    position: absolute;
    width: 100%;
    height: 2px;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(34,211,238,.8),
        transparent
    );
    animation: aiScan 2.5s ease-in-out infinite;
}

.ai-live-text {
    position: absolute;
    bottom: 22px;
    left: 0;
    right: 0;
    text-align: center;
    color: #67e8f9;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .14em;
    animation: textPulse 2s ease-in-out infinite;
}

.ai-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    margin-right: 7px;
    border-radius: 50%;
    background: #22d3ee;
    box-shadow: 0 0 12px rgba(34,211,238,.9);
    animation: dotPulse 1.2s infinite;
}

@keyframes aiOrbFloat {
    0%, 100% {
        transform: translateY(0) scale(1);
    }
    50% {
        transform: translateY(-9px) scale(1.05);
    }
}

@keyframes aiRing {
    from {
        transform: rotate(0deg) scale(.92);
        opacity: .45;
    }
    50% {
        opacity: 1;
    }
    to {
        transform: rotate(360deg) scale(1.08);
        opacity: .45;
    }
}

@keyframes aiScan {
    0% {
        top: 15%;
        opacity: 0;
    }
    20% {
        opacity: 1;
    }
    80% {
        opacity: 1;
    }
    100% {
        top: 85%;
        opacity: 0;
    }
}

@keyframes textPulse {
    0%, 100% {
        opacity: .55;
    }
    50% {
        opacity: 1;
        text-shadow: 0 0 12px rgba(34,211,238,.7);
    }
}

@keyframes dotPulse {
    0%, 100% {
        transform: scale(.8);
        opacity: .5;
    }
    50% {
        transform: scale(1.3);
        opacity: 1;
    }
}

</style>

<div class="ai-live-visual">
    <div class="ai-ring"></div>
    <div class="ai-ring two"></div>
    <div class="ai-ring three"></div>

    <div class="ai-orb"></div>

    <div class="ai-scan"></div>

    <div class="ai-live-text">
        <span class="ai-dot"></span>
        AI DATA ANALYSIS ACTIVE
    </div>
</div>
""", unsafe_allow_html=True)




st.title("🔎 AI Data Detective")


# =========================================================
# CUSTOM STYLING
# =========================================================

st.html("""
<style>

body {
    font-family: Arial, sans-serif;
}

.hero {
    padding: 42px;
    border-radius: 24px;
    background:
        radial-gradient(
            circle at 85% 15%,
            rgba(59, 130, 246, 0.20),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #111d38,
            #0b1224
        );
    border: 1px solid rgba(96, 165, 250, 0.25);
    box-shadow: 0 20px 60px rgba(0,0,0,0.25);
    margin-bottom: 35px;
}

.hero-badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 50px;
    background: rgba(59,130,246,0.12);
    border: 1px solid rgba(96,165,250,0.25);
    color: #93c5fd;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 0.8px;
    margin-bottom: 18px;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    line-height: 1.1;
    color: #f8fafc;
    margin-bottom: 18px;
}

.hero-title span {
    color: #60a5fa;
}

.hero-description {
    max-width: 760px;
    color: #a7b4c8;
    font-size: 16px;
    line-height: 1.7;
}

.workflow {
    margin-top: 25px;
    color: #94a3b8;
    font-size: 13px;
    font-weight: 600;
}

.section-title {
    color: #f8fafc;
    font-size: 28px;
    font-weight: 800;
    margin-top: 35px;
}

.section-description {
    color: #8190a6;
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 20px;
}

.card {
    min-height: 170px;
    padding: 24px;
    border-radius: 18px;
    background:
        linear-gradient(
            145deg,
            #18243b,
            #0e1729
        );
    border: 1px solid rgba(148,163,184,0.13);
    box-shadow: 0 12px 30px rgba(0,0,0,0.16);
}

.card-icon {
    font-size: 28px;
    margin-bottom: 15px;
}

.card-title {
    color: #f8fafc;
    font-size: 18px;
    font-weight: 750;
    margin-bottom: 8px;
}

.card-text {
    color: #8d9bb0;
    font-size: 13px;
    line-height: 1.6;
}

.step {
    min-height: 120px;
    padding: 20px;
    border-radius: 16px;
    background: rgba(15,23,42,0.75);
    border: 1px solid rgba(148,163,184,0.11);
}

.step-number {
    color: #60a5fa;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.step-title {
    color: #e2e8f0;
    font-size: 15px;
    font-weight: 700;
}

.step-text {
    color: #718096;
    font-size: 12px;
    margin-top: 7px;
}

</style>
""")


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">
    <div class="hero-badge">
        🔎 AI-POWERED DATA INVESTIGATION
    </div>
    <div class="hero-title">
        Turn raw data into
        <span>intelligent decisions.</span>
    </div>
    <div class="hero-description">
        AI Data Detective helps you explore, clean, analyze,
        visualize and understand your datasets from one
        intelligent workspace.
    </div>
    <div class="workflow">
        📁 UPLOAD &nbsp; → &nbsp;
        🔍 INVESTIGATE &nbsp; → &nbsp;
        📊 DISCOVER &nbsp; → &nbsp;
        🧠 PREDICT
    </div>
</div>
""")


# =========================================================
# FEATURES
# =========================================================

st.html("""
<div class="section-title">
    What can you investigate?
</div>

<div class="section-description">
    Everything you need to turn a dataset into useful evidence.
</div>
""")


col1, col2, col3 = st.columns(3)


with col1:
    st.html("""
    <div class="card">
        <div class="card-icon">📤</div>
        <div class="card-title">Upload Data</div>
        <div class="card-text">
            Import CSV or Excel datasets and
            begin your investigation instantly.
        </div>
    </div>
    """)


with col2:
    st.html("""
    <div class="card">
        <div class="card-icon">🔍</div>
        <div class="card-title">Analyze Data</div>
        <div class="card-text">
            Detect missing values, duplicates,
            statistics and important data patterns.
        </div>
    </div>
    """)


with col3:
    st.html("""
    <div class="card">
        <div class="card-icon">📈</div>
        <div class="card-title">Visualize Data</div>
        <div class="card-text">
            Transform complex datasets into clear,
            interactive charts and visual evidence.
        </div>
    </div>
    """)


col4, col5, col6 = st.columns(3)


with col4:
    st.html("""
    <div class="card">
        <div class="card-icon">🤖</div>
        <div class="card-title">AI Insights</div>
        <div class="card-text">
            Discover meaningful patterns and
            generate intelligent observations.
        </div>
    </div>
    """)


with col5:
    st.html("""
    <div class="card">
        <div class="card-icon">🧠</div>
        <div class="card-title">Machine Learning</div>
        <div class="card-text">
            Build predictive models and uncover
            relationships hidden inside your data.
        </div>
    </div>
    """)


with col6:
    st.html("""
    <div class="card">
        <div class="card-icon">📄</div>
        <div class="card-title">Investigation Report</div>
        <div class="card-text">
            Compile your findings into a clean,
            downloadable data investigation report.
        </div>
    </div>
    """)


# =========================================================
# WORKFLOW
# =========================================================

st.html("""
<div class="section-title">
    Investigation workflow
</div>

<div class="section-description">
    Follow your investigation from raw data to final findings.
</div>
""")


w1, w2, w3 = st.columns(3)


with w1:
    st.html("""
    <div class="step">
        <div class="step-number">01 / INGEST</div>
        <div class="step-title">📁 Upload your dataset</div>
        <div class="step-text">
            Start with CSV or Excel data.
        </div>
    </div>
    """)


with w2:
    st.html("""
    <div class="step">
        <div class="step-number">02 / INSPECT</div>
        <div class="step-title">🔍 Examine the evidence</div>
        <div class="step-text">
            Explore structure, quality and statistics.
        </div>
    </div>
    """)


with w3:
    st.html("""
    <div class="step">
        <div class="step-number">03 / VISUALIZE</div>
        <div class="step-title">📊 Find patterns</div>
        <div class="step-text">
            Transform data into visual evidence.
        </div>
    </div>
    """)


w4, w5, w6 = st.columns(3)


with w4:
    st.html("""
    <div class="step">
        <div class="step-number">04 / DISCOVER</div>
        <div class="step-title">🤖 Generate AI insights</div>
        <div class="step-text">
            Identify meaningful findings.
        </div>
    </div>
    """)


with w5:
    st.html("""
    <div class="step">
        <div class="step-number">05 / PREDICT</div>
        <div class="step-title">🧠 Run machine learning</div>
        <div class="step-text">
            Explore predictive possibilities.
        </div>
    </div>
    """)


with w6:
    st.html("""
    <div class="step">
        <div class="step-number">06 / REPORT</div>
        <div class="step-title">📄 Export your findings</div>
        <div class="step-text">
            Create your final investigation report.
        </div>
    </div>
    """)


# =========================================================
# FINAL MESSAGE
# =========================================================

st.success(
    "🕵️ Ready to investigate? Upload your dataset and start discovering what your data is hiding."
)