import streamlit as st

# Ρυθμίσεις σελίδας
st.set_page_config(page_title="Be My Valentine 💖", page_icon="❤️", layout="centered")

# Τίτλος και οδηγίες
st.markdown("<h1 style='text-align: center; color: pink;'>Annie Tzavella Will you be my Valentine? 💌</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose wisely...</p>", unsafe_allow_html=True)

# Δημιουργία δύο στηλών για τα κουμπιά
col1, col2 = st.columns(2)

with col1:
    if st.button("Yes 💖"):
        st.balloons()  # Confetti effect
        st.success("Yay! You made me so happy! 💕")
        st.markdown("<h2 style='color: red;'>I ❤️ you!</h2>", unsafe_allow_html=True)

with col2:
    st.button("No ❌", disabled=True)  # Απενεργοποιημένο κουμπί

# Προσθέτουμε λίγο στυλ για πιο cute εμφάνιση
st.markdown(
    """
    <style>
    body {
        background-color: #ffe6f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
