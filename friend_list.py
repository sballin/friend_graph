#!/usr/bin/env python

import json
import os
import string
import pickle

class Friend:

    def __init__(self, entry):
        self.fb_id = 0
        self.name = ''
        self.friends = []

        fields = entry.split()
        self.fb_id = int(fields[0])
        self.name = ' '.join(fields[1:])

    def add(self, mutuals, master_list):
        mutuals = mutuals.split('\n')
        mutuals = [s.lstrip() for s in mutuals]
        print self.name
        for name in mutuals:
            for friend in master_list:
                if name == friend.name:
                    self.friends.append(friend)
                    print '    ' + friend.name
                    break


friend_file = 'friend_list.p'
if not os.path.isfile(friend_file):
    friend_list = os.popen('fbcmd friends').read()
    friend_list = friend_list.split('\n')
    friend_list = [Friend(friend_list[i]) for i in range(1, len(friend_list)-1)]
    pickle.dump(friend_list, open(friend_file, 'wb'))
else:
    friend_list = pickle.load(open(friend_file))

mutuals_file = 'friend_mutuals.p'
if not os.path.isfile(mutuals_file):
    for index, friend in enumerate(friend_list):
        mutuals = os.popen('fbcmd mutual %d'%friend.fb_id).read()
        friend.add(mutuals, friend_list)
        print index
    pickle.dump(friend_list, open(mutuals_file, 'wb'))
else:
    friend_list = pickle.load(open(mutuals_file))
