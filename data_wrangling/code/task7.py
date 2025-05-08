import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlite3
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# for 1st plot we were asked to use scatter plot
# for rest of the task the plot type has been determined by the unique value aong x-index

# function to get Order Products from DB
def get_orderProducts():
    # establish db connection
    db_path = '../output/cleaned_data.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # read OrderProducts data from db
    cursor.execute('SELECT order_id, COUNT(*) as number_of_items FROM OrderProducts GROUP BY order_id')
    results = cursor.fetchall()
    return pd.DataFrame(results, columns=['order_id', 'number_of_items'])

# function to get cleaned orders from task4 csv
def get_orders():
    return pd.read_csv('../output/task4_output.csv')

# 1. function for scatter plot comparing checkout value to time of purchase (order hr of day)
def plot_checkout_vs_order_hour():
    # get data
    df = get_orders()
    df = df[(df['transaction_type'] == 'instore') | (df['transaction_type'] == 'online')]
    print(df.shape)

    # downsampling for visualization
    df_sampled = df.groupby('transaction_type').apply(lambda x: x.sample(500, random_state=42))

    # plotting the scatter plot
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=df_sampled,
        x='order_hour_of_day',
        y='checkout_value',
        hue='transaction_type',
        alpha=0.6,
        palette='Set1'
    )

    plt.title('Checkout Value vs Hour of Day (Downsampled to 500 records)')
    plt.xlabel('Hour of Day')
    plt.ylabel('Checkout Value')
    plt.savefig('../output/task7_order_hour.png')

# 2. function for box plot comparing checkout value to order day of week
def plot_checkout_vs_order_dow():
    # get data
    df = get_orders()
    df = df[(df['transaction_type'] == 'instore') | (df['transaction_type'] == 'online')]

    # generating the box plot
    plt.figure(figsize=(12, 6))
    sns.boxplot(
        data=df,
        x='order_dow',
        y='checkout_value',
        hue='transaction_type',
        palette='Set1'
    )

    plt.title('Checkout Value vs Day of Week')
    plt.xlabel('Day of week')
    plt.ylabel('Checkout Value')
    plt.savefig('../output/task7_order_dow.png')

# 3. function for box plot comparing checkout value to days since prior order
def plot_checkout_vs_days_since_prior_order():
    # get data 
    df = get_orders()
    df['days_since_prior_order'] = df['days_since_prior_order'].astype(int)
    df = df[(df['transaction_type'] == 'instore') | (df['transaction_type'] == 'online')]

    # generating the box plot
    plt.figure(figsize=(12, 6))
    sns.boxplot(
        data=df,
        x='days_since_prior_order',
        y='checkout_value',
        hue='transaction_type',
        palette='Set1'
    )

    plt.title('Checkout Value vs Day of Week')
    plt.xlabel('Day of week')
    plt.ylabel('Checkout Value')
    plt.savefig('../output/task7_days_since_prior_order.png')

# 4. function for scatter plot for checkout value vs number of items
def plot_checkout_vs_number_of_items():
    # get orders data 
    df = get_orders()
    df['days_since_prior_order'] = df['days_since_prior_order'].astype(int)
    df = df[(df['transaction_type'] == 'instore') | (df['transaction_type'] == 'online')]

    # get item count for each order
    item_count_df = get_orderProducts()
    df = pd.merge(df, item_count_df, on='order_id', how='inner')
    # print(df.columns)

    # plotting the scatter plot
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=df,
        x='number_of_items',
        y='checkout_value',
        hue='transaction_type',
        alpha=0.6,
        palette='Set1'
    )

    plt.title('Checkout Value vs Number of Items')
    plt.xlabel('Number of Items')
    plt.ylabel('Checkout Value')
    plt.savefig('../output/task7_number_of_items.png')

# 5. function to scatter plot pca vs checkout value
def plot_pca_vs_checkout_value():
    # get orders data 
    df = get_orders()
    df['days_since_prior_order'] = df['days_since_prior_order'].astype(int)
    df = df[(df['transaction_type'] == 'instore') | (df['transaction_type'] == 'online')]

    # convert values form float to int
    df['days_since_prior_order'] = df['days_since_prior_order'].astype(int)

    # initial features
    x = df[['order_hour_of_day', 'order_dow', 'days_since_prior_order']]
    
    # standaridze the data
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    # apply PCA
    pca = PCA(n_components=2)
    x_pca = pca.fit_transform(x_scaled)

    # build df to draw scatter plot
    final_df = pd.DataFrame(data=x_pca, columns=['PC1', 'PC2'])
    final_df['transaction_type'] = df['transaction_type'].values
    final_df['checkout_value'] = df['checkout_value'].values

    # plotting the scatter plot
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data = final_df,
        x = 'PC1',
        y = 'PC2',
        size = 'checkout_value',
        hue ='transaction_type',
        alpha = 0.6,
        palette = 'Set1'
    )

    plt.title('PCA (of time based value) vs (Checkout Value)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal COmponent 2')
    plt.savefig('../output/task7_pca_vs_checkout.png')


plot_checkout_vs_order_hour()
plot_checkout_vs_order_dow()
plot_checkout_vs_days_since_prior_order()
plot_checkout_vs_number_of_items()
plot_pca_vs_checkout_value()