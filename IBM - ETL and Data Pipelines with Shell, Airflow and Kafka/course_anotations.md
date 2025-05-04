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

# Module 2 - ETL & Data Pipelines: Tools and Techniques

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

## **Data Pipeline Tools and Technologies**

### **Understanding Data Pipeline Technologies**
Data pipelines are crucial for managing data **extraction, transformation, and delivery** across various systems. As businesses scale, they require modern **ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) solutions** that provide automation, security, and scalability.

Modern data pipeline tools offer:
- **Automation** to reduce manual intervention in data processing.
- **No-code interfaces** that allow non-technical users to build pipelines visually.
- **Security and compliance** mechanisms, including encryption and adherence to standards like **HIPAA and GDPR**.
- **Scalability**, ensuring efficient handling of structured and unstructured data.

Organizations select tools based on their **data volume, real-time processing needs, and operational complexity**, balancing cost, performance, and integration capabilities.

### **Open-Source Data Pipeline Tools**

#### > ***Pandas*: A Versatile Data Manipulation Library**
**Pandas** is widely used for **lightweight ETL pipelines** and **data analysis**. It provides a **data frame-based structure**, making it easy to manipulate structured data from formats such as **CSV, Excel, JSON, and SQL**.

- **Strengths**:
  - Facilitates **data cleaning, transformation, and aggregation** with minimal code.
  - Ideal for **prototyping ETL workflows** before full-scale deployment.
  - Supports various data sources and integration with **Jupyter Notebooks**.

- **Limitations**:
  - **Memory-bound processing**: Works best with small to mid-sized datasets.
  - **Not designed for distributed computing**: Lacks native scalability for big data workloads.

Alternatives like **Dask, Vaex, and Apache Spark** extend Pandas functionality for large-scale distributed data processing.

#### > ***Apache Airflow*: Orchestrating Complex Data Workflows**
**Apache Airflow**, developed by Airbnb, is a powerful workflow automation framework. It allows users to **define, schedule, and monitor data pipeline execution** programmatically.

- **Key Features**:
  - **Task Scheduling**: Ensures automated, repeatable execution of data workflows.
  - **Scalability**: Runs distributed workflows across multiple computing nodes.
  - **Cloud Integration**: Seamlessly connects with **AWS, Google Cloud, and Azure**.

Airflow is excellent for managing **scheduled ETL jobs**, though it is not designed for real-time event processing.

#### > ***Talend Open Studio*: A No-Code ETL Solution**
**Talend Open Studio** provides a **visual ETL development** environment, making it easy for users to design **data pipelines with a drag-and-drop interface**.

- **Advantages**:
  - **Supports big data & cloud integrations** with Hadoop, Spark, and various **databases**.
  - **Auto-generates Java code**, reducing manual coding effort.
  - **Built-in monitoring and scheduling** ensure pipeline reliability.

Talend is ideal for organizations that require **fast ETL deployment** without deep programming knowledge.

### **Enterprise-Grade Data Pipeline Tools**

#### > ***AWS Glue*: A Managed ETL Service**
**AWS Glue** is an enterprise-level **serverless ETL solution** that automates data extraction, transformation, and loading.

- **Key Benefits**:
  - **Schema Inference**: Automatically detects and structures datasets.
  - **Serverless Execution**: Eliminates infrastructure management.
  - **Tight Integration with AWS Services**: Works seamlessly with **Amazon S3, Redshift, and Athena**.

AWS Glue is best suited for **cloud-native organizations** looking for **a fully managed data processing environment**.

#### > ***IBM InfoSphere DataStage*: High-Performance ETL**
**IBM InfoSphere DataStage** is a **scalable data integration** platform optimized for large enterprises.

- **Key Features**:
  - **Parallel Processing**: Enhances speed and efficiency for large data volumes.
  - **Drag-and-Drop Workflow Designer**: Simplifies ETL process creation.
  - **Enterprise Connectivity**: Supports **multi-cloud and on-premises** data environments.

IBM DataStage is ideal for **complex enterprise-wide ETL and ELT operations**.

### **Streaming Data Pipeline Tools**

#### > ***IBM Streams*: Real-Time Data Processing**
**IBM Streams** is designed for **low-latency, real-time analytics**, enabling businesses to **process data streams continuously**.

- **Capabilities**:
  - Supports **Java, Python, and C++** for flexible integration.
  - **Sub-millisecond latency**, making it ideal for real-time analytics.
  - **Drag-and-drop UI** for building streaming workflows.

