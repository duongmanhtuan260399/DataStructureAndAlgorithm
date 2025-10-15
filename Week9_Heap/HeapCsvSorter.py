import os
import sys
import csv
import numpy as np

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Week9_Heap.DSAHeap import DSAHeap  # noqa: E402


class HeapCsvSorter:
    def __init__(self):
        self.heap = DSAHeap()

    def sort_file(self, input_csv_path: str, output_csv_path: str):
        self.heap = DSAHeap()
        with open(input_csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for rec in reader:
                if not rec or len(rec) < 2:
                    continue
                try:
                    priority = int(rec[0].strip())
                except ValueError:
                    continue
                value = rec[1].strip()
                self.heap.add(priority, value)

        # Sort in-place using heap
        self.heap.heapSort()

        with open(output_csv_path, "w", newline="", encoding="utf-8") as out:
            writer = csv.writer(out)
            for i in range(self.heap.count):
                entry = self.heap.heap[i]
                writer.writerow([entry.get_priority(), entry.get_value()])


def main():
    if len(sys.argv) < 3:
        print("Usage: python HeapCsvSorter.py <input_csv> <output_csv>")
        sys.exit(1)
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    sorter = HeapCsvSorter()
    sorter.sort_file(input_csv, output_csv)
    print(f"Sorted CSV written to: {output_csv}")


if __name__ == "__main__":
    main()


