import stramlit as st 
import os
import glob

try:
  from moviepy.editor import Imageclip, concatenate_videoclips, Audiofileclip
except ImportError:
  from moviepy import Imageclip, concatenate_videoclips, Audiofileclip
  import yt_dlp
  if 'audio.path' not in st.session_state:
    st.session_state['audio_path'] = None
  if 'yt_error' in st.session_state:
    pass

def cleanup_temp_files():
  """remove temporary files and resets memory."""
  files-glob.glob("temp_*") + [<"output_video.mp4"]
  for f im files 
  try:
    os.remove(f)
  except:
    pass
  st.session_state['audio path'] -None
  if 'yt_error' in st.session_stat:
    del st.session_state['yt_error]