IBM Streams is particularly valuable for industries such as **finance, IoT, and cybersecurity**, where real-time insights are critical.

#### > ***Apache Kafka*: Distributed Event Streaming**
**Apache Kafka** is a leading **event-driven streaming platform**, enabling real-time data ingestion and message brokering.

- **Key Strengths**:
  - **Scalability**: Handles millions of events per second.
  - **Fault Tolerance**: Ensures data persistence and recovery.
  - **Seamless Integration**: Works with **Flink, Spark, and Storm** for real-time analytics.

Kafka is widely used in **log monitoring, fraud detection, and recommendation engines**.

### **Key Takeaways**

#### **Choosing the Right Data Pipeline Tool**
The choice of a data pipeline tool depends on the organization’s *needs*, *data volume*, and *processing latency* requirements:
- <u>For small-scale ETL & prototyping</u>: **Pandas** provides a flexible and intuitive environment.
- <u>For large-scale workflow automation</u>: **Apache Airflow** ensures reliable orchestration.
- <u>For no-code ETL</u>: **Talend Open Studio** simplifies development for non-technical users.
- <u>For managed cloud-native ETL</u>: **AWS Glue** provides a fully automated pipeline experience.
- <u>For real-time processing</u>: **IBM Streams and Apache Kafka** enable instant data insights.

Modern data pipelines often **combine multiple tools**, leveraging **batch and streaming** technologies to build efficient and scalable architectures. Understanding these tools allows data engineers to create **reliable, high-performance data ecosystems**.

# Module 3 - Building Data Pipelines using Airflow

## **Apache Airflow Overview**

### **Introduction to Apache Airflow**
Apache Airflow is an *open-source workflow orchestration tool* designed to programmatically author, schedule, and monitor workflows. It provides a flexible and scalable solution for managing complex data pipelines.

### **Key Characteristics**
- **Open-source and actively maintained**: Apache Airflow is supported by a strong community, ensuring regular updates and enhancements.
- **Workflow Management**: Airflow enables users to define, execute, and monitor workflows programmatically.
- **Task Dependencies**: Workflows are structured as **Directed Acyclic Graphs (DAGs)**, where tasks execute in a specific, non-cyclic order.
- **Not a Streaming Solution**: While powerful for workflow orchestration, Apache Airflow is **not designed for real-time data streaming**.

### **Apache Airflow Components**
Apache Airflow consists of multiple components that work together to orchestrate tasks and workflows efficiently.

#### • **Scheduler**:
The *Scheduler* is responsible for triggering all scheduled workflows. It ensures that tasks are executed in the correct sequence according to their dependencies.

#### • **Executor**:
The *Executor* handles the execution of tasks by assigning them to available **workers**.

#### • **Workers**:
*Workers* are responsible for executing individual tasks. They process the assigned jobs and report back their status.

#### • **Web Server (UI)**:
Apache Airflow provides a **graphical user interface (UI)** that allows users to:
- Monitor workflows
- Trigger DAGs manually
- Debug and track task execution statuses

####  • **Metadata Database**
Airflow maintains a **metadata database** that stores:
- DAG definitions
- Task execution statuses
- Workflow schedules
- Logs and configuration details

#### • **DAG Directory**
The **DAG directory** contains all the Python scripts defining workflows. These scripts are accessed by the scheduler, executor, and workers to determine execution logic.

📌![Airflow Architecture](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/ApacheAirflow-architecture.jpg)

### **Apache Airflow DAG Example**
A **Directed Acyclic Graph (DAG)** in Airflow consists of **tasks** linked by dependencies. Here’s an example of a basic DAG:

1. **Ingest Data** → 2. **Analyze Data** → 3. **Check Integrity**
   - If **errors are found** → **Describe Integrity** → **Email Error** → **Report Issue**
   - If **no errors** → **Save Data** → **Generate Report**

This structure ensures that workflows execute in a **controlled and traceable manner**.

### **Task Lifecycle in Apache Airflow**
Each task in Airflow goes through a defined set of states:

📌  ![Airflow Task State](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/ApacheAirflow-TaskState.jpg)

1. **No Status** → Task has not yet been queued for execution.
2. **Scheduled** → The scheduler determines that dependencies are met and schedules the task.
3. **Removed** → The task is no longer in the DAG.
4. **Upstream Failed** → A previous dependent task has failed.
5. **Queued** → The task is waiting for an available worker.
6. **Running** → A worker is executing the task.
7. **Success** → Task completed successfully.
8. **Failed** → Task encountered an error and did not complete.
9. **Up for Retry** → Task is rescheduled for execution based on retry settings.

