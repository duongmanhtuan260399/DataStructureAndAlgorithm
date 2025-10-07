import sys
import os
import pytest

# Ensure the Week9_Heap directory is importable when running tests from repo root
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from DSAHeap import DSAHeap  # noqa: E402


def test_remove_from_empty_raises():
    heap = DSAHeap()
    with pytest.raises(IndexError) as exc:
        heap.remove()
    assert str(exc.value) == "Heap is empty"


def test_single_insert_and_remove():
    heap = DSAHeap()
    heap.add(10, "a")
    assert heap.remove() == "a"
    with pytest.raises(IndexError):
        heap.remove()


def test_multiple_inserts_ordering_by_priority():
    heap = DSAHeap()
    heap.add(5, "low")
    heap.add(10, "mid")
    heap.add(20, "high")
    assert heap.remove() == "high"
    assert heap.remove() == "mid"
    assert heap.remove() == "low"


def test_duplicates_priorities():
    heap = DSAHeap()
    heap.add(10, "a")
    heap.add(10, "b")
    heap.add(10, "c")
    values = {heap.remove(), heap.remove(), heap.remove()}
    assert values == {"a", "b", "c"}


def test_dynamic_resize_beyond_initial_capacity():
    # Default capacity is 5; insert more to force resize
    heap = DSAHeap()
    for i in range(12):
        heap.add(i, f"v{i}")
    # should return in descending priority
    for i in reversed(range(12)):
        assert heap.remove() == f"v{i}"


def test_display_output(capsys):
    heap = DSAHeap()
    heap.add(3, "x")
    heap.add(7, "y")
    heap.add(5, "z")
    heap.display()
    captured = capsys.readouterr().out.strip()
    # The internal array order depends on heap structure, but root should be highest priority
    assert captured.startswith("[") and captured.endswith("]")
    assert "(7, y)" in captured


def test_trickle_up_recursion_by_increasing_inserts():
    heap = DSAHeap()
    # Insert in strictly increasing priority to force repeated trickle ups
    for p in range(1, 9):
        heap.add(p, p)
    # Now remove to ensure max is always returned
    for expected in reversed(range(1, 9)):
        assert heap.remove() == expected


def test_trickle_down_recursion_by_root_replacements():
    heap = DSAHeap()
    priorities = [50, 40, 45, 10, 20, 30, 35]
    for p in priorities:
        heap.add(p, p)
    # Remove a few to exercise trickle-down
    assert heap.remove() == 50
    assert heap.remove() == 45
    assert heap.remove() == 40
    # remaining should still be a valid max-heap order
    # Compute remaining values after removing the three largest
    remaining_desc = sorted([10, 20, 30, 35], reverse=True)
    for expected in remaining_desc:
        assert heap.remove() == expected


def test_mixed_operations_stress():
    heap = DSAHeap()
    ops = [
        ("add", 5, "a"),
        ("add", 1, "b"),
        ("add", 8, "c"),
        ("remove", None, "c"),
        ("add", 7, "d"),
        ("add", 9, "e"),
        ("remove", None, "e"),
        ("remove", None, "d"),
        ("remove", None, "a"),
        ("remove", None, "b"),
    ]
    for op, p, v in ops:
        if op == "add":
            heap.add(p, v)
        else:
            assert heap.remove() == v


def test_heapsort_sorts_entries_by_priority_ascending():
    heap = DSAHeap()
    data = [(5, "a"), (2, "b"), (9, "c"), (1, "d"), (7, "e")]
    for p, v in data:
        heap.add(p, v)
    # Run in-place heapsort on internal array portion
    heap.heapSort()
    # After heapsort, the first `count` entries should be ascending by priority
    priorities_sorted = [heap.heap[i].get_priority() for i in range(heap.count)]
    values_sorted = [heap.heap[i].get_value() for i in range(heap.count)]
    assert priorities_sorted == sorted([p for p, _ in data])
    # Validate that values correspond to priorities; a stable order is not guaranteed
    assert set(values_sorted) == {v for _, v in data}


