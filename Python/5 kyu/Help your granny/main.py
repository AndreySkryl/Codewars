def get_leg(hypotenuse, other_leg):
    return (hypotenuse**2 - other_leg**2)**0.5


def tour(friends, friend_towns, home_to_town_distances):
    friend_towns_in_meters = []
    for friend in friends:
        friend_town = list(filter(lambda item: item[0] == friend, friend_towns))
        if friend_town:
            town = friend_town[0][1]
            home_to_town_distance = home_to_town_distances[town]
            friend_towns_in_meters.append([friend, home_to_town_distance])

    path = [friend_towns_in_meters[0][1], friend_towns_in_meters[-1][1]]
    path.extend([get_leg(friend_towns_in_meters[i][1], friend_towns_in_meters[i-1][1])
                 for i in range(1, len(friend_towns_in_meters))])
    return int(sum(path))


friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
assert tour(friends1, fTowns1, distTable1) == 889
