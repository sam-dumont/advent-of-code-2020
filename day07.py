import os
import re
import networkx as nx

rules = []

regex = r'((\d+)? ?([a-z]+\s[a-z]+) bags?)'

rules = nx.DiGraph()

containingBags = {}


def countPredecessors(bag, rules):
    for i in rules.predecessors(bag):
        containingBags[i] = True
        countPredecessors(i, rules)


def countContaining(bag, rules):
    count = 1
    for i in rules.successors(bag):
        data = rules.get_edge_data(u=bag, v=i)
        count = count + (data["amount"] * countContaining(i, rules))
    return count


with open("./input07.txt") as file:
    for rule in file:
        i = 1
        bags = re.findall(regex, rule)
        container = bags[0][2]
        while i < len(bags):
            if bags[i][1] != "":
                amount = int(bags[i][1])
            else:
                amount = 0
            if bags[i][2] != "no other":
                rules.add_edge(container, bags[i][2], amount=amount)
            i = i + 1

countPredecessors("shiny gold", rules)
print(len(containingBags))
print(countContaining("shiny gold", rules) - 1)
