# Module 1 - Data Processing Techniques

## **ETL Fundamentals**

### **What is an ETL process?**
- **Extract**: Obtains data from various sources (databases, APIs, files, etc.).
- **Transform**: Applies rules and functions to standardize, clean, and prepare data.
- **Load**: Stores processed data in a final repository for analysis.


### **What is extraction?**
- **Access configuration**: Defines how data will be accessed and read by an application.
- **Web scraping**: Collects data from web pages.
- **API connections**: Integrates data programmatically via APIs.
- **Types of data**:
  - **Static**: Data that does not change frequently.
  - **Streaming**: Continuous data transmission.


### **What is data transformation?**
*Also known as data wrangling*
- **Data processing**: Performs operations to adapt data to target systems.
- **Conforming to target systems**: Aligns data with required formats.
- **Cleaning**: Removes duplicate or inconsistent data.
- **Filtering**: Selects relevant data.
- **Joining** or **Merging**: Combines data from multiple sources. Most suitable for 'unlike' data sources
- **Feature engineering**: Creates new features from data.
- **Formatting and typing**: Standardizes data types for compatibility.


### **What is data loading?**
- **Moving data**: Transfers data to new environments.
- **Examples of targets**:
  - **Databases**.
  - **Data Warehouses**.
  - **Data Marts**.
- **Objective**: Make data available for analytics, dashboards, and reports.

### **Use cases for ETL pipelines**
- **Digital transformation**: Digitizing analog media (photos, videos, audio).
- **Data migration**:
  - **OLTP to OLAP**: Moves data from transactional to analytical systems.
- **Dashboards and Machine Learning**: Provides data for analytics and model training.

### **Recap**
- **ETL** stands for: **Extract, Transform, Load**.
- **Extraction**: Reading data from multiple sources.
- **Transformation**: Preparing data to meet destination requirements.
- **Loading**: Writing data to the final environment.
- **Purpose of ETL**: Curate and make data accessible to end-users.

---
---

## **Comparing ETL to ELT**

### **Introduction**
- ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) are data integration processes used to move and prepare data for analysis.
- The main difference lies in when and where the data transformation occurs.

### **Key Differences between ETL and ELT**
#### **1. Transformation Location**
- **ETL**: Transformation happens within the data pipeline before loading the data into the target system.
- **ELT**: Transformation occurs after loading the raw data into the destination environment, leveraging the power of cloud-based systems.


#### **2. Flexibility**
- **ETL**:
  - More rigid as it relies on pre-engineered pipelines according to user specifications.
- **ELT**:
  - More flexible, allowing end users to perform transformations as needed.


#### **3. Support for Big Data**
- **ETL**:
  - Typically used for structured, relational data in on-premise environments, facing scalability challenges.
- **ELT**:
  - Designed to handle both structured and unstructured data in cloud environments, solving scalability issues.

#### **4. Time-to-Insight**
- **ETL**:
  - Requires longer development time for specifying and building pipelines.
- **ELT**:
 
### **The Evolution from ETL to ELT**
- Driven by the need for access to raw data and the capabilities of cloud storage.
- **Staging Areas**:
  - In ELT, data lakes act as staging areas to store raw data.
  - Self-service data platforms have emerged as modern staging areas, enhancing accessibility.

### **The Shift from ETL to ELT**
- ETL is still relevant for specific use cases but has limitations for big data and real-time analytics.
- **ELT Advantages**:
  - Addresses challenges such as:
    - Lengthy time-to-insight.
    - Handling large-scale and diverse data.
    - Providing access to siloed information.

### **Recap**
- Key differences between ETL and ELT include:
  - **Transformation location, flexibility, scalability, and time-to-insight**.
- The demand for raw data access is driving the evolution to ELT.
- While ETL remains relevant, ELT enables ad-hoc, self-service analytics for modern data environments.

---
---

## **Data Extraction Techniques**

### **Examples of Raw Data Sources**
#### **1. Traditional Sources**
- **Paper Documents:** Physical documents converted to digital form using OCR (Optical Character Recognition).
- **Web Pages:** Extracted using web scraping techniques to gather structured or semi-structured data.
- **Analog Audio/Video:** Digitized for analysis, often through signal processing methods.
- **Surveys, Statistics, Economics:** Data collected from structured surveys and statistical reports.
- **Transactional Data:** Captured from databases and log files, essential for financial and operational analytics.

