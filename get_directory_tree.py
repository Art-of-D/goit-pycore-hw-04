# pip install colorama
def get_directory_tree(path):
  with open(path) as file:
    for line in file:
      print(line)

# get_directory_tree("path/to/directory")
# python hw03.py /шлях/до/вашої/директорії

# Output
# /шлях/до/вашої/директорії 
# 📦picture
#  ┣ 📂Logo
#  ┃ ┣ 📜IBM+Logo.png
#  ┃ ┣ 📜ibm.svg
#  ┃ ┗ 📜logo-tm.png
#  ┣ 📜bot-icon.png
#  ┗ 📜mongodb.jpg