Ideally, a task should flow throughout the scheduler from no status, to scheduled, to queued, to running, and finally to success.  
1. -> 2. -> 5. -> 6. -> 7.

### **Apache Airflow Features**
Apache Airflow provides several features that make it a powerful workflow management tool.

#### **1. Pure Python**
- Workflows are written in Python, allowing for **full flexibility** and easy customization.

#### **2. Useful UI**
- Airflow’s web-based UI enables users to **monitor, schedule, and debug workflows** with full visibility.

#### **3. Integration**
- Airflow provides **plug-and-play integrations** with various tools, including cloud platforms, databases, and monitoring systems.

#### **4. Ease of Use**
- Users with **Python experience** can easily create and manage complex workflows.
- Airflow supports **a wide range of operators** and sensors for different use cases.

#### **5. Open-Source Community**
- Apache Airflow has an **active developer community**, ensuring continuous improvements and new features.

### **Principles of Apache Airflow**
Apache Airflow is built on four key principles:

1. **Scalable** → Modular architecture supports distributed execution across multiple workers.
2. **Dynamic** → Workflows are defined in Python, allowing for flexible DAG creation.
3. **Extensible** → Users can create custom operators and extend functionality.
4. **Lean** → Designed with minimal overhead, ensuring efficiency in execution.

### **Apache Airflow Use Cases**
Many companies leverage Apache Airflow for workflow automation:

- **Adobe** → Custom operators for **workflow automation**.
- **Adyen** → Extends existing **ETL DAGs** for efficient task management.
- **Big Fish** → Uses **Python API** for dynamic workflow orchestration.
- **Walmart** → Automates **data processing and warehouse loading**.

### **Recap**
- **Apache Airflow** is an **open-source workflow orchestration tool** for scheduling and monitoring workflows.
- **Key components** include the **Scheduler, Executor, Workers, Web UI, Metadata Database, and DAG Directory**.
- **Workflows in Airflow** are structured as **Directed Acyclic Graphs (DAGs)**.
- **Airflow Features** include **Python-based workflows, an intuitive UI, plug-and-play integrations, ease of use, and an active open-source community**.
- **Common Use Cases** include **ETL workflows, machine learning pipeline dependencies, and workflow automation** in various industries.

---
---

## **Advantages of Representing Data Pipelines as DAGs in Apache Airflow**

### **Understanding DAGs and Their Role in Apache Airflow**
A **Directed Acyclic Graph (DAG)** is a fundamental concept in Apache Airflow, representing workflows in a structured manner. At its core, a DAG is a graph where tasks (nodes) are connected by dependencies (edges). Unlike general graphs, a DAG ensures that there are no cycles, meaning no task depends on itself, directly or indirectly. This acyclic property guarantees a clear execution order, making DAGs an ideal way to model data pipelines.

📌  ![DAG](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/DAG.jpg)

The simplest form of a DAG consists of two tasks, where one must complete before the other begins. More complex DAGs may have multiple branches and dependencies, but they all share the same principle: a directional flow of execution that prevents infinite loops.

### **How DAGs Represent Workflows in Airflow**
In Apache Airflow, DAGs serve as blueprints for data workflows. Each task within a DAG represents a unit of work, such as executing a SQL query, processing a dataset, or triggering an external API call. The relationships between these tasks define the sequence in which they should execute. For example, a DAG may start by extracting data from a database, then transform it into a new format, and finally load it into a destination system. Each of these steps is a task, and Airflow ensures they run in the correct order.

DAGs are not static representations; they are dynamic and coded in Python. This means that instead of configuring workflows manually, engineers define DAGs programmatically, allowing for automation, scalability, and maintainability. Each DAG script includes scheduling details, dependencies, and the specific logic each task needs to execute.

### **Defining Tasks and Operators in Airflow**
Tasks in a DAG are created using operators, which determine what each task does. Airflow provides several built-in operators tailored for different use cases. For instance, the `PythonOperator` executes Python functions, the `BashOperator` runs shell commands, and the `SQLOperator` executes queries in a database. Additionally, Airflow includes **sensor operators**, which continuously check for conditions to be met before allowing the workflow to proceed. A common example of a sensor is one that waits for a file to be available in a storage system before triggering the next task in the pipeline.

To illustrate this, imagine a DAG that processes daily sales reports. The first task, using a sensor, waits for a CSV file to be uploaded to a storage bucket. Once the file is available, the next task, a Python script, processes the data and extracts relevant insights. Finally, a SQL task loads the cleaned data into a reporting database. This step-by-step execution ensures that no task runs prematurely and that all dependencies are honored.

