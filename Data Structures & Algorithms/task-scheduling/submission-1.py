class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = defaultdict(int)
        for t in tasks: task_count[t] += 1

        count_task = [[-task_count[task], task] for task in task_count.keys()]
        heapq.heapify(count_task)

        cycle = 0
        cooldown = deque([])

        while count_task or cooldown:
            cycle += 1

            if cooldown and cooldown[0][1] == cycle:
                task = cooldown.popleft()[0]
                heapq.heappush(count_task, task)
            if count_task:
                task = heapq.heappop(count_task)
                task[0] += 1
                if task[0] < 0:
                    cooldown.append((task, cycle + n + 1))
        
        return cycle
