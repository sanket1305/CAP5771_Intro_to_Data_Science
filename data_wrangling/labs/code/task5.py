import io
import pandas as pd
import sqlite3
import sys
from mlxtend.frequent_patterns import apriori
from PIL import Image, ImageDraw, ImageFont

def mine_frequent_itemsets(support_count_threshold=10):
    # capture print oputput statements
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    # establish db connection
    db_path = "../output/cleaned_data.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # read OrderProducts data from db
    cursor.execute("SELECT order_id, product_id FROM OrderProducts")
    results = cursor.fetchall()
    order_products_df = pd.DataFrame(results, columns=['order_id', 'product_id'])
    # print("no. of OrderProducts", order_products_df.shape[0])

    # read Products data from db
    cursor.execute("SELECT product_id, product_name from Products")
    results = cursor.fetchall()
    products_df = pd.DataFrame(results, columns=['product_id', 'product_name'])
    # print("no. of Products", products_df.shape[0])

    # read csv file into dataframe
    df_orders = pd.read_csv("../output/task4_output.csv")
    # print("no. of orders", df_orders.shape[0])

    # filter out order for sunday having checkout_value > 3000
    filtered_orders_df = df_orders[(df_orders['order_dow'] == 0) & (df_orders['checkout_value'] > 3000)]
    # print("filtered orders", filtered_orders_df.shape[0])

    # filter out ineligible records from order_products df
    order_products_df = order_products_df[order_products_df['order_id'].isin(filtered_orders_df['order_id'])]

    # Merge the dataframes on the 'order_id' column
    result_df = pd.merge(order_products_df, products_df, on='product_id', how='left')
    # print("count of recrods for valid order-product mappings", result_df.shape[0])

    # map order_ids with their product_ids
    basket_df = result_df.groupby(['order_id', 'product_name']).size().unstack(fill_value=0)
    # print(basket_df.head(10))
    basket_df = basket_df.map(lambda x: True if x > 0 else False)
    # print(basket_df.head(10))

    # apply the Apriori algorithm for size-2 itemsets
    frequent_products = apriori(basket_df, 
                                min_support=support_count_threshold/len(basket_df), 
                                use_colnames=True)

    # convert support to count
    frequent_products['count'] = frequent_products['support'] * len(basket_df)
    # print(frequent_itemsets)

    # filter out itemsets with count < support_count_threshold
    frequent_products = frequent_products[frequent_products['count'] >= support_count_threshold]

    # sort the products 
    frequent_products['itemset'] = frequent_products['itemsets'].apply(lambda x: ', '.join(sorted([str(product) for product in x])))
    frequent_products = frequent_products.sort_values(by='count', ascending=False)

    # extract top 10 products
    max_itemset_count = 7
    for count in range(1, max_itemset_count+1):
        product_set_df = frequent_products[frequent_products['itemsets'].apply(len) == count]
        if not product_set_df.empty:
            print(f"{count}-itemsets")
            first_10_products_df = product_set_df.head(10)
            for ind, row in first_10_products_df.iterrows():
                print(f"{int(row['count'])}: {row['itemset']}")
    
    # Capture the output
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    # convert text to image
    font = ImageFont.load_default()
    lines = output.split('\n')
    width = 800
    height = 20*len(lines)

    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    y = 0
    for line in lines:
        draw.text((10, y), line, font=font, fill='black')
        y += 20
    
    # save the image
    image.save('../output/task5_frequent_itemset.png')

    for line in lines:
        print(line)

mine_frequent_itemsets(10)