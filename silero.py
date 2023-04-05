import os
from os import path
from torch import device as torch_device, hub, package, set_num_threads
import simpleaudio as sa
import Say as s


# print(s.say().text)
def say_silero():
    device = torch_device('cpu')
    set_num_threads(4)
    local_file = 'model_multi.pt'
    speakers = ['aidar', 'baya', 'kseniya', 'irina', 'ruslan', 'natasha',
                'thorsten', 'tux', 'gilles', 'lj', 'dilyara']

    if not path.isfile(local_file):
        hub.download_url_to_file('https://models.silero.ai/models/tts/multi/v2_multi.pt',
                                 local_file)

    model = package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    example_batch = [
        'Гра-та-та-та-та! Стреляю, па-па-па-па-па. Убегаешь от меня. Смотришь мне в глаза. Гра-та-та-та-та.']
    example_speakers = ['aidar']
    sample_rate = 16000

    audio_paths = model.save_wav(texts=example_batch,
                                 speakers=example_speakers,
                                 sample_rate=sample_rate)
    print(audio_paths)

    wave_obj = sa.WaveObject.from_wave_file('text.wav')
    play_obj = wave_obj.play()
    play_obj.wait_done()
