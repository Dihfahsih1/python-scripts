# import pandas as pd

# file_name = "list_of_emails.csv"

# file_name_output = "cleaned_emails.csv"

# df = pd.read_csv(file_name, sep="\t or ,")

# df.drop_duplicates(subset=None, inplace=True)

# df.to_csv(file_name_output, index=False)

infile = open("list_of_emails.csv", 'r')

outfile = open("cleaned_emails2.csv", 'w')

listLines = []

for line in infile:
    if line in listLines:
        continue
    else:
        outfile.write(line)
        listLines.append(line)
outfile.close()
infile.close()
