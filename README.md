## **1. Downloaded libraries used**
*   Pandas, numpy, seaborn, matplotlib.pyplot, sklearn.preprocessing, bs4, requests, csv
## **2. Web scraping process**
### **2.1. Requirement files** 
*   bonbanh.com.py
*   Other brands and models.txt
*   **These two files must be placed in the same folder**
*   Data are scraped from all of bonbanh.com pages
### **2.2. To do web scraping:**
*   1. Import necessary libraries
*   2. Run bonbanh.com.py. If the htlm layout of bonbanh.com is changed, this might not work
*   3. A dataset will be generated with name "dataset.csv"
### **2.3. Explanation of the code**
*   Loop through each page, for each page loop through each car's item
*   def find_car(n): Get to each page of bonbanh.com, apply 'utf-8' encoding, get that page htlm layout, find all car-items, get each car's name, brand, model and price, call another function to get more detail and then write details into a csv file
*   get_detail(address): Get to the car specific page and get the other informations
*   find_brand_model(soup): Get the brand and model from the cars page filter and from downloaded file :Other brands and models.txt because soup can't scraping them
*   write_csv(list): Write into dataset.csv file the detail of each car
## **3. EDA**
*   **Explained in EDA.ipynb**
## **4. Modelling**
## **5. Evaluation**
## **6. User Interface**

### **6.1. Install Dependencies**

- pip install -r requirements.txt
  
### **6.2. User Interface Demo**
```bash
streamlit  run  app.py
```
- Run: streamlit run app.py

### **6.3. File**
- [app.py](./app.py): Demo UI Application
- [model.ipynb](./model.ipynb): Machine learning models for car price prediction
- [processing-data.ipynb](./processing-data.ipynb): Data processing
- [dataset.csv](./dataset.csv): Raw crawled data
- [data.csv](./data.csv): Processed data for training models
- [data.json](./data.json): Car information for UI Demo

