import sys
from pathlib import Path

try:
    # Normal case: run as a package, e.g. `python -m members.TranThanhLoi27.w2`
    from .io_utils import load_tasks
except ImportError:  # pragma: no cover - fallback for direct script execution
    # Allow `python members/TranThanhLoi27/w2/__main__.py` from anywhere
    REPO_ROOT = Path(__file__).resolve().parents[3]
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from members.TranThanhLoi27.w2.io_utils import load_tasks

# Default sample file, resolved from this file instead of the current directory
DEFAULT_CSV = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> int:
    # Use path from command line arguments if provided, otherwise fallback to default sample path
    if len(sys.argv) >= 2:
        csv_path = Path(sys.argv[1])
    else:
        csv_path = DEFAULT_CSV

    try:
        # Load tasks from the CSV file
        tasks = load_tasks(csv_path)
    except (ValueError, KeyError, TypeError, OSError) as e:
        # Print the error if something goes wrong
        print(f"Error loading tasks: {e}", file=sys.stderr)
        return 1

    print(f"Successfully loaded {len(tasks)} tasks:")
    # Print each task nicely
    for task in tasks:
        print(f"- {task.title} (Deadline: {task.deadline})")
    return 0


# Check if this script is being run directly
if __name__ == "__main__":
    sys.exit(main())