### **Components of a DAG Definition**
An Airflow DAG is written as a Python script and consists of several sections.  

1. **Library imports** (e.g., `from airflow import DAG`)
2. **DAG arguments** (e.g., default execution parameters)
3. **DAG definition** (e.g., `dag = DAG(...)`)
4. **Task definitions** (defining tasks using operators)
5. **Task pipeline** (specifying task dependencies)

The first part of the script typically imports necessary libraries and defines default arguments such as the owner of the DAG, the start date, and the number of retry attempts in case of failure. Following this, the DAG itself is instantiated, specifying the workflow name, execution schedule, and any global settings.

Once the DAG is defined, tasks are created using operators. These tasks form the individual steps of the workflow and can be linked together using dependency operators. For example, in a simple DAG, `task1 >> task2` ensures that `task1` must complete before `task2` starts. This explicit definition of task order is what makes DAGs powerful in orchestrating complex workflows.

Below is an example of a basic DAG that consists of two tasks:

```python
# 1. Library imports
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt

# 2. DAG arguments
default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2021, 7, 28),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

# 3. DAG definitions
dag = DAG('simple_example',
          description='A simple example DAG',
          default_args=default_args,
          schedule_interval=dt.timedelta(seconds=5)
)

# 4. Task definitions
task1 = BashOperator(
    task_id='print_hello',
    bash_command='echo "Hello, Airflow!"',
    dag=dag,
)

task2 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# 5. Task pipeline
task1 >> task2
```
In this example, `task1` prints message, while `task2` prints the current date and time. 

The `task1 >> task2` notation states the tasks dependencies and ensures `task1` finishes before `task2` begins.

### **Apache Airflow Scheduler**

The scheduler is responsible for monitoring and triggering DAG runs based on the defined schedule. When a DAG is first loaded into Airflow, it remains inactive until the scheduler detects its start date and triggers its execution.

The scheduler deploys tasks to worker nodes that execute them independently. This distributed nature allows Airflow to handle large-scale workflows efficiently. For instance, if a DAG processes multiple datasets, different tasks can be executed in parallel across multiple workers, optimizing processing time.

### **Advantages of Workflows as Code**

Defining workflows as code in Apache Airflow offers several benefits:

- Maintainability: Code is structured and explicit. Engineers can easily review, modify, and debug workflows by inspecting the DAG code.
- Version Control: Changes can be tracked in Git or other VCS. Any changes to a DAG can be tracked over time, allowing teams to revert to previous versions if needed.
- Collaboration: Teams can work on DAGs together.
- Testability: Code can be validated and unit-tested before deployment.

### **Recap**

DAGs in Apache Airflow provide a structured way to define and manage workflows. By representing workflows as directed acyclic graphs, Airflow avoids loops and unnecessary complexity. Tasks within a DAG are implemented using operators, each defining specific actions to be performed. The Airflow Scheduler is responsible for executing these tasks, distributing them across worker nodes and handling failures as needed.

The ability to define DAGs as Python scripts brings multiple advantages. Workflows become more **maintainable**, **version-controlled**, and **testable**, allowing data teams to collaborate efficiently. With this flexibility and robustness, Airflow has become a standard tool for orchestrating data pipelines in modern data engineering.

---
---

## **Airflow Logging and Monitoring**

### **Understanding Logging and Monitoring in Airflow**

Monitoring data pipelines is crucial to ensure that tasks are executed properly and to diagnose any potential issues along the way.  
In Apache Airflow, this is achieved through a combination of logging and metrics monitoring. Each task execution generates logs, making it easier to review what happened during a DAG run.  

- **Development environment**: The log files are saved locally. 
- **Production environment**: it is common practice to move beyond local storage. Airflow recommends sending logs to cloud platforms like *IBM Cloud*, *AWS*, or *Azure*, and also to integrate them with tools such as *Elasticsearch* or *Splunk*. These platforms not only store the logs but allow quick searches and deeper analysis, essential when handling a large volume of task executions.

The way Airflow organizes these logs follows a logical path based on the *DAG ID*, *run ID*, *task ID*, and the *attempt number*.  
For example, if you want to locate the log of a task called `task1` from the DAG `dummy_dag`, you would navigate to a path like: `logs/dag_id=dummy_dag/run_id=scheduled_<timestamp>/task_id=task1/attempt=1.log`.  

Inside these logs, you find information such as which command was executed, the output of the execution, and whether the task succeeded or failed.

