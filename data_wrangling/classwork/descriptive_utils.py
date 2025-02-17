import pandas as pd
from io import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime

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