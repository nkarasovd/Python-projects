# python3

from collections import namedtuple
from queue import PriorityQueue

AssignedJob = namedtuple("AssignedJob", ["started_at", "worker"])


def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs(n_workers, jobs):
    result = []
    q = PriorityQueue()
    for i in range(n_workers):
        q.put(AssignedJob(0, i))

    for el in jobs:
        next_item = q.get()
        result.append(AssignedJob(next_item.started_at, next_item.worker))
        q.put(AssignedJob(next_item.started_at + el, next_item.worker))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