#### **2. Modern Sources**
- **Social Media:** Extracts user-generated content for sentiment analysis and trend detection.
- **Weather Station Networks:** Continuous data feeds for predictive analytics in meteorology.
- **IoT (Internet of Things):** Sensor data providing real-time analytics for smart devices.
- **Medical Records:** Structured and unstructured data used for healthcare analytics.
- **Human Genomes:** Genetic data for bioinformatics and personalized medicine.

### **Techniques for Extracting Data**
#### **1. Traditional Techniques**
- **OCR (Optical Character Recognition):** Converts scanned documents into machine-readable text.
- **ADC (Analog-to-Digital Conversion) and CCD (Charge-Coupled Device) Sampling:** Used for digitizing analog signals.
- **Surveys and Polls:** Data gathered through mail, phone, or in-person.
- **Cookies and User Logs:** Tracks user behavior for analytics and personalization.

#### **2. Advanced Techniques**
- **Web Scraping:** Extracts data from HTML pages using tools like Beautiful Soup and Scrapy.
- **APIs (Application Programming Interfaces):** Facilitates data exchange between applications.
- **Database Querying:** SQL and NoSQL queries for extracting structured data.
- **Edge Computing:** Processes data locally on devices to minimize latency.
- **Biomedical Devices:** Captures biometric data for diagnostic purposes.

### **Use Cases**
#### **1. API-Based Integration**
- **Integrating Structured Data Sources:** Facilitates data consolidation across platforms.
- **Capturing Events via APIs:** Enables real-time monitoring and historical analysis.

#### **2. Edge and IoT Applications**
- **Edge Computing for Surveillance:** Reduces network latency for time-sensitive data. Also reduces redundancy by filtering, aggregating, and extracting only relevant features at the edge, minimizing the volume of data that needs to be transmitted and stored.
- **Direct-to-Storage Data Migration:** Ensures seamless data transfer for later processing.

#### **3. Healthcare and Diagnostics**
- **Medical Diagnostics:** Utilizes biometric data for predictive healthcare analytics.

### **Recap**
- Raw data sources range from paper documents to IoT devices and biomedical data.
- Common extraction techniques include OCR, web scraping, APIs, and database querying.
- Use cases span from API integrations to medical diagnostics leveraging biometric data.

---
---

## **Introduction to Data Transformation Techniques**

- Data transformation is a key step in ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) processes.
- It involves converting raw data into a format suitable for analysis or storage.

### **1. Core Transformation Operations**
- **Data Typing:** Ensures that data types are consistent and compatible across systems.
- **Data Structuring:** Organizes data into a structured format such as tables, hierarchies, or JSON.
- **Anonymizing and Encrypting:** Protects sensitive information by masking or encrypting data.

### **2. Additional Transformation Techniques**
- **Cleaning:**
  - Involves removing duplicate records and handling missing values.
- **Normalizing:**
  - Converts data into a common format or unit for consistency.
- **Filtering, Sorting, Aggregating, Binning:**
  - **Filtering:** Extracts relevant subsets of data.
  - **Sorting:** Organizes data based on specified criteria.
  - **Aggregating:** Summarizes data, such as calculating averages or sums.
  - **Binning:** Groups continuous data into discrete intervals.
- **Joining:**
  - Combines data from multiple sources based on common fields.

### **Schema-on-Write vs. Schema-on-Read**
#### **1. Schema-on-Write (Conventional ETL Approach)**
- Defines a fixed schema before writing data.
- **Pros:**
  - Ensures consistency and efficiency.
- **Cons:**
  - Limited flexibility for handling unstructured data.

#### **2. Schema-on-Read (Modern ELT Approach)**
- Applies schema dynamically when reading data.
- **Pros:**
  - Offers greater versatility and supports diverse data formats.
  - Facilitates enhanced storage flexibility, enabling the handling of larger data volumes.

### **Information Loss in Transformation**
#### **1. Causes of Information Loss**
- **Lossy Data Compression:** Reduces file size by discarding some information.
- **Filtering:** Eliminates less relevant data but may lose important details.
- **Aggregation:** Summarizes data, potentially obscuring underlying patterns.
- **Edge Computing Devices:** May pre-process data, leading to loss of granularity.

