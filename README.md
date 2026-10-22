# Python Bootcamp — Team 07

This repository contains the 3-week Python Bootcamp homework exercises for **Team 07** in course **CSC10014 — Computational Thinking**.

## Repository Structure

```
python-bootcamp/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── python-hw.md      # Weekly homework issue template
│   └── workflows/
│       └── ci.yml            # CI automated linting and testing
├── .gitignore
├── PROGRESS.md               # Tracking progress table for all members
├── README.md                 # This file
├── members/                  # Individual exercise directories
│   ├── khanhf_ng820/ (w1/, w2/, w3/)
│   ├── Dang_Xuan_Phat/ (w1/, w2/, w3/)
│   ├── TranThanhLoi27/ (w1/, w2/, w3/)
│   ├── TranPhucKhanhh/ (w1/, w2/, w3/)
│   ├── KaKaAkagami/ (w1/, w2/, w3/)
│   └── kiethm07/  (w1/, w2/, w3/)
├── samples/                  # Shared sample datasets
│   ├── tasks.csv
│   └── tasks_bad.csv
├── shared/                   # Team code for T-W2 and T-W3
│   ├── contract.py
│   └── study_planner/
└── tests/                    # Instructor-provided automated tests
    ├── conftest.py
    ├── test_w1.py
    ├── test_w2.py
    └── test_w3.py
```

## Setup & Environment

Prerequisites: Python 3.10+ (Python 3.12 recommended), Git.

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1

# Install testing and linting tools
pip install pytest ruff
```

## Weekly Workflow for Members

1. **Pull latest changes:**
   ```bash
   git switch main
   git pull origin main
   ```

2. **Create your feature branch:**
   ```bash
   git switch -c py/w1-<username>
   ```

3. **Complete exercises one at a time:**
   - Write code exclusively in your member folder: `members/<your_folder>/wN/`.
   - Make at least 5 meaningful commits per week (e.g., `feat(py-w1): W1-2 word counter`).

4. **Run tests frequently:**
   ```bash
   pytest -q tests/test_w1.py --member <your_folder> --variant <variant_number>
   ```

5. **Lint your code:**
   ```bash
   ruff check .
   ```

6. **Push and open a Pull Request:**
   ```bash
   git push -u origin py/w1-<username>
   ```
   - Title PR: `py-w1: <username>`
   - Link your homework issue (`Closes #<issue_number>`).
   - Assign your rotation reviewer.

7. **Review & Merge:**
   - Assigned reviewer reviews the code and verifies all tests pass.
   - Once approved, merge into `main` and update your row in [`PROGRESS.md`](PROGRESS.md).

## Member Information & Directory Mapping

| Member Name | Student ID | Folder Name | C++ Translation Variant (W1-4) |
|---|---|---|---|
| Nguyễn Phúc Khánh | 25125086 | `khanhf_ng820` | Variant 1 (Binary search trên vector đã sắp xếp $\rightarrow$ trả về index hoặc -1: `binary_search(a, key)`) |
| Trần Thành Lợi | 25125059 | `TranThanhLoi27` | Variant 2 (Insertion sort (in-place) $\rightarrow$ trả về danh sách đã sắp xếp: `insertion_sort(a)`) |
| Lý Tuấn Kiệt | 25125022 | `kiethm07` | Variant 3 (Transpose of a matrix — chuyển vị ma trận 2 chiều vector of vectors: `transpose(a)`) |
| Nguyễn Minh Khang | 25125018 | `KaKaAkagami` | Variant 4 (Sieve of Eratosthenes $\rightarrow$ tìm các số nguyên tố $\le n$: `primes_up_to(n)`) |
| Trần Phúc Khánh | 25125020 | `TranPhucKhanhh` | Variant 5 (Merge two sorted vectors $\rightarrow$ trả về danh sách gộp đã sắp xếp: `merge_sorted(a, b)`) |
| Đặng Xuân Phát | 25125062 | `Dang_Xuan_Phat` | Variant 6 (Rotate vector right by $k$ steps $\rightarrow$ trả về danh sách đã xoay: `rotate_right(a, k)`) |
