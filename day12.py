import os
import re
import math

moves = []

with open("./input12.txt") as file:
    for movement in file:
        moves.append({"key": movement[0], "value": int(movement.strip()[1:])})

location = {"x": 0, "y": 0}

directions = {0: "E", 90: "N", 180: "W", 270: "S", 360: "E"}

currDir = directions[0]
currAngle = 0

for move in moves:
    if move["key"] == "L":
        currAngle = (currAngle + move["value"]) % 360
        currDir = directions[currAngle]
    if move["key"] == "R":
        currAngle = (currAngle - move["value"]) % 360
        currDir = directions[currAngle]

    if move["key"] == "F":
        location["x"] = location["x"] + \
            int((math.cos(math.radians(currAngle)) * move["value"]))
        location["y"] = location["y"] + \
            int((math.sin(math.radians(currAngle)) * move["value"]))
    if move["key"] == "N":
        location["y"] = location["y"] + move["value"]
    if move["key"] == "S":
        location["y"] = location["y"] - move["value"]
    if move["key"] == "W":
        location["x"] = location["x"] - move["value"]
    if move["key"] == "E":
        location["x"] = location["x"] + move["value"]

print(abs(location["x"]) + abs(location["y"]))

currDir = directions[0]
currAngle = 0
waypoint = {"x": 10, "y": 1}
location = {"x": 0, "y": 0}

for move in moves:
    if move["key"] in ["L", "R"]:
        if move["key"] == "L":
            angle = math.radians(0 + move["value"])
        if move["key"] == "R":
            angle = math.radians(360 - move["value"])

        sin = math.sin(angle)
        cos = math.cos(angle)
        waypoint = {"x": round(waypoint["x"]*cos - waypoint["y"]*sin),
                    "y": round(waypoint["x"]*sin + waypoint["y"]*cos)}

    if move["key"] == "F":
        location["x"] = location["x"] + (move["value"] * waypoint["x"])
        location["y"] = location["y"] + (move["value"] * waypoint["y"])

    if move["key"] == "N":
        waypoint["y"] = waypoint["y"] + move["value"]
    if move["key"] == "S":
        waypoint["y"] = waypoint["y"] - move["value"]
    if move["key"] == "W":
        waypoint["x"] = waypoint["x"] - move["value"]
    if move["key"] == "E":
        waypoint["x"] = waypoint["x"] + move["value"]

print(abs(location["x"]) + abs(location["y"]))
