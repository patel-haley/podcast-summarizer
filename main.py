from api_comms import *
import streamlit as st

st.title("Pod-Sum: A Podcast Summarizer")
st.header("Turn Any Podcast From ListenNotes into Summaries!")
episode_id = st.sidebar.text_input('Input episode id:')
button = st.sidebar.button('Summarize!', on_click=save_transcript,args=(episode_id))

def get_aesthetic_time(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        starts_t = f'{minutes:02d}:{seconds:02d}'

    return start_t

if button:
    filename = episode_id + '_chapters.json'
    with open(filename, 'r') as f:
        data = json.load(f)

        chapters = data['chapters']
        podcast_title = data['podcast_title']
        episode_title = data['episode_title']
        thumbnail = data['episode_thumbnail']

    st.header(f'{podcast_title} - {episode_title}')
    st.image(thumbnail)
    for chp in chapters:
        with st.expander(chp['gist'] + '-' + get_aesthetic_time(chp['start'])):
            chp['summary']
    

