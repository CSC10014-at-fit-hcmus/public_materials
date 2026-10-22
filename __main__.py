import sys

from io_utils import load_tasks


def main():
    # Check if user provided a file path in the terminal
    if len(sys.argv) < 2:
        print("Usage: python -m my_package <path_to_csv>")
        sys.exit(1)  # Exit with an error code

    # Get the file path from command line arguments
    csv_path = sys.argv[1]

    try:
        # Load tasks from the CSV file
        tasks = load_tasks(csv_path)
        print(f"Successfully loaded {len(tasks)} tasks:")

        # Print each task nicely
        for task in tasks:
            print(f"- {task.title} (Deadline: {task.deadline})")

    except (ValueError, KeyError, OSError) as e:
        # Print the error if something goes wrong
        print(f"Error loading tasks: {e}")


# Check if this script is being run directly
if __name__ == "__main__":
    main()