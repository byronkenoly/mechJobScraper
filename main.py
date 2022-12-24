from bs4 import BeautifulSoup
import requests

def printLine():
    for i in range(0, 40):
        print("-", end=" ")

    print("\n")

jobwebkenya = requests.get('https://jobwebkenya.com/?s=mechanical+engineer&location=&latitude=+&ptype=job_listing&latitude=&longitude=&full_address=&north_east_lng=&south_west_lng=&north_east_lat=&south_west_lat=').text
brighterMonday = requests.get('https://www.brightermonday.co.ke/jobs?q=mechanical+engineering').text

#jwk - job web kenya
jwkSoup = BeautifulSoup(jobwebkenya, 'lxml')
jwkJobs = jwkSoup.find_all('li', class_ = 'job')

#brighter - brighter monday
brighterSoup = BeautifulSoup(brighterMonday, 'lxml')
brighterJobs = brighterSoup.find_all('div', class_ = 'mx-5 md:mx-0 flex flex-wrap col-span-1 mb-5 bg-white rounded-lg border border-gray-300 hover:border-gray-400 focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-gray-500')

#number of jobs found
count = 0

def jwkFunc():
    for job in jwkJobs:
        global count
        datePosted = job.find('span', class_ = 'year').text
        
        if 'Dec' in datePosted:
            count += 1
            jobTitle = job.find('a').text
            jobDescription = job.find('div', class_ = 'lista').text

            print(jobTitle)
            print(jobDescription)
            print(datePosted)
            print("Website: jobwebkenya.com")
            printLine()

def brighterFunc():
    for job in brighterJobs:
        global count
        datePosted = job.find('p', class_ = 'ml-auto text-sm font-normal text-gray-700 text-loading-animate').text

        if 'day' in datePosted:
            count += 1
            jobTitle = job.find('p', class_ = 'text-lg font-medium break-words text-brand-linked').text
            #jobDescription = job.find('p', class_ = 'text-sm font-normal text-gray-700 md:text-gray-500 md:pl-5').text
            
            print(jobTitle)
            #print(jobDescription)
            print(datePosted)
            print("Website: brightermonday.co.ke")
            printLine()

def myjobmagFunc():
    for i in range(1, 6):
        myjobmag = requests.get('https://www.myjobmag.co.ke/jobs-by-field/engineering/{}'.format(i)).text

        #mjm - myjobmag
        mjmSoup = BeautifulSoup(myjobmag, 'lxml')
        mjmJobs = mjmSoup.find_all('li', 'job-info')

        for job in mjmJobs:
            global count
            datePosted = job.find('li', id = 'job-date').text

            if 'December' in datePosted:
                count += 1
                jobTitle = job.find('a').text
                jobDescription = job.find('li', class_ = 'job-desc').text

                print(jobTitle)
                print(jobDescription)
                print(datePosted)
                print("Website: myjobmag.co.ke")
                printLine()

def fuzuFunc():
    for i in range(1, 4):
        fuzu = requests.get('https://www.fuzu.com/kenya/job?filters[term]=mechanical%20engineering&filters[job_id]=452453&page={}'.format(i)).text

        fuzuSoup = BeautifulSoup(fuzu, 'lxml')
        fuzuJobs = fuzuSoup.find_all('a', class_ = 'Card__StyledDiv-sc-uckied-0 logKwD b2c-card clickable')

        for job in fuzuJobs:
            global count
            datePosted = job.find('p', class_ = 'Text__StyledText-sc-152w2ki-0 bpWsQZ b2c-text').text

            if 'remaining' or 'today' in datePosted:
                try:
                    companyName = job.find('p', class_ = 'Text__StyledText-sc-152w2ki-0 MDWeZ b2c-text').text
                    jobTitle = job.find('h6', class_ = 'Title__StyledTitle-sc-5s9ddm-0 cvLYDq title').text
                    jobLocation = job.find('p', class_ = 'Text__StyledText-sc-152w2ki-0 ckLUZM b2c-text').text
                    count += 1
                
                    print(companyName)
                    print(jobTitle)
                    print(jobLocation)
                    print(datePosted)
                    print("Website: fuzu.com")
                    printLine()
                except AttributeError:
                    pass


jwkFunc()
brighterFunc()
myjobmagFunc()
fuzuFunc()

print("Number of jobs found with MECHANICAL ENGINEER keyword: ", count)