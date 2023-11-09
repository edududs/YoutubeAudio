from pathlib import Path
import os
import sys
import moviepy.editor as mpe


class AudioEditor:
    BASE_ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.file_path = str(Path(self.BASE_ROOT, file_name))
        self.audio_file_editor = mpe.AudioFileClip(self.file_path)

    def convert_audio(self, file: str | None = None):
        if file is not None:
            output_file = str(Path(self.BASE_ROOT, file))
        else:
            output_file = str(Path(self.BASE_ROOT, self.file_name))
        self.audio_file_editor.write_audiofile(output_file, codec="libmp3lame")
        return output_file
