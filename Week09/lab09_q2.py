import threading
import time

def run_sequential(tasks):
    """Run tasks one after another."""
    for name, duration in tasks:
        print(f"[START] {name}")
        time.sleep(duration)
        print(f"[DONE]  {name} ({duration}s)")

def simulate_task(name, duration, lock):
    """
    Simulate a task with proper lock usage.
    1. Acquire lock, print START message, release lock
    2. Sleep for duration
    3. Acquire lock, print DONE message, release lock
    """
    lock.acquire()
    print(f"[START] {name}")
    lock.release()
    
    time.sleep(duration)
    
    lock.acquire()
    print(f"[DONE]  {name} ({duration}s)")
    lock.release()

def run_threaded(tasks, lock):
    """
    Run all tasks concurrently using threads.
    1. Create empty list for threads
    2. For each task, create a Thread targeting simulate_task with args
    3. Start all threads (first loop)
    4. Join all threads (second loop)
    """
    threads = []
    for name, duration in tasks:
        thread = threading.Thread(target=simulate_task, args=(name, duration, lock))
        threads.append(thread)

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

def main():
    print("=" * 60)
    print("  SEQUENTIAL vs THREADED EXECUTION")
    print("=" * 60)
    tasks = [
        ("Brew Coffee", 3),
        ("Toast Bread", 2),
        ("Fry Eggs", 4)
    ]
    
    # Sequential execution
    print("\n--- Running SEQUENTIALLY ---")
    start = time.time()
    run_sequential(tasks)
    sequential_time = time.time() - start
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Threaded execution
    print("\n--- Running with THREADS ---")
    lock = threading.Lock()
    start = time.time()
    run_threaded(tasks, lock)
    threaded_time = time.time() - start
    print(f"Threaded time: {threaded_time:.2f} seconds")
    
    # Speedup calculation
    if threaded_time > 0:
        speedup = sequential_time / threaded_time
        print(f"\nSpeedup: {speedup:.2f}x faster with threads!")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()