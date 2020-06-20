import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pdfkit
import re

def sanitize_name(name):
    name = (name.strip()).replace("\r","")
    name = re.sub(r"\s+","",name)
    name = name.replace("\x92","")
    name = name.replace(".","-") 
    name = name.replace("/","-")
    return name

if __name__ == '__main__': 
    # Configuring target url
    url = 'http://lathes.co.uk/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    # Parsing the response
    machine_list = soup.find('tr',{"style": "height:211.9pt"})
    machine_list = machine_list.find_all('a',href=True)

    # Building progress model
    total = len(machine_list)
    print("Total: " + str(total))

    # Check for inactive webpages
    inactive_pages = []
    search = False # Change to True to check for inactive pages
    if search:
        for link in machine_list:
            response = requests.get(link['href'])
            if response.status_code != 200:
                inactive_pages.append(link['href'])
                print(link['href'])
    else:
        inactive_pages = [
        "http://www.lathes.co.uk/americanlathepatents",
        "http://www.lathes.co.uk/clarksengineering",
        "http://www.lathes.co.uk/outilerve",
        "http://www.lathes.co.uk/glashutte"]
        
    total = len(machine_list) - len(inactive_pages) # Update total with inactive pages
    count = 0

    # Convert each HTML page to PDF and save locally
    for link in machine_list:
        progress = (count/total)*100 # Calculate progress
        url = link['href']
        if url not in inactive_pages: # Not converting pages where repsonse was not OK
            print('-'*30)  
            machine_name = link.contents[0]
            machine_name = sanitize_name(machine_name)
            print("""Progress: {:.2f}%
            Next URL to convert: {} 
            Machine name: {}""".format(
                progress,
                url,
                repr(machine_name))) # Displaying progress
            filename = 'pdfs/' + machine_name + '.pdf' # Creating the filename
            pdfkit.from_url(url,filename) # Creating the PDF from the HTML link
            count = count + 1
        else:
            print("Broken Link: {}".format(url)) 

