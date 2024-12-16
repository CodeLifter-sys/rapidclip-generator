import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a script and convert it to audio.")
    parser.add_argument("--theme", required=True,
                        help="The theme of the script.")
    parser.add_argument("--language", required=True,
                        help="The language of the script.")
    parser.add_argument("--voice_id", required=True,
                        help="The Eleven Labs voice ID to use.")
    parser.add_argument("--stability", type=float, default=0.75,
                        help="Stability setting for the voice (default: 0.75).")
    parser.add_argument("--similarity_boost", type=float, default=0.3,
                        help="Similarity boost setting for the voice (default: 0.3).")
    return parser.parse_args()
