import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
from io import BytesIO
from IPython.display import Audio, display

# ---------- STORIES ----------
stories = {
    "Shivaji Maharaj": [
        """Episode 1: The Birth of a Visionary.
In 1630, in the hill fort of Shivneri, a boy named Shivaji is born to Shahaji Bhosale and Jijabai.
From the very start, his mother fills him with the values of justice, courage, and love for the land.
Raised amidst the turbulent politics of the Deccan, he grows up listening to tales of heroism and freedom.
He begins to dream — not of wealth or titles — but of Swarajya, self-rule for his people.""",
        """Episode 2: The First Victory.
At just sixteen, Shivaji captures the Torna Fort — his first conquest and a bold message to the world.
Fort after fort comes under his command, and the Maratha flag flies high.
His guerrilla tactics — fast, unpredictable, devastating — keep enemies guessing.""",
        """Episode 3: The Clash with the Mughals.
Aurangzeb sends a massive force under Shaista Khan to crush the Maratha rise.
In a daring night raid, Shivaji infiltrates Khan’s residence at Lal Mahal and wounds him, sending shockwaves through the Mughal camp.
Later in Agra, Shivaji turns captivity into legend, escaping with brilliant cunning.""",
        """Episode 4: Coronation & Legacy.
In 1674, at Raigad, Shivaji is crowned Chhatrapati.
His reign stands for fair governance, religious tolerance, a strong navy, and Hindavi Swarajya.
He leaves behind more than a kingdom — he leaves an idea: freedom and self-rule are worth fighting for."""
    ],
    "Sambhaji Maharaj": [
        """Episode 1: The Prince's Early Years.
Born in 1657, Sambhaji, the elder son of Shivaji Maharaj, grows up amidst the struggle for Swarajya.
Trained in the art of war, statecraft, and diplomacy, his brilliance shows early.""",
        """Episode 2: Trials of Leadership.
After Shivaji’s passing, Sambhaji ascends the throne amid Mughal threats and internal dissent.
He proves himself a fearless warrior and a shrewd leader.""",
        """Episode 3: The Defiance Against Aurangzeb.
Sambhaji resists the might of Aurangzeb’s empire, inflicting heavy losses through relentless campaigns.
His unwavering spirit earns both fear and respect.""",
        """Episode 4: The Martyrdom.
Captured in 1689, Sambhaji refuses to bow to Aurangzeb’s demands.
He embraces torture and death over betrayal, becoming an eternal symbol of resistance."""
    ]
}

# ---------- STREAMLIT APP ----------
st.title("VeerGatha Audiobook 📖🎧")
hero_choice = st.selectbox("Choose Hero:", ["Shivaji Maharaj", "Sambhaji Maharaj"])
lang_choice = "en"

if st.button("Generate Audiobook"):
    episodes = stories[hero_choice]
    final_audio = AudioSegment.silent(duration=500)
    
    for ep in episodes:
        tts = gTTS(text=ep, lang=lang_choice, slow=False)
        buf = BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        ep_audio = AudioSegment.from_file(buf, format="mp3")
        final_audio += ep_audio + AudioSegment.silent(duration=1000)
    
    out_file = f"{hero_choice.replace(' ', '_')}_{lang_choice}.mp3"
    final_audio.export(out_file, format="mp3")
    
    st.audio(out_file, format="audio/mp3")
    st.success("✅ Audiobook generated!")
