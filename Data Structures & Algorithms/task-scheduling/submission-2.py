class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = defaultdict(int)
        for t in tasks: task_count[t] -= 1

        most_freq_tasks = list(task_count.values())
        heapq.heapify(most_freq_tasks)

        cycle = 0
        cooldown = deque([])

        while most_freq_tasks or cooldown:
            cycle += 1

            if cooldown and cooldown[0][1] == cycle:
                remaining_task_count = cooldown.popleft()[0]
                heapq.heappush(most_freq_tasks, remaining_task_count)
            if most_freq_tasks:
                remaining_task_count = heapq.heappop(most_freq_tasks)
                remaining_task_count += 1
                if remaining_task_count < 0:
                    cooldown.append((remaining_task_count, cycle + n + 1))
        
        return cycle
