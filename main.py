##############################################################
# created by: Deborah Sanchez
# email: debsanchez.business@outlook.com
# date: 9-27-2024
# desc: This sample Python project teaches you how to grab
# html from an api or a website. This project is week 2 of a 
# 5 week project which can be downloaded at 
# https://github.com/crickidie.
##############################################################

##############################################################
# This sample code uses the 'requests' object.
# To install this object, open terminal within
# your python session and run 'pip install requests'
##############################################################

import os
import requests

def get_html(url):
    rsp = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'})

    # rsp = requests.get(url)

    if (rsp.status_code == 200):
        return rsp.text
    else:
        print("The request failed.")

def main():
    os.system('cls')

    rtn = get_html('https://www.imdb.com/list/ls003832260/')

    print(rtn)

    input("Press enter to exit.")

if __name__ == "__main__":
    main()
