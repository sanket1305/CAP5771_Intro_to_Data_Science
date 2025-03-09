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
    ax.scatter(train_data['days_since_prior_order'], train_data['number_of_items'], train_data['checkout_value'], color='blue', label='Existing Data')

    # Plot predicted missing values
    ax.scatter(missing_data['days_since_prior_order'], missing_data['number_of_items'], predicted_values, color='red', label='Predicted Data')

    # Create a mesh grid for the regression plane
    A_mesh, B_mesh = np.meshgrid(np.linspace(result_df['days_since_prior_order'].min(), result_df['days_since_prior_order'].max(), 50),
                                np.linspace(result_df['number_of_items'].min(), result_df['number_of_items'].max(), 50))
    C_mesh = model.predict(pd.DataFrame(np.c_[A_mesh.ravel(), B_mesh.ravel()],
                                    columns=['days_since_prior_order', 'number_of_items'])).reshape(A_mesh.shape)

    # Plot the regression plane
    ax.plot_surface(A_mesh, B_mesh, C_mesh, alpha=0.4, color='cyan')

    # Set labels
    ax.set_xlabel('days_since_prior_order (Feature 1)')
    ax.set_ylabel('number_of_items (Feature 2)')
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

    df_order_item_count = pd.DataFrame(results, columns=['order_id', 'number_of_items'])

    # read csv file into dataframe
    df_orders = pd.read_csv("../output/task3_output.csv")

    # Merge the dataframes on the 'order_id' column
    result_df = pd.merge(df_orders, df_order_item_count, on='order_id', how='left')

    # drop records with no prev_orders (number_of_items missing)
    result_df = result_df.dropna(subset=['number_of_items'])

    # missing data imputation for 'days_since_prior_order' column
    result_df['days_since_prior_order'] = result_df['days_since_prior_order'].fillna(0)

    # getting non missing checkout value rows
    train_data = result_df[result_df['checkout_value'].notnull()]

    # get user specific data
    user_df = train_data[train_data['user_id'] == user_id]

    # Check if the DataFrame is empty
    if user_df.empty:
        # Features and target variable for training
        X_train = train_data[['number_of_items', 'days_since_prior_order']]
        y_train = train_data['checkout_value']
    else:
        X_train = user_df[['number_of_items', 'days_since_prior_order']]
        y_train = user_df['checkout_value']

    # Features for prediction
    X_missing = pd.DataFrame([[number_of_items, days_since_prior_order]],
                           columns=['number_of_items', 'days_since_prior_order'])

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Calculate R^2 score
    r2_score = model.score(X_train, y_train)
    print("score:", round(r2_score, 2))

    # print the prediction for given user
    predicted_value = model.predict(X_missing)[0]
    print("predicted checkout_value:", round(predicted_value))

    # uncoment below line if you want to visualise the model
    # plot(model, train_data, X_missing, result_df, predicted_value)
    return model

predict_checkout_value(93942, 0, 0)