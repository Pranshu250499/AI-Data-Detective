
import streamlit as st
from pathlib import Path
from datetime import datetime

from utils.auth import get_admin_supabase, is_admin, sign_out


# ============================================================
# ACCESS CONTROL
# ============================================================

if not is_admin():
    st.error("Admin access required.")
    st.stop()


# ============================================================
# PAGE STYLE
# ============================================================

st.markdown("""
<style>

.admin-hero {
    padding: 32px;
    border-radius: 22px;
    border: 1px solid rgba(56,189,248,.35);
    background:
        radial-gradient(circle at 85% 20%, rgba(34,211,238,.12), transparent 35%),
        linear-gradient(135deg, rgba(15,23,42,.98), rgba(8,18,35,.98));
    box-shadow:
        0 0 35px rgba(14,165,233,.10),
        inset 0 0 30px rgba(56,189,248,.03);
    margin-bottom: 24px;
}

.admin-title {
    font-size: 34px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 6px;
}

.admin-subtitle {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 16px;
}

.admin-badge {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    border: 1px solid rgba(34,211,238,.30);
    background: rgba(34,211,238,.08);
    color: #67e8f9;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .08em;
}

.stat-card {
    padding: 22px;
    min-height: 135px;
    border-radius: 18px;
    border: 1px solid rgba(59,130,246,.25);
    background: rgba(15,23,42,.90);
    transition: .25s ease;
}

.stat-card:hover {
    transform: translateY(-4px);
    border-color: rgba(34,211,238,.55);
    box-shadow: 0 0 25px rgba(34,211,238,.12);
}

.stat-icon {
    font-size: 25px;
    margin-bottom: 10px;
}

.stat-value {
    font-size: 28px;
    font-weight: 800;
    color: #f8fafc;
}

.stat-label {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 8px;
}

.section-box {
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(59,130,246,.22);
    background: rgba(15,23,42,.70);
    margin-top: 10px;
    margin-bottom: 20px;
}

.status-ok {
    padding: 14px 16px;
    border-radius: 12px;
    background: rgba(34,197,94,.08);
    border: 1px solid rgba(34,197,94,.25);
    color: #86efac;
}

.status-warning {
    padding: 14px 16px;
    border-radius: 12px;
    background: rgba(245,158,11,.10);
    border: 1px solid rgba(245,158,11,.25);
    color: #fbbf24;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="admin-hero">
    <div class="admin-title">Admin Control Center</div>
    <div class="admin-subtitle">
        AI Data Detective - System Administration Dashboard
    </div>
    <div class="admin-badge">
        ADMINISTRATOR ACCESS - SYSTEM ONLINE
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SUPABASE CONNECTION
# ============================================================

admin_supabase = None
users = []
connection_error = None

try:
    admin_supabase = get_admin_supabase()
    response = admin_supabase.auth.admin.list_users()

    if hasattr(response, "users"):
        users = response.users or []
    elif isinstance(response, dict):
        users = response.get("users", []) or []

except Exception as e:
    connection_error = str(e)


# ============================================================
# USER COUNTS
# ============================================================

registered_count = len(users)

verified_count = 0

for user in users:
    confirmed = getattr(user, "email_confirmed_at", None)
    if confirmed:
        verified_count += 1

unverified_count = registered_count - verified_count


# ============================================================
# STAT CARDS
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-icon">&#128101;</div>
        <div class="stat-value">{registered_count}</div>
        <div class="stat-label">Registered Users</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-icon">&#9989;</div>
        <div class="stat-value">{verified_count}</div>
        <div class="stat-label">Verified Users</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-icon">&#9203;</div>
        <div class="stat-value">{unverified_count}</div>
        <div class="stat-label">Unverified Users</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-icon">&#9679;</div>
        <div class="stat-value">ONLINE</div>
        <div class="stat-label">System Status</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# REFRESH
# ============================================================

st.write("")

if st.button("Refresh Dashboard", use_container_width=False):
    st.rerun()

st.caption(
    "Last refresh: " +
    datetime.now().strftime("%d %b %Y ? %I:%M:%S %p")
)


# ============================================================
# TABS
# ============================================================

tab_users, tab_analytics, tab_data, tab_system = st.tabs(
    [
        "Users",
        "Analytics",
        "Data Operations",
        "System"
    ]
)


# ============================================================
# USERS
# ============================================================

with tab_users:

    st.subheader("User Management")

    if connection_error:

        st.markdown(
            '<div class="status-warning">'
            'Unable to load Supabase users.<br><br>'
            '<b>Check SUPABASE_SECRET_KEY in Streamlit secrets.</b>'
            '</div>',
            unsafe_allow_html=True
        )

        with st.expander("Technical details"):
            st.code(connection_error)

    else:

        search = st.text_input(
            "Search users",
            placeholder="Search by email or user ID..."
        )

        filtered_users = users

        if search.strip():
            query = search.strip().lower()

            filtered_users = [
                u for u in users
                if query in str(getattr(u, "email", "")).lower()
                or query in str(getattr(u, "id", "")).lower()
            ]

        st.write(
            f"Showing {len(filtered_users)} of {len(users)} users"
        )

        if not filtered_users:

            st.info("No users found.")

        else:

            for user in filtered_users:

                email = getattr(user, "email", "Unknown")
                user_id = getattr(user, "id", "Unknown")
                created = getattr(user, "created_at", None)
                confirmed = getattr(user, "email_confirmed_at", None)

                if confirmed:
                    status = "Verified"
                else:
                    status = "Unverified"

                with st.container(border=True):

                    left, middle, right = st.columns([4, 2, 1])

                    with left:
                        st.markdown(f"**{email}**")
                        st.caption(f"ID: {user_id}")

                    with middle:
                        st.write(status)
                        if created:
                            st.caption(
                                "Created: " +
                                str(created)[:19]
                            )

                    with right:

                        delete_key = (
                            "delete_user_" + str(user_id)
                        )

                        if st.button(
                            "Delete",
                            key=delete_key
                        ):

                            try:
                                admin_supabase.auth.admin.delete_user(
                                    str(user_id)
                                )

                                st.success(
                                    f"Deleted {email}"
                                )

                                st.rerun()

                            except Exception as e:

                                st.error(
                                    "Delete failed: " + str(e)
                                )


# ============================================================
# ANALYTICS
# ============================================================

with tab_analytics:

    st.subheader("User Analytics")

    a1, a2, a3 = st.columns(3)

    with a1:
        st.metric(
            "Total Users",
            registered_count
        )

    with a2:
        st.metric(
            "Verified",
            verified_count
        )

    with a3:
        st.metric(
            "Unverified",
            unverified_count
        )

    st.markdown(
        '<div class="section-box">'
        '<b>Verification Overview</b>'
        '</div>',
        unsafe_allow_html=True
    )

    if registered_count > 0:

        verification_rate = (
            verified_count / registered_count
        ) * 100

        st.progress(
            verification_rate / 100
        )

        st.write(
            f"Verification rate: {verification_rate:.1f}%"
        )

    else:

        st.info("No registered users available for analytics.")


# ============================================================
# DATA OPERATIONS
# ============================================================

with tab_data:

    st.subheader("Data Operations")

    project_root = Path(__file__).resolve().parent.parent

    folders = {
        "Uploads": project_root / "uploads",
        "Reports": project_root / "reports",
        "Data": project_root / "data"
    }

    d1, d2, d3 = st.columns(3)

    for column, (name, folder) in zip(
        [d1, d2, d3],
        folders.items()
    ):

        try:
            if folder.exists():
                files_count = len(
                    [
                        x for x in folder.iterdir()
                        if x.is_file()
                    ]
                )
            else:
                files_count = 0

        except Exception:
            files_count = 0

        with column:
            st.metric(
                name,
                files_count
            )

    st.markdown(
        '<div class="section-box">'
        '<b>Storage Information</b><br>'
        'These values represent files available in the local project directories.'
        '</div>',
        unsafe_allow_html=True
    )

    for name, folder in folders.items():

        exists = folder.exists()

        if exists:
            st.write(
                f"{name}: Available"
            )
        else:
            st.write(
                f"{name}: Directory not found"
            )


# ============================================================
# SYSTEM
# ============================================================

with tab_system:

    st.subheader("System Status")

    if connection_error:

        st.markdown(
            '<div class="status-warning">'
            'Supabase Admin API connection failed.'
            '</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<div class="status-ok">'
            'Supabase Admin API connected successfully.'
            '</div>',
            unsafe_allow_html=True
        )

    st.write("")

    python_version = __import__("sys").version.split()[0]

    s1, s2, s3 = st.columns(3)

    with s1:
        st.metric(
            "Python",
            python_version
        )

    with s2:
        st.metric(
            "Users API",
            "Connected" if not connection_error else "Error"
        )

    with s3:
        st.metric(
            "Admin Session",
            "Active"
        )


# ============================================================
# LOGOUT
# ============================================================

st.divider()

if st.button(
    "Admin Logout",
    use_container_width=True
):

    sign_out()
    st.rerun()
