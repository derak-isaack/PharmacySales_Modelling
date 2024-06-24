![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=for-the-badge)
![SQL](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=fff&style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=fff&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?logo=apachekafka&logoColor=fff&style=for-the-badge)

## <div style="padding: 35px;color:white;margin:10;font-size:200%;text-align:center;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://images.pexels.com/photos/7078619/pexels-photo-7078619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)"><b><span style='color:black'><strong> Pharmacy Sales Tracker </strong></span></b> </div> 

`Motivation:` With the ever rising need for automation and real-time tracking across sales organizations to minimize human error and identify fraud, I sought to develop a `Streamlit` application which uses `MySQL server` database and is intergrated with `Apache Kafka` which offers `Low latency` to ensures `real-time data streaming`.

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Project Overview</span></b> </div>

Streamlit real-time Pharmacy sales tracker that uses the `star-schema` to track sales across several pharmacy outlets for a big pharma. The application leverages on using the `star-schema` which is:

* Easier to understand and manage
* Less dependant on table joins.
* High performance.

The application also uses the `MySQL server database` for data entry which  has several advantages namely:

* supports transactions.
* Supports data integrity.
* Handles severall transaction requests simultaneously.
* Offers atomicity. 

The application also intergates `Apache Kafka` for real-time data streaming as well as transformations. Using `Kafka` offers the following benefits namely:

* `Data durability and reliability` because data is stored on disk across brokers
* `Real-time data processing`
* Flexibility in `batch and stream processing.`
* `Data auditing and compliance`: With Change Data Capture (CDC) approaches, Kafka facilitates data replication across multiple systems or databases, ensuring accurate and consistent data for auditing and compliance purposes. 

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Objectives & description</span></b> </div>

Develop a data model that follows the `star-schema` approach having the `dimensions` and `facts` table. The `table-models` can be found [here](pharmacy_sales_tracker.sql) which typically follows the `sql` approach. 

Defining the tables in a separate file offers a more flexible approach for the application suppose further change may arise. It also provides easy debugging for the application. 

`ERD-diagram` ![ERD](ERD_diagram.png)

This [python-file](helpers.py) defines a class using the traditional `python OOP` approach which offers more customization and flavour to the main `streamlit application`.It also allows form sharing from the `doctor table`, `Employee table` and `Drug items` tables which are the `dimension tables` which very vital in providing more context to the `Facts table`. 

Intergrate `Apache Kafka` into the streamlit application to serve as the `Producer`. The data should be in `JSON` formart for easier ingestion into the `Kafka topics`. This is made possible by using the `serializer` which allows for transformation of data into `JSON` formart. 

Read data from `Kafka topics` by a consumer to allow for `Real-time` data streaming as well as processing. The consumer can be found [here](kafka_consumer.py)

To get started with `Apache Kafka`, the `Zookeper` should be running. On windows, the command to run the `Zookeeper` is `.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties`. The `Kafka server` should also be running and is possible by uisng the command `.\bin\windows\kafka-server-start.bat .\config\server.properties`. 

N/B: Apache Kafka should be correctly configured in the environment variables to allow port communication.

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Conclusion & Future steps</span></b> </div>

The `Sreamlit app` is deployed locally due to the constraints of the database being available locally and `Apache Kafka` port usage. Here is a snippet of the `User Interface` for inputting sales data to provide real-time tracking. 

![Dimensions-snippet](Dimensions.png)
![Facts-snippet](Facts.png)

After running the `Consumer`, here is a snapshot of how the data streams in from the streamlit application 

![Data-stream](data_stream.png)




