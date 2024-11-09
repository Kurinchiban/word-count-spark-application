# word-count-spark-application


# Spark Application Running Modes

This document outlines the different modes available to run Spark applications. Each mode serves different use cases depending on the environment in which Spark is deployed.

## 1. Local Mode

**Description**:  
Runs Spark on a single machine (your local machine). Typically used for development, testing, or small-scale applications.

**How to Run**:  
Use the following command to run a Spark application in local mode:
```bash
spark-submit --master local[4] your_spark_app.py
```
In this example, `local[4]` tells Spark to use 4 cores on your local machine.

---

## 2. Standalone Mode

**Description**:  
Spark runs on a cluster of machines but without the need for a Hadoop cluster. You manage the Spark cluster independently.

**How to Run**:  
Use the following command to submit a Spark application in standalone mode:
```bash
spark-submit --master spark://<spark-master-host>:<port> your_spark_app.py
```
Ensure that you have Spark installed on multiple nodes and that you start the master and worker nodes.

---

## 3. YARN (Yet Another Resource Negotiator) Mode

**Description**:  
Runs Spark on a Hadoop YARN cluster, which manages resources across multiple nodes. Suitable for large-scale, production environments.

**How to Run**:  
Use the following command to submit a Spark application on a YARN cluster:
```bash
spark-submit --master yarn --deploy-mode client your_spark_app.py
```
For running the driver on the cluster, use `--deploy-mode cluster`:
```bash
spark-submit --master yarn --deploy-mode cluster your_spark_app.py
```

---

## 4. Mesos Mode

**Description**:  
Runs Spark on Apache Mesos, a general-purpose cluster manager. This is an alternative to YARN and is suitable for various resource management needs.

**How to Run**:  
Submit a Spark application using Mesos mode:
```bash
spark-submit --master mesos://<mesos-master>:<port> your_spark_app.py
```

---

## 5. Kubernetes Mode

**Description**:  
Runs Spark on a Kubernetes cluster, ideal for cloud-native and containerized environments.

**How to Run**:  
Submit a Spark application to a Kubernetes cluster using the following command:
```bash
spark-submit --master k8s://<kubernetes-cluster-url> --deploy-mode cluster --conf spark.kubernetes.container.image=<image> your_spark_app.py
```
Ensure that Spark is properly set up with Kubernetes and Docker images.

---

## 6. Cluster Mode

**Description**:  
In this mode, the driver program runs on the cluster, and the client program submits the job remotely.

**How to Run**:  
Use the following command to run your Spark application in cluster mode:
```bash
spark-submit --master spark://<spark-master-host>:<port> --deploy-mode cluster your_spark_app.py
```

---

## Conclusion

Choose the appropriate mode based on your environment and deployment needs. Each mode offers specific advantages depending on whether you're working in a local development setup, standalone clusters, YARN, Mesos, Kubernetes, or a fully distributed cluster.

For further configuration and environment setup, refer to the official [Spark Documentation](https://spark.apache.org/docs/latest/).