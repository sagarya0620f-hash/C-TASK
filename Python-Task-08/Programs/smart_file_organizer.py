import os
import shutil
from datetime import datetime
from collections import Counter


class SmartFileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path

        self.categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
            "Videos": [".mp4", ".mkv", ".avi", ".mov"],
            "Audio": [".mp3", ".wav", ".aac"],
            "Archives": [".zip", ".rar", ".7z"],
            "Programs": [".exe", ".msi", ".py", ".c", ".cpp", ".java"]
        }

        self.files = []
        self.stats = Counter()
        self.duplicates = []

    def validate_directory(self):
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError("Folder does not exist.")

        if not os.path.isdir(self.folder_path):
            raise NotADirectoryError("Invalid directory.")

    def scan_files(self):
        self.files = []

        for item in os.listdir(self.folder_path):
            full_path = os.path.join(self.folder_path, item)

            if os.path.isfile(full_path):
                self.files.append(item)

        print("\n===== Files Found =====")
        print(f"Total Files : {len(self.files)}\n")

        for file in self.files:
            name, ext = os.path.splitext(file)
            print(f"{file} ({ext})")
    def organize_files(self):
        self.stats = Counter()

        for file in self.files:
            source = os.path.join(self.folder_path, file)

            if not os.path.exists(source):
                continue

            _, ext = os.path.splitext(file)
            ext = ext.lower()

            category = "Others"

            for folder, extensions in self.categories.items():
                if ext in extensions:
                    category = folder
                    break

            destination_folder = os.path.join(self.folder_path, category)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination = os.path.join(destination_folder, file)

            try:
                shutil.move(source, destination)
                self.stats[category] += 1
            except FileExistsError:
                print(f"{file} already exists.")
            except PermissionError:
                print(f"Permission denied: {file}")

        print("\nFiles organized successfully.")

    def display_statistics(self):
        print("\n===== File Statistics =====")
        print(f"Total Files      : {len(self.files)}")
        print(f"Images           : {self.stats['Images']}")
        print(f"Documents        : {self.stats['Documents']}")
        print(f"Videos           : {self.stats['Videos']}")
        print(f"Audio            : {self.stats['Audio']}")
        print(f"Archives         : {self.stats['Archives']}")
        print(f"Programs         : {self.stats['Programs']}")
        print(f"Others           : {self.stats['Others']}")

    def search_file_name(self):
        keyword = input("\nEnter file name: ").lower()

        result = [f for f in self.files if keyword in f.lower()]

        if result:
            print("\nMatching Files:")
            for file in result:
                print(file)
        else:
            print("No matching files found.")

    def search_extension(self):
        ext = input("\nEnter extension (example .pdf): ").lower()

        result = [f for f in self.files if f.lower().endswith(ext)]

        if result:
            print("\nMatching Files:")
            for file in result:
                print(file)
        else:
            print("No matching files found.")

    def find_duplicates(self):
        counter = Counter(self.files)

        self.duplicates = [file for file, count in counter.items() if count > 1]

        print("\n===== Duplicate Files =====")

        if self.duplicates:
            for file in self.duplicates:
                print(file)
        else:
            print("No Duplicate Files Found")
    def generate_report(self):
        report_path = os.path.join(self.folder_path, "file_report.txt")

        with open(report_path, "w") as report:
            report.write("===== Smart File Organizer Report =====\n")
            report.write(f"Date : {datetime.now()}\n")
            report.write(f"Folder : {self.folder_path}\n")
            report.write(f"Total Files : {len(self.files)}\n\n")

            report.write("Category-wise Count\n")
            report.write("---------------------------\n")
            report.write(f"Images : {self.stats['Images']}\n")
            report.write(f"Documents : {self.stats['Documents']}\n")
            report.write(f"Videos : {self.stats['Videos']}\n")
            report.write(f"Audio : {self.stats['Audio']}\n")
            report.write(f"Archives : {self.stats['Archives']}\n")
            report.write(f"Programs : {self.stats['Programs']}\n")
            report.write(f"Others : {self.stats['Others']}\n\n")

            report.write("Duplicate Files\n")
            report.write("---------------------------\n")

            if self.duplicates:
                for file in self.duplicates:
                    report.write(file + "\n")
            else:
                report.write("No Duplicate Files Found\n")

            report.write("\nOrganized Folder Structure\n")
            report.write("---------------------------\n")

            for folder in os.listdir(self.folder_path):
                folder_path = os.path.join(self.folder_path, folder)

                if os.path.isdir(folder_path):
                    report.write(f"\n{folder}\n")

                    for file in os.listdir(folder_path):
                        report.write(f"   {file}\n")

        print("\nReport generated successfully.")
        print("Report saved as file_report.txt")


def main():
    print("===== Smart File Organizer =====")

    folder = input("Enter Folder Path: ")

    try:
        organizer = SmartFileOrganizer(folder)

        organizer.validate_directory()
        organizer.scan_files()
        organizer.organize_files()
        organizer.display_statistics()

        print("\nSearch Options")
        print("1. Search by File Name")
        print("2. Search by Extension")

        choice = input("Enter choice: ")

        if choice == "1":
            organizer.search_file_name()
        elif choice == "2":
            organizer.search_extension()

        organizer.find_duplicates()
        organizer.generate_report()

    except FileNotFoundError:
        print("Error: Folder does not exist.")

    except NotADirectoryError:
        print("Error: Invalid folder.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":
    main()