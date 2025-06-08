import streamlit as st
from css_utils import inject_custom_css
from dotenv import load_dotenv
from llm_utils import query_agent, load_dataframe
import pandas as pd

load_dotenv()

st.set_page_config(page_title="CSV Data Analyzer", layout="centered")

# Cleaner header with CSS classes instead of inline styles
st.markdown("""
    <h1>CSV Data Analyzer</h1>
    <p class="subtitle">
        Upload your CSV file below and explore insights by asking questions about your data.
    </p>
""", unsafe_allow_html=True)

data = st.file_uploader(
    label="Upload your CSV file here:",
    type="csv",
    help="Only CSV files are supported."
)

if data:
    with st.spinner("Loading your data..."):
        df = load_dataframe(data)
        st.success("✅ CSV loaded successfully!")

    with st.expander("Preview of uploaded data"):
        st.dataframe(df.head(), use_container_width=True)

    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if numeric_cols:
        with st.expander("Visualizations"):
            chart_type = st.selectbox(
                "Select chart type",
                options=["Bar Chart", "Line Chart", "Area Chart"]
            )
            selected_columns = st.multiselect(
                "Select numeric columns to plot",
                options=numeric_cols,
                default=numeric_cols
            )
            if selected_columns:
                chart_data = df[selected_columns].head(10)
                if chart_type == "Bar Chart":
                    st.bar_chart(chart_data)
                elif chart_type == "Line Chart":
                    st.line_chart(chart_data)
                elif chart_type == "Area Chart":
                    st.area_chart(chart_data)
            else:
                st.warning("Please select at least one column to plot.")
    else:
        st.info("No numeric columns found in the CSV to plot charts.")

    st.markdown("<h3>Ask a question about your data</h3>", unsafe_allow_html=True)

    query = st.text_area(
        label="Enter your query here",
        height=120,
        placeholder="E.g., What is the average sales amount?"
    )

    if st.button("Generate Response", help="Click to get analysis"):
        if not query.strip():
            st.warning("Please enter a question before generating a response.")
        else:
            with st.spinner("Analyzing your query..."):
                response = query_agent(df, query)
            st.markdown("<h4>Response:</h4>", unsafe_allow_html=True)
            st.write(response)
else:
    st.info("Please upload a CSV file to start the analysis.")

# Inject CSS (now with just the background since header is color-based)
# At the end of your app.py:
inject_custom_css(
    bg_image_path="assets/background.png",  # Your actual image path
    css_path="style.css"
)