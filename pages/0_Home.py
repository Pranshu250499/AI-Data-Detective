import streamlit as st


st.title("🔎 AI Data Detective")

st.subheader(
    "Your Intelligent Data Analysis Assistant"
)


st.write(
    """
    Upload your dataset and let AI Data Detective
    help you clean, analyze, visualize and understand
    your data.
    """
)


st.success(
    "AI Data Detective is ready!"
)


st.divider()


st.header("🚀 What can you do?")


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("📤 Upload Data")

    st.write(
        "Upload CSV or Excel datasets."
    )


with col2:

    st.subheader("📊 Analyze Data")

    st.write(
        "Find missing values, duplicates and statistics."
    )


with col3:

    st.subheader("📈 Visualize Data")

    st.write(
        "Create interactive charts and graphs."
    )