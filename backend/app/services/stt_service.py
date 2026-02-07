# lightweight fallback STT: we will not install Whisper here automatically
def transcribe_audio(bytes_data: bytes):
    # For dev: return a fake transcript
    return {"transcript":"(simulated) This is a simulated transcription of audio input."}
