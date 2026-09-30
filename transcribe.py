from faster_whisper import WhisperModel

import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio with faster-whisper large-v3"
    )

    parser.add_argument(
        "audio",
        help="Path to input audio file",
    )

    parser.add_argument(
        "--output",
        default="/output/transcript.txt",
        help="Output transcript path",
    )

    args = parser.parse_args()

    model = WhisperModel(
        "/models/large-v3",
        device="cpu",
        compute_type="int8",
    )

    segments, info = model.transcribe(
        args.audio,
        language="zh",
        beam_size=5,
        vad_filter=True,
        initial_prompt=(
            "以下是一段台灣人的日常對話。"
            "主要使用台灣繁體中文、台灣華語，"
            "其中可能夾雜台語、英文、人名與口語表達。"
            "請忠實逐字轉錄，不要摘要。"
        ),
    )

    output_dir = os.path.dirname(args.output)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    print(
        f"Detected language: {info.language}",
        flush=True,
    )

    with open(
        args.output,
        "w",
        encoding="utf-8",
    ) as f:
        for segment in segments:
            text = segment.text.strip()

            line = (
                f"[{segment.start:08.2f} --> "
                f"{segment.end:08.2f}] "
                f"{text}"
            )

            print(line, flush=True)

            f.write(line + "\n")
            f.flush()

    print(
        f"Done: {args.output}",
        flush=True,
    )


if __name__ == "__main__":
    main()
