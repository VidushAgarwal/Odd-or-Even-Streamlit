import streamlit as st

st.title('odd or even')
a = st.number_input('Enter a number')
if (x).is_integer():
    if a%2==0:
        result = "even"
    else:
        result = "odd"
    st.write(a, '= ', result)
else:st.write("please enter integer number")
