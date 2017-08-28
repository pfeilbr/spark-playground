from pyspark.sql import SparkSession

logFile = "simple-app.py"  # Should be some file on your system
appName = "simple-app"
master = "local[4]" # local with 4 cores
spark = SparkSession.builder.appName(appName).master(master).getOrCreate()
spark.sparkContext.setLogLevel("WARN")
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()