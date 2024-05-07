from multiprocessing import Process, Queue

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result = Queue()
    num_threads = 5
    step = (END - START) // num_threads

    threads = []
    for i in range(num_threads):
        start = START + i * step
        end = start + step if i < num_threads - 1 else END
        th = Process(target=work, args=(i+1, start, end, result))
        th.name = f"th{i+1}"
        threads.append(th)

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp

    print(f"Result: {total}")
