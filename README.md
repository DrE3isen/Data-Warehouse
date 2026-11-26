# B-Tree Indexing for Employee Records

![Status](https://img.shields.io/badge/status-course_project-blue)
![Database](https://img.shields.io/badge/topic-data_warehousing-orange)
![Language](https://img.shields.io/badge/implementation-Python-yellow)

A data warehousing course project that explores **B-Tree indexing** on a large employee dataset. The project compares indexed searching with linear scanning and demonstrates exact lookup, range search, multi-condition filtering, dynamic insertion, and B-Tree performance characteristics.

**Course:** Data Warehouse (151002350)  
**University:** The Hashemite University - Prince Al-Hussein Bin Abdullah II Faculty for Information Technology  
**Supervisor:** Dr. Mo'taz Abdul Aziz Al-Hami  
**Deadline:** December 29, 2026

---

## Table of Contents

- [Overview](#overview)
- [Project Goals](#project-goals)
- [Dataset](#dataset)
- [Required Operations](#required-operations)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Running the Project](#running-the-project)
- [Performance Evaluation](#performance-evaluation)
- [Deliverables](#deliverables)
- [References and Resources](#references-and-resources)

---

## Overview

The employee collection is indexed using **Employee_ID** as the primary search key. A B-Tree organizes records and supporting pointers so that lookups, range queries, and insertions can be performed without scanning the complete dataset.

The project compares:

| Method | Search behavior | Expected cost |
|---|---|---|
| B-Tree index | Traverse from the root using key comparisons | Approximately logarithmic in the number of indexed keys |
| Linear scan | Inspect every employee record until matches are found | Linear in the number of records |

The implementation should report both result correctness and execution cost, including page or node visits where possible.

## Project Goals

- Design a B-Tree with configurable node order or degree.
- Construct the index from the employee dataset.
- Demonstrate balanced insertion and node splitting.
- Execute exact, range, and multi-condition queries.
- Insert a new employee dynamically and update the index.
- Compare B-Tree search against linear scan.
- Analyze tree height, node utilization, fan-out, and disk-I/O behavior.

## Dataset

The source workbook is stored at:

[`assets/BTree_Indexing_Employee_Dataset-v2 (1).xlsx`](assets/BTree_Indexing_Employee_Dataset-v2%20(1).xlsx)

The workbook contains:

| Sheet | Purpose |
|---|---|
| `Employee_Dataset` | Employee records and search-key data |
| `BTree_Order_Analysis` | B-Tree order and structural analysis |
| `Summary_&_Dashboard` | Summary metrics and dashboard content |

The main dataset sheet provides approximately **50,000 unique employee search keys**. Employee IDs are in the range **100001-150000** and are inserted in an intentionally unsorted order.

### Employee Record Schema

| Field | Example | Description |
|---|---:|---|
| `Record_Ptr` | `R00001` | Pointer or row identifier |
| `Employee_ID` | `109927` | Unique primary search key |
| `Full_Name` | `Seba Shatnawi` | Employee name |
| `Department` | `Sales` | Employee department |
| `Nationality` | `Jordanian` | Employee nationality |
| `Gender` | `F` | Employee gender |
| `Hire_Date` | `2025-12-19` | Date of hire |
| `Salary_JOD` | `1610` | Monthly salary in Jordanian Dinars |
| `Performance_Score` | `86` | Employee performance score |

## Required Operations

### 1. Exact Key Lookup

Retrieve the employee whose `Employee_ID` is `115`, or clearly document that this is an example ID and does not exist in the workbook's actual `100001-150000` key range.

The result should include:

- The B-Tree path or nodes visited.
- The tree level visited.
- The matching record, if present.
- Execution time and the number of node visits.

### 2. Range Scan

Retrieve all employees with:

```text
112 <= Employee_ID <= 116
```

As with the exact lookup example, use these IDs if they appear in an available follow-up dataset or adjusted assignment sample. For the provided workbook, this range should return no records unless it is intentionally adapted for a smaller dataset.

The implementation should find the start of the range, then traverse successor keys in sorted order.

### 3. Multi-Condition Search

Filter the dataset for employees who satisfy all of the following conditions:

- `Nationality = Jordanian`
- `Gender = M`
- `Department = HR`

Report matching records and the number of records examined.

### 4. Dynamic Insertion

Insert a new employee with the following data:

| Field | Value |
|---|---|
| `Employee_ID` | `120` |
| `Full_Name` | `Tareq` |
| `Department` | `Engineering` |
| `Nationality` | `Jordanian` |
| `Gender` | `M` |

Before insertion, verify whether the supplied key range permits this record. If key `120` is outside the workbook range, add it explicitly as a demonstration record rather than silently mixing it into the 100001-150000 dataset.

After insertion:

- Split nodes when required.
- Preserve B-Tree balance.
- Print or visualize the updated structure.
- Confirm that the inserted key can be found.

### 5. Performance Comparison

Measure and compare:

- Exact lookup time.
- Range query time.
- Linear scan time.
- B-Tree node visits.
- Tree height.
- Node occupancy and utilization.
- Estimated disk blocks or page reads.
- The effect of B-Tree order and fan-out.

> Run benchmarks several times and report averages rather than a single timing result.

## Project Structure

The repository currently contains the README and project assets. A suggested implementation layout is:

```text
warehouse_project/
├── assets/
│   ├── DW Project Fall 2026 2027.pdf
│   └── BTree_Indexing_Employee_Dataset-v2 (1).xlsx
├── src/
│   ├── btree.py
│   ├── data_loader.py
│   ├── queries.py
│   └── main.py
├── tests/
│   └── test_btree.py
├── README.md
└── requirements.txt
```

The `src/` and `tests/` directories can be created as the implementation is developed.

## Getting Started

### Prerequisites

- Python 3.11 or later
- Conda or a standard Python virtual environment
- The dataset workbook in [`assets/`](assets/)

### Conda Setup

```bash
conda create -n warehouse_env python=3.11 -y
conda activate warehouse_env
```

### Virtual Environment Setup

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies once `requirements.txt` is added:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For workbook access, a typical dependency is:

```bash
python -m pip install openpyxl
```

## Running the Project

The repository does not yet include an executable entry point. Once `src/main.py` is implemented, the project can be run with:

```bash
python src/main.py
```

A useful CLI should accept at least:

```bash
python src/main.py --order 4
python src/main.py --order 4 --benchmark
python src/main.py --order 4 --export results.csv
```

## Performance Evaluation

When reporting results, include:

1. B-Tree order and minimum key capacity.
2. Number of employee records and unique keys.
3. Tree height after full construction.
4. Number of node splits.
5. Node utilization after construction.
6. Nodes visited by each lookup.
7. Average and warm-cache timing results.
8. Linear-scan and B-Tree result counts.
9. A short explanation of surprising or inconsistent timing.

Example summary format:

| Metric | B-Tree | Linear Scan |
|---|---:|---:|
| Exact lookup average | _TBD_ | _TBD_ |
| Range query average | _TBD_ | _TBD_ |
| Nodes/records examined | _TBD_ | _TBD_ |

## Deliverables

- B-Tree implementation with insertion and search support.
- Workbook loading and record parsing.
- Exact lookup, range scan, and filtering operations.
- Dynamic insertion demonstration.
- Visualization or text display of the B-Tree.
- Benchmark script and reproducible results.
- Written analysis of indexing and disk-I/O behavior.

## References and Resources

- [`DW Project Fall 2026 2027.pdf`](assets/DW%20Project%20Fall%202026%202027.pdf) - Project statement and assignment requirements.
- [`BTree_Indexing_Employee_Dataset-v2 (1).xlsx`](assets/BTree_Indexing_Employee_Dataset-v2%20(1).xlsx) - Employee dataset and workbook analysis sheets.
