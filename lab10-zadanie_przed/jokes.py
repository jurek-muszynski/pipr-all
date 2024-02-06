from jokes_services import get_joke
import sys
import argparse
from time import sleep


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("--get-joke", action="store_true",
                        help="fetch a random dad joke")
    args = parser.parse_args(arguments[1:])

    if args.get_joke:
        joke = get_joke()
        sleep(0.5)
        save = input("Would you like to save this joke [y/N] ? ")
        if save == "y":
            joke.save_joke()


if __name__ == "__main__":
    main(sys.argv)