#### **2. Visualizing Information Loss**
- **ETL:** Typically involves greater information loss due to early transformations.
- **ELT:** Retains raw data longer, minimizing information loss until necessary.


### **Recap**
- Data transformation formats data to suit application needs.
- Common transformations: typing, structuring, normalizing, aggregating, and cleaning.
- **Schema-on-Write:** Used in ETL for consistency but is less flexible.
- **Schema-on-Read:** Used in ELT for versatility and flexibility.
- **Information Loss:** Common in compression, filtering, and aggregation processes.

---
---

## **Data Loading Techniques**

### **Data Loading Strategies**
- **Full Loading**:
  - Used to start tracking transactions in a new data warehouse.
  - Loads an initial history into a database.

- **Incremental Loading**:
  - Used to load data that has changed since previous loading.
  - Appends new data to existing datasets.
  - Accumulates transaction history.

### **Types of Incremental Loading**

#### **Stream Loading**
- **Characteristics**:
  - Data is loaded in real-time.
  - Continuous updates as data arrives.
  - Triggered by events such as:
    - **Real-time data**: Sensor data, social media feeds, IoT devices.
    - **Measurements**: Data size and threshold values.
    - **User requests**: Streaming video, music, web pages.

#### **Batch Loading**
- **Characteristics**:
  - Data is loaded in batches.
  - Periodic loading, such as daily transactions to a database.
  - Can be scheduled using:
    - **Windows Task Scheduler**.
    - **Cron jobs**.
    - **Daily stock updates**.

### **Push vs Pull Methodology**
- **Push**:
  - Source pushes data to the data warehouse.
  - Useful for real-time data integration.

- **Pull**:
  - Data warehouse pulls data from the source.
  - Suitable for scheduled extractions and batch loading.

### **Loading Plans**
- **Serial or Sequential Loading**:
  - Data is added one after the other in sequence.
  - Considered the default loading plan.

- **Parallel Loading**:
  - Data from different sources is loaded simultaneously.
  - Data from one source is split into chunks and loaded concurrently.
  - A faster and optimized approach.

### **Parallel Loading Techniques**
- **Multiple Data Streams**:
  - Allows simultaneous loading from various sources into the destination.
  
📌![Multiple Data Stream](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/Parallel-loading.jpg)

- **File Partitioning**:
  - Divides a large file into smaller chunks for parallel processing and loading.

📌![Multiple File Partitioning](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/Parallel-loading2.jpg)

### **Recap**
- **Key Points**:
  - Full and incremental are primary data loading strategies.
  - Data can be loaded in batches or streamed continuously.
  - Both push and pull methodologies are applicable for data loading.
  - Parallel loading enhances efficiency by handling multiple data streams or partitioned files concurrently.

---
---

# ETL & Data Pipelines: Tools and Techniques

## **ETL Workflow as Data Pipelines**

Traditionally, the primary focus of ETL workflows has been on accuracy rather than speed, ensuring that data transformations preserve the integrity and quality of information. However, efficiency is also a crucial factor to consider, especially as data volumes grow exponentially. By feeding data through a pipeline in smaller packets, ETL processes can handle large datasets more effectively. This approach allows data to move continuously through the workflow without interruption, leveraging parallel processing to minimize bottlenecks.

In a typical ETL pipeline, while one packet is being extracted, another is transformed, and yet another is loaded into the target system. This concurrent processing ensures that the data pipeline remains active and reduces latency, making the ETL process faster and more resource-efficient.

### **Batch Processing in ETL**

Batch processing is a method used in ETL pipelines to handle data in bulk, usually at scheduled intervals that can range from hours to days. It is particularly useful for managing large volumes of data that do not require real-time processing. In a conventional setup, data from OLTP (Online Transaction Processing) systems is collected and periodically transferred to OLAP (Online Analytical Processing) systems for analysis.

Batch processing intervals can be triggered in different ways:
- **Size-Based Triggers:** When the data reaches a certain size, it initiates a batch process.
- **Event-Based Triggers:** Specific events, such as security alerts, can activate the batch process.
- **On-Demand Triggers:** Web applications, like music or video streaming services, may initiate batch processing as needed.

