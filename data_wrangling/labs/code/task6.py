import pandas as pd
import sqlite3
from mlxtend.frequent_patterns import apriori, association_rules
from PIL import Image, ImageDraw, ImageFont

def report_top_association_rules(support_threshold: int, confidence_threshold: float):    

    # establish db connection
    db_path = '../output/cleaned_data.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # read OrderProducts data from db
    cursor.execute('SELECT order_id, product_id FROM OrderProducts')
    results = cursor.fetchall()
    order_products_df = pd.DataFrame(results, columns=['order_id', 'product_id'])
    # print('no. of OrderProducts', order_products_df.shape[0])

    # read Products data from db
    cursor.execute('SELECT product_id, product_name from Products')
    results = cursor.fetchall()
    products_df = pd.DataFrame(results, columns=['product_id', 'product_name'])
    # print('no. of Products', products_df.shape[0])

    # read csv file into dataframe
    df_orders = pd.read_csv('../output/task4_output.csv')
    # print('no. of orders', df_orders.shape[0])

    # filter out order for sunday having checkout_value > 3000
    filtered_orders_df = df_orders[(df_orders['order_dow'] == 0) & (df_orders['checkout_value'] > 3000)]
    # print('filtered orders', filtered_orders_df.shape[0])

    # filter out ineligible records from order_products df
    order_products_df = order_products_df[order_products_df['order_id'].isin(filtered_orders_df['order_id'])]

    # Merge the dataframes on the 'order_id' column
    result_df = pd.merge(order_products_df, products_df, on='product_id', how='left')
    # print('count of recrods for valid order-product mappings', result_df.shape[0])

    # map order_ids with their product_ids
    basket_df = result_df.groupby(['order_id', 'product_name']).size().unstack(fill_value=0)
    # print(basket_df.head(10))
    basket_df = basket_df.map(lambda x: True if x > 0 else False)
    # print(basket_df.head(10))

    # apply the Apriori algorithm for size-2 itemsets
    frequent_products = apriori(basket_df, min_support=support_threshold/len(basket_df), use_colnames=True)

    # convert support to count
    frequent_products['count'] = frequent_products['support'] * len(basket_df)
    # print(frequent_itemsets)

    # generate association rules
    association_rules_df = association_rules(frequent_products, metric='confidence', min_threshold = confidence_threshold)
    # print(association_rules_df.head())

    # get support counts for rules obtained
    # apriori results contains support count for all items >= support_threshold, 
    # however, association rule has return the results having confidence >= confidence_threshold
    # this step will allow us to find support count for each rule, by combining both columns (antecedents, consquents)
    # association_rules_df['support_count'] = association_rules_df['antecedents'].combine(association_rules_df['consequents'], lambda x,y: frequent_products.loc[frequent_products['itemsets'] == x.union(y), 'count'].values[0])

    # sort each value for antecedent and consquent columns
    association_rules_df['antecedent'] = association_rules_df['antecedents'].apply(lambda x: ', '.join(sorted(x)))
    association_rules_df['consequent'] = association_rules_df['consequents'].apply(lambda x: ', '.join(sorted(x)))

    # sort by value length and column 
    sorted_rules = association_rules_df.sort_values(by=['antecedent', 'consequent']).sort_values(by=['antecedents'], key=lambda x: x.apply(len), ascending=True, kind='stable')

    # display results
    for _, row in sorted_rules.iterrows():
        print(f"{row['antecedent']} -> {row['consequent']}")


    

report_top_association_rules(10, 1)