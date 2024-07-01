import streamlit as st

# Adding Title
st.write("Title : ")
st.title("Streamlit App")
st.write("--------------------------------------------------")

# Adding Button
st.write("Button : ")
if st.button("Click Me"):
    st.write("Button Clicked")
st.write("--------------------------------------------------")

# Adding Slider
st.write("Slider : ")
slider_value = st.slider("Select Value", min_value=0, max_value=100, value=50)
st.write('Selected value:', slider_value)
st.write("--------------------------------------------------")

# Adding Image
st.write("Image With Caption : ")
st.image("mountain.jpeg", caption="This Is a Mountain")