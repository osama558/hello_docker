from bs4 import BeautifulSoup as bs

import requests 

url = "https://en.wikipedia.org/wiki/Table_(information)"

def extract(url):
    try:    
        ''' This function aims to extract the required
        information from the website and save it to a data frame. The
        function returns the data frame for further processing. '''
        page = requests.get(url).text
        data = bs(page,'html.parser')
        #df = pd.DataFrame(columns=table_attribs)
        tables = data.find_all('tbody')
        #print(tables)
        rows = tables[0].find_all('tr')
    #print(rows)
        for row in rows:
            col = row.find_all('td')
            
            if len(col)!=0:
               # print(col[0].contents[0])
                data_dict = {"Rank": col[0].contents[0],
                    "Name": col[1].contents[0],
                    "MC_USD_Billion": col[2].contents[0][:-1],
                    }
                #print(data_dict)
        #       df1 = pd.DataFrame(data_dict, index=[0])
        #        df = pd.concat([df,df1], ignore_index=True)
        #return df
        return data_dict
    except requests.exceptions.MissingSchema:
        print('Url invalid')


i = extract(url)