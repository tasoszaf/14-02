import streamlit as st

st.set_page_config(page_title="Be My Valentine 💖", page_icon="❤️", layout="centered")

st.markdown("<h1 style='text-align: center; color: pink;'>Annie tzavella, will you be my Valentine? 💌</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose wisely...</p>", unsafe_allow_html=True)

# Κεντραρισμένο κουμπί Yes
yes_clicked = st.button("Yes 💖")

if yes_clicked:
    st.success("Yay! It's a date! 💕")
    # Εμφάνιση φωτογραφίας
    st.image("success.jpg")

# Κουμπί No απενεργοποιημένο
st.button("No ❌", disabled=True)

# Ροζ φόντο
st.markdown("""
<style>
body { background-color: #ffe6f0; }
</style>
""", unsafe_allow_html=True)
