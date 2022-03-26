import argparse
import random


def read_talks_file():
    with open('talks.txt') as talks_file:
        t = talks_file.readlines()

    return t


if __name__ == '__main__':
    # configure arguments
    parser = argparse.ArgumentParser(description='Randomly selects a conference talk.')

    # retrieve list of talks
    talks = read_talks_file()

    # randomly pick talk
    selected_talk = random.choice(talks)

    print(selected_talk)
