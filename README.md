# miu-bdt-final-project
`Twitter API v2 -> Kafka -> Spark Streaming -> Hive`

This repo includes source of the final project implemented as a final project of CS523: Big Data Technology in Maharishi Internation University.


Topics:
* Requirements
* 

## Requirements

| Name | Version |
| - | - |
| Lubuntu | 20.04 |
| Python | 3.6.7 |
| Scala | 2.11.12 |
| Hadoop | 2.8.5 |
| Hive | 2.3.5 |
| Kafka (For Hadoop2) | 2.12 |
| Spark (For Hadoop2) | 3.1.2 |

Python requirements:

| Package | Version |
| - | - |
| pyspark | 2.4.3 |
| kafka-python | 1.4.6 |
| tweepy | 4.0.0 |

Download spark streaming to kafka util from 
https://search.maven.org/search?q=a:spark-streaming-kafka-0-8-assembly_2.11

Hive Installer
http://archive.apache.org/dist/hive/hive-2.3.5/

Spark for Hadoop2
https://www.apache.org/dyn/closer.lua/spark/spark-3.1.2/spark-3.1.2-bin-hadoop2.7.tgz

Kafka:
https://kafka.apache.org/downloads

Hadoop2
https://hadoop.apache.org/release/2.8.5.html

### Start Zookeeper
```
bayartsogt@ubuntu:~/kafka$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Start Kafka Broker
```
bayartsogt@ubuntu:~/kafka$ bin/kafka-server-start.sh config/server.properties
```
### Start Hive MetaStore 
```
bayartsogt@ubuntu:~$ hive --service metastore
```

### Create Hive Table
```
(general) bayartsogt@ubuntu:~$ hive
hive> show databases;
OK
default
Time taken: 1.09 seconds, Fetched: 1 row(s)
hive> use default;
OK
Time taken: 0.061 seconds
hive> CREATE TABLE tweets (text STRING, sentiment DOUBLE)
    > ROW FORMAT DELIMITED FIELDS TERMINATED BY '\\|'
    > STORED AS TEXTFILE;
OK
Time taken: 0.72 seconds
hive> show tables;
OK
tweets
Time taken: 0.066 seconds, Fetched: 1 row(s)
```
### Download nltk toolkit
```python
>>> import nltk
>>> nltk.download('brown')
[nltk_data] Downloading package brown to /home/bayartsogt/nltk_data...
[nltk_data]   Unzipping corpora/brown.zip.
True
```
### Start Twitter Producer

First go to `src` folder
```
cd ./src
```

Then run producer by following command:
```
python producer.py
```

Now we will submit the consumer script by following command:
```
spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.4.8.jar consumer.py
```
