from dagster import asset, AssetExecutionContext
import polars as pl

@asset
def asset2(context: AssetExecutionContext):
    df = pl.read_csv("s3://ray-example-data/iris.csv")
    context.log.info(df.head())
