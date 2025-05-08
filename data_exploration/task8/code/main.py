import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

# 1. function to plot line chart illustrating sales volume over time
def sales_trends_over_time():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get aggregated total_selling_price over each month
    query = "SELECT " +\
                "sum(selling_price) as total_selling_price, " +\
                "strftime('%Y-%m', datetime(sold_on, 'unixepoch')) AS formatted_date " +\
            "FROM "+\
                "Sales " +\
            "GROUP BY " +\
                "formatted_date " +\
            "ORDER BY " +\
                "formatted_date"
    df_sales_data = pd.read_sql(query, conn)

    conn.close()

    # print(len(df_sales_data))
    # print(df_sales_data.size)

    # we have data now plot the grph
    plt.figure(1, figsize=(35, 8))
    plt.plot(df_sales_data['formatted_date'], df_sales_data['total_selling_price'], marker='o')

    plt.title('Price Over Time', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Price', fontsize=8)

    # if you want to roatet labels on x axis
    plt.xticks(rotation=45)

    plt.grid(True)
    plt.tight_layout()

    plt.savefig('../images/sales_trend.png')

# 2. function to plot bar chart displaying the top 10 products based on total sales
def product_performance():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get top 10 products based on sales from table
    query = "SELECT " +\
                "p.name, s.total_sales " +\
            "FROM " +\
                "ProductDetail as p " +\
            "INNER JOIN " +\
                "(SELECT " +\
                    "product_detail_id, " +\
                    "SUM(selling_price) as total_sales " +\
                "FROM " +\
                    "Sales " +\
                "GROUP BY " +\
                    "product_detail_id " +\
                "ORDER BY " +\
                    "total_sales " +\
                "DESC LIMIT 10) as s " +\
            "ON " +\
                "p.id = s.product_detail_id "+\
            "ORDER BY " +\
                "s.total_sales ASC"
    df_sales_data = pd.read_sql(query, conn)

    # print(df_sales_data)

    # Create horizontal bar chart
    fig, ax = plt.subplots(figsize=(16, 8), num="top products")
    bars = ax.barh(df_sales_data['name'], df_sales_data['total_sales'])

    # Add bar labels on top of bars 
    ax.bar_label(bars, label_type='edge', padding=4)

    # Customize the plot
    ax.set_xlabel('Products')
    ax.set_title('Top 10 Products (based on sales)')

    # Adjust layout and display
    plt.tight_layout()

    # uncomment below code to save graph in vertical format

    # plt.figure(2, figsize=(14, 6))
    # plt.barh(df_sales_data['name'], df_sales_data['total_sales'])

    # # Add labels and title
    # plt.xlabel('Categories')
    # plt.ylabel('Values')
    # plt.title('Basic Vertical Bar Graph')

    # plt.xticks(rotation='vertical', ha='right')
    # plt.tight_layout(pad=2.0)
    # plt.grid(True)

    # Display the plot
    plt.savefig('../images/product_performance.png')

# 3. function to plot bar chart showing total sales by retail location
def regional_performance():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get sales data by region from table
    query = "SELECT "+\
                "r.store_name, s.total_sales "+\
            "FROM "+\
                "RetailLocation as r "+\
            "INNER JOIN "+\
                "(SELECT "+\
                    "retail_location_id, SUM(selling_price) as total_sales "+\
                "FROM "+\
                    "Sales "+\
                "GROUP BY "+\
                    "retail_location_id "+\
                "ORDER BY "+\
                    "total_sales DESC) as s "+\
            "ON "+\
                "r.id = s.retail_location_id "+\
            "ORDER BY "+\
                "r.store_name"
    df_sales_data = pd.read_sql(query, conn)

    # All the labels has 'GetorRetialNYC tag, remove it and keep labels compact to fit in graph
    df_sales_data['store_name'] = df_sales_data['store_name'].str.replace("GatorRetailNYC @ ", "")

    # print(df_sales_data)

    # Create horizontal bar chart
    fig, ax = plt.subplots(figsize=(10, 6), num="regional performance")
    bars = ax.bar(df_sales_data['store_name'], df_sales_data['total_sales'])

    # Add bar labels on top of bars
    ax.bar_label(bars, label_type='edge', padding=2, rotation=90)
    ax.set_ylim(top=10000)

    # Customize the plot
    ax.set_xlabel('Regions')
    ax.set_ylabel('Total Sales')
    ax.set_title('Total sales (by Region)')

    # Adjust layout and display
    plt.tight_layout()

    plt.xticks(rotation='vertical')
    plt.tight_layout(pad=2.0)

    # Display the plot
    plt.savefig('../images/regional_performance.png')

# 4. function to plot histogram representing the distribution of employee salaries across 50 bins.
def salary_distribution():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get salary of all employees from table
    query = "SELECT salary FROM Salary"
    df_salary_data = pd.read_sql(query, conn)

    # print(df_salary_data)

    plt.figure(4, figsize=(10, 6))
    plt.hist(df_salary_data['salary'], bins=50, edgecolor='black')

    plt.title('Employee Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')

    # Add grid lines for better readability
    plt.grid(axis='y', alpha=0.75)

    plt.tight_layout()

    # Display the plot
    plt.savefig('../images/salary_distribution.png')

# 5. function for scatter plot comparing total campaign spending to revenue generated (sales) for each product
def campaign_effectiveness():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get revenue and expenses for each product from tables
    query = "SELECT "+\
                "s.product_detail_id, s.revenue, c.expenses "+\
            "FROM "+\
                "(SELECT "+\
                    "product_detail_id, sum(selling_price) as revenue "+\
                "FROM "+\
                    "Sales "+\
                "GROUP BY "+\
                    "product_detail_id) as s "+\
            "INNER JOIN "+\
                "(SELECT "+\
                    "target_product_id, expenditure as expenses "+\
                "FROM Campaigns) as c "+\
            "ON "+\
                "s.product_detail_id = c.target_product_id"
    df_product_data = pd.read_sql(query, conn)

    # print(df_product_data)

    # create scatter plot
    plt.figure(5, figsize=(12, 6))
    plt.scatter(df_product_data['expenses'], df_product_data['revenue'])

    # Add labels and title
    plt.xlabel('Expenditure')
    plt.ylabel('Revenue')
    plt.title('Revenue (Sales) vs Expenses for each product')

    # print(df_product_data['expenses'].isna().sum())  # Check for NaN
    # print(df_product_data['revenue'].isna().sum())
    # print(df_product_data['product_detail_id'].isna().sum())

    plt.grid(True)

    # Display the plot
    plt.savefig('../images/campaign_effectiveness.png')
    # plt.show()

sales_trends_over_time()
product_performance()
regional_performance()
salary_distribution()
campaign_effectiveness()