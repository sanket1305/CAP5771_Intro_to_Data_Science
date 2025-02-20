import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from datetime import datetime
from io import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# function to describe dataset, including column types and different statistics for numerical dtype
def describe_data(df):
    output = StringIO()     # Create a StringIO object to capture

    print("***Describing the data:***", file=output)
    num_rows, num_columns = df.shape

    print(f"Number of rows: {num_rows}", file=output)
    print(f"Number of columns: {num_columns}", file=output)

    # added this code based on data observation
    df["Date"] = pd.to_datetime(df["Date"], format = "mixed")

    df = df.astype({
        'Type': 'category',
        'Method': 'category',
        'Postcode': 'category',
        'YearBuilt': 'category',
        'Regionname': 'category'
    })

    print("\nColumn details:", file=output)
    for column in df.columns:
        col_data = df[column]
        col_dtype = col_data.dtype
        print(f"\nColumn: {column}, Type: {col_dtype}", file=output)

        # if data type is numeric, then calculate min, max, mean, median
        if pd.api.types.is_numeric_dtype(col_data):
            min_val = col_data.min()
            max_val = col_data.max()

            mean_val = col_data.mean()
            median_val = col_data.median()

            print(f"  Min: {min_val}", file=output)
            print(f"  Max: {max_val}", file=output)
            print(f"  Mean: {mean_val:.2f}", file=output)
            print(f"  Median: {median_val}", file=output)
        elif pd.api.types.is_categorical_dtype(col_data) or col_data.dtype == 'object':
            # Note 1 in Learning.md
            # some columns like Type, Method, postcode, YearBuilt, Regionname can be treated as category ???
            num_categories = col_data.nunique()
            print(f"  Number of categories: {num_categories}", file=output)

            if num_categories <= 10:
                print("  Counts per category:", file=output)
                category_counts = col_data.value_counts()
                for index, value in category_counts.items():
                    print(f"   {index}: {value}", file=output)
        elif pd.api.types.is_datetime64_any_dtype(col_data):
            # why "Date" column was treated as object above ???? should we convert it??
            min_date = col_data.min()
            max_date = col_data.max()
            print(f"  Date Range: {min_date} to {max_date}", file=output)
            print(f"  Number of unique dates: {col_data.nunique()}", file=output)
        else:
            unique_vals = col_data.unique()
            if len(unique_vals) <= 10:
                print("  Unique values:", file=output)
                for val in unique_vals:
                    print(f"    {val}", file=output)
    
    return num_rows, num_columns, output.getvalue()

def count_nulls(df):
    print("Describing Nulls in the data:")

    # null counts for each column
    null_counts_columns = df.isnull().sum()
    print("Null Counts per variable:")
    print(null_counts_columns)

    # null counts for each row
    null_counts_rows = df.isnull().sum(axis=1)
    # identifying max no. of nulls in a row
    max_nulls = null_counts_rows.max()
    # number of rows with most nulls
    rows_with_most_nulls = null_counts_rows[null_counts_rows == max_nulls].index.tolist()

    # calculating % of rows having any nulls
    total_rows = len(df)
    rows_with_any_nulls = (null_counts_rows > 0).sum()
    percentage_with_nulls = (rows_with_any_nulls / total_rows) * 100

    print(f"\nRows with the highest number of nulls ({max_nulls} nulls):")
    print(rows_with_most_nulls)
    print(rows_with_any_nulls)
    print(f"Percentage of rows with any nulls: {percentage_with_nulls:.2f}%")

    directory = "Images"
    # creating 2 subplots with 1st one being 3 times as of 2nd one
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5), gridspec_kw={'width_ratios': [3, 1]})

    # plotting histogram for no. of null values in rows
    sns.histplot(null_counts_rows, bins=max_nulls, color='blue', ax=ax1)
    ax1.set_title('Histogram of Nulls Per Row')
    ax1.set_xlabel('Number of Nulls')
    ax1.set_ylabel('Frequency of Rows')
    ax1.grid(True)

    for p in ax1.patches:
        ax1.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom', color='black', xytext=(0, 5), textcoords='offset points')

    # plotting barplot for finding outliers for null_counts_rows data
    sns.boxplot(y=null_counts_rows, color='green', ax=ax2)
    ax2.set_title('Box Plot of Nulls Per Row')
    ax2.set_ylabel('Number of Nulls')  

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{directory}/Null_distributions_{current_time}.png"
    plt.savefig(filename)
    plt.close()
    print(f"Saved histogram and boxplot as: {filename}")

    # based on the graph generated we can see that,
    # only 3 oberservation has more than 10 null values in rows and are outliers
    # most rows will have 0-2 null values in them




# Function to save findings to PDF using ReportLab
def save_findings_to_pdf(content, output_file="data_findings.pdf"):
    """
    Save findings into a PDF using ReportLab.

    Parameters:
        content (str): The text content to write into the PDF.
        output_file (str): The name of the output PDF file.
    """
    pdf = canvas.Canvas(output_file, pagesize=letter)

    # Add title and metadata
    pdf.setTitle("Data Description Report")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, 750, "Data Description Report")

    # Add date and time
    current_date = datetime.now().strftime("%A, %B %d, %Y, %I:%M %p")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(100, 730, f"Generated on: {current_date}")

    # Add content line by line
    pdf.setFont("Helvetica", 12)
    y_position = 700
    line_height = 14

    for line in content.split("\n"):
        if y_position < 50:  # Check if there's enough space on the page
            pdf.showPage()  # Create a new page
            y_position = 750

        pdf.drawString(50, y_position, line)
        y_position -= line_height

    pdf.save()
    print(f"PDF saved as '{output_file}'")