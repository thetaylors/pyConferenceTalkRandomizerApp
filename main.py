import argparse
import random


def read_talks_file():
    with open('talks.txt') as talks_file:
        t = talks_file.readlines()
    return t


def random_talk_number(count):
    return random.randint(0, count)


if __name__ == '__main__':
    # configure arguments
    parser = argparse.ArgumentParser(description='Randomly selects a conference talk.')
    parser.add_argument('--count', action='store', help='a count of the most recent conference talks that should be'
                                                        ' included more often than others')

    # retrieve args
    args = parser.parse_args()

    # retrieve list of talks
    talks = read_talks_file()

    # randomly pick talk
    if args.count:
        random_num = random_talk_number(count=int(args.count))
        selected_talk = talks[random_num]
    else:
        selected_talk = random.choice(talks)

    print(selected_talk)
