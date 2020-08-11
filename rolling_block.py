import matplotlib.pyplot as plt
import csv

def read_csv(csv_name):
    """
    reads a csv and pulls out the x and y coordinates
    :param csv_name: The name of the csv to be opened
    :return: a list of x and y coordinates
    """
    x = []
    y = []
    with open(csv_name, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
    return x, y


def write_csv(csv_name, x, y, average):
    """
    Creates a new csv using the given csv_name and adds all of the x, y, and rolling block average data to it
    :param csv_name: The name of the csv to be created
    :param x: A list of x-axis data
    :param y: A list of y-axis data
    :param average: A list of the rolling block average data
    :return: None
    """
    with open(csv_name, mode='w+') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(x)):
            if (i < len(average)):
                writer.writerow([x[i], y[i], average[i]])
            else:
                writer.writerow([x[i], y[i]])


def rolling_block(block, y):
    """
    Calculates the rolling block average of a given list using a given block size
    :param block: The size of the block for the rolling average
    :param y: The list of data points to be averaged
    :return: A list of the averaged data
    """
    average = []
    j = block - 1
    for i in range(len(y) - block):
        block_sum = 0
        while i <= j:
            block_sum += y[i]
            i += 1
        average.append(block_sum/block)
        j += 1
    return average


def plot_average(name, x, x_label, y, y_label, y_average, block):
    """
    Plots the rolling block average data and the regular un-smoothed data
    :param name: The name of the plot
    :param x: A list of the x-axis data
    :param x_label: The title of the x-axis
    :param y: A list of the y-axis data
    :param y_label: The title of the y-axis
    :param y_average: A list of the averaged data
    :param block: The size of the block used to calculate the rolling average
    :return: None
    """

    plt.plot(x, y)
    # Remove end indices of time that isn't used in average (equivalent to block)
    del x[-block:]

    plt.plot(x, y_average)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(name + ' using a rolling block of ' + str(block) + ' samples')
    plt.show()


def display_and_write_data(csv_name, x_label, y_label, csv_out_name, block_size):
    """
    Reads the CSV, displays the data and creates the new csv
    :param csv_name: The name of the csv to read from
    :param x_label: The title of the x-axis
    :param y_label: The title of the y-axis
    :param csv_out_name: The name of the csv to create/write to
    :param block_size: The size of the block used to calculate the rolling average
    :return: None
    """
    x, y = read_csv(csv_name)
    y_average = rolling_block(block_size, y)
    plot_average(csv_name, x, x_label, y, y_label,  y_average, block_size)
    write_csv(csv_out_name, x, y, y_average)