This method is cost-effective and reduces the strain on system resources by allowing data to accumulate before processing. However, it is not suitable for use cases that require real-time data analysis due to its inherent delay between data capture and availability for analytics.

📌  
![Data Packets](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/Data-packet.jpg)

### **Staging Areas in ETL**

Staging areas play a vital role in ETL pipelines by serving as intermediate storage for data being transferred from source systems to the data warehouse. The primary function of a staging area is to decouple the ETL process from source systems, ensuring that data extraction, transformation, and loading can occur independently without impacting the performance of the source systems.

In a staging area, raw data from various sources is consolidated, cleaned, and transformed. This step is particularly important for integrating data from disparate OLTP systems that may use different schemas or formats. The staging area also helps in managing changes in source data, such as new fields or modified data types, by applying transformations before loading the data into the final destination.

For instance, in a cost accounting OLAP system, data from payroll, sales, and purchasing OLTP systems may first be collected in a staging area. Here, it undergoes transformations to standardize formats and ensure consistency before being loaded into the OLAP system for reporting and analysis.

📌  ![Staging Areas](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/Staging-areas.jpg)

### **ETL Workflows as DAGs**

Managing the complexity of ETL workflows requires a structured approach, which is where Directed Acyclic Graphs (DAGs) come into play. In tools like Apache Airflow, ETL workflows are represented as DAGs to manage task dependencies effectively. A DAG ensures that tasks execute in a predefined order, preventing cycles or repetitions that could lead to infinite loops or data inconsistencies.

In Airflow, a DAG consists of tasks that are represented as nodes, with directed edges indicating dependencies. Tasks can be scheduled to run sequentially or in parallel, optimizing the ETL process for performance and efficiency. For example, tasks like data extraction can run concurrently with transformation tasks, provided there are no interdependencies.

Airflow’s flexibility in defining DAGs using Python scripts allows data engineers to implement complex workflows, including retries for failed tasks, monitoring, and alerting mechanisms to ensure data integrity and reliability.

📌  ![Airflow DAG](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/ApacheAirflow-DAG.jpg)

### **Popular ETL Tools**

Choosing the right ETL tool is crucial for managing data pipelines efficiently. Modern ETL tools offer a range of features, including automation, drag-and-drop interfaces, and compliance with security standards like HIPAA and GDPR.

#### Talend Open Studio
Talend Open Studio is an open-source ETL tool that provides a user-friendly drag-and-drop interface for designing data pipelines. It supports integration with big data platforms and cloud data warehouses, making it a versatile choice for both small and large-scale ETL projects. One of its standout features is the ability to auto-generate Java code for data transformation tasks, reducing manual coding effort.

#### AWS Glue
AWS Glue is a fully managed ETL service designed to simplify data preparation for analytics on the AWS cloud platform. It offers schema discovery and metadata management, enabling users to automate the process of crawling data sources and defining tables. AWS Glue's serverless architecture means that users do not need to manage infrastructure, allowing them to focus entirely on data transformations and analytics.

#### IBM InfoSphere DataStage
IBM InfoSphere DataStage is an enterprise-grade ETL tool known for handling large volumes of data with parallel processing capabilities. It provides a graphical interface for designing ETL jobs and integrates seamlessly with IBM's broader data ecosystem. DataStage's ability to handle both ETL and ELT (Extract, Load, Transform) processes makes it a robust choice for organizations with diverse data integration needs.

#### Alteryx
Alteryx focuses on self-service analytics, providing an intuitive drag-and-drop interface that allows business users to create ETL pipelines without needing to write code. It integrates with a wide range of data sources and offers powerful analytics capabilities, making it a favorite among non-technical users who need to manipulate data quickly and efficiently.

#### Apache Airflow and Python
Apache Airflow is a platform for programmatically authoring, scheduling, and monitoring workflows. Its flexibility in defining ETL tasks as code makes it a powerful tool for managing complex pipelines. By using Python to define workflows, data engineers can implement custom transformations, integrate with APIs, and handle error conditions with precision.

