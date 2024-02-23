import streamlit as st
from st_audiorec import st_audiorec
from xtts_korean import *
from gpt import *
from stt import *

import os

st.set_page_config(
    page_title='rvc'
)

st.title("GPT-3 TTS(mallang service)")
st.markdown("---")
st.write("이 페이지는 말랑의 tts 질문 서비스입니다.")
st.markdown("---")

st.header("음성으로 질문하기")
st.write("질문하고 싶은 내용을 음성으로 녹음해주세요.")

#openai API 키 인증
OPENAI_API_KEY = "api_key"

wav_audio_data = st_audiorec()
if wav_audio_data is not None:
    with open('./wavs/gpt_input.wav', 'wb') as f:
            f.write(wav_audio_data)
    query = my_stt('./wavs/gpt_input.wav')
    query = query['alternative'][0]['transcript']
    st.write(query)
else:
    st.write("음성 파일을 입력해주세요.")

button = st.button("질문하기")

if button and wav_audio_data is not None:
    with st.spinner('답변 생성중...'):
        st.markdown("---")
        response = gpt3(query, OPENAI_API_KEY)
        st.markdown(response)
        tts(text=response, audio="./wavs/gpt_input.wav", ouput="./wavs/gpt_output.wav")
    # 답변 생성
        st.audio("./wavs/gpt_output.wav", format='audio/wav')

