import time

import streamlit as st

st.title("FAST Streamlit reruns!")

selected_page = st.radio("Page", ["Foo", "Bar", "Baz"])

with st.spinner(f"Computing {selected_page}..."):
    time.sleep(5)

st.write(f"{selected_page}: done!")
