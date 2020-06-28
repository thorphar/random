# Lathes.co.uk Web Scraper


## Prerequisites

```
 -  conda install -c conda-forge selenium 
 -  conda install -c conda-forge beautifulsoup4 
 -  conda install -c conda-forge python-pdfkit 
 ```

 You will also need to install wkhtmltopdf however I've had issues with 0.12.4 which is installed when you run ``` sudo apt install wkhtmltopdf ``` so you will need to install the more recent one to resolve these issues. The version used in this example was from the [ wkhtmltopdf - 0.12.6 r1](https://github.com/wkhtmltopdf/packaging/releases/0.12.6-1) releases page. 

 ```
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb
sudo dpkg --install wkhtmltox*
rm wkhtmltox*
 ```
Thanks to [trentmu](https://discuss.erpnext.com/t/wkhtmltopdf-error-since-last-update/49744) for the solution.