#### Pandas Python Library
Pandas is a powerful open-source library for Python that simplifies data manipulation and analysis. Its DataFrame structure allows users to handle tabular data with ease, making it an excellent choice for small to medium-sized ETL tasks. However, Pandas is not well-suited for large-scale ETL processes due to memory constraints and its single-threaded execution model.

#### Overview:

Overall, the choice of ETL tool depends on factors such as data volume, real-time processing needs, and integration capabilities. By understanding the strengths and limitations of each tool, organizations can design efficient ETL pipelines that meet their specific requirements.

--- 
---

## **ETL Using Shell Scripting**

Shell scripting is a powerful tool for implementing ETL (Extract, Transform, Load) pipelines efficiently. In this context, we'll explore how to build an ETL process using Bash to report temperature statistics collected from a remote sensor. The goal is to capture temperature readings, process them to extract meaningful insights, and load the results into a dashboard for real-time visualization.

### **Temperature Reporting Scenario**

The scenario involves reporting the hourly average, minimum, and maximum temperatures from a remote sensor that updates every minute. The process relies on two APIs: `get_temp_api` to extract temperature data and `load_stats_api` to upload the processed statistics to a reporting dashboard.

#### Requirements
- `get_temp_api`: API to extract temperature data.
- `load_stats_api`: API to upload processed data to a dashboard.


### **ETL Workflow Overview**

The ETL process consists of three main phases:

- **Extract**: Fetch temperature readings using `get_temp_api` and append them to a log file (`temperature.log`).
- **Transform**: Process the most recent hour of readings using a Python script (`get_stats.py`) to calculate the minimum, maximum, and average temperatures, saving the results in a CSV file (`temp_stats.csv`).
- **Load**: Use `load_stats_api` to upload the processed CSV data to the dashboard.


### **Creating the ETL Shell Script**

Start by creating a shell script file:

`touch Temperature_ETL.sh`

Open the file in a text editor:

`gedit Temperature_ETL.sh`


### **Script Content**

Add the following code to the script:

```bash
# Transform your file into a bash shell script
!/bin/bash

# Extract temperature reading using get_temp_api
get_temp_api >> temperature.log

# Buffer last 60 readings (approximately last hour)
tail -60 temperature.log > temp_buffer.log
mv temp_buffer.log temperature.log

# Transform: Call Python script to process readings
python3 get_stats.py temperature.log temp_stats.csv

# Load: Upload processed stats using load_stats_api
load_stats_api temp_stats.csv
```

#### Explanation of the script

- **Extract Phase:**  
The command `get_temp_api >> temperature.log` captures temperature data and appends it to the temperature.log file. Using `>>` ensures that new readings are added without overwriting previous data.

- **Buffering Data:**  
To keep only the most recent hour of readings, `tail -60 temperature.log > temp_buffer.log` extracts the last 60 lines (assuming one reading per minute). The buffered data is then moved back to temperature.log using `mv temp_buffer.log temperature.log`

- **Transformation Phase:**  
The script calls the Python script with:  
`python3 get_stats.py temperature.log temp_stats.csv`  
This script processes the buffered data to compute min, max, and average temperatures, saving the results to *temp_stats.csv*.

- **Load Phase:**  
The command `load_stats_api temp_stats.csv` uploads the transformed data to the dashboard.

#### Setting Permissions for the Script
Before executing the script, make it executable:  
`chmod +x Temperature_ETL.sh`

#### Scheduling the ETL Job
To automate the ETL process every minute, use crontab:  
1. Open the crontab editor:  
`crontab -e`

2. Add the following line to schedule the script:

`* * * * * /path/to/Temperature_ETL.sh`  
*This line ensures that the ETL script runs every minute, automating data extraction, transformation, and loading.*

### **Summary**
This example demonstrates how Bash scripting can be leveraged to build a complete ETL pipeline.  
By using simple commands and integrating APIs for data extraction and loading, we can efficiently automate the process of capturing, processing, and visualizing temperature data in real-time.


## **Introduction to Data Pipelines**

### **What is a Pipeline?**
A **pipeline** consists of a series of connected processes where the **output of one process serves as input** to the next. This concept is widely used in different industries, including **manufacturing**, **software development**, and **data processing**.

- In an assembly line, each worker or machine **performs a specific task**, then passes the product down the line.
- In software, a pipeline ensures **sequential execution** of processes, optimizing efficiency and resource utilization.
- In computing, pipelines **process data step by step**, transforming it at each stage.

