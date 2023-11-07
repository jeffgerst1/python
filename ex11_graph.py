# create a bar graph visualizing the different vaccine types and their frequency

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np
raw_file = "C:/Users/jeffg/Downloads/ex11_vaccineViz/ex11_vaccineViz/vaccine_data.txt"
def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file, and safely close it when we're done
    opened_file = open(raw_file)

    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Setup an empty list
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = next(csv_data)

    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the CSV file
    opened_file.close()

    return parsed_data

# update this function
def visualize_vaccineType(raw_file):
    """Visualize data by vaccine type in a bar graph"""
    vaccine_types = ["TT1", "TT2+", "BCG", "DTP1", "DTP3", "MCV1", "Pol1", "Pol3", "FULL", "PAB", "HepB1", "Hib1", "Hib3", "TT2", "TT3", "TT4", "TT5", "PCV1", "PCV3"]
    data_file = parse(raw_file, ",")
    counter = Counter([item["vaccine"] for item in data_file if item["vaccine"] in vaccine_types])
    labels = tuple(counter.keys())
    xlocations = np.array(range(len(labels))) + 0.5
    width = 0.5
    plt.xlabel('Vaccine Type')
    plt.ylabel('Number of Patients')
    plt.title('Distribution of Vaccines by Type')
    # Set the y-axis limits
    plt.ylim([0, max(counter.values())+1])

    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations, labels, rotation=90)

    # Save the plot
    plt.savefig("vaccine_type_bar_chart.png")

    # Close figure
    plt.clf()
    # visualize_days() # commenting out the visualize_days() function
def main():
    visualize_vaccineType(raw_file)
if __name__ == "__main__":
    main()    