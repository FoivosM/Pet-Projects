# 🎵 Generate .cue files
A personal project to convert `.txt` to `.cue` files. [CUE](https://en.wikipedia.org/wiki/Cue_sheet_(computing)) files are an easy way to separate long audio files into chapters, without the need for complicated modifications to the original file, or the use of third-party applications.

## Usage
The prerequisites are an **audio file** (i.e. `my_audio.opus`) and an empty `.txt` file. The text file must be in the same folder and have **exactly** the same name as the audio file. To create a chapter, all you need to do is add a line in the `.txt` with the timestamp in `HH:MM:SS` format, followed by a single space, and then the chapter title enclosed in `"` (e.g. `"Chapter 1"`). It is a good practice to always begin the text file with `00:00:00 "Stat"`. Otherwise, the audio section between the beginning of the file and the first chapter will not be accessible during playback of the `.cue` file.

🚨 Warning: **ONLY English** titles are allowed. **No empty lines**, beyond the last chapter, are allowed. Here is a `.txt` example:
```txt
00:00:00 "Start"
00:02:10 "Chapter 1"
02:34:45 "Chapter 8"
```
This script is designed with `OPUS` files in mind, but you can easily modify the code (line 23) to handle any filetype you like. Optionally, you can specify the folder in which you usually store your audio files, for easier conversions. Upon execution, you will be asked for the name of the text file (i.e `my_audio.txt`). The text file will be replaced with the `my_audio.cue` file. ✨Now you can execute the `.cue` file with the media player of your choice.

## Quick Start
0. You have the audio file `my_audio.opus`.
1. Create `my_audio.txt` in the same folder.
2. Add timestamps and chapters in the text file, like in the example above.
3. Execute `generate_cue.py` and provide the full-path to the `.txt` file.

You are ready! Now use the `.cue` file instead of the original.

## Bonus!
If you are using MPV, you can add `input.conf` to your `C:\Users\User\AppData\Roaming\mpv` folder. This file specifies two custom keymaps:
- **Display Chapters**: Use `0` on the numpad to display the current chapter and some of its neighbors.
- **Copy timestamp**: `Ctrl+c` copies current timestamp into clipboard, following the `HH:MM:SS` format.