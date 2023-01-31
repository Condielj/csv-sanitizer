import pandas as pd
import sys


def remove_non_utf8(name):
    # Read in the CSV file
    print(f"Sanitizing {name}... ")
    df = pd.read_csv(name, encoding="latin9")

    # Replace any non-UTF-8 characters with a space
    df.replace({r"[^\x00-\x7F]+": " "}, regex=True, inplace=True)

    # Write the cleaned data to a new CSV file
    output = f"{name[:-4]}_sanitized.csv"
    df.to_csv(output, encoding="utf-8", index=False)

    print(f"Done. Output to {output}.")


if __name__ == "__main__":
    remove_non_utf8(sys.argv[1])
