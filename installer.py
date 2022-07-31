import argparse
import subprocess
import os
import glob

def parse_files(dir):
    os.chdir(dir)
    return glob.glob('*.exe')

def install(files):
    for file in files:
        if not os.path.exists(file):
            print(f'File {file} does not exist, skipping...')
            continue
        subprocess.run(['wine', file])

def main():
    parser = argparse.ArgumentParser(description='Enter a list of --files or a --dir')
    parser.add_argument('-f','--files', nargs='+', help='List of files', required=False)
    parser.add_argument('-d', '--dir', help='Directory', required=False)
    args = parser.parse_args()
    if args.dir:
        files = parse_files(args.dir)
        install(files)
    else:
        install(args.files)

if __name__ == '__main__':
    main()