import streamlit as st

st.set_page_config(page_title="Be My Valentine 💖", page_icon="❤️", layout="centered")

st.markdown("<h1 style='text-align: center; color: pink;'>Annie Tzavella will you be my Valentine? 💌</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose wisely...</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Yes 💖"):
        st.success("Yay! 💕")
        st.markdown("<h2 style='color: red;'>I ❤️ you!</h2>", unsafe_allow_html=True)

        # Καρδούλες animation με HTML+CSS
        st.markdown("""
        <style>
        .heart {
            position: fixed;
            width: 30px;
            height: 30px;
            background: red;
            transform: rotate(-45deg);
            animation: floatUp 3s linear forwards;
        }
        .heart:before,
        .heart:after {
            content: "";
            position: absolute;
            width: 30px;
            height: 30px;
            background: red;
            border-radius: 50%;
        }
        .heart:before {
            top: -15px;
            left: 0;
        }
        .heart:after {
            left: 15px;
            top: 0;
        }
        @keyframes floatUp {
            0% {transform: translateY(0) rotate(-45deg); opacity:1;}
            100% {transform: translateY(-400px) rotate(-45deg); opacity:0;}
        }
        </style>
        <script>
        for(let i=0;i<20;i++){
            let heart = document.createElement("div");
            heart.className = "heart";
            heart.style.left = Math.random() * window.innerWidth + "px";
            heart.style.animationDuration = 2 + Math.random()*2 + "s";
            document.body.appendChild(heart);
            setTimeout(()=>heart.remove(), 4000);
        }
        </script>
        """, unsafe_allow_html=True)

with col2:
    st.button("No ❌", disabled=True)

st.markdown("""
<style>
body {
    background-color: #ffe6f0;
}
</style>
""", unsafe_allow_html=True)
