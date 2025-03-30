import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter By Jabbar Jatoi", layout="Centered")

st.title("🔐 Password Strength Meter By Jabbar Jatoi")
st.write("Enter your password below to check its security level")

#Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be **atleast 8 character long**,")

    if re.search(r"[A-Z]", password) and re.search(f"[a-z]", password):
        score += 1
    else:
        feedback.append(" Password should include **Both uppercase (A-Z) and lowercase (a-z) letters**,")                   

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append(" Password should include **atleast one number (0-9)**,")
    
    if re.search(r"[!@#$%&*]", password):
        score += 1
        feedback.append(" Password should include **special character (!@#$%&*)**,")
    
    # Display Passsword stength
    if score == 4:
        st.success(" **Strong Password** Your Password is Secure,")

    elif score == 3:
        st.info(" **Moderate Password** - Consider improving security by adding more feature")
    else:
        st.error(" **Week Password** - Follow the Suggestion below to strength it.")
    
    if feedback:
        with st.expander(" **Improve your Password** "):
            for item in feedback:
                st.write(item)
    password = st.text_input("Enter your password.", type="password", help="Ensure your password is strong")

    if st.button("Check Strength"):
        if password:
            check_password_strength(password)
    else:
        st.warning("Please Enter a Password First!") 
            
        
