# coding: utf-8
import twitter
import os
import csv
import datetime

api = twitter.Api(
        consumer_key        = os.environ["C_KEY"],
        consumer_secret     = os.environ["C_SECRET"],
        access_token_key    = os.environ["AT_KEY"],
        access_token_secret = os.environ["AT_SECRET"],
        )



with open('mat/data.csv', 'rU') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if datetime.datetime.today().month == int(row[3]):
            if datetime.datetime.today().day == int(row[4]):
                comment = '[' + str(datetime.datetime.today().year) + '/' + str(datetime.datetime.today().month) + '/' + str(datetime.datetime.today().day) + ']\n' + row[0] + ' / ' + row[1] + ' was released ' + str(datetime.datetime.today().year - int(row[2])) + ' years ago today!'
                api.PostUpdate(comment)
