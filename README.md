# InterPlus

InterPlus is a simple command-line utility that leverages Windows' native capabilities to efficiently manage compressed files. This program allows users to easily zip and unzip files with minimal effort.

## Features

- **Zip files**: Compress a directory into a zip file.
- **Unzip files**: Extract contents of a zip file into a specified directory.

## Requirements

- Python 3.x
- Windows OS with PowerShell support

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/InterPlus.git
```

Navigate to the directory:

```bash
cd InterPlus
```

## Usage

InterPlus can be run from the command line and requires Python to be installed on the system.

### Zipping Files

To zip a directory, use the following command:

```bash
python interplus.py zip <source_directory> <output_zip_file>
```

- `<source_directory>`: Directory you want to compress.
- `<output_zip_file>`: The name of the output zip file.

Example:

```bash
python interplus.py zip "C:\MyFiles" "C:\MyFiles.zip"
```

### Unzipping Files

To unzip a file, use the following command:

```bash
python interplus.py unzip <zip_file> <destination_directory>
```

- `<zip_file>`: The zip file you want to extract.
- `<destination_directory>`: The directory where files should be extracted.

Example:

```bash
python interplus.py unzip "C:\MyFiles.zip" "C:\ExtractedFiles"
```

## Error Handling

- Ensure paths for the source and destination are valid.
- For zipping, the source must be a directory.
- For unzipping, the source must be a valid zip file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For any inquiries or feedback, please contact [your email here].

```

Replace `[your email here]` and the GitHub repository URL placeholders with your actual contact information and repository URL.