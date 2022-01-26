from typing import Optional, Any, Dict
import csv
from tempfile import NamedTemporaryFile
import os
import shutil

DELIMITER = ";"

MOVIE_FIELDS = ['Id', 'Movies', 'Picture', 'Genres', 'Director', 'Rating', 'Synopsis', 'Time', 'Rating Count', 'Rating Sum', 'View Count']
MOVIE_CSV_FILE = os.path.join("database", "movies.csv")

MOVIE_ID_INDEX = 0
MOVIE_VIEW_COUNT_INDEX = 10

# DEFAULTS = [
#     "",  # ID
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     0,  # MOVIE_RATING_COUNT
#     0,  # SUM
#     0,  # VIEW COUNT
# ]


def get_movie_metadata_as_list(find_movie_id: int) -> Optional[list]:
    with open(MOVIE_CSV_FILE, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            line = line.rstrip("/n")
            movie_metadata = line.split(";")
            movie_id = movie_metadata[MOVIE_ID_INDEX]
            try:
                if int(movie_id) == int(find_movie_id):
                    return movie_metadata
            except ValueError:
                pass
    return None


def get_movie_metadata(movie_id: int) -> Optional[Dict[Any, Any]]:
    with open(MOVIE_CSV_FILE, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=MOVIE_FIELDS, delimiter=DELIMITER, quoting=csv.QUOTE_NONE)
        for row in reader:
            print(row)
            try:
                if int(row["Id"]) == int(movie_id):
                    return row
            except ValueError:
                pass
        return None


def save_movie_metadata(movie_id: int, field: str, value: Any) -> None:

    temp_file = NamedTemporaryFile(mode='w', delete=False, newline='')
    
    with open(MOVIE_CSV_FILE, 'r') as csvfile, temp_file:
        reader = csv.DictReader(csvfile, fieldnames=MOVIE_FIELDS, delimiter=DELIMITER, quoting=csv.QUOTE_NONE)
        writer = csv.DictWriter(temp_file, fieldnames=MOVIE_FIELDS, delimiter=DELIMITER, quoting=csv.QUOTE_NONE)

        headers = next(reader, None)
        if headers:
            writer.writerow(headers)

        for row in reader:
            try:
                if int(row["Id"]) == int(movie_id):
                    row[field] = value
                writer.writerow(row)
            except ValueError:
                pass
        
    shutil.move(temp_file.name, MOVIE_CSV_FILE)
        

def increment_movie_view_count(movie_id: int) -> None:
    movie_metadata = get_movie_metadata(movie_id)
    if movie_metadata:
        try:
            current_view_count = int(movie_metadata.get("View Count")) or 0
        except:
            current_view_count = 0
        save_movie_metadata(movie_id, "View Count", current_view_count + 1)
