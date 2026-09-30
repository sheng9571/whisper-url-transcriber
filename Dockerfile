FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    HF_HOME=/models/huggingface

WORKDIR /app

RUN pip install --no-cache-dir \
    faster-whisper \
    huggingface-hub

# Download faster-whisper large-v3 during image build.
# Runtime no longer needs to download the model.
RUN python - <<'PY'
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="Systran/faster-whisper-large-v3",
    local_dir="/models/large-v3",
)
PY

COPY transcribe.py /app/transcribe.py

ENTRYPOINT ["python", "/app/transcribe.py"]
