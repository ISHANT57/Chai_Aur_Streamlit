import streamlit as st
# import chai_streamlit as cs


st.title("My First Streamlit App")
st.subheader("This is a subheader")
st.text("Welcome to my first Streamlit App")
st.write("Choose your favorite chai variety")
st.markdown("☕ **Enjoy your steaming cup of chai!** 🍵")
st.image("https://www.healthshots.com/wp-content/uploads/2020/09/green-tea-superfood-600x340.jpg", caption="Masala Chai", width=300)

sugar = st.slider("Sugar level (teaspoons)", 0, 5, 2)
milk = st.radio("Add milk?", ["Yes", "No"])

chai=st.selectbox(
    "Choose your favorite chai variety",
    ["Masala Chai", "Lemon Chai", "Kulfi Chai", "Ginger Chai", "Cardamom Chai"]
)

if chai:
    st.write(f"You selected: **{chai}**. EXCELLENT CHOICE!")

st.success("your chai has been prepared")