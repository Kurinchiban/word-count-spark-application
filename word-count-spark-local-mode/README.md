# SparkContext vs. SparkSession

## SparkContext

`SparkContext` is the original entry point for Spark functionality, used primarily in older versions (before Spark 2.0). It is responsible for coordinating the Spark application and connecting to the cluster. It also manages resources and serves as the conduit to create and execute RDDs (Resilient Distributed Datasets), which are the building blocks of data in Spark.

## SparkSession

Introduced in Spark 2.0, `SparkSession` is now the recommended entry point for working with Spark. It serves as a unified context for Spark functionalities, combining the capabilities of `SQLContext`, `HiveContext`, and `SparkContext`. Through `SparkSession`, users can create DataFrames and interact with Spark's SQL, DataFrame, and streaming APIs.

## Evolution from SparkContext to SparkSession

Before Spark 2.0, Spark offered different contexts (e.g., `SQLContext`, `HiveContext`, `SparkContext`) for different types of operations. This approach could be cumbersome, requiring users to manage multiple contexts and import various libraries.

**Solution**: `SparkSession` unified these contexts, allowing users to work with RDDs, DataFrames, and SQL queries within a single entry point. This unified API simplifies code and reduces the learning curve, making it easier to perform both structured and unstructured data processing.

---

## Example: Word Count Using RDD Transformations

1. **flatMap** breaks lines into words.
2. **map** pairs each word with a count of 1.
3. **reduceByKey** aggregates the counts for each unique word, giving a final RDD of word counts.

## Requirements

To run this code, you need to install `pyspark`. You can install it using the following command:

```bash
pip install pyspark