### **What is a Data Pipeline?**
A **data pipeline** is a structured sequence of processes that move and transform data between systems.

- The **primary goal** of a data pipeline is to efficiently move **data from one place or format to another**.
- Any system that **extracts**, **transforms**, and **loads data (ETL)** is considered a **data pipeline**.

Data pipelines exist at different levels:
- **Low-level hardware architectures**, managing data transfer at a machine level.
- **Software-driven processes**, which involve **commands, programs, and execution threads**.
- **Bash pipelines**, which connect multiple commands to facilitate data processing using the `|` operator.

### **Packet Flow Through a Pipeline**
Data flows through a pipeline in **packets** (logical units of data).
- A **queued data packet** enters the pipeline.
- Each step **transforms or processes** the packet.
- The time a packet **spends within the pipeline** is called **pipeline latency**.
- The **gap between data packets being processed** is the **throughput delay**.

### **Data Pipeline Performance**
There are two key performance considerations regarding data pipelines:

#### **Latency**:
- **Latency** is the total time it takes for a **single data packet** to pass through the entire pipeline.
- It is determined by the **slowest process** in the sequence.
- Example: If a **web server is slow**, page loading time is affected, even if the internet connection is fast.

#### **Throughput**
- **Throughput** refers to the **amount of data** processed per unit time.
- Higher **packet sizes** improve throughput efficiency.
- Example: In an **assembly line**, increasing batch size optimizes production speed.

### **Use Cases of Data Pipelines**
Data pipelines serve multiple purposes:
- **Backing up files** to ensure data availability.
- **Integrating raw data** from multiple sources into a data lake.
- **Moving transactional records** to a data warehouse.
- **Streaming IoT data** to dashboards and machine learning models.
- **Processing raw data** for machine learning applications.
- **Message transmission** (emails, SMS, video streaming, etc.).

### **Recap**
- **Data pipelines** move and transform data between systems.
- **Latency and throughput** are key performance metrics.
- **Real-world use cases** include data lakes, backups, IoT streaming, and ML pipelines.

---
---


## **Key Data Pipeline Processes**
Data pipelines consist of multiple stages that ensure the efficient flow of data from its source to a destination system. These stages include extraction, ingestion, transformation, loading, scheduling, monitoring, and optimization.

### **Monitoring and Optimization**
Ensuring that a data pipeline runs efficiently requires continuous monitoring. Key performance metrics include:
- **Latency**: The time required for data to travel through the pipeline.
- **Throughput**: The amount of data processed within a given time.
- **Error detection**: Identifying system failures or data inconsistencies.
- **Utilization rate**: Measuring how efficiently system resources are used.

A logging and alerting system is essential to notify administrators of failures or performance issues.

### **Load Balanced Pipelines**
For optimal performance, a pipeline should have **just-in-time** data processing, meaning that each stage operates without unnecessary delays. A well-balanced pipeline ensures that no step is left idle while waiting for another stage to complete its task.

### **Handling Unbalanced Loads**
When processing speeds vary across pipeline stages, bottlenecks may occur. There are several strategies to mitigate this issue:
- **Parallelization**: Running multiple instances of a slow stage to increase efficiency.
- **Process replication**: Spreading workloads across multiple CPUs, cores, or threads.
- **Data partitioning**: Distributing data packets dynamically to prevent delays.

For example, if one transformation step takes significantly longer than others, replicating it across multiple threads can improve throughput.

### **Stage Synchronization**
To ensure smooth transitions between pipeline stages, **I/O buffers** are used as temporary storage areas that regulate data flow. These buffers help align different processing speeds, preventing data congestion.

A common implementation is using message queues like RabbitMQ, which temporarily store data before it is processed by the next stage.

📌![Handling unbalanced loads - Parallelization](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/handlingloads-parallelization.jpg)

### **Recap**
- Data pipeline processes involve extraction, transformation, loading, scheduling, monitoring, and optimization.
- Monitoring key metrics such as latency, throughput, and resource utilization ensures optimal pipeline performance.
- Techniques like parallelization and I/O buffers help mitigate bottlenecks and balance the workload across different pipeline stages.

