import teslacam
from teslacam import *
from pathlib import Path
import nest_asyncio

# Aplicar nest_asyncio si estás en un notebook
nest_asyncio.apply()

def main():
    print(f"Available layouts: {', '.join(teslacam.constants.LAYOUT.keys())}")
    print(f'Available codecs: {teslacam.constants.CODEC_OPTIONS.items()}')
    
    extract_videos(
        FFMpegPaths(
            Path(r'C:\ProgramData\chocolatey\bin\ffprobe.exe'),
            Path(r'C:\ProgramData\chocolatey\bin\ffmpeg.exe')
        ),
        LayoutOptions(
            'hevc_nvenc',  # Codec name (usa 'libx264' si no tienes GPU NVIDIA)
            'fast',        # Codec preset
            'pyramid',     # Layout name
            DONT_REDUCE   # Percentage value from 1-100 (or DONT_REDUCE constant)
        ),
        BaseFolderPaths(
            Path(r'E:\TeslaCam'),   # Path to your USB stick
            Path(r'C:\Users\juani\Videos\TeslaCam')  # Destination path
        ),
        True  # Keep temporary working folder
    )

if __name__ == '__main__':
    main()
