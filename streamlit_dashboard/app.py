mport streamlit as st
import pandas as pd

st.set_page_config(page_title="US Credit Fairness Audit", layout="wide")

st.title("Credit Fairness Audit for US Applicants")
uploaded_file = st.file_uploader(" Upload your US applicant CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data Preview")
    st.dataframe(df.head())

    st.subheader("Bias Audit Summary")

    if "gender" in df.columns:
        st.markdown("### Gender Distribution")
        gender_counts = df["gender"].value_counts()
        st.bar_chart(gender_counts)

    if "ethnicity" in df.columns:
        st.markdown("### Ethnicity Distribution")
        ethnicity_counts = df["ethnicity"].value_counts()
        st.bar_chart(ethnicity_counts)

    if "credit_score" in df.columns:
        st.markdown("### Credit Score Distribution")
        st.line_chart(df["credit_score"])
else:
    st.info(" Please upload a valid CSV file to begin the bias audit.")
