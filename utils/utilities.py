import psutil

class Util:
    def __init__(self, cpu_power):
        self.cpu_power = cpu_power
        self.pids = psutil.pids()
        self.processes = []
        self.cpu_percent = psutil.cpu_percent()

    def get_cpu_power_per_process(self, process_cpu_percent: float) -> float:
        return process_cpu_percent * self.cpu_power * 0.01 * self.cpu_percent

    def get_running_processes (self, limit, page_num):
        inter = 1
        for proc in psutil.process_iter(['pid', 'name','cpu_percent']):
            if inter == limit * page_num:
                break
            name = proc.info["name"]
            pid = proc.info["pid"]
            cpu_percent = proc.info['cpu_percent']
            self.processes.append({"pid":pid, "process_cpu_percent": cpu_percent * 0.01, "name": name})
            inter += 1
        return self.processes

    def get_running_process_power(self, limit=20, page_num=1):
        processes = self.get_running_processes(limit, page_num)
        return [
            {
                "pid": process['pid'],
                "name": process['name'],
                "process_cpu_percent": process["process_cpu_percent"],
                "power": self.get_cpu_power_per_process(process["process_cpu_percent"])
            }
            for process in processes
        ]
