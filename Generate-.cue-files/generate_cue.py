"""_summary_ convert .txt with chapters in the following form and then delete the txt. Make sure there are no empty lines in the end. Accepts only English.

HH:MM:SS "Chapter 1"
HH:MM:SS "Chapter 2"
"""
import os
# os.chdir("D:/05 Audio/") # Add folder path of audio files for faster conversion.

def convert_timestamps_to_cue_and_delete_input():
    # Ask for the input file path
    input_file_path = input("Enter the path of the input file: ")

    # Extracting the base file name without extension for TITLE
    base_name = input_file_path.split('.')[0]

    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    output_lines = [
        "REM GENRE \"Recording\"",
        "REM DATE \"2024\"",
        f"TITLE \"{base_name}\"",
        f"FILE \"{base_name}.opus\" OPUS" # MODIFY <-
    ]

    for i, line in enumerate(lines):
        timestamp, title = line.strip().split(' ', 1)
        hours, minutes, seconds = map(int, timestamp.split(':'))
        total_minutes = hours * 60 + minutes
        output_lines.append(f"  TRACK {i+1:02d} AUDIO")
        output_lines.append(f"    TITLE {title}")
        output_lines.append(f"    INDEX 01 {total_minutes:02d}:{seconds:02d}:00")

    cue_file_content = '\n'.join(output_lines)

    # Saving the result to a .cue file
    with open(f"{base_name}.cue", 'w') as cue_file:
        cue_file.write(cue_file_content)

    # Deleting the input file
    os.remove(input_file_path)

# Run the function to prompt for input file path, process it, and delete the input file
convert_timestamps_to_cue_and_delete_input()
