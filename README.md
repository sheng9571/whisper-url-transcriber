# Whisper URL Transcriber

Transcribe audio from a direct download URL using:

- faster-whisper
- Whisper large-v3
- Docker
- GitHub Actions
- GitHub Container Registry

The Docker image contains the Whisper model, so the model does not
need to be downloaded during each transcription job.

## Usage

1. Open `Actions`
2. Select `Transcribe Audio`
3. Click `Run workflow`
4. Enter a direct audio download URL
5. Wait for the workflow to finish
6. Download the `transcript` artifact

The artifact contains:

transcript.txt

## Supported input

Any audio format supported by the underlying audio decoder, including
common formats such as:

- M4A
- MP3
- WAV
- AAC
- FLAC

## Privacy

Audio files are not stored in this repository.

The GitHub Actions runner downloads the audio to temporary runner
storage and the runner is destroyed after the job finishes.

The generated transcript is uploaded as a GitHub Actions artifact with
a retention period of 1 day.

Do not use sensitive URLs containing long-lived credentials as
workflow inputs.

## Docker

Build:

docker build -t whisper-url-transcriber .

Run:

docker run --rm \
  -v "$PWD/a.m4a:/data/audio:ro" \
  -v "$PWD/output:/output" \
  whisper-url-transcriber \
  /data/audio
