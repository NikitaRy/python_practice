from abc import ABC, abstractmethod
import sys


class LineInterpreter(ABC):
    def __init__(self, source_file_name: str) -> None:
        self.source_file_name: str = source_file_name
        with open(source_file_name, 'r', encoding='utf8') as source_file:
            self._lines: list[str] = [l.rstrip() for l in source_file]
        self.current_line_idx: int = 0 if len(self._lines) else -1
        if len(self._lines) == 0:
            self.quit(f"Empty source file: {source_file_name}")

    def quit(self, message: str = ''):
        if message != "":
            print(message, file=sys.stderr)
        sys.exit(0)

    def current_line(self) -> str:
        if not (0 <= self.current_line_idx < len(self._lines)):
            self.quit('Program is over')
        return self._lines[self.current_line_idx]

    def abs_jump(self, line_no: int) -> None:
        self.current_line_idx = line_no

    def rel_jump(self, offset: int) -> None:
        self.current_line_idx += offset

    def step(self) -> None:
        self.rel_jump(1)

    @abstractmethod
    def execute_current_line(self) -> None:
        ...

    def run(self) -> None:
        while True:
            self.execute_current_line()
            self.step()
