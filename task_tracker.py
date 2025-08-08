from argparse import ArgumentParser


def _construct_argparser() -> ArgumentParser:
    parser = ArgumentParser()

    return parser


def _main_cli():
    args = _construct_argparser().parse_args()


if __name__ == '__main__':
    _main_cli()
