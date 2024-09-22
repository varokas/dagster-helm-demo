from dagster import asset, AssetExecutionContext
import pandas as pd

@asset
def asset1(context: AssetExecutionContext):
    df = pd.read_csv("s3://ray-example-data/iris.csv")
    context.log.info(df.head())