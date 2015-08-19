###
### test
###

import sys
from fantasyfootball import fanPool, fanLeague, fanPlayer

MIN_PER_LEAGUE = 8

pools = {}

with open(sys.argv[1]) as f:
    file = f.readlines()

for line in file:
    name, cost, dept = line.strip().split("\t")
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

