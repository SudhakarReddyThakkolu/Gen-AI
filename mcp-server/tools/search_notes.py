import json

File="../storage/notes.json"

def search_notes(query:str):
  with open(File,"r") as f:
      notes=json.load(f)
  results=[]

  for n in notes:
    if query.lower() in n["text"].lower():
        results.append(n)
  return{"results":results}

if __name__=="__main__":
    result=search_notes(" radhika")
    print(result)
    result=search_notes(" Sudhakar")
    print(result)
