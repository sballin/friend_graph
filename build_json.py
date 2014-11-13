#!/usr/bin/env python

import codecs
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


def find_friend_number(name, friend_list):
    return [friend.number for friend in friend_list if friend.name == name][0]


def graph_json(list, include_self):
    # Create node list
    output = "{\n  \"nodes\":[\n"
    if include_self:
        output += "    {\"name\":\"me\"},\n"
    for index, friend in enumerate(friend_list):
        friend.number = index + 1
        output += "    {\"name\":\"%s\"},\n" % friend.number    # anonymize
    output += "  ],\n  \"links\":[\n"
    links = set()

    # Create list of links, checking if unique before adding
    for index, friend in enumerate(friend_list):
        print str(index) + "\t" + friend.name
        if include_self:
            output += "    {\"source\":%d,\"target\":%d},\n"
        for mutual in friend.friends:
            a = friend.number
            b = find_friend_number(mutual, friend_list)
            pair = (a, b) if a < b else (b, a)
            if pair not in links:
                output += "    {\"source\":%d,\"target\":%d},\n" % pair
                links.add(pair)

    # Finish up JSON formatting and write file
    output += "  ]\n}"
    output = output.replace(",\n  ]", "\n  ]")
    with codecs.open('friends.json', 'w', encoding='utf-8') as f:
        f.write(output)


execfile("scrape_fb.py")
graph_json(friend_list, include_self=False)
