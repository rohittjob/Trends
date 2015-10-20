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
* Create a database called 'trends'
* Run createsuperuser to create an admin
* Homepage can be opened using the url: 127.0.0.1:8000/home or localhost:8000/home
* TopTrends model has a topic object and a rank object. Will be modified to include graphs n all when implementation is done.
* Create some top trends using the admin site. I have included a screenshot for UI after creating some sample topics(with ranks). It will redirect to the details page after clicking(see screenshots).

# Tweet Extractor

* PyCharms project for extracting tweets
* **twitter_streaming.py** extracts tweets

#Screenshots
* of samples can be added for demonstration