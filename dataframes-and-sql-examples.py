from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "dataframes-and-sql-examples")
sqlContext = SQLContext(sc)

df = sqlContext.jsonFile("data/wwdc-sessions-json-obj-on-each-line.json")

# Show the content of the DataFrame
df.show()

# Print the schema in a tree format
df.printSchema()