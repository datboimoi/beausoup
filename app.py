#import beautifulsoup and request here
from urllib import response
from bs4 import BeautifulSoup
import requests
import json 

# Setting up Flask
from flask import Flask, render_template
app = Flask(__name__, template_folder = 'templates')

@app.route('/')

# Displaying html file
def displayJobDetails(name=response):
    return render_template('index.html', response = response)


# Function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'
def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here
    # Python request from code snippet off Postman
    payload={}
    headers = {
    'Cookie': 'AWSALB=WhC08lJfwR7hGPOtEMAEI5qmoRZf0Y+tFNWBRz0S7lHg/D+AHqsC/v1pAK1F4opXAEXGfGeEclHkLIdU7oxRcu+T+RtI1jbgi5QizAdO7mZ8a+QrKCSeeFWztAPY'
    }

    # Getting status code with request & printing it out
    response = requests.request("GET", url, headers=headers, data=payload)
    status = requests.get(url).status_code
    print("Status Code: ", status, "\n")
    html_doc = response.text

    # Putting results into an array using soup
    soup = BeautifulSoup(html_doc, 'html.parser')
    JobDetails = soup.find_all('div', class_='card card__job')
    # Creating an array to hold results
    jobList = []
    # Looping through html_doc & parsing
    for job in JobDetails:
        jobTitle = job.find('h2', class_='card__job-title').text.strip()
        company = job.find('div', class_='card__job-empname-label').text.strip()
        description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
        # Turning parsed doc into dictionary
        jobDetailsjson = {
            "Title": jobTitle,
            "Company": company,
            "Description": description
        }
        # Adding json to jobList array
        jobList.append(jobDetailsjson)

    # Printing out search results
    print("Search Results: \n")
    for result in jobList:
        print(str(result) + '\n')
    
    return jobList

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON\n")
    with open('jobDetails.json', 'w') as outfile:
        json.dump(jobDetails, outfile)

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search: ")
    role = input()
    print("Enter the location you want to search: ")
    location = input()
    print('')
    
    #print("Role: ", role, "Location: ", location)

    # Complete the missing part of this function here
    jobDetails = getJobList(role, location)

    saveDataInJSON(jobDetails)

if __name__ == '__main__':
    main()
