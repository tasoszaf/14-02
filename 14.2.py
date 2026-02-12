import streamlit as st

# Ρυθμίσεις σελίδας
st.set_page_config(page_title="Be My Valentine 💖", page_icon="❤️", layout="centered")

# Τίτλος και οδηγίες
st.markdown("<h1 style='text-align: center; color: pink;'>Annie tzavella will you be my Valentine? 💌</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose wisely...</p>", unsafe_allow_html=True)

# Κουμπιά κεντραρισμένα
st.markdown("""
<div style='text-align: center; margin-top: 30px;'>
    <form>
        <input type="submit" value="Yes 💖" style="padding: 10px 30px; font-size: 18px; margin-right: 20px;" onclick="window.parent.postMessage({funcName:'yes_clicked'}, '*')">
        <input type="submit" value="No ❌" style="padding: 10px 30px; font-size: 18px;" disabled>
    </form>
</div>
""", unsafe_allow_html=True)

# Streamlit διαχείριση του Yes κουμπιού
yes_clicked = st.button("Yes 💖")
if yes_clicked:
    st.success("Yay! It's a date! 💕")
    st.markdown("<h2 style='color: red;'>I ❤️ you!</h2>", unsafe_allow_html=True)


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
