#!/usr/bin/env python

# recursion
def advent_6(input, orbits):
    for key, value in input.items():
        if value[-1] == "COM":
            orbits[key] = len(value)
        else:
            value.append(input[value[-1]][0])

    if len(orbits) == len(input):
        # 6a - remove two keys because they are not in 6a testing set, they are in the real input though,
        # but it does not matter here
        try:
            orbits.pop("YOU")
            orbits.pop("SAN")
        except KeyError:
            print("Key(s) not found")

        # 6b
        # intersection of two lists: (a & b)
        # symmetric difference:      (a ^ b) = (a | b) - (a & b)
        diff = list(set(input["YOU"]) ^ set(input["SAN"]))
        transf = len(diff)

        return orbits, transf
    

    return advent_6(input, orbits)


if __name__ == "__main__":
    import time

    start_time = time.time()
    test = False

    if test:
        input = dict()
        input["B"] = ["COM"]
        input["C"] = ["B"]
        input["D"] = ["C"]
        input["E"] = ["D"]
        input["F"] = ["E"]
        input["G"] = ["B"]
        input["H"] = ["G"]
        input["I"] = ["D"]
        input["J"] = ["E"]
        input["K"] = ["J"]
        input["L"] = ["K"]

        input["YOU"] = ["K"]
        input["SAN"] = ["I"]

        orbits, transf = advent_6(input, dict())
        # print(orbits)
        print("6a: ", sum(orbits.values()))
        print("6b: ", transf)
    else:
        input = dict()
        with open("inputs/input_06.txt", "r") as f:
            for line in f:
                planet = line.split(")")
                input[planet[1].strip("\n")] = [planet[0]]
        f.close()

        orbits, transf = advent_6(input, dict())
        print("6a: ", sum(orbits.values()))
        print("6b: ", transf)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
