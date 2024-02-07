from argparse import ArgumentParser

def get_input_args():
    parser = ArgumentParser(description='Math Dictionary')
    parser.add_argument('-n', '--number', type=int, default=3, help='Number of similar words to display')
    parser.add_argument('-co', '--cutoff', type=float, default=0.6, help='The minimum similarity ratio (0 to 1) to consider a word as similar.')
    
    return parser.parse_args()