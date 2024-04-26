from openai import OpenAI
import streamlit as st
from streamlit_star_rating import st_star_rating
# import fontawesome as fa


def function_on_click(value, index):
    if index is not None:
        st.session_state.feedback_list[index] = value
        print(st.session_state.feedback_list)
    else:
        st.session_state.feedback_list.append(value)

# st.image('/home/vinic/projetos/teste_streamlit/HFW_1920X1080.jpg', width=500)
with st.columns(4)[1]:
    st.image('/home/vinic/projetos/teste_streamlit/c-vale-logo-93F0C0E232-seeklogo.com.png', width=350)

st.title("ChatGPT-like clone")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if 'feedback_list' not in st.session_state:
    st.session_state.feedback_list = []

index_feedback = 0
for message in st.session_state.messages:
    if message['role'] == 'user':
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    else:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
            st_star_rating(
            'Avalie minha resposta:',
            maxValue=5,
            defaultValue=st.session_state.feedback_list[index_feedback],
            size=20,
            key=f'rating{index_feedback}',
            customCSS='h3 {font-size: 1rem;}',
            on_click=function_on_click,
            on_click_kwargs={'index': index_feedback}
        )
            # st.write(f'nota: {st.session_state.feedback_list[index_feedback]}')
        index_feedback+=1


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner('Pensando...'):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)

            # Criando a interface de feedback
            user_feedback = st_star_rating(
                'Avalie minha resposta:',
                maxValue=5,
                defaultValue=5,
                size=20,
                key=f'rating{len(st.session_state.feedback_list)}',
                customCSS='h3 {font-size: 1rem;}',
                on_click=function_on_click,
                on_click_kwargs={'index': None}
            )

    # Armazenando o feedback na lista
    st.session_state.feedback_list.append(user_feedback)

    # armazenando mensagens
    st.session_state.messages.append({"role": "assistant", "content": response})

    print(st.session_state.messages)
    print()
    print(st.session_state.feedback_list)
