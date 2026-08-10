import streamlit as st
import plotly.express as px


st.title("📈 Data Visualization")

st.write(
    "Create interactive charts from your dataset."
)


# Check dataset
if "df" not in st.session_state:

    st.warning(
        "⚠️ Please upload a dataset first."
    )

    st.stop()


df = st.session_state["df"]


st.success(
    f"Visualizing: {st.session_state.get('file_name', 'Dataset')}"
)


# =========================================================
# SELECT COLUMNS
# =========================================================

columns = df.columns.tolist()


st.header("⚙️ Chart Settings")


chart_type = st.selectbox(
    "Select Chart Type",
    [
        "Bar Chart",
        "Line Chart",
        "Scatter Plot",
        "Histogram",
        "Box Plot",
        "Pie Chart"
    ]
)


# =========================================================
# BAR / LINE / SCATTER
# =========================================================

if chart_type in [
    "Bar Chart",
    "Line Chart",
    "Scatter Plot"
]:

    col1, col2 = st.columns(2)

    with col1:

        x_column = st.selectbox(
            "Select X-axis",
            columns
        )

    with col2:

        y_column = st.selectbox(
            "Select Y-axis",
            columns
        )


    if chart_type == "Bar Chart":

        fig = px.bar(
            df,
            x=x_column,
            y=y_column,
            title=f"{y_column} by {x_column}"
        )


    elif chart_type == "Line Chart":

        fig = px.line(
            df,
            x=x_column,
            y=y_column,
            markers=True,
            title=f"{y_column} over {x_column}"
        )


    else:

        fig = px.scatter(
            df,
            x=x_column,
            y=y_column,
            title=f"{y_column} vs {x_column}"
        )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# HISTOGRAM
# =========================================================

elif chart_type == "Histogram":

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()


    if not numeric_columns:

        st.warning(
            "No numeric columns available."
        )

    else:

        column = st.selectbox(
            "Select Column",
            numeric_columns
        )


        fig = px.histogram(
            df,
            x=column,
            title=f"Distribution of {column}"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# BOX PLOT
# =========================================================

elif chart_type == "Box Plot":

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()


    if not numeric_columns:

        st.warning(
            "No numeric columns available."
        )

    else:

        column = st.selectbox(
            "Select Column",
            numeric_columns
        )


        fig = px.box(
            df,
            y=column,
            title=f"Box Plot of {column}"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# PIE CHART
# =========================================================

elif chart_type == "Pie Chart":

    col1, col2 = st.columns(2)


    with col1:

        category_column = st.selectbox(
            "Select Category",
            columns
        )


    with col2:

        value_column = st.selectbox(
            "Select Value",
            columns
        )


    try:

        fig = px.pie(
            df,
            names=category_column,
            values=value_column,
            title=f"{value_column} by {category_column}"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception:

        st.error(
            "Pie charts require a suitable categorical "
            "column and numeric value column."
        )