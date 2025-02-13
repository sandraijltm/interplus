import os
import subprocess
import argparse

def zip_files(source_dir, output_zip):
    """Zips the specified directory using Windows native zip capabilities."""
    command = f'powershell Compress-Archive -Path "{source_dir}\\*" -DestinationPath "{output_zip}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully zipped {source_dir} to {output_zip}")
    else:
        print(f"Error zipping files: {result.stderr}")

def unzip_file(zip_file, destination_dir):
    """Unzips the specified file using Windows native unzip capabilities."""
    command = f'powershell Expand-Archive -Path "{zip_file}" -DestinationPath "{destination_dir}" -Force'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully unzipped {zip_file} to {destination_dir}")
    else:
        print(f"Error unzipping files: {result.stderr}")

def main():
    parser = argparse.ArgumentParser(description="InterPlus: Simplify zipping and unzipping of files using Windows native capabilities.")
    parser.add_argument('operation', choices=['zip', 'unzip'], help="Operation to perform: zip or unzip")
    parser.add_argument('source', help="Source directory for zipping or zip file for unzipping")
    parser.add_argument('destination', help="Destination zip file for zipping or destination directory for unzipping")

    args = parser.parse_args()

    if args.operation == 'zip':
        if not os.path.isdir(args.source):
            print("Error: Source should be a valid directory for zipping.")
            return
        zip_files(args.source, args.destination)
    elif args.operation == 'unzip':
        if not os.path.isfile(args.source):
            print("Error: Source should be a valid zip file for unzipping.")
            return
        unzip_file(args.source, args.destination)

if __name__ == '__main__':
    main()