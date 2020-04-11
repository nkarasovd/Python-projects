# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        arrived_at = request.arrived_at
        start_time = self.finish_time[-1] if len(self.finish_time) > 0 else 0
        start_time = max(start_time, arrived_at)
        finish_time = start_time + request.time_to_process

        j = -1
        for i in range(len(self.finish_time)):
            if self.finish_time[i] <= arrived_at:
                j = i
            else:
                break
        if j != -1:
            self.finish_time = self.finish_time[j + 1:]

        if len(self.finish_time) >= self.size:
            return Response(True, -1)
        else:
            self.finish_time.append(finish_time)
            return Response(False, start_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
