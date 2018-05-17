import pickle
import random


class TweetGenerator:

    def __init__(self):
        self.transition_dict = {}
        self.loaded = False

    def load_generator(self, filename):
        """
        Prep the generator by specifying the markov chain's transition probabilities.
        :param filename: file location of the pickle object to be loaded
        """
        self.transition_dict = pickle.load(open(filename, "rb"))
        self.loaded = True    

    def generate_tweet(self):
        """
        Generate a fake tweet based on the trigram model markov chain.
        :return: string denoting the fake tweet
        """
        w1 = "BEGIN"
        w2 = "TWEET"
        tweet = ""
        w3 = random.choice(self.transition_dict[(w1, w2)])
        while w3 != "END":
            tweet = tweet + " " + w3
            w1 = w2
            w2 = w3
            w3 = random.choice(self.transition_dict[(w1, w2)])

        return tweet
