import os
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["API_KEY"]


st.title("Business Profiler")

st.write("Enter a company that you would like to learn about.")


companyName = st.text_input("Company Name:", "Allstate")


st.write("")
st.write("We can add more configuration options but I won't use them in the return statement for this demo.")

dept = st.selectbox("Select a department:", ('Finance', 'Marketing', 'IT'))
brief = st.checkbox("Brief Version")
usecaseMax = st.slider("Maximum number of use cases", 0, 10, 3)



if st.button('Generate profile'):
    describePrompt = "Briefly Describe the company : " + companyName + " and what they do."
    result = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sales manager just looking for high level information."},
            {"role": "user", "content": describePrompt}
        ],
        max_tokens=4096,
        temperature=0.2)
    response = result.choices[0].message.content
    st.divider()
    st.markdown("**What does " + companyName + " do?**")
    st.markdown(response)

    st.divider()
    revenuePrompt = "Describe how the company : " + companyName + "makes money."
    result = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data scientist trying to explain your value."},
            {"role": "user", "content": revenuePrompt}
        ],
        max_tokens=4096,
        temperature=0.2)
    response = result.choices[0].message.content
    st.markdown("**How does the company make money?**")
    st.markdown(response)

    st.divider()
    usecasePrompt = "Write a list of use cases that are important to the company, : " + companyName + ". The use cases must include data science with intensive prep and blend."
    result = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a data scientist trying to explain your value."},
                {"role": "user", "content": usecasePrompt}
            ],
            max_tokens=4096,
            temperature=0.2)
    response = result.choices[0].message.content
    st.markdown("**What are some important use cases?**")
    st.markdown(response)

    st.divider()
    performancePrompt = "Write a list of ways Alteryx can help improve the business performance of : " + companyName + "."
    result = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a sales manager trying to explain your value."},
                {"role": "user", "content": performancePrompt}
            ],
            max_tokens=4096,
            temperature=0.2)
    response = result.choices[0].message.content
    st.markdown("**How can Alteryx help improve their business performance?**")
    st.markdown(response)
