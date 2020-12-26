from dataclasses import dataclass, field

ms: int = int(1e-6)

@dataclass
class PerfMeta:
    _perf_statistics: dict = field(default_factory=dict)


@dataclass
class PerfMetaMeasure:
    min: int = int(1e12)
    mean: int = 0
    total: int = 0
    max: int = 0
    last: int = 0
    count: int = 1

    def __str__(self):
        return f'{self.last * ms} <{self.min * ms},{self.mean * ms},{self.max * ms}> ms'

    def update_measure(self, measure):
        if measure < self.min:
            self.min = measure
        if measure > self.max:
            self.max = measure
        self.total += measure
        self.mean = int(self.total / self.count)
        self.last = measure
        self.count += 1

    def reset_measure(self):
        self.count = 0
        self.total = 0
        self.min = int(1e12)
        self.max = 0
