# init

* Clone the git repository
* Download dataset(s) from the [Drive folder](https://drive.google.com/folderview?id=0B4cI0VUerUweVWhuOGJSTGR0b28&usp=sharing "Google Drive") *(to be added)*
  * The **full_dataset.rar** contains all **2 Million** tweets
  * Optionally, you can download parts of this dataset from the **Parts** folder, each _(dataset\*.rar)_ containing **200,000** tweets 
  * Extract into the **data** folder
  * Make sure the __data\*.json__ files are in the **data** folder
  * Each *.json* file contains **10,000** tweets
* Run the integrity test by executing the **test.py** script in the **data** folder

# Portal

* The **portal** folder is the django project for the web portal

# Tweet Extractor

* PyCharms project for extracting tweets
* **twitter_streaming.py** extracts tweets
