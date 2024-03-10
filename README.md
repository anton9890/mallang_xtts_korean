# mallang 서비스에 활용한 xttx_korean demo
---

base model : xtts v2 (https://huggingface.co/coqui/XTTS-v2)

data : 감성 및 발화스타일 동시 고려 음성합성 데이터
(https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71349)

---
# Usage

```bash
pip install requirements.txt
streamlit run app.py
```

---
# streamlit 데모
![demo](https://github.com/pincesslucy/mallang_xtts_korean/assets/98650288/d0292b83-8271-4c9c-8c83-f0df8fee4e9f)


---
# changed
- tokenizer text length limit 수정:
xtts\lib\site-packages\TTS\tts\layers\xtts\tokenizer.py 에서

```python
class VoiceBpeTokenizer:
    def __init__(self, vocab_file=None):
        self.tokenizer = None
        if vocab_file is not None:
            self.tokenizer = Tokenizer.from_file(vocab_file)
        self.char_limits = {
            "en": 250,
            "de": 253,
            "fr": 273,
            "es": 239,
            "it": 213,
            "pt": 203,
            "pl": 224,
            "zh": 82,
            "ar": 166,
            "cs": 186,
            "ru": 182,
            "nl": 251,
            "tr": 226,
            "ja": 71,
            "hu": 224,
            "ko": 9000,
        }
  ```

- fomatter 수정:
  xtts\lib\site-packages\TTS\tts\datasets\formatters.py 에서
  ```python
  def ljspeech(root_path, meta_file, **kwargs):  # pylint: disable=unused-argument
    """Normalizes the LJSpeech meta data file to TTS format
    https://keithito.com/LJ-Speech-Dataset/"""
    txt_file = os.path.join(root_path, meta_file)
    items = []
    speaker_name = "ljspeech"
    with open(txt_file, "r", encoding="utf-8") as ttf:
        for line in ttf:
            cols = line.split("|")
            wav_file = os.path.join(root_path, "wavs", cols[0] + ".wav")
            text = cols[2]
            items.append({"text": text, "audio_file": wav_file, "speaker_name": speaker_name, "root_path": root_path})
    return items
  ```
