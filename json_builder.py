#!/usr/bin/env python

import codecs
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


def find_friend_number(name, friend_list):
    return [friend.number for friend in friend_list if friend.name == name][0]


def graph_json(list):
    # Create node list
    output = "{\n  \"nodes\":[\n"
    for index, friend in enumerate(friend_list):
        output += "    {\"name\":\"%s\",\"group\":1},\n" % friend.name
        friend.number = index
    output += "  ],\n  \"links\":[\n"
    links = []

    # Create list of links, checking if unique before adding
    for index, friend in enumerate(friend_list):
        print str(index) + "\t" + friend.name
        for mutual in friend.friends:
            a = friend.number
            b = find_friend_number(mutual, friend_list)
            pair = (a, b) if a < b else (b, a)
            if pair not in links:
                output += "    {\"source\":%d,\"target\":%d,\"value\":1},\n" % pair
                links.append(pair)

    # Finish up JSON formatting and write file
    output += "  ]\n}"
    output = output.replace(",\n  ]", "\n  ]")
    with codecs.open('friends.json', 'w', encoding='utf-8') as f:
        f.write(output)

execfile("make_list.py")
graph_json(friend_list)
