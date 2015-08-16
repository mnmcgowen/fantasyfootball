class fanPlayer:
    def __init__(self, _name, _cost, _dept):
        self.dept = _dept
        self.cost = _cost
        self.name = _name

class fanLeague:
    def __init__(self, _cost):
        self.cost = _cost
        self.depts = []
        self.players = []
    def dept_count(self):
        return len(self.depts)
    def add_player(self, p):
        if (p.dept in self.depts):
            self.depts.remove(p.dept)
        self.depts.append(p.dept)
        self.players.append(p)

class fanPool:
    def __init__(self, _cost):
        self.cost = _cost
        self.depts = {}
        self.size = 0
    def add_player(self, p):
        if p.dept not in self.depts.keys():
            self.depts[p.dept] = [p]
        else:
            self.depts[p.dept].append(p)
        self.size += 1
    def find_player(self, l):
        for dept, ps in self.depts.iteritems():
            if dept not in l.depts:
                self.size -= 1
                return ps.pop()
        for dept in l.depts:
            if dept in self.depts and len(self.depts[dept]):
                self.size -= 1
                return self.depts[dept].pop()
        return null # could not add a player

###
### test
###

import sys

MIN_PER_LEAGUE = 8

pools = {}

with open(sys.argv[1]) as f:
    file = f.readlines()

for line in file:
    name, cost, dept = line.split()
    if cost not in pools.keys():
        pools[cost] = fanPool(cost)
    pools[cost].add_player(fanPlayer(name, cost, dept))

for cost, pool in pools.iteritems():
    num_leagues = pool.size / MIN_PER_LEAGUE # todo check for error
    leagues = [fanLeague(pool.cost) for count in xrange(num_leagues)]
    while (pool.size > 0): # todo check for even count
        for league in leagues:
            league.add_player(pool.find_player(league))
            league.add_player(pool.find_player(league))
            if (pool.size == 0):
                break
    for league in leagues:
        print(league.cost + " LEAGUE")
        for player in league.players:
            print(player.name + "\t" + player.dept)


            
