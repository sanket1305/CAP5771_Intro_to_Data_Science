import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def plot(model, train_data, missing_data, result_df, predicted_values):
    # ===========================
    # 3D Plot with Regression Plane
    # ===========================
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot existing data points
    ax.scatter(train_data['days_since_prior_order'], train_data['item_count'], train_data['checkout_value'], color='blue', label='Existing Data')

    # Plot predicted missing values
    ax.scatter(missing_data['days_since_prior_order'], missing_data['item_count'], predicted_values, color='red', label='Predicted Data')

    # Create a mesh grid for the regression plane
    A_mesh, B_mesh = np.meshgrid(np.linspace(result_df['days_since_prior_order'].min(), result_df['days_since_prior_order'].max(), 50),
                                np.linspace(result_df['item_count'].min(), result_df['item_count'].max(), 50))
    C_mesh = model.predict(pd.DataFrame(np.c_[A_mesh.ravel(), B_mesh.ravel()],
                                    columns=['days_since_prior_order', 'item_count'])).reshape(A_mesh.shape)

    # Plot the regression plane
    ax.plot_surface(A_mesh, B_mesh, C_mesh, alpha=0.4, color='cyan')

    # Set labels
    ax.set_xlabel('days_since_prior_order (Feature 1)')
    ax.set_ylabel('item_count (Feature 2)')
    ax.set_zlabel('checkout_value (Target/Output)')

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()

def predict_checkout_value(user_id: int, number_of_items: int, days_since_prior_order: int = None) -> None:
    # print(user_id, number_of_items, days_since_prior_order)
    # get number of items in order
    # connect to db, to get "OrderProducts" table data (csv only has "Orders" table data)
    db_path = "../output/cleaned_data.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT order_id, count(*) FROM OrderProducts GROUP BY order_id")
    results = cursor.fetchall()

    df_order_item_count = pd.DataFrame(results, columns=['order_id', 'item_count'])

    # read csv file into dataframe
    df_orders = pd.read_csv("../output/task3_output.csv")

    # Merge the dataframes on the 'order_id' column
    result_df = pd.merge(df_orders, df_order_item_count, on='order_id', how='left')

    result_df['days_since_prior_order'] = result_df['days_since_prior_order'].fillna(0)

    user_df = result_df[result_df['user_id'] == user_id]

    # Check if the DataFrame is empty
    if not user_df.empty:
        check_not_null = user_df[user_df['checkout_value'].notnull()]
        if not check_not_null.empty:
            result_df = user_df.copy()
    
    result_df['item_count'] = result_df['item_count'].fillna(0)
    
    # Split the data into two parts
    train_data = result_df[result_df['checkout_value'].notnull()]
    missing_data = result_df[result_df['checkout_value'].isnull()]

    # Features and target variable for training
    X_train = train_data[['days_since_prior_order', 'item_count']]
    y_train = train_data['checkout_value']

    # Features for prediction
    X_missing = pd.DataFrame([[days_since_prior_order, number_of_items]],
                           columns=['days_since_prior_order', 'item_count'])

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Calculate R^2 score
    r2_score = model.score(X_train, y_train)
    print("score:", round(r2_score, 2))

    # print the prediction for given user
    predicted_value = model.predict(X_missing)[0]
    print("predicted checkout_value:", round(predicted_value))

    plot(model, train_data, X_missing, result_df, predicted_value)

predict_checkout_value(93942, 0, 0)