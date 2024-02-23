import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from huggingface_hub import snapshot_download

#snapshot_download(repo_id="princesslucy/mallang_xtts_large", local_dir='./model')
config = XttsConfig()
config.load_json("./model/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="./model")
model.cuda()

def tts(text, temperature=0.3, length_penalty=1, repetition_penalty=2.0, speed=1.0, audio="./wavs/input.wav", ouput="./wavs/output.wav"):
    gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=[audio])

    out = model.inference(
    text,
    gpt_cond_latent=gpt_cond_latent,
    speaker_embedding=speaker_embedding,
    temperature=temperature, # Add custom parameters here
    language="ko",
    length_penalty=length_penalty,
    repetition_penalty=repetition_penalty,
    speed=speed
)
    return torchaudio.save(ouput, torch.tensor(out["wav"]).unsqueeze(0), 24000)