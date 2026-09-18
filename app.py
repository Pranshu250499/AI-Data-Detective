import streamlit as st

from utils.auth import (
    sign_in,
    sign_up,
    save_session,
    is_logged_in,
    sign_out,
    admin_sign_in,
    is_admin
)

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Data Detective",
    page_icon=chr(0x1F50E),
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# ðŸŽ¨ SIDEBAR ANIMATIONS
# =========================

st.markdown("""
<style>

/* ===== SIDEBAR ===== */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #20212a 0%,
        #242631 50%,
        #1d1e26 100%
    );

    border-right: 1px solid rgba(120, 140, 255, 0.15);
    animation: sidebarEnter 0.8s ease-out;
}


/* Sidebar entrance */

@keyframes sidebarEnter {
    from {
        opacity: 0;
        transform: translateX(-35px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}


/* ===== SIDEBAR CONTENT ===== */

[data-testid="stSidebar"] > div:first-child {
    padding-top: 25px;
}


/* ===== MENU ITEMS ===== */

[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    border: none !important;
    border-radius: 10px !important;

    background: transparent !important;

    color: #d9dcff !important;

    text-align: left !important;

    transition:
        transform 0.25s ease,
        background 0.25s ease,
        box-shadow 0.25s ease,
        color 0.25s ease;

    position: relative;
    overflow: hidden;
}


/* Hover animation */

[data-testid="stSidebar"] .stButton > button:hover {

    transform: translateX(7px);

    background:
        linear-gradient(
            90deg,
            rgba(70, 120, 255, 0.22),
            rgba(120, 70, 255, 0.12)
        ) !important;

    color: #ffffff !important;

    box-shadow:
        0 0 15px rgba(80, 120, 255, 0.18);

}


/* ===== GLOW EFFECT ===== */

[data-testid="stSidebar"] .stButton > button::before {

    content: "";

    position: absolute;

    left: 0;
    top: 50%;

    width: 3px;
    height: 0;

    background: linear-gradient(
        180deg,
        #00c6ff,
        #7b61ff
    );

    border-radius: 10px;

    transform: translateY(-50%);

    transition:
        height 0.3s ease,
        box-shadow 0.3s ease;
}


/* Hover indicator */

[data-testid="stSidebar"] .stButton > button:hover::before {

    height: 70%;

    box-shadow:
        0 0 10px #4d8cff,
        0 0 20px rgba(90, 110, 255, 0.7);

}


/* ===== ICON ANIMATION ===== */

[data-testid="stSidebar"] .stButton > button:hover span {

    transition: transform 0.25s ease;

}


/* ===== SIDEBAR HEADINGS ===== */

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {

    color: #ffffff;

    transition:
        text-shadow 0.3s ease,
        transform 0.3s ease;

}


[data-testid="stSidebar"] h1:hover,
[data-testid="stSidebar"] h2:hover,
[data-testid="stSidebar"] h3:hover {

    transform: translateX(4px);

    text-shadow:
        0 0 8px rgba(80, 150, 255, 0.7),
        0 0 18px rgba(100, 80, 255, 0.4);

}


/* ===== LOGOUT BUTTON ===== */

[data-testid="stSidebar"] button {

    transition:
        all 0.25s ease !important;

}

[data-testid="stSidebar"] button:hover {

    border-color: rgba(90, 150, 255, 0.7) !important;

}


/* ===== SCROLLBAR ===== */

[data-testid="stSidebar"] ::-webkit-scrollbar {

    width: 5px;

}

[data-testid="stSidebar"] ::-webkit-scrollbar-track {

    background: transparent;

}

[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {

    background: linear-gradient(
        180deg,
        #318cff,
        #795cff
    );

    border-radius: 10px;

}


/* ===== SUBTLE GLOW ===== */

[data-testid="stSidebar"]::after {

    content: "";

    position: absolute;

    top: 20%;
    right: -2px;

    width: 2px;
    height: 60%;

    background: linear-gradient(
        transparent,
        #408cff,
        #8a5cff,
        transparent
    );

    opacity: 0.5;

    animation: glowLine 3s ease-in-out infinite;

}


@keyframes glowLine {

    0%, 100% {
        opacity: 0.25;
    }

    50% {
        opacity: 0.9;
    }

}


/* ===== MOBILE / SMALL SCREEN ===== */

@media (max-width: 768px) {

    [data-testid="stSidebar"] .stButton > button:hover {

        transform: translateX(4px);

    }

}

/* =========================================================
   ðŸš€ ULTRA PREMIUM SIDEBAR ANIMATIONS
   ========================================================= */


/* ---------------------------------------------------------
   SIDEBAR MOVING ENERGY
   --------------------------------------------------------- */

[data-testid="stSidebar"] {
    position: relative !important;
    overflow: hidden !important;

    background:
        linear-gradient(
            180deg,
            #080b16 0%,
            #101525 45%,
            #080b16 100%
        ) !important;

    box-shadow:
        inset -1px 0 0 rgba(56, 189, 248, 0.15),
        10px 0 40px rgba(0, 0, 0, 0.20);
}


/* Moving vertical light */
[data-testid="stSidebar"]::before {

    content: "";

    position: absolute;

    width: 2px;
    height: 180px;

    right: 0;
    top: -180px;

    background:
        linear-gradient(
            180deg,
            transparent,
            #22d3ee,
            #60a5fa,
            transparent
        );

    box-shadow:
        0 0 10px #22d3ee,
        0 0 25px rgba(34, 211, 238, 0.6);

    animation:
        sidebarScanner 5s linear infinite;

    z-index: 10;

    pointer-events: none;
}

@keyframes sidebarScanner {

    0% {
        top: -180px;
        opacity: 0;
    }

    10% {
        opacity: 1;
    }

    50% {
        opacity: 1;
    }

    90% {
        opacity: 1;
    }

    100% {
        top: 100%;
        opacity: 0;
    }
}


/* ---------------------------------------------------------
   SIDEBAR AMBIENT LIGHT
   --------------------------------------------------------- */

[data-testid="stSidebar"]::after {

    content: "";

    position: absolute;

    width: 300px;
    height: 300px;

    left: -180px;
    top: 25%;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(37, 99, 235, 0.15),
            rgba(6, 182, 212, 0.05),
            transparent 70%
        );

    filter: blur(25px);

    animation:
        sidebarOrb 8s ease-in-out infinite;

    pointer-events: none;

    z-index: 0;
}

@keyframes sidebarOrb {

    0%,
    100% {
        transform:
            translate(0, 0)
            scale(1);
    }

    50% {
        transform:
            translate(120px, 80px)
            scale(1.3);
    }
}


/* ---------------------------------------------------------
   BRAND AREA
   --------------------------------------------------------- */

.sidebar-brand {

    position: relative;

    transition:
        transform 0.3s ease;
}

.sidebar-brand:hover {

    transform:
        translateX(4px);
}


/* Brand icon futuristic glow */

.brand-icon {

    position: relative;

    box-shadow:
        0 0 15px rgba(37, 99, 235, 0.35),
        0 0 35px rgba(6, 182, 212, 0.10);

    animation:
        brandFloat 3s ease-in-out infinite,
        brandEnergy 2.5s ease-in-out infinite alternate;

    transition:
        transform 0.3s ease;
}

.brand-icon:hover {

    transform:
        scale(1.12)
        rotate(-6deg);

    box-shadow:
        0 0 25px rgba(37, 99, 235, 0.55),
        0 0 55px rgba(6, 182, 212, 0.25);
}

@keyframes brandFloat {

    0%,
    100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-5px);
    }
}

@keyframes brandEnergy {

    from {
        box-shadow:
            0 0 12px rgba(37, 99, 235, 0.25);
    }

    to {
        box-shadow:
            0 0 25px rgba(37, 99, 235, 0.55),
            0 0 45px rgba(6, 182, 212, 0.18);
    }
}


/* ---------------------------------------------------------
   BRAND TITLE SHIMMER
   --------------------------------------------------------- */

.brand-title {

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #67e8f9,
            #ffffff
        );

    background-size: 200% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation:
        brandTextShimmer 4s linear infinite;
}

@keyframes brandTextShimmer {

    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 200% center;
    }
}


/* ---------------------------------------------------------
   COMMAND CENTER LABEL
   --------------------------------------------------------- */

[data-testid="stSidebarNav"]::before {

    animation:
        commandPulse 3s ease-in-out infinite;

    text-shadow:
        0 0 10px rgba(34, 211, 238, 0.15);
}

@keyframes commandPulse {

    0%,
    100% {
        opacity: 0.45;
    }

    50% {
        opacity: 0.9;
    }
}


/* ---------------------------------------------------------
   NAVIGATION ITEMS
   --------------------------------------------------------- */

[data-testid="stSidebarNav"] a {

    position: relative !important;

    overflow: hidden !important;

    transition:
        all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
}


/* Moving shine */

[data-testid="stSidebarNav"] a::after {

    content: "";

    position: absolute;

    top: 0;
    left: -120%;

    width: 70%;
    height: 100%;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255, 255, 255, 0.07),
            transparent
        );

    transform:
        skewX(-20deg);

    transition:
        left 0.55s ease;

    pointer-events: none;
}

[data-testid="stSidebarNav"] a:hover::after {

    left: 140%;
}


/* Nav hover */

[data-testid="stSidebarNav"] a:hover {

    transform:
        translateX(7px) !important;

    background:
        linear-gradient(
            90deg,
            rgba(37, 99, 235, 0.20),
            rgba(6, 182, 212, 0.08),
            transparent
        ) !important;

    border-color:
        rgba(56, 189, 248, 0.28) !important;

    box-shadow:
        0 0 18px rgba(37, 99, 235, 0.10),
        inset 3px 0 0 rgba(34, 211, 238, 0.7);
}


/* ---------------------------------------------------------
   ACTIVE PAGE
   --------------------------------------------------------- */

[data-testid="stSidebarNav"]
a[aria-current="page"] {

    position: relative !important;

    background:
        linear-gradient(
            90deg,
            rgba(37, 99, 235, 0.35),
            rgba(6, 182, 212, 0.15),
            transparent
        ) !important;

    border-color:
        rgba(34, 211, 238, 0.35) !important;

    box-shadow:
        0 0 25px rgba(37, 99, 235, 0.12),
        inset 3px 0 0 #22d3ee !important;

    animation:
        activeNavGlow 2.5s ease-in-out infinite !important;
}


/* Active glowing line */

[data-testid="stSidebarNav"]
a[aria-current="page"]::before {

    content: "";

    position: absolute;

    left: 0;
    top: 15%;

    width: 3px;
    height: 70%;

    border-radius: 10px;

    background:
        linear-gradient(
            180deg,
            #3b82f6,
            #22d3ee,
            #3b82f6
        );

    box-shadow:
        0 0 10px #22d3ee,
        0 0 25px rgba(34, 211, 238, 0.5);

    animation:
        activeLinePulse 1.5s ease-in-out infinite;
}

@keyframes activeNavGlow {

    0%,
    100% {
        box-shadow:
            0 0 15px rgba(37, 99, 235, 0.08),
            inset 3px 0 0 #22d3ee;
    }

    50% {
        box-shadow:
            0 0 30px rgba(37, 99, 235, 0.20),
            0 0 50px rgba(6, 182, 212, 0.06),
            inset 3px 0 0 #22d3ee;
    }
}

@keyframes activeLinePulse {

    0%,
    100% {
        opacity: 0.45;
        transform: scaleY(0.8);
    }

    50% {
        opacity: 1;
        transform: scaleY(1);
    }
}


/* ---------------------------------------------------------
   USER CARD
   --------------------------------------------------------- */

.user-card {

    position: relative;

    overflow: hidden;

    transition:
        all 0.3s ease;
}

.user-card::before {

    content: "";

    position: absolute;

    top: 0;
    left: -100%;

    width: 100%;
    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            #22d3ee,
            transparent
        );

    animation:
        userCardScan 4s linear infinite;
}

.user-card:hover {

    transform:
        translateY(-2px);

    border-color:
        rgba(34, 211, 238, 0.30);

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.20),
        0 0 20px rgba(34, 211, 238, 0.06);
}

@keyframes userCardScan {

    0% {
        left: -100%;
    }

    50% {
        left: 100%;
    }

    100% {
        left: 100%;
    }
}


/* ---------------------------------------------------------
   ONLINE STATUS
   --------------------------------------------------------- */

.status-dot {

    animation:
        statusPulse 1.5s ease-in-out infinite,
        statusScale 2s ease-in-out infinite;
}

@keyframes statusScale {

    0%,
    100% {
        transform: scale(0.8);
    }

    50% {
        transform: scale(1.25);
    }
}


/* ---------------------------------------------------------
   LOGOUT BUTTON
   --------------------------------------------------------- */

[data-testid="stSidebar"] .stButton > button {

    position: relative;

    overflow: hidden;

    transition:
        all 0.25s ease !important;
}

[data-testid="stSidebar"] .stButton > button:hover {

    transform:
        translateY(-2px);

    color: #ffffff !important;

    border-color:
        rgba(34, 211, 238, 0.35) !important;

    box-shadow:
        0 0 20px rgba(34, 211, 238, 0.12) !important;
}


/* ---------------------------------------------------------
   SIDEBAR FOOTER
   --------------------------------------------------------- */

.sidebar-footer {

    animation:
        footerPulse 4s ease-in-out infinite;
}

@keyframes footerPulse {

    0%,
    100% {
        opacity: 0.45;
    }

    50% {
        opacity: 0.85;
    }
}


/* ---------------------------------------------------------
   SIDEBAR FLOATING PARTICLES
   --------------------------------------------------------- */

[data-testid="stSidebar"] .user-card::after {

    content: "-  -     -   -       -";

    position: absolute;

    left: 15px;
    bottom: -5px;

    width: 100%;

    color: rgba(34, 211, 238, 0.18);

    font-size: 14px;
    letter-spacing: 8px;

    animation:
        sidebarParticles 6s linear infinite;

    pointer-events: none;
}

@keyframes sidebarParticles {

    0% {
        transform:
            translateY(15px);
        opacity: 0;
    }

    30% {
        opacity: 0.7;
    }

    100% {
        transform:
            translateY(-25px);
        opacity: 0;
    }
}


/* ---------------------------------------------------------
   SMOOTH SIDEBAR LOAD
   --------------------------------------------------------- */

[data-testid="stSidebarNav"] a {

    animation:
        sidebarNavAppear 0.5s ease both;
}

[data-testid="stSidebarNav"] a:nth-child(1) {
    animation-delay: 0.05s;
}

[data-testid="stSidebarNav"] a:nth-child(2) {
    animation-delay: 0.10s;
}

[data-testid="stSidebarNav"] a:nth-child(3) {
    animation-delay: 0.15s;
}

[data-testid="stSidebarNav"] a:nth-child(4) {
    animation-delay: 0.20s;
}

[data-testid="stSidebarNav"] a:nth-child(5) {
    animation-delay: 0.25s;
}

[data-testid="stSidebarNav"] a:nth-child(6) {
    animation-delay: 0.30s;
}

[data-testid="stSidebarNav"] a:nth-child(7) {
    animation-delay: 0.35s;
}

@keyframes sidebarNavAppear {

    from {
        opacity: 0;
        transform:
            translateX(-15px);
    }

    to {
        opacity: 1;
        transform:
            translateX(0);
    }
}

/* =========================================================
   SIDEBAR ANIMATION FIX
   Clean â€¢ Smooth â€¢ Premium HUD
   ========================================================= */


/* ---------------------------------------------------------
   REMOVE THE OVER-BRIGHT SIDEBAR SCANNER
   --------------------------------------------------------- */

[data-testid="stSidebar"]::before {

    content: "";

    position: absolute;

    right: 0;
    top: 0;

    width: 1px;
    height: 100%;

    background:
        linear-gradient(
            180deg,
            transparent 0%,
            rgba(34, 211, 238, 0.15) 20%,
            rgba(34, 211, 238, 0.45) 50%,
            rgba(59, 130, 246, 0.15) 80%,
            transparent 100%
        );

    filter: none;

    animation:
        sidebarEdgeGlow 4s ease-in-out infinite;

    pointer-events: none;

    z-index: 10;
}

@keyframes sidebarEdgeGlow {

    0%,
    100% {
        opacity: 0.35;
    }

    50% {
        opacity: 0.9;
    }
}


/* ---------------------------------------------------------
   KEEP AMBIENT SIDEBAR LIGHT SUBTLE
   --------------------------------------------------------- */

[data-testid="stSidebar"]::after {

    width: 280px;
    height: 280px;

    left: -190px;
    top: 35%;

    background:
        radial-gradient(
            circle,
            rgba(37, 99, 235, 0.10),
            rgba(6, 182, 212, 0.035),
            transparent 70%
        );

    filter: blur(35px);

    animation:
        sidebarAmbient 10s ease-in-out infinite;

    pointer-events: none;
}

@keyframes sidebarAmbient {

    0%,
    100% {
        transform:
            translate(0, 0)
            scale(1);
    }

    50% {
        transform:
            translate(100px, -40px)
            scale(1.15);
    }
}


/* ---------------------------------------------------------
   REMOVE UGLY USER-CARD SCANNING LINE
   --------------------------------------------------------- */

[data-testid="stSidebar"] .user-card::before {

    content: none !important;
}

[data-testid="stSidebar"] .user-card::after {

    content: none !important;
}


/* ---------------------------------------------------------
   USER CARD CLEAN GLOW
   --------------------------------------------------------- */

[data-testid="stSidebar"] .user-card {

    position: relative;

    transition:
        transform 0.3s ease,
        border-color 0.3s ease,
        box-shadow 0.3s ease;

    box-shadow:
        0 0 0 rgba(34, 211, 238, 0);
}

[data-testid="stSidebar"] .user-card:hover {

    transform:
        translateY(-2px);

    border-color:
        rgba(34, 211, 238, 0.28);

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.25),
        0 0 18px rgba(34, 211, 238, 0.07);
}


/* ---------------------------------------------------------
   BRAND ICON - SMOOTH PULSE
   --------------------------------------------------------- */

[data-testid="stSidebar"] .brand-icon {

    animation:
        sidebarLogoFloat 4s ease-in-out infinite,
        sidebarLogoGlow 3s ease-in-out infinite alternate;

    transform-origin:
        center center;
}

@keyframes sidebarLogoFloat {

    0%,
    100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-4px);
    }
}

@keyframes sidebarLogoGlow {

    from {
        box-shadow:
            0 0 12px rgba(37, 99, 235, 0.25);
    }

    to {
        box-shadow:
            0 0 25px rgba(37, 99, 235, 0.45),
            0 0 40px rgba(6, 182, 212, 0.10);
    }
}


/* ---------------------------------------------------------
   NAVIGATION - CLEAN HOVER
   --------------------------------------------------------- */

[data-testid="stSidebarNav"] a {

    transform:
        translateX(0) !important;

    transition:
        background 0.25s ease,
        border-color 0.25s ease,
        transform 0.25s ease,
        box-shadow 0.25s ease !important;
}


/* Remove excessive shine */
[data-testid="stSidebarNav"] a::after {

    opacity: 0;

    transition:
        left 0.5s ease,
        opacity 0.3s ease;
}

[data-testid="stSidebarNav"] a:hover::after {

    opacity: 1;
    left: 130%;
}


/* Smooth hover */

[data-testid="stSidebarNav"] a:hover {

    transform:
        translateX(4px) !important;

    background:
        linear-gradient(
            90deg,
            rgba(37, 99, 235, 0.14),
            rgba(6, 182, 212, 0.045),
            transparent
        ) !important;

    box-shadow:
        inset 2px 0 0 rgba(34, 211, 238, 0.45),
        0 4px 15px rgba(0, 0, 0, 0.15);
}


/* ---------------------------------------------------------
   ACTIVE NAV ITEM
   --------------------------------------------------------- */

[data-testid="stSidebarNav"]
a[aria-current="page"] {

    background:
        linear-gradient(
            90deg,
            rgba(37, 99, 235, 0.25),
            rgba(6, 182, 212, 0.09),
            transparent
        ) !important;

    border:
        1px solid rgba(56, 189, 248, 0.20) !important;

    box-shadow:
        inset 3px 0 0 #22d3ee,
        0 0 15px rgba(37, 99, 235, 0.08) !important;

    animation:
        activePagePulse 3s ease-in-out infinite !important;
}

@keyframes activePagePulse {

    0%,
    100% {
        box-shadow:
            inset 3px 0 0 #22d3ee,
            0 0 10px rgba(37, 99, 235, 0.05);
    }

    50% {
        box-shadow:
            inset 3px 0 0 #22d3ee,
            0 0 22px rgba(37, 99, 235, 0.14);
    }
}


/* ---------------------------------------------------------
   ACTIVE LEFT BAR
   --------------------------------------------------------- */

[data-testid="stSidebarNav"]
a[aria-current="page"]::before {

    content: "";

    position: absolute;

    left: 0;
    top: 20%;

    width: 3px;
    height: 60%;

    border-radius: 5px;

    background:
        linear-gradient(
            180deg,
            #3b82f6,
            #22d3ee,
            #3b82f6
        );

    box-shadow:
        0 0 8px rgba(34, 211, 238, 0.6);

    animation:
        activeBarPulse 2s ease-in-out infinite;
}

@keyframes activeBarPulse {

    0%,
    100% {
        opacity: 0.55;
    }

    50% {
        opacity: 1;
    }
}


/* ---------------------------------------------------------
   ONLINE STATUS
   --------------------------------------------------------- */

[data-testid="stSidebar"] .status-dot {

    animation:
        cleanStatusPulse 2s ease-in-out infinite;
}

@keyframes cleanStatusPulse {

    0%,
    100% {
        transform: scale(0.85);
        box-shadow:
            0 0 5px rgba(34, 197, 94, 0.4);
    }

    50% {
        transform: scale(1.15);
        box-shadow:
            0 0 12px rgba(34, 197, 94, 0.8);
    }
}


/* ---------------------------------------------------------
   LOGOUT BUTTON
   --------------------------------------------------------- */

[data-testid="stSidebar"] .stButton > button {

    transition:
        all 0.25s ease !important;
}

[data-testid="stSidebar"] .stButton > button:hover {

    transform:
        translateY(-1px) !important;

    box-shadow:
        0 0 15px rgba(34, 211, 238, 0.10) !important;
}


/* ---------------------------------------------------------
   FOOTER
   --------------------------------------------------------- */

[data-testid="stSidebar"] .sidebar-footer {

    animation:
        footerFade 5s ease-in-out infinite;
}

@keyframes footerFade {

    0%,
    100% {
        opacity: 0.45;
    }

    50% {
        opacity: 0.75;
    }
}

/* ===== SIDEBAR BRAND FIX ===== */

.sidebar-brand {
    background: transparent !important;
    box-shadow: none !important;
    border: none !important;
}

.brand-row {
    background: transparent !important;
    box-shadow: none !important;
    border: none !important;
}

.brand-icon {
    width: 44px !important;
    height: 44px !important;
    min-width: 44px !important;

    display: flex !important;
    align-items: center !important;
    justify-content: center !important;

    border-radius: 13px !important;

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #06b6d4
        ) !important;

    box-shadow:
        0 0 18px rgba(37, 99, 235, 0.35) !important;

    animation:
        cleanBrandFloat 4s ease-in-out infinite !important;
}

@keyframes cleanBrandFloat {

    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-3px);
    }
}

/* =========================================================
   SIDEBAR V2 â€” FUTURISTIC AI ANIMATION
   ========================================================= */


/* ---------- SIDEBAR EDGE ENERGY ---------- */

[data-testid="stSidebar"] {
    position: relative !important;
    overflow: hidden !important;
}

/* subtle animated edge */
[data-testid="stSidebar"] {
    box-shadow:
        inset -1px 0 rgba(56, 189, 248, 0.18),
        8px 0 35px rgba(0, 0, 0, 0.18);
}


/* ---------- BRAND LOGO ---------- */

[data-testid="stSidebar"] .brand-icon {
    position: relative !important;

    animation:
        sidebarLogoFloat 4s ease-in-out infinite,
        sidebarLogoGlow 3s ease-in-out infinite alternate !important;

    transition:
        transform 0.35s ease !important;
}

[data-testid="stSidebar"] .brand-icon:hover {
    transform:
        scale(1.12)
        rotate(-5deg) !important;
}

@keyframes sidebarLogoFloat {

    0%,
    100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-5px);
    }
}

@keyframes sidebarLogoGlow {

    0% {
        box-shadow:
            0 0 10px rgba(37, 99, 235, 0.25);
    }

    100% {
        box-shadow:
            0 0 22px rgba(37, 99, 235, 0.55),
            0 0 38px rgba(6, 182, 212, 0.18);
    }
}


/* ---------- BRAND TEXT SHIMMER ---------- */

[data-testid="stSidebar"] .brand-title {

    background:
        linear-gradient(
            90deg,
            #f8fafc,
            #67e8f9,
            #f8fafc
        );

    background-size: 200% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation:
        brandShimmer 4s linear infinite;
}

@keyframes brandShimmer {

    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 200% center;
    }
}


/* =========================================================
   NAVIGATION ITEMS
   ========================================================= */

[data-testid="stSidebarNav"] a {

    position: relative !important;
    overflow: hidden !important;

    transition:
        transform 0.25s ease,
        background 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease !important;

    animation:
        navEntry 0.55s ease both;
}


/* staggered entrance */

[data-testid="stSidebarNav"] a:nth-child(1) {
    animation-delay: 0.05s;
}

[data-testid="stSidebarNav"] a:nth-child(2) {
    animation-delay: 0.10s;
}

[data-testid="stSidebarNav"] a:nth-child(3) {
    animation-delay: 0.15s;
}

[data-testid="stSidebarNav"] a:nth-child(4) {
    animation-delay: 0.20s;
}

[data-testid="stSidebarNav"] a:nth-child(5) {
    animation-delay: 0.25s;
}

[data-testid="stSidebarNav"] a:nth-child(6) {
    animation-delay: 0.30s;
}

[data-testid="stSidebarNav"] a:nth-child(7) {
    animation-delay: 0.35s;
}

@keyframes navEntry {

    from {
        opacity: 0;
        transform: translateX(-18px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}


/* ---------- MOVING HOVER LIGHT ---------- */

[data-testid="stSidebarNav"] a::after {

    content: "";

    position: absolute;

    top: 0;
    left: -120%;

    width: 80%;
    height: 100%;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(103, 232, 249, 0.10),
            rgba(255, 255, 255, 0.08),
            transparent
        );

    transform:
        skewX(-20deg);

    pointer-events: none;

    transition:
        left 0.55s ease;
}

[data-testid="stSidebarNav"] a:hover::after {
    left: 140%;
}


/* ---------- HOVER STATE ---------- */

[data-testid="stSidebarNav"] a:hover {

    transform:
        translateX(6px) !important;

    background:
        linear-gradient(
            90deg,
            rgba(37, 99, 235, 0.16),
            rgba(6, 182, 212, 0.06),
            transparent
        ) !important;

    border-color:
        rgba(56, 189, 248, 0.25) !important;

    box-shadow:
        inset 3px 0 rgba(34, 211, 238, 0.55),
        0 5px 20px rgba(37, 99, 235, 0.08) !important;
}


/* =========================================================
   ACTIVE PAGE
   ========================================================= */

[data-testid="stSidebarNav"]
a[aria-current="page"] {

    background:
        linear-gradient(
            90deg,
            rgba(37, 99, 235, 0.28),
            rgba(6, 182, 212, 0.10),
            transparent
        ) !important;

    border:
        1px solid rgba(56, 189, 248, 0.25) !important;

    box-shadow:
        inset 3px 0 #22d3ee,
        0 0 18px rgba(37, 99, 235, 0.10) !important;

    animation:
        activeNavGlow 3s ease-in-out infinite !important;
}


/* glowing active line */

[data-testid="stSidebarNav"]
a[aria-current="page"]::before {

    content: "";

    position: absolute;

    left: 0;
    top: 18%;

    width: 3px;
    height: 64%;

    border-radius: 5px;

    background:
        linear-gradient(
            180deg,
            #3b82f6,
            #22d3ee,
            #3b82f6
        );

    box-shadow:
        0 0 8px #22d3ee,
        0 0 18px rgba(34, 211, 238, 0.45);

    animation:
        activeLine 2s ease-in-out infinite;
}

@keyframes activeNavGlow {

    0%,
    100% {
        box-shadow:
            inset 3px 0 #22d3ee,
            0 0 10px rgba(37, 99, 235, 0.05);
    }

    50% {
        box-shadow:
            inset 3px 0 #22d3ee,
            0 0 25px rgba(37, 99, 235, 0.18),
            0 0 40px rgba(6, 182, 212, 0.05);
    }
}

@keyframes activeLine {

    0%,
    100% {
        opacity: 0.45;
        transform: scaleY(0.75);
    }

    50% {
        opacity: 1;
        transform: scaleY(1);
    }
}


/* =========================================================
   USER CARD
   ========================================================= */

[data-testid="stSidebar"] .user-card {

    transition:
        transform 0.3s ease,
        border-color 0.3s ease,
        box-shadow 0.3s ease !important;
}

[data-testid="stSidebar"] .user-card:hover {

    transform:
        translateY(-3px) !important;

    border-color:
        rgba(34, 211, 238, 0.28) !important;

    box-shadow:
        0 8px 28px rgba(0, 0, 0, 0.25),
        0 0 20px rgba(34, 211, 238, 0.07) !important;
}


/* =========================================================
   ONLINE STATUS
   ========================================================= */

[data-testid="stSidebar"] .status-dot {

    animation:
        onlinePulse 1.8s ease-in-out infinite !important;
}

@keyframes onlinePulse {

    0%,
    100% {
        transform: scale(0.8);

        box-shadow:
            0 0 5px rgba(34, 197, 94, 0.35);
    }

    50% {
        transform: scale(1.2);

        box-shadow:
            0 0 12px rgba(34, 197, 94, 0.85),
            0 0 20px rgba(34, 197, 94, 0.20);
    }
}


/* =========================================================
   LOGOUT
   ========================================================= */

[data-testid="stSidebar"] .stButton > button {

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease !important;
}

[data-testid="stSidebar"] .stButton > button:hover {

    transform:
        translateY(-2px) !important;

    box-shadow:
        0 0 18px rgba(34, 211, 238, 0.12) !important;
}


/* =========================================================
   FOOTER
   ========================================================= */

[data-testid="stSidebar"] .sidebar-footer {

    animation:
        footerGlow 4s ease-in-out infinite;
}

@keyframes footerGlow {

    0%,
    100% {
        opacity: 0.45;
    }

    50% {
        opacity: 0.85;
    }
}

/* =========================================================
   ðŸš€ SIDEBAR â€” JARVIS / AI HUD ANIMATION
   ========================================================= */

/* ---------- MAIN SIDEBAR ENERGY ---------- */

[data-testid="stSidebar"] {
    position: relative !important;
    overflow: hidden !important;

    background:
        radial-gradient(
            circle at 20% 15%,
            rgba(37, 99, 235, 0.16),
            transparent 28%
        ),
        radial-gradient(
            circle at 80% 70%,
            rgba(6, 182, 212, 0.10),
            transparent 30%
        ),
        linear-gradient(
            180deg,
            #070b17 0%,
            #0b1120 50%,
            #060a14 100%
        ) !important;

    background-size:
        100% 100%,
        100% 100%,
        100% 100%;

    box-shadow:
        inset -1px 0 rgba(34, 211, 238, 0.25),
        8px 0 40px rgba(0, 0, 0, 0.25) !important;
}


/* =========================================================
   ðŸŒŒ MOVING AI GRID
   ========================================================= */

[data-testid="stSidebar"]::after {

    content: "";

    position: absolute;

    inset: 0;

    pointer-events: none;

    z-index: 0;

    opacity: 0.22;

    background-image:
        linear-gradient(
            rgba(34, 211, 238, 0.08) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(34, 211, 238, 0.08) 1px,
            transparent 1px
        );

    background-size:
        35px 35px;

    animation:
        aiGridMove 12s linear infinite;
}

@keyframes aiGridMove {

    0% {
        background-position:
            0 0,
            0 0;
    }

    100% {
        background-position:
            0 35px,
            35px 0;
    }
}


/* =========================================================
   âš¡ MOVING NEON SCANNER
   ========================================================= */

[data-testid="stSidebar"]::before {

    content: "";

    position: absolute;

    left: -20%;

    top: -20%;

    width: 140%;

    height: 2px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(37, 99, 235, 0.05),
            #22d3ee,
            #60a5fa,
            rgba(34, 211, 238, 0.10),
            transparent
        );

    box-shadow:
        0 0 8px #22d3ee,
        0 0 25px rgba(34, 211, 238, 0.55),
        0 0 50px rgba(37, 99, 235, 0.25);

    opacity: 0.8;

    z-index: 20;

    pointer-events: none;

    animation:
        sidebarScan 5s linear infinite;
}

@keyframes sidebarScan {

    0% {
        top: -10%;
        opacity: 0;
    }

    8% {
        opacity: 0.9;
    }

    50% {
        opacity: 0.75;
    }

    92% {
        opacity: 0.9;
    }

    100% {
        top: 110%;
        opacity: 0;
    }
}


/* =========================================================
   ðŸ”µ BRAND ICON â€” AI CORE
   ========================================================= */

[data-testid="stSidebar"] .brand-icon {

    position: relative !important;

    animation:
        aiCoreFloat 3s ease-in-out infinite,
        aiCoreGlow 2s ease-in-out infinite alternate !important;

    box-shadow:
        0 0 15px rgba(37, 99, 235, 0.5),
        0 0 35px rgba(6, 182, 212, 0.18) !important;
}


/* rotating ring around logo */

[data-testid="stSidebar"] .brand-icon::before {

    content: "";

    position: absolute;

    inset: -7px;

    border-radius: 16px;

    border:
        1px solid rgba(34, 211, 238, 0.45);

    border-top-color:
        #22d3ee;

    border-bottom-color:
        transparent;

    animation:
        logoRing 2.5s linear infinite;

    pointer-events: none;
}


/* second ring */

[data-testid="stSidebar"] .brand-icon::after {

    content: "";

    position: absolute;

    inset: -12px;

    border-radius: 20px;

    border:
        1px solid rgba(59, 130, 246, 0.18);

    border-left-color:
        #3b82f6;

    border-right-color:
        transparent;

    animation:
        logoRingReverse 4s linear infinite;

    pointer-events: none;
}

@keyframes logoRing {

    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}

@keyframes logoRingReverse {

    from {
        transform: rotate(360deg);
    }

    to {
        transform: rotate(0deg);
    }
}

@keyframes aiCoreFloat {

    0%,
    100% {
        transform:
            translateY(0)
            scale(1);
    }

    50% {
        transform:
            translateY(-5px)
            scale(1.04);
    }
}

@keyframes aiCoreGlow {

    0% {
        box-shadow:
            0 0 12px rgba(37, 99, 235, 0.35),
            0 0 25px rgba(6, 182, 212, 0.08);
    }

    100% {
        box-shadow:
            0 0 25px rgba(37, 99, 235, 0.65),
            0 0 50px rgba(6, 182, 212, 0.20);
    }
}


/* =========================================================
   âœ¨ BRAND TITLE
   ========================================================= */

[data-testid="stSidebar"] .brand-title {

    background:
        linear-gradient(
            90deg,
            #f8fafc 0%,
            #67e8f9 30%,
            #60a5fa 50%,
            #f8fafc 70%
        );

    background-size:
        250% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation:
        titleShimmer 4s linear infinite;
}

@keyframes titleShimmer {

    0% {
        background-position:
            200% center;
    }

    100% {
        background-position:
            -50% center;
    }
}


/* =========================================================
   ðŸ§­ NAVIGATION
   ========================================================= */

[data-testid="stSidebarNav"] a {

    position: relative !important;

    overflow: hidden !important;

    transition:
        all 0.3s cubic-bezier(
            0.2,
            0.8,
            0.2,
            1
        ) !important;
}


/* animated light sweep */

[data-testid="stSidebarNav"] a::after {

    content: "";

    position: absolute;

    top: 0;

    left: -120%;

    width: 75%;

    height: 100%;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(103, 232, 249, 0.12),
            rgba(255, 255, 255, 0.10),
            transparent
        );

    transform:
        skewX(-25deg);

    pointer-events: none;

    transition:
        left 0.6s ease;
}

[data-testid="stSidebarNav"] a:hover::after {

    left: 140%;
}


/* hover */

[data-testid="stSidebarNav"] a:hover {

    transform:
        translateX(8px) !important;

    background:
        linear-gradient(
            90deg,
            rgba(37, 99, 235, 0.22),
            rgba(6, 182, 212, 0.09),
            transparent
        ) !important;

    border-color:
        rgba(34, 211, 238, 0.32) !important;

    box-shadow:
        inset 3px 0 #22d3ee,
        0 0 20px rgba(37, 99, 235, 0.12) !important;
}


/* =========================================================
   ðŸ”¥ ACTIVE PAGE
   ========================================================= */

[data-testid="stSidebarNav"]
a[aria-current="page"] {

    position: relative !important;

    background:
        linear-gradient(
            90deg,
            rgba(37, 99, 235, 0.35),
            rgba(6, 182, 212, 0.12),
            transparent
        ) !important;

    border:
        1px solid rgba(34, 211, 238, 0.32) !important;

    box-shadow:
        inset 4px 0 #22d3ee,
        0 0 25px rgba(37, 99, 235, 0.15) !important;

    animation:
        activeHUD 2.2s ease-in-out infinite !important;
}


/* moving active light */

[data-testid="stSidebarNav"]
a[aria-current="page"]::before {

    content: "";

    position: absolute;

    left: 0;

    top: 0;

    width: 3px;

    height: 100%;

    background:
        linear-gradient(
            180deg,
            transparent,
            #22d3ee,
            #60a5fa,
            #22d3ee,
            transparent
        );

    background-size:
        100% 200%;

    box-shadow:
        0 0 10px #22d3ee,
        0 0 25px rgba(34, 211, 238, 0.5);

    animation:
        activeBeam 1.8s linear infinite;
}

@keyframes activeBeam {

    0% {
        background-position:
            0 -100%;
    }

    100% {
        background-position:
            0 100%;
    }
}

@keyframes activeHUD {

    0%,
    100% {
        box-shadow:
            inset 4px 0 #22d3ee,
            0 0 10px rgba(37, 99, 235, 0.06);
    }

    50% {
        box-shadow:
            inset 4px 0 #22d3ee,
            0 0 28px rgba(37, 99, 235, 0.22),
            0 0 45px rgba(6, 182, 212, 0.06);
    }
}


/* =========================================================
   ðŸŽ¬ NAVIGATION ENTRY
   ========================================================= */

[data-testid="stSidebarNav"] a {

    animation:
        navBoot 0.65s ease both;
}

[data-testid="stSidebarNav"] a:nth-child(1) {
    animation-delay: 0.05s;
}

[data-testid="stSidebarNav"] a:nth-child(2) {
    animation-delay: 0.12s;
}

[data-testid="stSidebarNav"] a:nth-child(3) {
    animation-delay: 0.19s;
}

[data-testid="stSidebarNav"] a:nth-child(4) {
    animation-delay: 0.26s;
}

[data-testid="stSidebarNav"] a:nth-child(5) {
    animation-delay: 0.33s;
}

[data-testid="stSidebarNav"] a:nth-child(6) {
    animation-delay: 0.40s;
}

[data-testid="stSidebarNav"] a:nth-child(7) {
    animation-delay: 0.47s;
}

@keyframes navBoot {

    from {
        opacity: 0;

        transform:
            translateX(-30px);

        filter:
            blur(5px);
    }

    to {
        opacity: 1;

        transform:
            translateX(0);

        filter:
            blur(0);
    }
}


/* =========================================================
   ðŸŸ¢ SECURITY STATUS
   ========================================================= */

[data-testid="stSidebar"] .status-dot {

    animation:
        securityPulse 1.5s ease-in-out infinite !important;
}

@keyframes securityPulse {

    0%,
    100% {
        transform:
            scale(0.75);

        box-shadow:
            0 0 4px rgba(34, 197, 94, 0.4);
    }

    50% {
        transform:
            scale(1.25);

        box-shadow:
            0 0 12px rgba(34, 197, 94, 0.9),
            0 0 25px rgba(34, 197, 94, 0.25);
    }
}


/* =========================================================
   ðŸ‘¤ USER CARD
   ========================================================= */

[data-testid="stSidebar"] .user-card {

    transition:
        all 0.35s ease !important;
}

[data-testid="stSidebar"] .user-card:hover {

    transform:
        translateY(-4px) !important;

    border-color:
        rgba(34, 211, 238, 0.35) !important;

    box-shadow:
        0 12px 30px rgba(0, 0, 0, 0.30),
        0 0 25px rgba(34, 211, 238, 0.08) !important;
}


/* =========================================================
   ðŸšª LOGOUT
   ========================================================= */

[data-testid="stSidebar"] .stButton > button {

    transition:
        all 0.3s ease !important;
}

[data-testid="stSidebar"] .stButton > button:hover {

    transform:
        translateY(-3px)
        scale(1.03) !important;

    box-shadow:
        0 0 20px rgba(34, 211, 238, 0.15) !important;
}


/* =========================================================
   ðŸŒ™ FOOTER
   ========================================================= */

[data-testid="stSidebar"] .sidebar-footer {

    animation:
        footerBreath 4s ease-in-out infinite;
}

@keyframes footerBreath {

    0%,
    100% {
        opacity: 0.35;
    }

    50% {
        opacity: 0.85;
    }
}

/* =========================================================
   ðŸ‘¤ AUTHENTICATED USER â€” PREMIUM PROFILE CARD
   ========================================================= */

[data-testid="stSidebar"] .user-card {
    position: relative !important;
    overflow: hidden !important;

    margin-top: 14px !important;
    padding: 16px !important;

    border-radius: 16px !important;

    background:
        linear-gradient(
            145deg,
            rgba(15, 23, 42, 0.92),
            rgba(8, 15, 30, 0.82)
        ) !important;

    border:
        1px solid rgba(96, 165, 250, 0.20) !important;

    box-shadow:
        0 12px 30px rgba(0, 0, 0, 0.25),
        inset 0 1px rgba(255, 255, 255, 0.04) !important;

    transition:
        transform 0.35s ease,
        border-color 0.35s ease,
        box-shadow 0.35s ease !important;

    animation:
        userCardAppear 0.8s ease both;
}


/* Moving light across card */

[data-testid="stSidebar"] .user-card::before {

    content: "";

    position: absolute;

    top: 0;
    left: -120%;

    width: 70%;
    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            #22d3ee,
            #60a5fa,
            transparent
        );

    box-shadow:
        0 0 12px #22d3ee;

    animation:
        userCardScan 4s linear infinite;

    pointer-events: none;
}


@keyframes userCardScan {

    0% {
        left: -120%;
    }

    50% {
        left: 120%;
    }

    100% {
        left: 120%;
    }
}


/* Card hover */

[data-testid="stSidebar"] .user-card:hover {

    transform:
        translateY(-4px) !important;

    border-color:
        rgba(34, 211, 238, 0.38) !important;

    box-shadow:
        0 15px 35px rgba(0, 0, 0, 0.35),
        0 0 25px rgba(34, 211, 238, 0.08),
        inset 0 1px rgba(103, 232, 249, 0.08) !important;
}


/* =========================================================
   AUTHENTICATED USER LABEL
   ========================================================= */

[data-testid="stSidebar"] .user-label {

    display: flex;
    align-items: center;
    gap: 8px;

    color: #64748b !important;

    font-size: 9px !important;

    letter-spacing: 1.8px !important;

    margin-bottom: 9px !important;
}


/* little glowing dot */

[data-testid="stSidebar"] .user-label::before {

    content: "";

    width: 6px;
    height: 6px;

    border-radius: 50%;

    background: #22c55e;

    box-shadow:
        0 0 6px #22c55e,
        0 0 14px rgba(34, 197, 94, 0.45);

    animation:
        userOnlineDot 1.8s ease-in-out infinite;
}


@keyframes userOnlineDot {

    0%,
    100% {
        transform: scale(0.8);
        opacity: 0.6;
    }

    50% {
        transform: scale(1.25);
        opacity: 1;
    }
}


/* =========================================================
   EMAIL
   ========================================================= */

[data-testid="stSidebar"] .user-email {

    color: #f1f5f9 !important;

    font-size: 12px !important;

    font-weight: 600 !important;

    line-height: 1.5 !important;

    padding: 8px 10px !important;

    border-radius: 9px !important;

    background:
        rgba(30, 41, 59, 0.55) !important;

    border:
        1px solid rgba(96, 165, 250, 0.10);

    transition:
        all 0.25s ease;
}


[data-testid="stSidebar"] .user-card:hover .user-email {

    border-color:
        rgba(34, 211, 238, 0.20);

    background:
        rgba(30, 41, 59, 0.75) !important;

    box-shadow:
        0 0 15px rgba(34, 211, 238, 0.05);
}


/* =========================================================
   SECURE SESSION STATUS
   ========================================================= */

[data-testid="stSidebar"] .status-row {

    margin-top: 11px !important;

    padding: 7px 9px !important;

    border-radius: 8px !important;

    background:
        rgba(34, 197, 94, 0.045) !important;

    border:
        1px solid rgba(34, 197, 94, 0.10);

    color:
        #94a3b8 !important;

    transition:
        all 0.25s ease;
}


[data-testid="stSidebar"] .user-card:hover .status-row {

    border-color:
        rgba(34, 197, 94, 0.20);

    background:
        rgba(34, 197, 94, 0.07) !important;
}


/* =========================================================
   USER CARD ENTRANCE
   ========================================================= */

@keyframes userCardAppear {

    from {
        opacity: 0;
        transform:
            translateY(15px)
            scale(0.97);
    }

    to {
        opacity: 1;
        transform:
            translateY(0)
            scale(1);
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# GLOBAL STYLE
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       HIDE STREAMLIT DEFAULT HEADER
       ===================================================== */

    [data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
    }


    /* =====================================================
       MAIN BACKGROUND
       ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 20% 20%,
                rgba(37, 99, 235, 0.08),
                transparent 35%
            ),
            radial-gradient(
                circle at 80% 80%,
                rgba(6, 182, 212, 0.06),
                transparent 35%
            ),
            #080c15;
    }


    .block-container {
        padding-top: 4.8rem !important;
        padding-bottom: 3rem !important;
    }


    /* =====================================================
       ANIMATIONS
       ===================================================== */

    @keyframes pulseGlow {

        0% {
            box-shadow:
                0 0 8px rgba(34, 211, 238, 0.20),
                0 0 20px rgba(37, 99, 235, 0.10);
        }

        50% {
            box-shadow:
                0 0 20px rgba(34, 211, 238, 0.55),
                0 0 45px rgba(37, 99, 235, 0.25);
        }

        100% {
            box-shadow:
                0 0 8px rgba(34, 211, 238, 0.20),
                0 0 20px rgba(37, 99, 235, 0.10);
        }
    }


    @keyframes floatLogo {

        0% {
            transform: translateY(0);
        }

        50% {
            transform: translateY(-4px);
        }

        100% {
            transform: translateY(0);
        }
    }


    @keyframes floatParticle {

        0% {
            transform:
                translateY(0)
                translateX(0);
            opacity: 0.25;
        }

        50% {
            transform:
                translateY(-30px)
                translateX(15px);
            opacity: 0.8;
        }

        100% {
            transform:
                translateY(0)
                translateX(0);
            opacity: 0.25;
        }
    }


    @keyframes gradientMove {

        0% {
            background-position: 0% 50%;
        }

        50% {
            background-position: 100% 50%;
        }

        100% {
            background-position: 0% 50%;
        }
    }


    @keyframes statusPulse {

        0% {
            transform: scale(1);
            opacity: 0.65;
        }

        50% {
            transform: scale(1.4);
            opacity: 1;
        }

        100% {
            transform: scale(1);
            opacity: 0.65;
        }
    }
    
    /* ================================
   EXTRA FUTURISTIC LOGIN EFFECTS
   ================================ */

/* Extra ambient glow */
.login-wrapper::before {
    content: "";
    position: absolute;
    inset: -100%;
    background-image:
        linear-gradient(
            rgba(34, 211, 238, 0.045) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(34, 211, 238, 0.045) 1px,
            transparent 1px
        );

    background-size: 45px 45px;

    transform:
        perspective(500px)
        rotateX(55deg);

    animation: movingGrid 12s linear infinite;

    pointer-events: none;
    z-index: 1;
}

@keyframes movingGrid {

    from {
        transform:
            perspective(500px)
            rotateX(55deg)
            translateY(0);
    }

    to {
        transform:
            perspective(500px)
            rotateX(55deg)
            translateY(45px);
    }
}


/* Scanning laser */
.login-wrapper::after {
    content: "";

    position: absolute;

    left: 0;
    right: 0;

    top: -5%;

    height: 2px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(34, 211, 238, 0.15),
            rgba(34, 211, 238, 0.95),
            rgba(34, 211, 238, 0.15),
            transparent
        );

    box-shadow:
        0 0 12px rgba(34, 211, 238, 0.8),
        0 0 35px rgba(34, 211, 238, 0.45);

    animation:
        scanningBeam 5s ease-in-out infinite;

    pointer-events: none;

    z-index: 4;
}

@keyframes scanningBeam {

    0% {
        top: 5%;
        opacity: 0;
    }

    10% {
        opacity: 1;
    }

    50% {
        opacity: 0.9;
    }

    90% {
        opacity: 1;
    }

    100% {
        top: 95%;
        opacity: 0;
    }
}


/* ================================
   CARD FLOAT + NEON PULSE
   ================================ */

.login-card {
    animation:
        cardAppear 0.7s ease,
        loginCardFloat 5s ease-in-out 1s infinite;
}

@keyframes loginCardFloat {

    0%,
    100% {
        transform: translateY(0);
        box-shadow:
            0 30px 80px rgba(0, 0, 0, 0.45),
            0 0 45px rgba(37, 99, 235, 0.08);
    }

    50% {
        transform: translateY(-5px);
        box-shadow:
            0 35px 90px rgba(0, 0, 0, 0.5),
            0 0 65px rgba(37, 99, 235, 0.18),
            0 0 100px rgba(6, 182, 212, 0.05);
    }
}


/* ================================
   LOGIN CARD BORDER GLOW
   ================================ */

.login-card::before {

    content: "";

    position: absolute;

    inset: -1px;

    border-radius: 25px;

    padding: 1px;

    background:
        linear-gradient(
            120deg,
            transparent 20%,
            rgba(34, 211, 238, 0.7),
            transparent 45%,
            rgba(59, 130, 246, 0.6),
            transparent 70%
        );

    background-size: 250% 250%;

    animation:
        borderFlow 5s linear infinite;

    pointer-events: none;

    opacity: 0.45;

    z-index: -1;
}

@keyframes borderFlow {

    0% {
        background-position: 0% 50%;
    }

    100% {
        background-position: 250% 50%;
    }
}


/* ================================
   EXISTING PARTICLES - ENHANCED
   ================================ */

.particle {

    animation:
        floatParticle 6s ease-in-out infinite,
        particleGlow 2s ease-in-out infinite alternate;
}

@keyframes particleGlow {

    from {
        opacity: 0.35;
        transform: scale(0.8);
    }

    to {
        opacity: 1;
        transform: scale(1.5);
    }
}


/* ================================
   MORE PARTICLES
   ================================ */

.login-wrapper .p5,
.login-wrapper .p6,
.login-wrapper .p7,
.login-wrapper .p8 {

    position: absolute;

    width: 3px;
    height: 3px;

    border-radius: 50%;

    background: #67e8f9;

    box-shadow:
        0 0 8px #22d3ee,
        0 0 18px rgba(34, 211, 238, 0.7);

    z-index: 2;
}

.p5 {
    left: 40%;
    top: 12%;
    animation:
        particleDrift 7s ease-in-out infinite;
}

.p6 {
    left: 60%;
    top: 78%;
    animation:
        particleDrift 9s ease-in-out 1s infinite reverse;
}

.p7 {
    left: 88%;
    top: 35%;
    animation:
        particleDrift 8s ease-in-out 2s infinite;
}

.p8 {
    left: 7%;
    top: 48%;
    animation:
        particleDrift 10s ease-in-out 1.5s infinite reverse;
}

@keyframes particleDrift {

    0%,
    100% {
        transform:
            translate(0, 0)
            scale(0.7);

        opacity: 0.25;
    }

    50% {
        transform:
            translate(30px, -35px)
            scale(1.4);

        opacity: 1;
    }
}


/* ================================
   INPUT GLOW
   ================================ */

[data-testid="stTextInput"] input {

    transition:
        all 0.25s ease !important;
}

[data-testid="stTextInput"] input:focus {

    border-color:
        rgba(34, 211, 238, 0.75) !important;

    box-shadow:
        0 0 0 1px rgba(34, 211, 238, 0.18),
        0 0 20px rgba(34, 211, 238, 0.18),
        inset 0 0 15px rgba(34, 211, 238, 0.035) !important;

    transform:
        translateY(-1px);
}


/* ================================
   BUTTON HOVER EFFECT
   ================================ */

.stButton > button {

    transition:
        transform 0.2s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease !important;
}

.stButton > button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 0 20px rgba(34, 211, 238, 0.20),
        0 8px 25px rgba(0, 0, 0, 0.25) !important;
}

.stButton > button:active {

    transform:
        translateY(0)
        scale(0.98);
}


    /* =====================================================
       LOGIN PAGE
       ===================================================== */

    .login-wrapper {

        min-height: 75vh;

        display: flex;

        align-items: center;

        justify-content: center;

        position: relative;

        overflow: hidden;

        padding: 30px;
    }


    /* Ambient glow */

    .login-glow-one {

        position: absolute;

        width: 420px;

        height: 420px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(37, 99, 235, 0.20),
                transparent 70%
            );

        filter: blur(25px);

        left: 5%;

        top: 5%;

        animation:
            floatParticle 8s ease-in-out infinite;
    }


    .login-glow-two {

        position: absolute;

        width: 350px;

        height: 350px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(6, 182, 212, 0.16),
                transparent 70%
            );

        filter: blur(25px);

        right: 5%;

        bottom: 5%;

        animation:
            floatParticle 10s ease-in-out infinite reverse;
    }


    /* Particle dots */

    .particle {

        position: absolute;

        width: 4px;

        height: 4px;

        border-radius: 50%;

        background: #67e8f9;

        box-shadow:
            0 0 10px #22d3ee;

        animation:
            floatParticle 6s ease-in-out infinite;
    }


    .p1 {
        left: 18%;
        top: 22%;
        animation-delay: 0s;
    }

    .p2 {
        left: 72%;
        top: 18%;
        animation-delay: 1s;
    }

    .p3 {
        left: 82%;
        top: 65%;
        animation-delay: 2s;
    }

    .p4 {
        left: 15%;
        top: 72%;
        animation-delay: 3s;
    }


    /* Login card */

    .login-card {

        width: 430px;

        max-width: 95%;

        padding: 34px;

        border-radius: 24px;

        background:
            linear-gradient(
                145deg,
                rgba(15, 23, 42, 0.94),
                rgba(8, 15, 29, 0.94)
            );

        border:
            1px solid
            rgba(96, 165, 250, 0.22);

        box-shadow:
            0 30px 80px
            rgba(0, 0, 0, 0.45),
            0 0 45px
            rgba(37, 99, 235, 0.08);

        backdrop-filter:
            blur(20px);

        position: relative;

        z-index: 5;

        animation:
            cardAppear 0.7s ease;
    }


    @keyframes cardAppear {

        from {
            opacity: 0;
            transform:
                translateY(25px)
                scale(0.97);
        }

        to {
            opacity: 1;
            transform:
                translateY(0)
                scale(1);
        }
    }


    .login-logo {

        width: 68px;

        height: 68px;

        border-radius: 19px;

        display: flex;

        align-items: center;

        justify-content: center;

        margin:
            0 auto 18px auto;

        font-size: 32px;

        background:
            linear-gradient(
                135deg,
                #2563eb,
                #06b6d4
            );

        animation:
            pulseGlow 3s ease-in-out infinite,
            floatLogo 4s ease-in-out infinite;
    }


    .login-title {

        text-align: center;

        color: #f8fafc;

        font-size: 30px;

        font-weight: 800;

        letter-spacing: -0.8px;

        margin-bottom: 5px;
    }


    .login-subtitle {

        text-align: center;

        color: #94a3b8;

        font-size: 13px;

        margin-bottom: 28px;
    }


    .login-badge {

        width: fit-content;

        margin:
            0 auto 20px auto;

        padding:
            5px 11px;

        border-radius: 999px;

        background:
            rgba(34, 211, 238, 0.08);

        border:
            1px solid
            rgba(34, 211, 238, 0.18);

        color:
            #67e8f9;

        font-size: 9px;

        letter-spacing: 1.5px;

        font-weight: 700;
    }
    
    /* =========================================================
   ULTRA FUTURISTIC AI LOGIN EFFECTS
   ========================================================= */

/* ---------- Moving Cyber Grid ---------- */

.login-wrapper::before {

    content: "";

    position: absolute;

    width: 200%;
    height: 200%;

    left: -50%;
    top: -50%;

    background-image:
        linear-gradient(
            rgba(34, 211, 238, 0.055) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(34, 211, 238, 0.055) 1px,
            transparent 1px
        );

    background-size: 42px 42px;

    transform:
        perspective(600px)
        rotateX(60deg);

    animation:
        cyberGridMove 12s linear infinite;

    opacity: 0.8;

    pointer-events: none;

    z-index: 1;
}

@keyframes cyberGridMove {

    0% {
        transform:
            perspective(600px)
            rotateX(60deg)
            translateY(0);
    }

    100% {
        transform:
            perspective(600px)
            rotateX(60deg)
            translateY(42px);
    }
}


/* =========================================================
   MULTI COLOR ATMOSPHERIC LIGHT
   ========================================================= */

.login-wrapper .login-glow-one {

    animation:
        glowMoveOne 7s ease-in-out infinite,
        glowPulseOne 4s ease-in-out infinite alternate;
}

.login-wrapper .login-glow-two {

    animation:
        glowMoveTwo 9s ease-in-out infinite,
        glowPulseTwo 5s ease-in-out infinite alternate;
}

@keyframes glowMoveOne {

    0%,
    100% {
        transform:
            translate(0, 0)
            scale(1);
    }

    50% {
        transform:
            translate(100px, 60px)
            scale(1.25);
    }
}

@keyframes glowMoveTwo {

    0%,
    100% {
        transform:
            translate(0, 0)
            scale(1);
    }

    50% {
        transform:
            translate(-100px, -70px)
            scale(1.2);
    }
}

@keyframes glowPulseOne {

    from {
        opacity: 0.5;
    }

    to {
        opacity: 1;
    }
}

@keyframes glowPulseTwo {

    from {
        opacity: 0.4;
    }

    to {
        opacity: 0.9;
    }
}


/* =========================================================
   LASER SCANNER
   ========================================================= */

.login-wrapper .scanner-line {

    position: absolute;

    left: 0;
    right: 0;

    height: 3px;

    background:
        linear-gradient(
            90deg,
            transparent,
            #22d3ee,
            #ffffff,
            #22d3ee,
            transparent
        );

    box-shadow:
        0 0 10px #22d3ee,
        0 0 30px #22d3ee,
        0 0 60px rgba(34, 211, 238, 0.5);

    z-index: 4;

    animation:
        laserScan 4.5s ease-in-out infinite;
}

@keyframes laserScan {

    0% {
        top: 0%;
        opacity: 0;
    }

    8% {
        opacity: 1;
    }

    50% {
        opacity: 1;
    }

    92% {
        opacity: 1;
    }

    100% {
        top: 100%;
        opacity: 0;
    }
}


/* =========================================================
   LOGIN CARD HOLOGRAM EFFECT
   ========================================================= */

.login-card {

    animation:
        cardAppear 0.8s ease-out,
        hologramFloat 5s ease-in-out 1s infinite;

    transition:
        transform 0.4s ease,
        box-shadow 0.4s ease,
        border-color 0.4s ease;
}

.login-card:hover {

    border-color:
        rgba(34, 211, 238, 0.55);

    box-shadow:
        0 35px 100px rgba(0, 0, 0, 0.55),
        0 0 50px rgba(37, 99, 235, 0.22),
        0 0 100px rgba(6, 182, 212, 0.10);
}

@keyframes hologramFloat {

    0%,
    100% {
        transform:
            translateY(0)
            scale(1);
    }

    50% {
        transform:
            translateY(-7px)
            scale(1.008);
    }
}


/* =========================================================
   CARD NEON BORDER
   ========================================================= */

.login-card::before {

    content: "";

    position: absolute;

    inset: -2px;

    border-radius: 26px;

    background:
        conic-gradient(
            from 0deg,
            transparent 0deg,
            transparent 60deg,
            rgba(34, 211, 238, 0.8) 90deg,
            transparent 120deg,
            transparent 210deg,
            rgba(59, 130, 246, 0.8) 250deg,
            transparent 290deg,
            transparent 360deg
        );

    animation:
        rotateBorder 4s linear infinite;

    z-index: -2;

    opacity: 0.8;
}

.login-card::after {

    content: "";

    position: absolute;

    inset: 1px;

    border-radius: 23px;

    background:
        linear-gradient(
            145deg,
            rgba(15, 23, 42, 0.98),
            rgba(8, 15, 29, 0.98)
        );

    z-index: -1;
}

@keyframes rotateBorder {

    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}


/* =========================================================
   LOGO AREA
   ========================================================= */

.login-logo {

    animation:
        logoFloat 3s ease-in-out infinite,
        logoEnergy 2s ease-in-out infinite alternate;

    position: relative;

    transition:
        transform 0.3s ease;
}

.login-logo:hover {

    transform:
        scale(1.12)
        rotate(-5deg);
}

@keyframes logoFloat {

    0%,
    100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-8px);
    }
}

@keyframes logoEnergy {

    from {

        box-shadow:
            0 0 15px rgba(34, 211, 238, 0.2),
            inset 0 0 15px rgba(34, 211, 238, 0.05);
    }

    to {

        box-shadow:
            0 0 30px rgba(34, 211, 238, 0.65),
            0 0 70px rgba(37, 99, 235, 0.22),
            inset 0 0 25px rgba(34, 211, 238, 0.12);
    }
}


/* =========================================================
   ORBIT RINGS AROUND LOGO
   ========================================================= */

.login-logo::before {

    content: "";

    position: absolute;

    width: 125px;
    height: 42px;

    left: 50%;
    top: 50%;

    transform:
        translate(-50%, -50%)
        rotate(-25deg);

    border:

        1px solid
        rgba(34, 211, 238, 0.55);

    border-radius: 50%;

    box-shadow:
        0 0 10px rgba(34, 211, 238, 0.25);

    animation:
        logoOrbitOne 3s linear infinite;

    pointer-events: none;
}

.login-logo::after {

    content: "";

    position: absolute;

    width: 125px;
    height: 42px;

    left: 50%;
    top: 50%;

    transform:
        translate(-50%, -50%)
        rotate(55deg);

    border:

        1px solid
        rgba(59, 130, 246, 0.5);

    border-radius: 50%;

    animation:
        logoOrbitTwo 4s linear infinite reverse;

    pointer-events: none;
}

@keyframes logoOrbitOne {

    from {
        transform:
            translate(-50%, -50%)
            rotate(-25deg);
    }

    to {
        transform:
            translate(-50%, -50%)
            rotate(335deg);
    }
}

@keyframes logoOrbitTwo {

    from {
        transform:
            translate(-50%, -50%)
            rotate(55deg);
    }

    to {
        transform:
            translate(-50%, -50%)
            rotate(415deg);
    }
}


/* =========================================================
   TITLE ANIMATION
   ========================================================= */

.login-title {

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #67e8f9,
            #3b82f6,
            #ffffff,
            #67e8f9
        );

    background-size: 300% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation:
        titleGlow 4s linear infinite,
        titleEntrance 1s ease-out;
}

@keyframes titleGlow {

    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 300% center;
    }
}

@keyframes titleEntrance {

    0% {

        opacity: 0;

        transform:
            translateY(15px);

        filter:
            blur(8px);
    }

    100% {

        opacity: 1;

        transform:
            translateY(0);

        filter:
            blur(0);
    }
}


/* =========================================================
   SUBTITLE
   ========================================================= */

.login-subtitle {

    animation:
        subtitleEntrance 1s ease-out 0.25s both;
}

@keyframes subtitleEntrance {

    from {

        opacity: 0;

        transform:
            translateY(10px);

        letter-spacing: 4px;
    }

    to {

        opacity: 0.7;

        transform:
            translateY(0);

        letter-spacing: 1.5px;
    }
}


/* =========================================================
   SECURITY BADGE
   ========================================================= */

.login-badge {

    position: relative;

    overflow: hidden;

    animation:
        badgeEntrance 1s ease-out 0.45s both,
        badgePulse 2s ease-in-out 1.5s infinite;
}

.login-badge::after {

    content: "";

    position: absolute;

    top: 0;
    bottom: 0;

    width: 40px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.5),
            transparent
        );

    transform:
        translateX(-80px)
        skewX(-20deg);

    animation:
        badgeScan 3s ease-in-out infinite;
}

@keyframes badgeEntrance {

    from {

        opacity: 0;

        transform:
            scale(0.7);
    }

    to {

        opacity: 1;

        transform:
            scale(1);
    }
}

@keyframes badgeScan {

    0% {
        left: -30%;
    }

    45% {
        left: 130%;
    }

    100% {
        left: 130%;
    }
}

@keyframes badgePulse {

    0%,
    100% {
        box-shadow:
            0 0 10px rgba(34, 211, 238, 0.05);
    }

    50% {
        box-shadow:
            0 0 25px rgba(34, 211, 238, 0.25);
    }
}


/* =========================================================
   PARTICLE ENERGY
   ========================================================= */

.particle {

    animation:
        particleFloat 5s ease-in-out infinite,
        particleBlink 1.8s ease-in-out infinite alternate;
}

@keyframes particleFloat {

    0%,
    100% {

        transform:
            translate(0, 0)
            scale(0.8);
    }

    50% {

        transform:
            translate(20px, -30px)
            scale(1.5);
    }
}

@keyframes particleBlink {

    from {
        opacity: 0.2;
    }

    to {
        opacity: 1;
    }
}


/* =========================================================
   EXTRA PARTICLES
   ========================================================= */

.login-wrapper .p5,
.login-wrapper .p6,
.login-wrapper .p7,
.login-wrapper .p8,
.login-wrapper .p9,
.login-wrapper .p10 {

    position: absolute;

    width: 3px;
    height: 3px;

    border-radius: 50%;

    background: #67e8f9;

    box-shadow:
        0 0 8px #22d3ee,
        0 0 20px rgba(34, 211, 238, 0.8);

    z-index: 3;
}

.p5 {
    left: 35%;
    top: 15%;
    animation:
        extraParticle 6s ease-in-out infinite;
}

.p6 {
    left: 65%;
    top: 20%;
    animation:
        extraParticle 8s ease-in-out 1s infinite reverse;
}

.p7 {
    left: 90%;
    top: 45%;
    animation:
        extraParticle 7s ease-in-out 2s infinite;
}

.p8 {
    left: 10%;
    top: 45%;
    animation:
        extraParticle 9s ease-in-out 1s infinite reverse;
}

.p9 {
    left: 25%;
    top: 85%;
    animation:
        extraParticle 7s ease-in-out 3s infinite;
}

.p10 {
    left: 75%;
    top: 82%;
    animation:
        extraParticle 8s ease-in-out 2s infinite reverse;
}

@keyframes extraParticle {

    0%,
    100% {

        transform:
            translate(0, 0)
            scale(0.5);

        opacity: 0.2;
    }

    50% {

        transform:
            translate(
                35px,
                -45px
            )
            scale(1.5);

        opacity: 1;
    }
}


/* =========================================================
   INPUT ANIMATION
   ========================================================= */

[data-testid="stTextInput"] {

    animation:
        formEntrance 0.7s ease-out both;
}

[data-testid="stTextInput"] input {

    transition:
        all 0.3s ease !important;
}

[data-testid="stTextInput"] input:hover {

    border-color:
        rgba(34, 211, 238, 0.4) !important;

    box-shadow:
        0 0 15px rgba(34, 211, 238, 0.08) !important;
}

[data-testid="stTextInput"] input:focus {

    border-color:
        #22d3ee !important;

    box-shadow:
        0 0 0 1px rgba(34, 211, 238, 0.25),
        0 0 25px rgba(34, 211, 238, 0.2),
        inset 0 0 20px rgba(34, 211, 238, 0.04) !important;

    transform:
        translateY(-2px);
}

@keyframes formEntrance {

    from {

        opacity: 0;

        transform:
            translateY(18px);
    }

    to {

        opacity: 1;

        transform:
            translateY(0);
    }
}


/* =========================================================
   BUTTON POWER EFFECT
   ========================================================= */

.stButton > button {

    position: relative;

    overflow: hidden;

    transition:
        all 0.25s ease !important;
}

.stButton > button::after {

    content: "";

    position: absolute;

    top: 0;
    left: -100%;

    width: 70%;
    height: 100%;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.18),
            transparent
        );

    transform:
        skewX(-20deg);

    transition:
        left 0.5s ease;
}

.stButton > button:hover::after {

    left: 130%;
}

.stButton > button:hover {

    transform:
        translateY(-3px);

    box-shadow:
        0 0 25px rgba(34, 211, 238, 0.25),
        0 10px 30px rgba(0, 0, 0, 0.25) !important;
}


/* =========================================================
   CORNER HUD MARKERS
   ========================================================= */

.login-wrapper .hud-corner {

    position: absolute;

    width: 35px;
    height: 35px;

    z-index: 3;

    opacity: 0.55;
}

.hud-corner::before,
.hud-corner::after {

    content: "";

    position: absolute;

    background: #22d3ee;
}

.hud-corner::before {

    width: 35px;
    height: 1px;
}

.hud-corner::after {

    width: 1px;
    height: 35px;
}

.hud-top-left {
    left: 25px;
    top: 25px;
}

.hud-top-right {
    right: 25px;
    top: 25px;
    transform: rotate(90deg);
}

.hud-bottom-left {
    left: 25px;
    bottom: 25px;
    transform: rotate(-90deg);
}

.hud-bottom-right {
    right: 25px;
    bottom: 25px;
    transform: rotate(180deg);
}


/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 700px) {

    .login-wrapper {
        min-height: 65vh;
        padding: 15px;
    }

    .login-card {
        width: 92%;
        padding: 28px 20px;
    }

    .login-card::before {
        opacity: 0.5;
    }

    .login-wrapper::before {
        background-size: 30px 30px;
    }
}

</style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOGIN / SIGNUP PAGE
# =========================================================

if not is_logged_in():

    # Hide sidebar while logged out
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Animated background
    st.html(
        """
        <div class="login-wrapper">

            <!-- Futuristic HUD corner markers -->
            <div class="hud-corner hud-top-left"></div>
            <div class="hud-corner hud-top-right"></div>
            <div class="hud-corner hud-bottom-left"></div>
            <div class="hud-corner hud-bottom-right"></div>

            <!-- Ambient energy glows -->
            <div class="login-glow-one"></div>
            <div class="login-glow-two"></div>

            <!-- Floating particles -->
            <div class="particle p1"></div>
            <div class="particle p2"></div>
            <div class="particle p3"></div>
            <div class="particle p4"></div>
            <div class="particle p5"></div>
            <div class="particle p6"></div>
            <div class="particle p7"></div>
            <div class="particle p8"></div>
            <div class="particle p9"></div>
            <div class="particle p10"></div>

            <!-- Main futuristic login card -->
            <div class="login-card">

                <div class="login-logo">&#128269;</div>

                <div class="login-title">
                    AI Data Detective
                </div>

                <div class="login-subtitle">
                    Intelligent Data Investigation Platform
                </div>

                <div class="login-badge">
                    SECURE ACCESS
                </div>

            </div>

        </div>
        """
    )


   # -----------------------------------------------------

# =========================================================
# =========================================================
# AUTHENTICATION GATE
# =========================================================

if not is_admin() and not is_logged_in():

    # AUTHENTICATION
    # =========================================================

    if "auth_mode" not in st.session_state:
        st.session_state["auth_mode"] = "login"

    if "login_type" not in st.session_state:
        st.session_state["login_type"] = "user"


    # =========================================================
    # LOGIN TYPE SELECTOR
    # =========================================================

    if st.session_state["auth_mode"] == "login":

        col1, col2 = st.columns(2)

        with col1:

            if st.session_state["login_type"] == "user":

                st.markdown(
                    """
                    <div style="
                        text-align:center;
                        color:#67e8f9;
                        font-weight:700;
                        padding:10px;
                        border-radius:10px;
                        background:rgba(34,211,238,0.08);
                        border:1px solid rgba(34,211,238,0.35);
                    ">
                        USER LOGIN
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                if st.button(
                    "USER LOGIN",
                    use_container_width=True,
                    key="select_user_login"
                ):
                    st.session_state["login_type"] = "user"
                    st.rerun()


        with col2:

            if st.session_state["login_type"] == "admin":

                st.markdown(
                    """
                    <div style="
                        text-align:center;
                        color:#c084fc;
                        font-weight:700;
                        padding:10px;
                        border-radius:10px;
                        background:rgba(168,85,247,0.08);
                        border:1px solid rgba(168,85,247,0.40);
                    ">
                        ADMIN LOGIN
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                if st.button(
                    "ADMIN LOGIN",
                    use_container_width=True,
                    key="select_admin_login"
                ):
                    st.session_state["login_type"] = "admin"
                    st.rerun()


        st.write("")


        # =====================================================
        # ADMIN LOGIN
        # =====================================================

        if st.session_state["login_type"] == "admin":

            st.markdown(
                """
                <div style="
                    text-align:center;
                    color:#c084fc;
                    font-size:20px;
                    font-weight:800;
                    margin:20px 0;
                ">
                    ADMINISTRATOR ACCESS
                </div>
                """,
                unsafe_allow_html=True
            )

            admin_email_input = st.text_input(
                "Admin Email",
                placeholder="Enter administrator email",
                key="admin_email_login"
            )

            admin_password_input = st.text_input(
                "Admin Password",
                type="password",
                placeholder="Enter administrator password",
                key="admin_password_login"
            )

            if st.button(
                "LOGIN TO ADMIN PANEL",
                use_container_width=True,
                type="primary",
                key="admin_login_submit"
            ):

                if not admin_email_input or not admin_password_input:

                    st.warning(
                        "Please enter admin email and password."
                    )

                elif admin_sign_in(
                    admin_email_input.strip(),
                    admin_password_input
                ):

                    st.success(
                        "Administrator authentication successful."
                    )

                    st.rerun()

                else:

                    st.error(
                        "Invalid admin email or password."
                    )


        # =====================================================
        # USER LOGIN
        # =====================================================

        else:

            st.markdown(
                """
                <div style="
                    text-align:center;
                    color:#67e8f9;
                    font-size:20px;
                    font-weight:800;
                    margin:20px 0;
                ">
                    USER ACCESS
                </div>
                """,
                unsafe_allow_html=True
            )

            user_email_input = st.text_input(
                "Email",
                placeholder="Enter your email",
                key="user_email_login"
            )

            user_password_input = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password",
                key="user_password_login"
            )

            if st.button(
                "LOGIN TO USER PANEL",
                use_container_width=True,
                type="primary",
                key="user_login_submit"
            ):

                if not user_email_input or not user_password_input:

                    st.warning(
                        "Please enter your email and password."
                    )

                else:

                    try:

                        response = sign_in(
                            user_email_input.strip(),
                            user_password_input
                        )

                        save_session(response)

                        if is_logged_in():

                            st.success(
                                "Login successful."
                            )

                            st.rerun()

                        else:

                            st.error(
                                "Unable to create user session."
                            )

                    except Exception as e:

                        st.error(
                            f"Login failed: {e}"
                        )


        # =====================================================
        # CREATE USER ACCOUNT
        # =====================================================

        if st.session_state["login_type"] == "user":

            st.markdown(
                """
                <div style="
                    text-align:center;
                    color:#64748b;
                    font-size:12px;
                    margin-top:20px;
                ">
                    Don't have a user account
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "CREATE NEW USER ACCOUNT",
                use_container_width=True,
                key="open_user_signup"
            ):

                st.session_state["auth_mode"] = "signup"
                st.session_state["login_type"] = "user"
                st.rerun()


    # =========================================================
    # USER SIGNUP
    # =========================================================

    elif st.session_state["auth_mode"] == "signup":

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "BACK TO LOGIN",
                use_container_width=True,
                key="back_to_login"
            ):

                st.session_state["auth_mode"] = "login"
                st.session_state["login_type"] = "user"
                st.rerun()

        with col2:

            st.markdown(
                """
                <div style="
                    text-align:center;
                    color:#67e8f9;
                    font-weight:700;
                    padding:10px;
                ">
                    CREATE ACCOUNT
                </div>
                """,
                unsafe_allow_html=True
            )


        st.write("")

        st.markdown(
            """
            <div style="
                text-align:center;
                color:#94a3b8;
                margin-bottom:15px;
            ">
                Create your secure user account.
            </div>
            """,
            unsafe_allow_html=True
        )

        signup_email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="signup_email"
        )

        signup_password = st.text_input(
            "Password",
            type="password",
            placeholder="Minimum 8 characters",
            key="signup_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Re-enter your password",
            key="confirm_password"
        )

        if st.button(
            "CREATE MY ACCOUNT",
            use_container_width=True,
            type="primary",
            key="signup_submit"
        ):

            if not signup_email or not signup_password:

                st.warning(
                    "Please fill in all required fields."
                )

            elif signup_password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            elif len(signup_password) < 8:

                st.warning(
                    "Password must contain at least 8 characters."
                )

            else:

                try:

                    response = sign_up(
                        signup_email.strip(),
                        signup_password
                    )

                    if response.user is not None:

                        st.success(
                            "Account created successfully."
                        )

                        st.info(
                            "Please verify your email before logging in."
                        )

                        st.session_state["auth_mode"] = "login"
                        st.session_state["login_type"] = "user"

                    else:

                        st.error(
                            "Account could not be created."
                        )

                except Exception as e:

                    st.error(
                        f"Sign up failed: {e}"
                    )


    st.stop()




