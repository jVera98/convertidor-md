"""This is a simple script to parse PDF into MD to help me to give the AI the file in a format that´d
help the conversion and make a roadmap to study."""
import pymupdf4llm
from pathlib import Path
from pymupdf import FileDataError
while True:

    try:
        user_input = int(input("Insert 0 to quit and 1 to enter the path:"))

    except ValueError:
        print("Please, just 1 or 0.")
        continue

    if user_input == 0:
        break


    elif user_input == 1:
        path = Path(input("Please the path must be in temas/[tema-que-queremos]:"))
        if path.is_file():
            if path.suffix.lower()==".pdf":
                path_md = path.with_suffix(".md")
                try:
                    print("loading...")
                    path_md.write_text(pymupdf4llm.to_markdown(path),encoding="utf-8")
                    print(f"File available in temas/{path_md}")
                except FileDataError:
                    print("The true format is not .pdf")
            else:
                print("The suffix is not .pdf")
        else:
            print("The file is not found.")
            

    else:
        print("Just insert 1 or 0.")



