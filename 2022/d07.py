#!/usr/bin/env python3

import re


def dir_size_tot(fs):
    fs_size = {}
    for key in fs:
        dir_tot = 0
        flag = ""
        for item in fs[key]:
            try:
                dir_tot += int(item)
            except ValueError:
                # there is a string with directory in the fs[key] list
                flag = "err"

        if flag == "err":
            fs_size[key] = -1
        else:
            fs_size[key] = dir_tot
    return fs_size


def dir_sizes_all(history):
    fs = {}
    dirpath = ""
    tmp = []

    i = 0
    while i < len(history):
        command = history[i]
        if command.startswith("$ cd "):
            if command != "$ cd ..":
                dirname = command.split()[2]
                if dirname == "/":
                    # I don't like slash in the string path
                    dirpath = "root"
                else:
                    dirpath += ":" + dirname
            else:
                # cd .., one up
                ridx = dirpath.rfind(":")
                dirpath = dirpath[0:ridx]
        else:
            if command.startswith("$ ls"):
                if dirpath in fs:
                    tmp = fs[dirpath]
                else:
                    tmp = []
            elif command.startswith("dir"):
                # deal with directory which is empty with no files
                dirpath_empty = dirpath + ":" + command.split()[1]
                if not dirpath_empty in fs:
                    fs[dirpath_empty] = []
                tmp.append(dirpath_empty)
            else:
                # get file size
                filesize = re.match(pattern=r"\d+", string=command)
                if filesize:
                    tmp.append(int(filesize.group()))
                else:
                    pass
            fs[dirpath] = tmp
        i += 1

    # empty directory with no files = 0
    fs_size = dir_size_tot(fs)
    for dkey in fs:
        if len(fs[dkey]) == 0:
            fs[dkey] = [0]
            fs_size[dkey] = 0
    # print(fs)
    # print(fs_size)

    # print("LOOP")
    # sort of recursion, go through all files until all directories have int values (not -1)
    i = 0
    while True:
        for nkey in fs_size:
            nkey_val = fs_size[nkey]
            if nkey_val >= 0:
                for dkey in fs:
                    tmpar = fs[dkey]
                    if nkey in tmpar:
                        # find the index of "dir key" and replace with number
                        idx = tmpar.index(nkey)
                        tmpar = tmpar[:idx] + [nkey_val] + tmpar[idx + 1:]
                        fs[dkey] = tmpar
        fs_size = dir_size_tot(fs)

        if all(fs_size_val >= 0 for fs_size_val in fs_size.values()) or i == 40:
            return fs_size
        i += 1


def advent_a(history):
    fs_size = dir_sizes_all(history)

    smaler_size = 0
    for key in fs_size:
        if fs_size[key] <= 100000:
            smaler_size += fs_size[key]

    return smaler_size


def advent_b(history):
    fs_size = dir_sizes_all(history)

    smallest = 0
    unused_min = 70000000
    free_space = unused_min - fs_size["root"]
    for key in fs_size:
        unused = free_space + fs_size[key]
        if unused_min > unused > 30000000:
            unused_min = unused
            smallest = fs_size[key]

    return smallest


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        arr = ["$ cd /",
               "$ ls",
               "dir a",
               "14848514 b.txt",
               "8504156 c.dat",
               "dir d",
               "$ cd a",
               "$ ls",
               "dir eee",
               "dir x",
               "29116 f",
               "2557 g",
               "62596 h.lst",
               "$ cd eee",
               "$ ls",
               "584 i",
               "$ cd ..",
               "$ cd ..",
               "$ cd d",
               "$ ls",
               "4060174 j",
               "8033020 d.log",
               "5626152 d.ext",
               "7214296 k"]
        pass
    else:
        with open("inputs/input_07.txt", "r") as f:
            arr = f.readlines()
            arr = [x.strip() for x in arr]
        f.close()

    print(advent_a(arr))
    print(advent_b(arr))

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