# =========================================================
# AUTHENTICATED APPLICATION
# =========================================================

user = st.session_state.get("user")

user_email = "User"

if user is not None:
    user_email = getattr(user, "email", None) or "User"


# =========================================================
# CLEAN ROLE-BASED NAVIGATION
# =========================================================

user_pages = [
    st.Page(
        "pages/0_Home.py",
        title="Home",
        icon="\U0001F3E0"
    ),
    st.Page(
        "pages/1_Upload_Data.py",
        title="Upload Data",
        icon="\U0001F4E5"
    ),
    st.Page(
        "pages/2_Data_Analysis.py",
        title="Data Analysis",
        icon="\U0001F4CA"
    ),
    st.Page(
        "pages/3_Data_Visualization.py",
        title="Data Visualization",
        icon="\U0001F4C8"
    ),
    st.Page(
        "pages/4_AI_Insights.py",
        title="AI Insights",
        icon="\U0001F916"
    ),
    st.Page(
        "pages/5_Machine_Learning.py",
        title="Machine Learning",
        icon="\U0001F9E0"
    ),
    st.Page(
        "pages/6_Report_Download.py",
        title="Report Download",
        icon="\U0001F4C4"
    ),
]

admin_pages = [
    st.Page(
        "pages/7_Admin_Panel.py",
        title="Admin Dashboard",
        icon="\U0001F6E1"
    ),
]


