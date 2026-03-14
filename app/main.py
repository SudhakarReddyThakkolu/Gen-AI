import os
import ollama
transcript_folder = "../data/transcripts"

for file in os.listdir(transcript_folder):
    with open(os.path.join(transcript_folder,file),"r",encoding="utf-8") as f:
        transcript=f.read()
    print("transcript loading...")
    print(transcript[:200])

    prompt=f""" Extract the following details from the motor insurance claim transcript:
    - Policy Number
    - Vehicle Number
    - Accident Date
    - Damage Description
    Transcript:{transcript}:"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role":"user","content":prompt}]
        )
    print("Processing : ", file)
    print(response["message"]["content"])