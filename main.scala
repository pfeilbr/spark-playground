import org.apache.log4j.{Level, Logger}

val rootLogger = Logger.getRootLogger()
rootLogger.setLevel(Level.ERROR)

val textFile = sc.textFile("file:///src/data/wwdc-sessions-json-obj-on-each-line.json")
textFile.count()
