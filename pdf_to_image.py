import os
import pytesseract
from pdf2image import convert_from_path

base = os.getcwd()
os.mkdir("sample_output")
os.chdir(os.path.join(base, "sample_input"))


total_files = os.listdir()
for input_file in total_files:
    output_file = input_file[:-4] + ".png"
    pages = convert_from_path(input_file, 950)
    os.chdir(os.path.join(base, "sample_output"))
    pages[0].save(output_file, "JPEG")
    os.chdir(os.path.join(base, "sample_input"))
