# Program 3: Automated CSV File Inspector and Data Exporter

import csv
import os


def read_file(filename, delimiter):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data = list(reader)

    return reader.fieldnames, data


def inspect_data(fields, data):
    print("\n===== File Information =====")

    print("Number of rows:", len(data))
    print("Number of columns:", len(fields))

    print("\nColumns:")
    for field in fields:
        print("-", field)

    print("\nNumerical Column Statistics:")

    for field in fields:
        values = []

        for row in data:
            try:
                values.append(float(row[field]))
            except (ValueError, TypeError):
                pass

        if values:
            total = sum(values)
            average = total / len(values)

            print("\nColumn:", field)
            print("Minimum:", min(values))
            print("Maximum:", max(values))
            print("Average:", round(average, 2))


def export_data(fields, data, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(data)

    print("\nData exported successfully to:", output_file)


def main():
    print("===== CSV File Inspector =====")

    filename = input("Enter CSV/TSV filename: ")

    if not os.path.exists(filename):
        print("File does not exist!")
        return

    extension = os.path.splitext(filename)[1].lower()

    if extension == ".tsv":
        delimiter = "\t"
    else:
        delimiter = ","

    try:
        fields, data = read_file(filename, delimiter)

        inspect_data(fields, data)

        choice = input("\nDo you want to export the data? (y/n): ")

        if choice.lower() == "y":
            output_file = input("Enter output filename: ")
            export_data(fields, data, output_file)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
