import re
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Read_text_file") \
    .master("spark://BTCCHL0016:7077") \
    .getOrCreate()

# Get the SparkContext from the SparkSession
sc = spark.sparkContext

# Read the text file
lines = sc.textFile('/word-count-spark-application/word-count-spark-local-mode/Sample_data.txt')

def clean_word(word):
    return re.sub(r'[^a-zA-Z0-9]', '', word)

# Process the lines to count words
words = lines.flatMap(lambda line: line.split(' '))
cleaned_words = words.map(lambda word: clean_word(word))
words_count = cleaned_words.map(lambda x: (x, 1))
word_count = words_count.reduceByKey(lambda a, b: a + b)

# Collect and print the results
result = word_count.collect()
for (word, count) in result:
    print(f"{word}: {count}")

# Stop the Spark session
spark.stop()