import os
import shutil
import argparse
import hashlib
import time
import logging

def md5(file):
    with open(file, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def sync(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
        logging.info(f"Created directory: {dst}")

    for item in os.listdir(src):
        s_path, d_path = os.path.join(src, item), os.path.join(dst, item)

        if os.path.isdir(s_path):
            sync(s_path, d_path)
        elif not os.path.exists(d_path) or md5(s_path) != md5(d_path):
            shutil.copy2(s_path, d_path)
            logging.info(f"Copied: {s_path} -> {d_path}")

    for item in os.listdir(dst):
        d_path = os.path.join(dst, item)
        if not os.path.exists(os.path.join(src, item)):
            if os.path.isdir(d_path):
                shutil.rmtree(d_path)
            else:
                os.remove(d_path)
            logging.info(f"Deleted: {d_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("replica")
    parser.add_argument("--interval", type=int, default=10)
    parser.add_argument("--log", required=True, help="Path to log file")
    args = parser.parse_args()

    logging.basicConfig(
        filename=args.log,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.getLogger().addHandler(logging.StreamHandler())  # Add console logging

    while True:
        sync(args.source, args.replica)
        time.sleep(args.interval)

if __name__ == "__main__":
    main()