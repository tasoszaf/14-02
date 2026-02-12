import streamlit as st

st.set_page_config(page_title="Be My Valentine 💖", page_icon="❤️", layout="centered")

st.title("Will you be my Valentine? 💌")
st.write("Please choose wisely...")

col1, col2 = st.columns(2)

with col1:
    if st.button("Yes"):
        st.success("Yay! 💖 You made me so happy!")

with col2:
    # Κουμπί "Όχι" απενεργοποιημένο
    st.button("No", disabled=True)
    st.write("you are officialy my date")  