## **Batch versus Streaming Data Pipeline Use Cases**

### **Batch Data Pipelines**
Batch pipelines process large sets of data at scheduled intervals. They are ideal for use cases where the latest data is not immediately required, and processing accuracy is a priority. These pipelines execute on a **fixed schedule** (e.g., hourly, daily, or weekly) or based on specific triggers such as data size thresholds.

#### **Characteristics of Batch Processing**
Batch pipelines are designed to handle structured data processing with high reliability:
- **Periodic Execution**: Jobs run at predefined intervals rather than continuously.
- **Trigger-Based Execution**: Processing can be initiated when a certain amount of data accumulates.
- **Higher Accuracy**: Data is cleaned and processed in bulk, ensuring reliable outputs.
- **Latency Trade-off**: Since data is processed in batches, results are delayed.

#### **Common Use Cases**
Batch pipelines are useful when accuracy is more important than real-time availability:
- **Data backups** to ensure redundancy and disaster recovery.
- **Transaction history loading** for financial reporting and auditing.
- **Billing and order processing** in e-commerce and subscription services.
- **Data modeling** for predictive analytics.
- **Sales and weather forecasting** using large datasets.
- **Medical image processing**, where precision is critical for diagnosis.

### **Streaming Data Pipelines**
Streaming pipelines process continuous flows of data in near real-time. Instead of processing data in bulk, they handle individual records as they arrive.

#### **Characteristics of Streaming Processing**
- **Low Latency**: Data is processed as it arrives, minimizing delays.
- **Event-Driven Processing**: Each new data point triggers immediate processing.
- **Scalability**: Designed for high-velocity data environments.
- **Potential for Errors**: Due to rapid ingestion, error handling is more complex.

#### **Common Use Cases**
Streaming pipelines are essential when real-time data processing is required:
- **Social media monitoring and sentiment analysis** for trend tracking.
- **Fraud detection** in financial transactions, identifying anomalies in real time.
- **User behavior tracking** for targeted advertising.
- **Stock market trading**, where small delays impact financial outcomes.
- **Real-time product pricing** in e-commerce.
- **Recommender systems** used by content platforms.

### **Micro-Batch Data Pipelines**
Micro-batching is a hybrid approach that processes small batches at high frequency, simulating real-time behavior while maintaining structured processing.

#### **Key Benefits of Micro-Batching**
- **Near Real-Time Processing**: Faster than batch but more structured than streaming.
- **Improved Load Balancing**: Smaller batch sizes reduce latency and enhance efficiency.
- **Ideal for Short Data Windows**: Useful when quick insights are needed but continuous streaming isn't necessary.

### **Batch vs Stream Trade-offs**
Choosing between batch and streaming processing depends on balancing **accuracy, latency, and fault tolerance**:
- **Batch processing ensures high data quality but introduces processing delays.**
- **Streaming prioritizes speed but may result in incomplete or less reliable data.**
- **Data cleaning in batch processing improves reliability but increases processing time.**
- **Lowering latency in streaming increases the risk of errors and inconsistencies.**

### **Lambda Architecture**
Lambda Architecture is a hybrid approach that combines batch and streaming data processing to support large-scale, real-time analytics.

#### **Components of Lambda Architecture**
- **Batch Layer**: Stores and processes historical data in bulk.
- **Speed Layer**: Processes real-time data for immediate insights.
- **Serving Layer**: Merges batch and speed layer results for a unified data view.

#### **When to Use Lambda Architecture**
- **When both speed and accuracy are required**: Ensures real-time insights with a historical data foundation.
- **When access to earlier data is needed**: Allows retrospective analysis while handling real-time data ingestion.
- **When system complexity is manageable**: Requires expertise and careful integration.

📌![Handling unbalanced loads - Parallelization](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/lambda-architecture.jpg)

### **Recap**
- **Batch pipelines** process large amounts of data at scheduled intervals.
- **Batch processing** is best when accuracy is prioritized over real-time availability.
- **Streaming pipelines** process individual data points continuously for real-time insights.
- **Streaming is useful** for fraud detection, stock trading, and personalized recommendations.
- **Micro-batching** provides a near-real-time balance between batch and stream processing.
- **Lambda architecture** merges batch and streaming processing for both speed and accuracy.

---
---
