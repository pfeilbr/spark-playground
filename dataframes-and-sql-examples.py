from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "dataframes-and-sql-examples")
sqlContext = SQLContext(sc)

df = sqlContext.jsonFile("data/wwdc-sessions-json-obj-on-each-line.json")

# Show the content of the DataFrame
df.show()

# Print the schema in a tree format
df.printSchema()

# Select only the "name" column
df.select("title").show()

# register dataframe as table
df.registerTempTable("session")

# use sql to query the table
years = sqlContext.sql("select year from session")
years.show()