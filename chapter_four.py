# import streamlit as st
# import pandas as pd

# st.title("Chai Sales Dashboard")
# file=st.file_uploader("Upload a CSV file", type=["csv"] )

# if file:
#     df=pd.read_csv(file)
#     st.subheader("Data Preview")
#     # st.write(df.head())
#     st.dataframe(df)
#     st.write("File uploaded successfully!")

import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Chai Sales Dashboard", page_icon="📊", layout="wide")

# Title & Header
st.markdown("<h1 style='text-align: center; color: brown;'>📊 Chai Sales Dashboard</h1>", unsafe_allow_html=True)
st.markdown("### Upload your chai sales CSV file to analyze the data:")

# File Upload
file = st.file_uploader("📁 Choose a CSV file", type=["csv"])

# If file is uploaded
if file is not None:
    try:
        df = pd.read_csv(file)

        st.success("✅ File uploaded and loaded successfully!")
        
        
        # Display preview
        st.subheader("🔍 Data Preview")
        st.dataframe(df, use_container_width=True)

        # Display summary
        st.markdown("---")
        st.subheader("📈 Dataset Overview")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Rows", df.shape[0])
        with col2:
            st.metric("Columns", df.shape[1])
        with col3:
            st.metric("Column Names", ", ".join(df.columns.tolist()))

        
        name=df["Name"].unique()
        select_name=st.selectbox("Select a Name", name)
        filter_df=df[df["Name"]==select_name]
        st.dataframe(filter_df, use_container_width=True)
        # Optional: Show data types
        with st.expander("🧠 View Column Data Types"):
            st.write(df.dtypes)

        # Optional: Describe data
        with st.expander("📊 View Summary Statistics"):
            st.write(df.describe(include='all'))

    except Exception as e:
        st.error(f"❌ Error loading file: {e}")

else:
    st.warning("📂 Please upload a CSV file to view the dashboard.")
