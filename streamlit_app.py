import time

import streamlit as st

st.set_page_config(page_title="SLOW reruns")

st.title("SLOW Streamlit reruns")
st.markdown("[Fast reruns here](https://share.streamlit.io/tconkling/streamlitfastrerundemo/FastReruns)")

selected_page = st.radio("Page", ["Foo", "Bar", "Baz"])

with st.spinner(f"Computing {selected_page}..."):
    time.sleep(5)

st.write(f"{selected_page}: done!")
