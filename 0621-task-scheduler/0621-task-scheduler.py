class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        tasks_with_max_frequency = sum(1 for count in task_counts.values() if count == max_frequency)
        full_cycles = max_frequency - 1
        cycle_length = n + 1
        basic_schedule_length = full_cycles * cycle_length
        schedule_length_with_final_tasks = basic_schedule_length + tasks_with_max_frequency
        return max(len(tasks), schedule_length_with_final_tasks)

solution = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
result = solution.leastInterval(tasks, n)
print(f"Minimum units of time: {result}")