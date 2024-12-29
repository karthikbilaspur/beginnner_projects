import os
import shutil
import datetime
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_by_type(directory):
    """
    Organize files by type.

    Args:
    directory (str): Path to the directory containing files.
    """
    file_types = {
        'Documents': ['.txt', '.pdf', '.docx', '.doc', '.odt', '.rtf'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.webm'],
        'Audio': ['.mp3', '.wav', '.aac', '.ogg'],
        'Spreadsheets': ['.xls', '.xlsx', '.ods', '.csv'],
        'Presentations': ['.ppt', '.pptx', '.odp'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Executables': ['.exe', '.msi', '.apk'],
        'Code': ['.py', '.java', '.cpp', '.js', '.php']
    }

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for file_type, extensions in file_types.items():
                if file_extension in extensions:
                    destination_dir = os.path.join(directory, file_type)
                    os.makedirs(destination_dir, exist_ok=True)
                    try:
                        shutil.move(file_path, destination_dir)
                        logging.info(f"Moved {filename} to {file_type}")
                        moved = True
                        break
                    except Exception as e:
                        logging.error(f"Error moving {filename}: {str(e)}")
            if not moved:
                logging.warning(f"Unrecognized file type: {filename}")


def organize_by_date(directory):
    """
    Organize files by date.

    Args:
    directory (str): Path to the directory containing files.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            timestamp = os.path.getctime(file_path)
            date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m')
            destination_dir = os.path.join(directory, date)
            os.makedirs(destination_dir, exist_ok=True)
            try:
                shutil.move(file_path, destination_dir)
                logging.info(f"Moved {filename} to {date}")
            except Exception as e:
                logging.error(f"Error moving {filename}: {str(e)}")


def organize_by_size(directory):
    """
    Organize files by size.

    Args:
    directory (str): Path to the directory containing files.
    """
    size_ranges = {
        'Small': (0, 1024 * 1024),  # 0-1MB
        'Medium': (1024 * 1024, 1024 * 1024 * 10),  # 1-10MB
        'Large': (1024 * 1024 * 10, 1024 * 1024 * 100),  # 10-100MB
        'Extra Large': (1024 * 1024 * 100, float('inf'))  # 100MB+
    }

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            for size_range, size_bounds in size_ranges.items():
                if size_bounds[0] <= file_size < size_bounds[1]:
                    destination_dir = os.path.join(directory, size_range)
                    os.makedirs(destination_dir, exist_ok=True)
                    try:
                        shutil.move(file_path, destination_dir)
                        logging.info(f"Moved {filename} to {size_range}")
                        break
                    except Exception as e:
                        logging.error(f"Error moving {filename}: {str(e)}")


def organize_by_extension(directory):
    """
    Organize files by extension.

    Args:
    directory (str): Path to the directory containing files.
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            destination_dir = os.path.join(directory, file_extension[1:])
            os.makedirs(destination_dir, exist_ok=True)
            try:
                shutil.move(file_path, destination_dir)
                logging.info(f"Moved {filename} to {file_extension[1:]}")
            except Exception as e:
                logging.error(f"Error moving {filename}: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description='File Organizer')
    parser.add_argument('-d', '--directory', required=True, help='Directory path')
    parser.add_argument('-o', '--organize', choices=['type', 'date', 'size', 'extension'], required=True, help='Organization method')
    args = parser.parse_args()

    directory = args.directory
    organize_method = args.organize

    if organize_method == 'type':
        organize_by_type(directory)
    elif organize_method == 'date':
        organize_by_date(directory)
    elif organize_method == 'size':
        organize_by_size(directory)
    elif organize_method == 'extension':
        organize_by_extension(directory)


if __name__ == "__main__":
    main()