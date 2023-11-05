import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import base64

# Web App Title
st.markdown('''
# **The EDA App**

This is the **EDA App** created in Streamlit using the **pandas-profiling** library.

**Credit:** App built in `Python` + `Streamlit` by Parag Sakhare

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file]
""")

download_button = None  # Initialize download button variable

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv

    df = load_csv()
    pr = ProfileReport(df, explorative=True)

    # Add a button to download the report
    html_report = pr.to_html()
    b64 = base64.b64encode(html_report.encode()).decode()
    download_button = f'<a href="data:text/html;base64,{b64}" download="pandas_profiling_report.html">Download Report</a>'

    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a

        df = load_data()
        pr = ProfileReport(df, explorative=True)

        # Add a button to download the report
        html_report = pr.to_html()
        b64 = base64.b64encode(html_report.encode()).decode()
        download_button = f'<a href="data:text/html;base64,{b64}" download="pandas_profiling_report.html">Download Report</a>'

        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)

# Display the download button
if download_button:
    st.markdown(download_button, unsafe_allow_html=True)