Beyond accessing logs through the file system, Airflow's Web UI offers a more intuitive way to review task events through search filters like *DAG ID*, *Task ID*, and *Logical Date* to quickly retrieve specific task runs. The interface shows statuses such as "success," "failed," or "running," and provides direct access to the related logs without the need to browse folders manually.

📌  ![AirflowUI](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/Airflow-TaskLogUI.jpg)

### **The Role of Metrics in Airflow Monitoring**

Besides logging, Airflow also produces operational metrics that help you keep track of your workflows efficiency. These metrics are divided into three main categories. 

- **Counters**: represent values that are always increasing, such as the total number of successful or failed tasks.  
- **Gauges**: Values that can fluctuate — they indicate things like the current number of running tasks or the size of the DAG bag at any moment. 
- **Timers**: Associated with time-based measurements, capturing how long tasks take to complete or how quickly they reach a *success* or *failure* state.

Monitoring these metrics gives you a deeper sense of your system’s behavior. If, for instance, you notice an unusual increase in task failures (a **counter** metric) or a sudden spike in task execution time (a **timer** metric), you can investigate the root cause before it impacts downstream processes.

### **Storing and Visualizing Metrics for Production**

While it’s possible to monitor metrics locally during development, production environments demand a more scalable approach. Airflow recommends sending metrics using *StatsD*, a network daemon capable of receiving and forwarding metrics efficiently.  
From there, *Prometheus* takes over the role of storing, analyzing, and making sense of the data. It can also visualize these metrics through customizable dashboards, providing teams with real-time insights into their deployments.

Having such a setup means you’re not just collecting data — you're empowering yourself to anticipate problems, optimize workflows, and ensure that service levels are consistently met.

### **Recap**

In this lesson, we explored how Apache Airflow provides powerful tools to monitor and maintain data pipelines. Logs are generated for each task run and can either be stored locally or sent to cloud storage and log analysis systems like *Elasticsearch* and *Splunk*. Airflow’s Web server serves as an interactive UI that simplifies event searching and log access, making the monitoring process more efficient.

We also learned that Airflow emits metrics in the form of *counters*, *gauges*, and *timers*, offering different dimensions for monitoring the health of workflows.

With these capabilities, Airflow ensures that teams can keep their pipelines reliable, performant, and easy to debug, even as systems grow in complexity.

___
___

# Module 4 - Building Streaming Pipelines using Kafka

## **Distributed Event Streaming Platform Components**

### **Understanding Events in the Context of Streaming**

An *event* represents a change in the observable state of an entity over time. It's the core building block in event-driven systems: *A moving vehicle*, constantly updating its GPS location; *a room thermometer*, reporting temperature changes; *a health monitor* capturing a patient’s blood pressure — **each of these updates is an event**.

Events come in different formats depending on the context. They can be: 
- **Primitive Values** like plain text or numbers. 
- **Key-value pairs** like an ID mapped to a GPS coordinate.
- **Key-value pairs with timestamps** giving the event a specific moment in time. The format chosen depends on how much context and traceability the system requires.


### **From Simple to Complex Streaming Scenarios**

In a basic event pipeline, data flows from a single *event source* (a sensor, database, or application) to a single *event destination*. This one-to-one streaming works fine in isolated systems.

Real-world systems are rarely this simple. Enterprises often deal with numerous sources and destinations, and each connection may rely on different communication protocols like *FTP*, *HTTP*, *JDBC*, or *SCP*.  
Managing these interactions manually becomes unfeasible. That’s why we introduce a more structured intermediary: the **Event Streaming Platform (*ESP*)**.

### **What Is an Event Streaming Platform (ESP)?**

An ESP functions as a centralizer for handling events. Instead of connecting every source to every destination individually, sources *send events* to the ESP, and destinations simply *subscribe* to what they need.  This architecture decouples producers from consumers and creates a more maintainable and scalable system.

The ESP acts not only as a conduit but also as a layer that can store, analyze, and process data in real time.

### **Core Components of an ESP**

To support this functionality, most ESPs are built with a modular architecture that includes:

- **<u>Event Broker</u>(clustered servers)**: The main component responsible for receiving, processing, and delivering events. It has three parts:
  - The **Ingester**, which collects data from various sources.
  - The **Processor**, which transforms, encrypts, compresses, or formats the data.
  - The **Consumption Layer**, which manages the delivery of data to subscribers.

📌  ![ESP Event Broker](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/ESP-EventBroker.png)


