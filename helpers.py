def load(filename):
   try:
       with open(filename, "r", encoding="utf-8") as file:
           data = file.read()
           return data
   except IOError as e:
       print(f"Error: {e}")

def save(filename, content):
   try:
       with open(filename, "w", encoding="utf-8") as file:
           file.write(content)
   except IOError as e:
       print(f"Error saving file: {e}")