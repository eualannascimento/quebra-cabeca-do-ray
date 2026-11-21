#!/usr/bin/env python3
"""Gera os 24 arquivos audio/hora_00.mp3 .. audio/hora_23.mp3 localmente via Coqui XTTS-v2.

Uso:
  1. python3 -m venv .venv-tts && source .venv-tts/bin/activate
  2. pip install TTS pydub
  3. Coloque um audio limpo de 6 a 15 segundos chamado referencia.wav na raiz do projeto
  4. python3 scripts/gerar_vozes_hora.py referencia.wav
"""

import os
import sys
from pathlib import Path

from TTS.api import TTS


def phrase_for(hour: int) -> str:
    if hour == 0:
        return "Atenção! Deu meia-noite!"
    if hour == 1:
        return "Atenção! É uma hora da madrugada!"
    if 2 <= hour <= 5:
        return f"Atenção! São {hour} horas da madrugada!"
    if hour == 6:
        return "Atenção! São seis horas da manhã!"
    if 7 <= hour <= 11:
        return f"Atenção! São {hour} horas da manhã!"
    if hour == 12:
        return "Atenção! Deu meio-dia!"
    if hour == 13:
        return "Atenção! É uma hora da tarde!"
    if 14 <= hour <= 17:
        return f"Atenção! São {hour - 12} horas da tarde!"
    return f"Atenção! São {hour - 12} horas da noite!"


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python3 scripts/gerar_vozes_hora.py <caminho_referencia.wav>")
        sys.exit(1)

    ref_path = Path(sys.argv[1]).expanduser().resolve()
    if not ref_path.exists():
        print(f"Arquivo de referência não encontrado: {ref_path}")
        sys.exit(1)

    out_dir = Path(__file__).resolve().parent.parent / "audio"
    out_dir.mkdir(parents=True, exist_ok=True)

    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    for hour in range(24):
        wav_tmp = out_dir / f"hora_{hour:02d}.wav"
        mp3_out = out_dir / f"hora_{hour:02d}.mp3"
        text = phrase_for(hour)
        print(f"[{hour:02d}/23] Gerando: {text}")
        tts.tts_to_file(
            text=text,
            speaker_wav=str(ref_path),
            language="pt",
            file_path=str(wav_tmp),
        )
        os.system(f'ffmpeg -y -i "{wav_tmp}" -codec:a libmp3lame -qscale:a 3 "{mp3_out}" -loglevel error')
        if wav_tmp.exists():
            wav_tmp.unlink()

    print("Concluído! 24 arquivos salvos em:", out_dir)


if __name__ == "__main__":
    main()