- **<u>Event Storage</u>**: Temporarily or permanently stores events so they can be retrieved later by consumers. This ensures durability and allows asynchronous processing.

- **<u>Analytic and Query Engine</u>**: Provides interfaces for querying historical data or analyzing trends, often using SQL-like syntax or integrated dashboards.

Together, these components create a robust ecosystem where events can flow continuously and be consumed at the pace and scale each destination requires.


### **Popular ESP Technologies**

Several platforms have become popular in this domain due to their scalability and rich ecosystems:

- **Apache Kafka**: The most recognized open-source ESP, widely used across industries.
- **Amazon Kinesis** & **Azure Event Hub**: Cloud-native solutions with seamless integration into their respective ecosystems.
- **Apache Flink**: Particularly strong in stream processing and real-time analytics.
- **IBM Event Stream**: Tailored for enterprises seeking secure and scalable deployments, especially in regulated industries.

Each tool brings unique strengths and trade-offs, and the right choice depends on the organization’s architecture and goals.

### **Recap**

Throughout this lesson, we learned that:

- Events describe observable state changes and are central to streaming architectures.
- Events may be primitive, structured as key-value pairs, or include timestamps.
- Simple pipelines can be extended into complex networks of sources and destinations.
- ESPs provide a unified solution to manage this complexity by acting as centralized intermediaries.
- Core components of an ESP include the **event broker**, **event storage**, and **query/analytic engine**.
- Tools like **Apache Kafka**, **Amazon Kinesis**, and **Apache Flink** are among the leading technologies powering modern event-driven systems.

These platforms are fundamental to enabling responsive, scalable, and real-time data architectures in today’s distributed digital ecosystems.

---
---

## **Apache Kafka Overview**

### **Understanding Apache Kafka as an Event Streaming Platform**

**Apache Kafka** is an open-source event streaming platform designed to handle real-time data flows at massive scale. It serves as a central hub where event *producers* send data that can then be consumed by multiple applications. Originally created to track user activities - keystrokes, page views, or mouse clicks, it has since evolved into a general-purpose system capable of handling a broad range of use cases, from sensor data and application logs to financial transactions and analytics pipelines.

Kafka simplifies the complexity of modern data architectures by decoupling data sources from destinations. *Producers* push event records into Kafka, which then stores them durably and makes them available to *consumers* via a *subscription* model. These *consumers* can store the data, process it in real time, trigger alerts, or feed dashboards and AI models. This architecture enables asynchronous and scalable communication between distributed systems.

### **Kafka Architecture**

Kafka follows a **client-server architecture** based on TCP protocol. Its architecture comprises three primary layers:

- **Producers**: Applications written in Java, Python, Go, or REST clients, publish events to Kafka topics.
- **Clustered servers** (**brokers**): receive the events and store them across partitions with configurable replication for fault tolerance.
- **Consumers**: Subscribe to topics and read the events at their own pace, independently of producers.

*Kafka Connect* is used to integrate with external data sources or sinks (e.g., databases, file systems), and *Kafka Controller* manages metadata and broker coordination.  
Older versions relied on **Zookeeper**, but Kafka now supports **KRaft**, a native consensus mechanism that eliminates this dependency, simplifying deployment and management.

📌  ![Kafka Architecture](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/Kafka-Architecture.jpg)

### **Common Use Cases**

Kafka is widely used across industries because of its reliability and performance:

- Capturing user activity for behavioral analytics.
- Streaming metrics from infrastructure or applications.
- Centralizing log aggregation across distributed services.
- Processing financial transactions in real time with guaranteed durability.
- Enabling real-time analytics, including dashboards and machine learning pipelines.
- Supporting governance and audit trails, especially in regulated sectors like banking.

Its flexible and decoupled design makes it ideal for hybrid and multi-cloud data architectures.

### **Main Features of Apache Kafka**

Kafka is designed to support high-throughput, low-latency workloads. Its key features include:

- **Distributed system** that supports parallel processing.
- **High scalability** through horizontal clustering of brokers.
- **Reliability** via partitioning and replication.
- **Permanent event storage**, allowing late consumers to catch up without data loss.
- **Open source and extensible**, with active community support and robust documentation.

Kafka's persistent storage means consumers can read data at any point in time — a significant advantage over traditional messaging systems where data is transient.

### **Kafka as a Service**

Running Kafka in production requires careful tuning and monitoring. To simplify this, several managed service providers offer Kafka-based streaming platforms:

