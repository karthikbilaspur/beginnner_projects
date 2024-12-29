import os
import re
import hashlib
import stat
import datetime
import threading
from getpass import getuser
from grp import getgrgid
from pwd import getpwuid

class FileSearch:
    def __init__(self, directory):
        self.directory = directory
        self.results = []
        self.total_files = 0

    def search_files(self, filename=None, extensions=None, exclude_dirs=None, min_size=None, max_size=None,
                     regex=None, content=None, min_date=None, max_date=None):
        for root, dirs, files in os.walk(self.directory):
            if exclude_dirs and any(exclude_dir in root for exclude_dir in exclude_dirs):
                continue

            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_date = datetime.fromtimestamp(os.path.getmtime(file_path))

                self.total_files += 1
                print(f"\rSearching... ({self.total_files})", end="")

                if (filename and file.lower() == filename.lower()) or \
                   (extensions and any(file.lower().endswith(ext.lower()) for ext in extensions)) or \
                   (regex and re.search(regex, file)) or \
                   (not filename and not extensions and not regex):
                    if (min_size is None or file_size >= min_size) and (max_size is None or file_size <= max_size):
                        if (min_date is None or file_date >= min_date) and (max_date is None or file_date <= max_date):
                            if content:
                                try:
                                    with open(file_path, 'r') as f:
                                        if content in f.read():
                                            self.results.append((file_path, file_size, file_date))
                                except UnicodeDecodeError:
                                    pass  # Skip non-text files
                            else:
                                self.results.append((file_path, file_size, file_date))

    def calculate_hashes(self, file_path):
        hashes = {}
        with open(file_path, 'rb') as f:
            hashes['md5'] = hashlib.md5(f.read()).hexdigest()
            f.seek(0)
            hashes['sha1'] = hashlib.sha1(f.read()).hexdigest()
            f.seek(0)
            hashes['sha256'] = hashlib.sha256(f.read()).hexdigest()
        return hashes

    def get_metadata(self, file_path):
        metadata = {}
        file_stat = os.stat(file_path)
        metadata['owner'] = getpwuid(file_stat.st_uid).pw_name
        metadata['group'] = getgrgid(file_stat.st_gid).gr_name
        metadata['permissions'] = stat.filemode(file_stat.st_mode)
        return metadata

    def save_search(self, search_params):
        with open('search_history.txt', 'a') as f:
            f.write(str(search_params) + '\n')

def main():
    directory = input("Enter directory path: ")
    filename = input("Enter filename (optional): ")
    extensions = input("Enter file extensions (optional, comma-separated, e.g., .txt, .docx): ")
    exclude_dirs = input("Enter directories to exclude (optional, comma-separated): ")
    min_size = input("Enter minimum file size (optional, bytes): ")
    max_size = input("Enter maximum file size (optional, bytes): ")
    regex = input("Enter regex pattern (optional): ")
    content = input("Enter file content to search (optional): ")
    min_date = input("Enter minimum file date (optional, YYYY-MM-DD): ")
    max_date = input("Enter maximum file date (optional, YYYY-MM-DD): ")

    filename = filename.strip() if filename else None
    extensions = [ext.strip() for ext in extensions.split(",")] if extensions else None
    exclude_dirs = [dir.strip() for dir in exclude_dirs.split(",")] if exclude_dirs else None
    min_size = int(min_size) if min_size else None
    max_size = int(max_size) if max_size else None
    min_date = datetime.strptime(min_date, "%Y-%m-%d").date() if min_date else None
    max_date = datetime.strptime(max_date, "%Y-%m-%d").date() if max_date else None

    search = FileSearch(directory)
    search_thread = threading.Thread(target=search.search_files, args=(filename, extensions, exclude_dirs, min_size, max_size,
                                                                  regex, content, min_date, max_date))
    search_thread.start()
    search_thread.join()

    print("\nDone.")
    if search.results:
        print("Matching files:")
        for file_path, file_size, file_date in search.results:
            hashes = search.calculate_hashes(file_path)
            metadata = search.get_metadata(file_path)
            print(f"{file_path} ({file_size} bytes, {file_date})")
            print(f"  Hashes: MD5={hashes['md5']}, SHA-1={hashes['sha1']}, SHA-256={hashes['sha256']}")
            print(f"  Metadata: Owner={metadata['owner']}, Group={metadata['group']}, Permissions={metadata['permissions']}")
    else:
        print("No matching files found.")

    search_params = {
        'directory': directory,
        'filename': filename,
        'extensions': extensions,
        'exclude_dirs': exclude_dirs,
        'min_size': min_size,
        'max_size': max_size,
        'regex': regex,
        'content': content,
        'min_date': min_date,
        'max_date': max_date
    }
    search.save_search(search_params)


if __name__ == "__main__":
    main()