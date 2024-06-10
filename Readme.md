![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=for-the-badge)
![SQL](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=fff&style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=fff&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)

## <div style="padding: 35px;color:white;margin:10;font-size:200%;text-align:center;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://images.pexels.com/photos/7078619/pexels-photo-7078619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)"><b><span style='color:black'><strong> Pharmacy Sales Tracker </strong></span></b> </div> 

`Motivation:` With the ever rising need for automation across sales organizations to minimize human error, I sought to develop a `Streamlit` application which uses an `OLTP` database namely `SQLITE3` which has `Low latency` which ensures `real-time updates`.

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Project Overview</span></b> </div>

Pharmacy sales tracker Streamlit application that uses the `star-schema` to track sales across several pharmacy outlets for a big pharma. The application leverages on using the `star-schema` which is:

* Easier to understand and manage
* Less dependant on table joins.
* High performance.

The application also uses the `SQLite3 OLTP database` for data entry which  has several advantages namely:

* supports transactions.
* Supports data integrity.
* Handles severall transaction requests simultaneously.
* Offers atomicity. 

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Objectives & description</span></b> </div>

Develop a data model that follows the `star-schema` approach having the `dimensions` and `facts` table. The `table-models` can be found [here](pharmacy_sales_tracker.sql) which typically uses the `sql` approach. 

Defining the tables in a separate file offers more control to the application. It also provides easy debugging for the application. 

`ERD-diagram` ![ERD](ERD_diagram.png)

This [python-file](helpers.py) defines a class using the traditional `python OOP` approach which offers more customization and flavour to the main `streamlit application`.It also allows form sharing from the `doctor table`, `Employee table` and `Drug items` tables which are the `dimension tables` which very vital in providing more context to the `Facts table`. 