- **Confluent Cloud** provides a fully managed Kafka deployment with additional tools for stream processing and data governance.
- **IBM Event Streams** enhances Kafka with enterprise-grade features like disaster recovery and security compliance.
- **Amazon MSK (Managed Streaming for Kafka)** offers Kafka as a native AWS service, simplifying deployment and integration with the AWS ecosystem.

These services allow teams to focus on building data pipelines rather than managing infrastructure.

### **Recap**

In this lesson, you learned that **Apache Kafka** is a leading open-source **event streaming platform** (**ESP**) that enables high-throughput, fault-tolerant data pipelines.  Kafka decouples event producers and consumers, providing a scalable architecture for real-time analytics, log collection, metric tracking, and financial transaction processing.

You also explored Kafka’s architecture, including its *brokers*, *topics*, *partitions*, and *replication model*, and saw how **Kafka Connect** and **Kafka Controller** support integration and coordination. With the move from Zookeeper to **KRaft**, Kafka has streamlined its internal management.

Finally, you discovered that although Kafka is powerful, it can be complex to manage at scale. Providers like **Confluent Cloud**, **IBM Event Streams**, and **Amazon MSK** offer managed Kafka services to help organizations deploy and operate Kafka more easily, while still leveraging all of its core capabilities.

---
---

## **Building Event Streaming Pipelines Using Kafka**

### **Core Kafka Components and Structure**

Kafka operates as a cluster of **brokers**, each of which acts as a dedicated server responsible for storing, processing, and distributing data.

Each broker maintains one or more **topics**, which serve as logical containers for event data. These topics are used to classify streams of information, such as *log_topic*, *payment_topic*, or *user_click_topic*, depending on the use case.

To ensure scalability and fault tolerance, Kafka topics are divided into **partitions**, which can be **replicated** across multiple brokers. This allows multiple consumers to read in parallel while protecting the system against broker failures. For instance, *log_topic* can be split into partitions 0 and 1, with each partition replicated at least once to ensure availability.

### **Managing Topics with Kafka CLI**

Kafka offers a command-line interface (**CLI**) to manage topics:

```Bash
# Creating a topic involves specifying the number of partitions and replication factor:   
  kafka-topics --bootstrap-server localhost:9092 --topic log_topic --create --partitions 2 --replication-factor 2

# Describing topic details:  
  kafka-topics --bootstrap-server localhost:9092 --describe log_topic

# Deleting a topic:  
  kafka-topics --bootstrap-server localhost:9092 --topic log_topic --delete
```


### **Kafka Producers and Publishing Logic**

**Kafka producers** are client applications that publish events to specific topic partitions. Events can optionally include a *key*. If a key is provided, Kafka ensures that all events with the same key go to the same partition — preserving order. Without a key, events are distributed across partitions in a round-robin manner.

For example, a *log_producer* may publish system logs, while a *user_producer* might emit user activity data. Events associated with a user ID (key) are directed to the same partition, enabling efficient replay and consistency.

#### **Kafka Producer in Action**

In practice, you might have one event source generating logs and another generating user activity events. These sources are connected to Kafka via producers. Events are serialized and stored in their corresponding topic partitions (*log_topic*, *user_topic*, etc.).

To publish via CLI:

```python
# Without Keys
  kafka-console-producer --broker-list localhost:9092 --topic log_topic
```
-log1  
-log2

```python
# With Keys
  kafka-console-producer --broker-list localhost:9092 --topic user_topic --property parse.key=true --property key.separator=,
```
 -user1,login website  
  -user1,click item 

### **Kafka Consumers and Event Replay**

**Kafka consumers** subscribe to topics and read data in the same order it was written. Each consumer tracks its *offset*, indicating where it last left off. This offset is critical for ensuring data consistency and enabling replay.

Kafka supports two consumption modes:

```python
# Consume from last offset (default behavior)
kafka-console-consumer --bootstrap-server localhost:9092 --topic log_topic
# Consume from beginning to replay all historical events:
kafka-console-consumer --bootstrap-server localhost:9092 --topic log_topic --from-beginning
```

This flexibility makes Kafka suitable for both real-time and retrospective analytics.

### **Example: Weather and Twitter Pipeline**

Imagine integrating weather data with social sentiment analysis:

📌  ![Weather Pipeline Example](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/WeatherPipeline-example.jpg)

1. **Producers** pull JSON data from the *IBM Weather API* and *Twitter API*.
2. Data is published to two topics: *weather_topic* and *twitter_topic*.
3. **Consumers** deserialize the data and pass it to a *DB Writer*.
4. The writer stores records in a *relational database* (*RDBMS*).
5. A **dashboard** queries and visualizes the data for pattern analysis — for example, showing how users react online to extreme weather events.

