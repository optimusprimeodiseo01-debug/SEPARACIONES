import time


class Runner:
    """
    Persistent local operator.

    The Runner maintains the continuity of the Tapiz system.
    It executes one cycle, waits, and continues indefinitely.
    """

    def run(self):
        pass


def main():
    runner = Runner()

    while True:
        runner.run()
        time.sleep(60)


if __name__ == "__main__":
    main()
