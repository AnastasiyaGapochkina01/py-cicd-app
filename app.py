import argparse
import time
import random
import sys

def main():
    parser = argparse.ArgumentParser(description="CI/CD example app")
    parser.add_argument('--action', required=True, choices=['test', 'check', 'build', 'apply'], help='Action to perform')
    parser.add_argument('--env', help='Environment for apply action')

    args = parser.parse_args()

    if args.action == 'test':
        print("Running synthetic tests...")
        time.sleep(2)
        print("Test 1/3 passed by 2 seconds")
        time.sleep(5)
        print("Test 2/3 passed by 5 seconds")
        time.sleep(2)
        print("Test 3/3 passed by 2 seconds")
        print("All tests passed.")
    elif args.action == 'check':
        print("Running healthcheck...")
        print("Healthcheck OK.")
    elif args.action == 'build':
        print("Building...")
        time.sleep(3)
        rand_num = random.randint(100, 999)
        print(f"Builded version {rand_num}")
    elif args.action == 'apply':
        if not args.env:
            print("Error: --env is required for apply action", file=sys.stderr)
            sys.exit(1)
        print(f"apply to {args.env}")

if __name__ == "__main__":
    main()
