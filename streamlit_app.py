import time

import streamlit as st

st.title("SLOW Streamlit reruns")

selected_page = st.radio("Page", ["Foo", "Bar", "Baz"])

for ii in range(5):
    with st.spinner(f"Computing {selected_page} (Step {ii + 1}/{5})..."):
        time.sleep(5)

st.write(f"{selected_page}: done!")
