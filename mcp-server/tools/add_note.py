import json
from datetime import datetime
File = "../storage/notes.json"

def add_notes(text:str):
    with open(File, "r") as f:
        notes=json.load(f)
    notes.append(
        {
            "text":text,
            "created_at":datetime.now().isoformat()
        }
    )
    with open(File,"w") as f:
        json.dump(notes,f,indent=2)
    return{"success": True}

if __name__=="__main__":
    result=add_notes(" This is Sudhakar Reddy thakkolu")
    print(result)

        