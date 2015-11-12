# Workflow

* Control of engine starts with **manager.py**
* **manager.py** makes us of *multiprocess* and *subprocess* to spawn extractor, preprocessor and postprocessor as separate processes
* **config.py** in the **utilities** package stores tuning parameters such as 'alarm' times, file limit etc.
* Refer to [this](https://drive.google.com/file/d/0B4cI0VUerUwedEVlNHF2bTk0ckU/view?usp=sharing) .ppt for further information

# Manager

* **manager.py** first spawns the extractor and preprocessor
* It then waits for an *alarm (stop)* 
* Once the *alarm* goes off, it kills the extractor and signals preprocessor to stop
* It then calls the postprocessor and waits for another *alarm (restart)*
* Once the *alarm* goes off it starts all over
* The alarms have been temporarily set to *23:55* of the current day and to *00:05* of the next day respectively

# Extractor

* Uses Twitter Streaming API to extract tweets
* Stores tweets in a file till file limit is reached
* It then moves the file to the *temp* folder

# PreProcessor

* It processes files in the *temp* folder periodically
* It dumps relevant information into the current day's *raw* collection
* It then deletes the file

# PostProcessor

* It calls two subprocesses
* The first one calculates the current day's aggregate
* The second one calculates the new weekly aggregate as mentioned in the .ppt


# init

* Clone the git repository
* Run the **start_mongo.bat** to start MongoDB
* Run **manager.py** to start engine **(Do not do this yet)**

# Dataset

* Download dataset(s) from the [Drive folder](https://drive.google.com/folderview?id=0B4cI0VUerUweVWhuOGJSTGR0b28&usp=sharing "Google Drive")
  * The **full_dataset.rar** contains all **2 Million** tweets
  * Optionally, you can download parts of this dataset from the **Parts** folder, each _(dataset\*.rar)_ containing **200,000** tweets 
  * Each *.json* file contains **10,000** tweets

# Portal

* The **portal** folder is the django project for the web portal
* Create a database called 'trends'
* In the settings file, change password for mysql root, in case it is different
* Run createsuperuser to create an admin
* Create some top trends using the admin site. I have included a screenshot for UI after creating some sample topics(with ranks). It will redirect to the details page after clicking(see screenshots).
* Homepage can be opened using the url: 127.0.0.1:8000/home or localhost:8000/home
* TopTrends model has a topic object and a rank object. Will be modified to include graphs n all when implementation is done.

#Screenshots
* of samples can be added for demonstration
