# import streamlit as st

# st.title("Chai Maker App")

# if st.button("Make Chai"):
#     st.success("Your chai is being brewed")

# add_masala = st.checkbox("Add Masala")

# if add_masala:
#     st.write("Masala added to your chai")

# tea_type = st.radio("Pick your chai base: ", ["Milk", "Water", "Almond Milk"])
# st.write(f"Selected base {tea_type}")
# flavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])
# st.write(f"Selected Flavour {flavour}")

# sugar = st.slider("Sugar level (spoon)", 0, 5, 4)
# st.write(f"Selected sugar level {sugar}")

# cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
# st.write(f"Selected sugar level {cups}")

# name = st.text_input("Enter your name")
# if name:
#     st.write(f"Welcome, {name} ! Your chai is on the way")

# dob = st.date_input("Select your date of birth")
# st.write(f"Your date of birth {dob}")

import streamlit as st
from datetime import date

st.set_page_config(page_title="Chai Maker", page_icon="☕", layout="centered")

st.markdown("<h1 style='text-align: center; color: brown;'>☕ Chai Maker App</h1>", unsafe_allow_html=True)
st.markdown("### 🫖 Customize your perfect cup of chai:")

st.image("https://www.healthshots.com/wp-content/uploads/2020/09/green-tea-superfood.jpg", caption="Freshly Brewed Chai", use_container_width=True)

# Start brewing button
if st.button("👉 Make Chai"):
    st.success("🫖 Your chai is being brewed with love!")

# Layout: Two columns for options
col1, col2 = st.columns(2)

with col1:
    add_masala = st.checkbox("🧂 Add Masala")
    if add_masala:
        st.info("Masala added! Spicy and flavorful!")

    tea_type = st.radio("🧋 Choose your chai base:", ["Milk", "Water", "Almond Milk"])
    st.write(f"✅ Base selected: **{tea_type}**")

    flavour = st.selectbox("🌿 Choose flavour:", ["Adrak (Ginger)", "Kesar (Saffron)", "Tulsi (Basil)"])
    st.write(f"✅ Flavour selected: **{flavour}**")

with col2:
    sugar = st.slider("🍬 Sugar level (spoons)", 0, 5, 2)
    st.write(f"✅ Sugar level: **{sugar} spoons**")

    cups = st.number_input("🍵 How many cups?", min_value=1, max_value=10, step=1)
    st.write(f"✅ Cups: **{cups}**")

    name = st.text_input("📝 Enter your name")
    if name:
        st.success(f"Welcome, **{name}**! Your chai will be ready shortly ☺️")

    dob = st.date_input("📅 Select your date of birth", min_value=date(1940, 1, 1), max_value=date.today())
    st.write(f"📍 Your date of birth: **{dob.strftime('%d %B, %Y')}**")

# Final message
st.markdown("---")
st.markdown("### 💖 Thank you for using Chai Maker App!")
st.markdown("Enjoy your perfect cup of chai ☕🫶")
