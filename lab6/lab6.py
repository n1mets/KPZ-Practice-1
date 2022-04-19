
# Task 1 - get unique word and their count from text file

def get_text_info(filepath):
    from collections import Counter
    import os.path

    if not os.path.exists(filepath):
        return "Invalid file path!"

    text = open(filepath).read()

    wordArr = []
    word = ""

    text = text.lower()

    for index, i in enumerate(text):
        if not i.isalpha():
            if len(word) != 0:
                wordArr.append(word)
                word = ""
        else:
            word += i
            if index == len(text)-1:
                wordArr.append(word)
                word = ""

    return Counter(wordArr)


# print(get_text_info("article.txt"))


# Task 2 - Work with csv file


def download_csv(urlpath):
    import requests
    import numpy as np
    import csv

    response = requests.get(urlpath)

    with open("originalUserData.csv", 'wb') as f:
        f.write(response.content)

    with open("originalUserData.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        data_read = [row for row in reader]

    del data_read[-1]

    arr = np.asarray(data_read)
    with open('originalUserData.csv', 'w') as f:
        mywriter = csv.writer(f, delimiter=',')
        mywriter.writerows(arr)

    print('Completed!')


#CSV_URL = 'https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv'
# download_csv(CSV_URL)
