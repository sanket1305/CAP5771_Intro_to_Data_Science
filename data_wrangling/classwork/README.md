# This contains the classwork done for "data_wranging"

Data Cleaning

For this purpose we will import a dataset from Kaggle. We will use kagglehub to import the data into our Data wrangling demo folder.

`
import kagglehub
kagglehub.dataset_download("anthonypino/melbourne-housing-market")
`

The data will land in `.cache` folder, with below file names. Move both files to our workspace using `mv` command.

Use the `descriptive_utils.py` to understand what do we need to do in terms of data cleaning. Let's go function by function

def describe_data(df):

