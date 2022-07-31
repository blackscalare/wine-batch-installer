import argparse
import subprocess
import os

def install(files):
    for file in files:
        if not os.path.exists(file):
            print(f'File {file} does not exist, skipping...')
            continue
        subprocess.run(['wine', file])

def main():
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('-f','--files', nargs='+', help='<Required> Set flag', required=True)
    args = parser.parse_args()

    install(args.files)

if __name__ == '__main__':
    main()