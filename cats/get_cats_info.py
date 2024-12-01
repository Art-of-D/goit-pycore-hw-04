from pathlib import Path


def get_cats_info(path: Path) -> list:
  """
  Read a CSV file and return a list of dictionaries,
  where each dictionary contains the id, name and age of a cat.

  The file should contain one line per cat, with the id, name and age
  separated by commas.

  If the file does not exist, or if there are no valid lines in the
  file, then the function will return an empty list.

  :param path: Path to the file to read.
  :return: A list of dictionaries, where each dictionary contains the id, name and age of a cat.
  """
  list = []
  try:
      with path.open(encoding="utf-8") as file:
          for line in file:
              try:
                  id, name, age = line.strip().split(",")
                  list.append({"id": id, "name": name, "age": age})
              except ValueError:
                  continue
  except FileNotFoundError:
      print("File not found")
      return list

  return list

file_path = Path("./data/cats.csv")
cats_info = get_cats_info(file_path)
print(cats_info)
