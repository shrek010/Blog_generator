import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers 


#Retrieve llama model response

def get_llama_response(input, num_words, blog_style):
    llm = CTransformers(model = "model/llama-2-7b-chat.Q8_0.gguf",
                        model_type = "llama",
                        config = {"max_new_tokens":256,
                                  "temperature":0.01})
    
    ##Prompt Template 
    template = """
                write a blog for {blog_style} for topic {input} within {num_words} words. Dont start a sentence in the end which wont be completed¸
               """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input", "num_words"],
                            template=template)
    
    
    #Generate response from LLama2 model
    response = llm(prompt.format(blog_style=blog_style, input=input, num_words=num_words))
    print(response)
    return response 

st.set_page_config(page_title="Blogger",
                   page_icon="🧊",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate blogs 🤖")

input_text = st.text_input("Enter a topic")

#Creating two columns for additional two fields

col1, col2 = st.columns([5,5])

with col1:
    num_words = st.text_input("Enter the number of words you'd want")

with  col2:
    blog_style = st.selectbox("This blog is for", 
                              ("Researchers", "Data Scientist", "Common People"), index=0)
    
submit_button = st.button("Generate")


##Final response

if submit_button:
    st.write(get_llama_response(input_text, num_words, blog_style))
    