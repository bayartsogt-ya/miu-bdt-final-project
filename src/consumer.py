#!/usr/bin/python3

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from textblob import TextBlob


def get_sentiment(tweet):
    return TextBlob(tweet).sentiment.polarity

def handle_rdd(rdd):
    if not rdd.isEmpty():
        global ss
        df = ss.createDataFrame(rdd, schema=['text', 'sentiment'])
        df.show()
        df.write.saveAsTable(name='default.tweets', format='hive', mode='append')

sc = SparkContext(appName="FinalProject")
ssc = StreamingContext(sc, 5)
ss = SparkSession.builder.appName("FinalProject").config("spark.sql.warehouse.dir", "/user/hive/warehouse").config("hive.metastore.uris", "thrift://localhost:9083").enableHiveSupport().getOrCreate()

ss.sparkContext.setLogLevel('WARN')

ks = KafkaUtils.createDirectStream(ssc, ['tweets'], {'metadata.broker.list': 'localhost:9092'})
lines = ks.map(lambda x: x[1])
transform = lines.map(lambda tweet: (tweet, get_sentiment(tweet)))
transform.foreachRDD(handle_rdd)

ssc.start()
ssc.awaitTermination()
