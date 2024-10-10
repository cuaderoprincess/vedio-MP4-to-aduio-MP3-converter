import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog, messagebox

def select_mp4_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    return file_path

def check_if_file_is_valid(file_path):
    return file_path.lower().endswith('.mp4') and os.path.exists(file_path)

def convert_to_mp3(input_file):
    try:
        video = VideoFileClip(input_file)
        audio = video.audio
        output_file = os.path.splitext(input_file)[0] + ".mp3"
        audio.write_audiofile(output_file)
        video.close()
        audio.close()
        return output_file
    except Exception as e:
        raise Exception(f"Conversion failed: {str(e)}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    while True:
        # Start
        # Select MP4 file
        input_file = select_mp4_file()
        if not input_file:
            break  # User cancelled file selection

        # Check if file is valid
        if check_if_file_is_valid(input_file):
            try:
                # Convert to MP3
                output_file = convert_to_mp3(input_file)
                # Download MP3 file
                messagebox.showinfo("Success", f"MP3 file saved as: {output_file}")
            except Exception as e:
                # Show error message
                messagebox.showerror("Error", str(e))
        else:
            # Show error message
            messagebox.showerror("Error", "Invalid file selected. Please choose a valid MP4 file.")

        # Ask if the user wants to convert another file
        if not messagebox.askyesno("Continue", "Do you want to convert another file?"):
            break

    # End
    root.destroy()

if __name__ == "__main__":
    main()
