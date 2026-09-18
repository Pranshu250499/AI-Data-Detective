import streamlit as st
from supabase import create_client


@st.cache_resource
def get_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)


# =========================
# USER SIGN UP
# =========================

@st.cache_resource
def get_admin_supabase():
    url = st.secrets["SUPABASE_URL"]
    secret_key = st.secrets["SUPABASE_SECRET_KEY"]
    return create_client(url, secret_key)


def sign_up(email, password):
    supabase = get_supabase()

    return supabase.auth.sign_up({
        "email": email,
        "password": password
    })


# =========================
# USER LOGIN
# =========================

def sign_in(email, password):
    supabase = get_supabase()

    return supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })


# =========================
# SAVE SESSION
# =========================

def save_session(response):

    if response.user is not None:
        st.session_state["user"] = response.user

    if response.session is not None:
        st.session_state["session"] = response.session


# =========================
# USER LOGIN CHECK
# =========================

def is_logged_in():
    return st.session_state.get("user") is not None


# =========================
# CURRENT USER
# =========================

def get_current_user():
    return st.session_state.get("user")


# =========================
# ADMIN LOGIN
# =========================

def admin_sign_in(email, password):

    admin_email = st.secrets.get("ADMIN_EMAIL", "")
    admin_password = st.secrets.get("ADMIN_PASSWORD", "")

    if (
        email.strip().lower() == admin_email.strip().lower()
        and password == admin_password
    ):
        st.session_state["admin_logged_in"] = True
        return True

    return False


# =========================
# ADMIN CHECK
# =========================

def is_admin():
    return st.session_state.get("admin_logged_in", False)


# =========================
# LOGOUT
# =========================

def sign_out():

    try:
        supabase = get_supabase()
        supabase.auth.sign_out()
    except Exception:
        pass

    st.session_state.pop("user", None)
    st.session_state.pop("session", None)
    st.session_state.pop("admin_logged_in", None)