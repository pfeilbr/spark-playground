from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "dataframes-and-sql-examples")
sc.setLogLevel("WARN")
sqlContext = SQLContext(sc)

df = sqlContext.read.json("data/wwdc-sessions-json-obj-on-each-line.json")
df.createTempView("sessions")
sessions = sqlContext.sql("select id, title from sessions")
sessions.show(5)


# # Show the content of the DataFrame
# df.show()

# print('count: %d' % df.count())

# # Print the schema in a tree format
# df.printSchema()

# # Select only the "name" column
# df.select("title").show()

# # register dataframe as table
# df.registerTempTable("session")

# # use sql to query the table
# years = sqlContext.sql("select year from session")
# years.show()