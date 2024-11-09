# Word Count Spark Application

## Steps to Run the Application:

1. **Ensure Spark and Hadoop are Installed**:  
   Make sure your system has Spark and Hadoop installed, and that your Hadoop cluster is properly set up if you're using HDFS (Hadoop Distributed File System). If you're using a local file system for testing, you can adjust the input/output paths accordingly. If you haven't installed them yet, follow the steps outlined in the following blog:  
   [Install Spark on Ubuntu](https://phoenixnap.com/kb/install-spark-on-ubuntu)

2. **Prepare the Application Code**:  
   Make sure you have the `word_count.py` script ready, and update your master url there.

3. **Submit the Job**:  
   You can submit the Spark job via the command line using the following command:
   ```bash
   spark-submit word_count.py
