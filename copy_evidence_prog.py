import os
import shutil


def copy_evidence_prog():
    source_root = "/Users/aboudonji/Library/CloudStorage/GoogleDrive-aboudonji@gmail.com/My Drive/Universidad Anáhuac/Conference Presentations/Programming and Algorithms"
    dest_root = os.path.join(source_root, "Evidencias")

    print(f"Source Root: {source_root}")
    print(f"Dest Root: {dest_root}")

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_root):
        os.makedirs(dest_root)
        print(f"Created directory: {dest_root}")
    else:
        print(f"Directory already exists: {dest_root}")

    # Iterate over items in the source root
    for item in os.listdir(source_root):
        source_item_path = os.path.join(source_root, item)

        # Skip if it's not a directory
        if not os.path.isdir(source_item_path):
            continue

        # Skip the destination folder itself
        if item == "Evidencias":
            continue

        # Define the new destination folder for this item
        dest_item_path = os.path.join(dest_root, item)

        # Create the subfolder in Evidencias
        if not os.path.exists(dest_item_path):
            os.makedirs(dest_item_path)
            print(f"Created subfolder: {dest_item_path}")

        # Walk through the source subfolder to find PDFs
        files_copied = 0
        files_in_source = os.listdir(source_item_path)

        for file in files_in_source:
            if file.lower().endswith(".pdf"):
                src_file = os.path.join(source_item_path, file)
                dst_file = os.path.join(dest_item_path, file)
                try:
                    shutil.copy2(src_file, dst_file)
                    files_copied += 1
                except Exception as e:
                    print(f"  ERROR: Failed to copy {file}. Reason: {e}")

        print(
            f"Copied {files_copied} PDFs from '{item}' to 'Evidencias/{item}'")


if __name__ == "__main__":
    copy_evidence_prog()
