import time
import sys
import random
import pygame

# Mac terminal ke liye Bold aur Radiant (Glow) colors
COLORS = [
    '\033[1;91m', # Neon Red
    '\033[1;92m', # Neon Green
    '\033[1;93m', # Radiant Yellow
    '\033[1;94m', # Bright Blue
    '\033[1;95m', # Glowing Pink/Magenta
    '\033[1;96m', # Neon Cyan
]
RESET = '\033[0m' # Text color wapas normal karne ke liye

# Yahan par apne gaane ke full lyrics paste kar dena
lyrics = """
Aankhein Yeh Mujhse Kahe
Bas Tumko Yeh Takti Rahein
Tu Hi Tu Basa Dil Mein Hardum Bepanah

Dil Toh Chahe Dede Tujhko
Phoolon Se Bhari Raahein
Tumhari Har Ada Tumahri Har Nazar
Pe Hum Marne Lage
Un Pe Hum Marne Lage…

Is Kadar Tumse Pyaar Ho Gaya
Is Kadar Dil Nisaar Ho Gaya
Is Kadar Bekaraar Ho Gaya
Is Kadar Ab Khumaar Ho Gaya

Is Qadar Tumse Pyaar Ho Gaya
Is Qadar Dil Nisaar Ho Gaya
Is Qadar Bekaraar Ho Gaya
Is Qadar Ab Khumaar Ho Gaya
"""

def play_song_with_lyrics(audio_file):
    # Audio system initialize karna
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error: Gana load nahi ho paya. Check karo ki .mp3 file same folder mein hai ya nahi. Details: {e}")
        return

    print("\n🎵 Song Play Hona Start Ho Gaya Hai...\n")
    
    # Pehle word ke liye ek random color pick karna
    current_color = random.choice(COLORS)
    
    for char in lyrics:
        # Agar character space ya enter (newline) hai
        if char.isspace():
            sys.stdout.write(char) # Space ko normal print karo
            # Naya word aane wala hai, toh naya radiant color pick karo
            current_color = random.choice(COLORS)
        else:
            # Alphabet ko current color mein print karo (word-by-word color logic)
            sys.stdout.write(current_color + char + RESET)
        
        sys.stdout.flush()
        time.sleep(0.08) # Har alphabet print hone ki speed

    # Jab tak gaana chal raha hai, script ko close mat hone do
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    print("\n\n✅ Song Finished!")

if __name__ == "__main__":
    # Dhyan rakhein: Yahan file ka naam wahi hona chahiye jo tumhari mp3 file ka hai
    mp3_file_path = "/Users/ayushkumar/Desktop/Radiant & Glowing vibe/ISS QADAR PART 2 SONG(2).mp3" 
    play_song_with_lyrics(mp3_file_path)