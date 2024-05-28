import os
import subprocess

def convert_doc_to_pdf(doc_path, pdf_path):
    subprocess.run(['unoconv', '-f', 'pdf', '-o', pdf_path, doc_path], check=True)

def create_output_folder_structure(input_folder, output_folder):
    for dirpath, dirnames, filenames in os.walk(input_folder):
        structure = os.path.join(output_folder, os.path.relpath(dirpath, input_folder))
        if not os.path.isdir(structure):
            os.makedirs(structure)
        for filename in filenames:
            if filename.endswith(('.doc', '.docx')):
                file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(structure, f"{os.path.splitext(filename)[0]}.pdf")
                convert_doc_to_pdf(file_path, new_file_path)

def main(input_folder, output_folder):
    if not os.path.isdir(input_folder):
        print("Input folder does not exist.")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    create_output_folder_structure(input_folder, output_folder)
    print(f"Files converted and saved to {output_folder}")

if __name__ == "__main__":
    input_folder = "/Users/stavrosdidakis/Downloads/CONVERT/in"
    output_folder = "/Users/stavrosdidakis/Downloads/CONVERT/out"
    main(input_folder, output_folder)
