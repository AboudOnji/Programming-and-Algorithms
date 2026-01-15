import os
import subprocess
import shutil


def compile_missing_pdfs():
    source_root = "/Users/aboudonji/Library/CloudStorage/GoogleDrive-aboudonji@gmail.com/My Drive/Universidad Anáhuac/Conference Presentations/Programming and Algorithms"
    dest_root = os.path.join(source_root, "Evidencias")

    print(f"Source Root: {source_root}")

    for item in os.listdir(source_root):
        source_item_path = os.path.join(source_root, item)

        # Skip if not a directory or if it's the Evidencias folder
        if not os.path.isdir(source_item_path) or item == "Evidencias":
            continue

        # Check for existing PDFs
        files = os.listdir(source_item_path)
        pdfs = [f for f in files if f.lower().endswith(".pdf")]

        if pdfs:
            print(f"Skipping '{item}': Already has PDFs ({len(pdfs)})")
            continue

        # Check for TeX files
        tex_files = [f for f in files if f.lower().endswith(".tex")]
        if not tex_files:
            print(f"Skipping '{item}': No TeX files found")
            continue

        print(
            f"Processing '{item}': No PDFs found, but has TeX files: {tex_files}")

        # Compile each TeX file
        for tex_file in tex_files:
            print(f"  Compiling {tex_file}...")
            try:
                # Run pdflatex. We use cwd=source_item_path so it finds included files/images.
                # -interaction=nonstopmode prevents it from hanging on errors.
                result = subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", tex_file],
                    cwd=source_item_path,
                    capture_output=True,
                    text=True
                )

                if result.returncode == 0:
                    print(f"  SUCCESS: Compiled {tex_file}")
                else:
                    print(
                        f"  WARNING: Compilation of {tex_file} returned code {result.returncode}")
                    # Sometimes PDF is generated even with errors, so we check for the file.

                # Check if PDF was generated
                pdf_name = os.path.splitext(tex_file)[0] + ".pdf"
                pdf_path = os.path.join(source_item_path, pdf_name)

                if os.path.exists(pdf_path):
                    # Copy to Evidencias
                    dest_item_path = os.path.join(dest_root, item)
                    if not os.path.exists(dest_item_path):
                        os.makedirs(dest_item_path)

                    shutil.copy2(pdf_path, os.path.join(
                        dest_item_path, pdf_name))
                    print(f"  Copied {pdf_name} to Evidencias/{item}")
                else:
                    print(
                        f"  ERROR: PDF not found after compilation: {pdf_name}")

            except Exception as e:
                print(f"  EXCEPTION: {e}")


if __name__ == "__main__":
    compile_missing_pdfs()