### **Recap**

In this lesson, you learned: 
- How to construct streaming pipelines using **Apache Kafka**. Core components include *brokers*, *topics*, *partitions*, *replications*, *producers*, and *consumers*. 
- How to interact with Kafka using CLI tools like `kafka-topics`, `kafka-console-producer`, and `kafka-console-consumer`.

Kafka’s architecture allows for both *real-time streaming* and *retrospective analysis*, with powerful features like *offset management*, *replication*, and *key-based partitioning*.

---
---

## **Kafka Streaming Process**

### **Ad Hoc Stream Processing in Kafka**

Kafka stream processing involves transforming raw events into refined insights — often in real time. An initial, direct way to do this is by setting up an [*ad hoc*](https://dictionary.cambridge.org/dictionary/english/ad-hoc) pipeline where a consumer reads from a topic, applies logic (like filtering or transformation), and writes to a new topic through a producer.

Take the example of processing weather data: raw JSON events are published to the `raw_weather_topic`. A **consumer** then reads this stream and passes it to a *weather data **processor***, which might filter out only extreme conditions. The transformed events are then re-published to a `processed_weather_topic`, from which a new consumer can read and push data to a weather dashboard.

📌  ![Ad hoc Stream Processing Example](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/adhoc-streamprocessing.jpg)

While this model works, it quickly becomes unmanageable at scale. Each new processing logic requires manually orchestrating consumers and producers.


### **Kafka Streams API: Declarative Stream Processing**

Kafka addresses this complexity through the **Kafka Streams API** — a lightweight Java client library tailored for processing data stored in Kafka topics. The API handles stream ingestion, transformation, and re-publication within a single application, simplifying development and improving maintainability.

It enforces *exactly-once processing* semantics by ensuring each record is processed a single time. More importantly, it processes events *record by record*, which keeps latency low.

📌 ![Kafka Stream API](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/KafkaStreamsAPI.jpg)

The Streams API is built around a **computational graph**, called a *stream processing topology*, where:
- **Nodes** are stream processors (each performs a transformation like filtering or aggregating).
- **Edges** are streams of events flowing between processors.
- The **source processor** reads from Kafka topics and begins the flow.
- The **sink processor** publishes the final result to a Kafka topic.


### **Stream Topology in Action**

The stream processing topology formalizes the flow of data through a series of processors.

📌 ![Stream Topology](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/StreamTopology.jpg)

A possible flow might look like this:
1. A **source processor** consumes from the `topic`.
2. A downstream **stream processor** filters for extreme events.
3. The final **sink processor** writes to the `processed_weather_topic`.

This topology approach eliminates the need to manage separate consumer/producer logic manually and scales much more gracefully in complex scenarios.

### **Kafka Weather Processing with Streams API**

Let’s revisit the weather processing pipeline — this time using the **Kafka Streams API**:

📌 ![Kafka Weather Stream](https://raw.githubusercontent.com/vbs-matheus/coursera/refs/heads/main/imgs/KafkaWeatherStreamsAPI.jpg)

1. A *weather producer* publishes raw weather data to `raw_weather_topic`.
2. The Streams API consumes from this topic using a **source processor**.
3. A **stream processor** filters for high-temperature records.
4. A **sink processor** publishes the result to `processed_weather_topic`.
5. Finally, a consumer reads the processed stream for dashboard visualization.

This design dramatically simplifies logic and promotes reuse and scalability.

### **Recap**

- The **Kafka Streams API** is a lightweight client library for stream processing within Kafka pipelines.
- It replaces manual consumer-producer setups with **stream topologies**, where processors handle transformations.
- A **source processor** ingests data from Kafka topics, and a **sink processor** publishes it back.
- Stream processing becomes more manageable, composable, and resilient using this model — especially when scaling across many topics or complex workflows.

Kafka Streams empowers developers to create real-time, declarative, and fault-tolerant data applications directly within the Kafka ecosystem.

## Final Assignment

The final assignment is the final module, where we apply our knowledge to explore two hands-on labs. “Creating ETL Data Pipelines using Apache Airflow”.

The tasks for this final module will be:
- To build ETL pipelines using real-world scenarios - **extract**, **transform**, and **load** data into a *CSV file*. 


### Task Resolutions
- The hands-on lab tasks resolution are on the [ETL_tool_data.py](https://raw.githubusercontent.com/vbs-matheus/coursera/main/ETL_tool_data.py) file.  
   The data set used for the the task can be downloaded on this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz)