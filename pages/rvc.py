import streamlit as st
from st_audiorec import st_audiorec

############################RVC DEMO##########################
st.set_page_config(
    page_title='rvc'
)
# from VoiceConversion import getParameter, get_vc, vc_single, get_tgt_sr #RVC inference module
# from scipy.io import wavfile
import requests

# def inference(characterId,userAge,userGender):
#     f0up_key,input_path,index_path,f0method,model_path,index_rate,filter_radius,resample_sr,rms_mix_rate,protect = getParameter(characterId,userAge,userGender)
#     #get model by model path
#     get_vc(model_path)
#     #inference
#     opt_wav=vc_single(0,input_path,f0up_key,None,f0method,index_path,index_rate,filter_radius,resample_sr,rms_mix_rate,protect)
#     wavfile.write("/wavs/vc_output.wav",get_tgt_sr(),opt_wav)

url = 'url'
# url = 'http://127.0.0.1:5000'

# male = 1
# female = 0

st.title("Voice Conversion Demo(mallang service)")
st.markdown("---")
st.write("이 페이지는 말랑의 캐릭터 음성변환 체험 서비스입니다.")
st.markdown("---")


st.header("음성 녹음 또는 파일 업로드")
st.write("바꾸고 싶은 목소리의 오디오 파일을 업로드해주세요.")
file_upload = st.checkbox("오디오 파일 업로드(mp3, wav)")
if not file_upload :
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        with st.spinner('녹음된 음성을 저장중...'):
            with open('wavs/user.wav', 'wb') as f:
                    f.write(wav_audio_data)
else:
    wav_audio_data = st.file_uploader("Upload audio", type=['wav'])
    if wav_audio_data is not None:
        st.audio(wav_audio_data, format='audio/wav')
        # 오디오 저장
        with st.spinner('업로드된 음성을 저장중...'):
            with open('wavs/user.wav', 'wb') as f:
                f.write(wav_audio_data.read())

st.header("본인 정보 입력 및 캐릭터 선택")
gender_list = ['남자', '여']
selected_gender = st.selectbox("성별을 선택해 주세요", gender_list)
if selected_gender == '남자': gender = 1
elif selected_gender == '여자': gender = 0
else:
    print("성별 선택이 잘못되었습니다.")

st.write("나이를 입력해주세요")
age = st.slider("age", value=5, min_value=0, max_value=100, step=1)

character_list = ['rabbit', 'turtle']
character_name = st.selectbox("바꾸고 싶은 캐릭터를 입력해주세요", character_list)

def upload_file():
    files = {'wav': open('wavs/user.wav', 'rb')}
    data = {'CharacterId': character_name, 
            'gender': gender, 
            'age': age}
    response = requests.post(f'{url}/upload', files=files, data=data)
    print(response.text)

def download_file():
    response = requests.get(f'{url}/download')
    with open(f'wavs/userTo{character_name}.wav', 'wb') as file:
        file.write(response.content)

if st.button("변환"):
    if wav_audio_data is not None and gender is not None and character_name is not None and age is not None:
        with st.spinner('음성 변환중...'):
            upload_file()
            download_file()
            st.audio(f'wavs/userTo{character_name}.wav', format='audio/wav')
        st.success('완료')
    else:
        st.write("음성 파일과 텍스트를 모두 입력해주세요.")

