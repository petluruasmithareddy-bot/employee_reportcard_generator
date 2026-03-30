import random
import string
import streamlit as st


# Function
def password_generator(length, use_letters, use_digits, use_symbols, use_upper, use_lower):
    characters = ""

    # Add character types based on user choice
    if use_letters:
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    # If nothing selected
    if characters == "":
        return "⚠️ Please select at least one option!"

    # Generate password
    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


# UI
st.title("🔐 Password Generator")

length = st.number_input("Enter password length", min_value=4)

st.subheader("Customize your password")

# Options
use_letters = st.checkbox(f"Include Letters")
use_upper = st.checkbox(f"Include Uppercase (A-Z)")
use_lower = st.checkbox(f"Include Lowercase (a-z)")
use_digits = st.checkbox(f"Include Digits (0-9)")
use_symbols = st.checkbox(f"Include Symbols (!@#)")

# Generate button
if st.button("Generate Password"):
    result = password_generator(length, use_letters, use_digits, use_symbols, use_upper, use_lower)
    st.success(f"Generated Password: {result}")