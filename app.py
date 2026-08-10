import streamlit as st


st.set_page_config(
    page_title="AI Data Detective",
    page_icon="🔎",
    layout="wide"
)


pages = {
    "AI Data Detective": [
        st.Page(
            "pages/0_Home.py",
            title="Home",
            icon="🏠"
        ),
        st.Page(
            "pages/1_Upload_Data.py",
            title="Upload Data",
            icon="📤"
        ),
        st.Page(
            "pages/2_Data_Analysis.py",
            title="Data Analysis",
            icon="📊"
        ),
        st.Page(
            "pages/3_Data_Visualization.py",
            title="Data Visualization",
            icon="📈"
        ),
        st.Page(
            "pages/4_AI_Insights.py",
            title="AI Insights",
            icon="🤖"
        ),
        st.Page(
             "pages/5_Machine_Learning.py",
            title="Machine Learning",
            icon="🧠"
        ),
        st.Page(
            "pages/6_Report_Download.py",
            title="Report Download",
            icon="📄"
        ),
    ]
}


pg = st.navigation(pages)

pg.run()