import pickle
import sys


def generate_trigrams(words):
    if len(words) < 3:
        return
    for i in range(0, len(words) - 2):
        yield (words[i], words[i + 1], words[i + 2])


def main():
    if len(sys.argv) != 2:
        print("Please input the text file location for chain generation")

    filename = sys.argv[1]
    chain = {}

    with open(filename, "r") as fp:
        for line in fp.readlines():
            words = line.decode('utf-8').split()
            for w1, w2, w3 in generate_trigrams(words):
                key = (w1, w2)
                if key in chain:
                    chain[key].append(w3)
                else:
                    chain[key] = [w3]
    pickle.dump(chain, open("markov_chain", "wb"))


if __name__ == "__main__":
    main()
