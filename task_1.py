import random
import timeit
import matplotlib.pyplot as plt


def partition(arr, low, high, pivot_func):
    pivot = pivot_func(arr, low, high)
    arr[pivot], arr[high] = (
        arr[high],
        arr[pivot],
    )  # Переміщення опорного елемента до кінця
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def iterative_quick_sort(arr, pivot_func):
    size = len(arr)
    stack = [(0, size - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(arr, low, high, pivot_func)

            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))
            if low < pivot_index - 1:
                stack.append((low, pivot_index - 1))


def randomized_pivot(arr, low, high):
    return random.randint(low, high)


def first_pivot(arr, low, high):
    return low


def middle_pivot(arr, low, high):
    return low + (high - low) // 2


def last_pivot(arr, low, high):
    return high


def iterative_randomized_quick_sort(arr):
    iterative_quick_sort(arr, randomized_pivot)


def iterative_deterministic_first_quick_sort(arr):
    iterative_quick_sort(arr, first_pivot)


def iterative_deterministic_middle_quick_sort(arr):
    iterative_quick_sort(arr, middle_pivot)


def iterative_deterministic_last_quick_sort(arr):
    iterative_quick_sort(arr, last_pivot)


def generate_test_arrays(sizes, seed=42):
    random.seed(seed)
    return {size: [random.randint(0, size) for _ in range(size)] for size in sizes}


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def measure_time(sort_function, arr, number_of_runs=5):
    timer = timeit.Timer(lambda: sort_function(arr.copy()))
    return timer.timeit(number=number_of_runs) / number_of_runs


def main():
    sizes = [10000, 50000, 100000, 500000]
    test_arrays = generate_test_arrays(sizes)
    results = {"randomized": {}, "first": {}, "middle": {}, "last": {}}

    for size in sizes:
        arr = test_arrays[size]
        results["randomized"][size] = measure_time(iterative_randomized_quick_sort, arr)
        results["first"][size] = measure_time(
            iterative_deterministic_first_quick_sort, arr
        )
        results["middle"][size] = measure_time(
            iterative_deterministic_middle_quick_sort, arr
        )
        results["last"][size] = measure_time(
            iterative_deterministic_last_quick_sort, arr
        )

        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {results['randomized'][size]:.6f} секунд")
        print(
            f"   Детермінований QuickSort (перший елемент): {results['first'][size]:.6f} секунд"
        )
        print(
            f"   Детермінований QuickSort (середній елемент): {results['middle'][size]:.6f} секунд"
        )
        print(
            f"   Детермінований QuickSort (останній елемент): {results['last'][size]:.6f} секунд\n"
        )

    # Побудова графіку
    plt.figure(figsize=(12, 8))
    for label, times in results.items():
        plt.plot(
            sizes,
            [times[size] for size in sizes],
            marker="o",
            label=f"QuickSort ({label})",
        )

    plt.xlabel("Розмір масиву")
    plt.ylabel("Час виконання (секунди)")
    plt.title("Порівняння QuickSort алгоритмів за часом виконання")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