# =========================================================
# ONLY ONE NAVIGATION OBJECT
# =========================================================

if is_admin():

    pg = st.navigation(
        {
            "ADMIN PANEL": admin_pages
        }
    )

elif is_logged_in():

    pg = st.navigation(
        {
            "USER PANEL": user_pages
        }
    )

else:

    st.stop()


# =========================================================
# SIDEBAR BRANDING
# =========================================================

# =========================================================

with st.sidebar:

    st.html(
        """
        <div class="sidebar-brand">

         
            <div class="brand-row">

                <div class="brand-icon">
                    &#128269;
                </div>

                <div>

                    <div class="brand-title">
                        AI Data Detective
                    </div>

                    <div class="brand-subtitle">
                        Intelligence Platform
                    </div>

                </div>

            </div>

        </div>
        """
    )


# =========================================================
# SIDEBAR USER INFORMATION
# =========================================================

with st.sidebar:

    st.html(
        f"""
        <div class="sidebar-divider"></div>

        <div class="user-card">

            <div class="user-label">
                AUTHENTICATED USER
            </div>

            <div class="user-email">
                {user_email}
            </div>

            <div class="status-row">

                <div class="status-dot"></div>

                <span>
                    Secure session active
                </span>

            </div>

        </div>
        """
    )


# =========================================================
# LOGOUT BUTTON
# =========================================================

with st.sidebar:

    if st.button(
        "\U0001F6AA  Logout",
        use_container_width=True
    ):

        sign_out()

        st.session_state["auth_mode"] = "login"

        st.rerun()


# =========================================================
# SIDEBAR FOOTER
# =========================================================

with st.sidebar:

    st.html(
        """
        <div class="sidebar-footer">
            AI DATA DETECTIVE - v1.0
        </div>
        """
    )


# =========================================================
# RUN APPLICATION
# =========================================================

pg.run()

