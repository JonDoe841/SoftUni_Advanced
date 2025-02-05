import os
from collections import defaultdict

# Input: Directory path
directory = input("Enter the directory path: ")

# Dictionary to store files grouped by their extensions
files_by_extension = defaultdict(list)

# Traverse the directory and its first nested level
for root, dirs, files in os.walk(directory):
    for file in files:
        # Get the file extension
        file_extension = os.path.splitext(file)[1]
        # Add the file to the corresponding extension group
        files_by_extension[file_extension].append(file)

    # Break after the first level of nesting
    break

# Sort extensions alphabetically
sorted_extensions = sorted(files_by_extension.keys())

# Write the report to report.txt
report_path = os.path.join(directory, "report.txt")
with open(report_path, 'w') as report_file:
    for extension in sorted_extensions:
        # Write the extension
        report_file.write(f"{extension}\n")
        # Sort files alphabetically and write them
        for file in sorted(files_by_extension[extension]):
            report_file.write(f"- - - {file}\n")

print(f"Report generated at: {report_path}")