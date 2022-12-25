import LineInterpreter


class nikiborg_lang(LineInterpreter.LineInterpreter):
    def __init__(self, source_file_name: str) -> None:
        super().__init__(source_file_name)
        self.stack: list[float] = []

    def execute_current_line(self) -> None:
        l = self.current_line()

        if len(l) == 0 or l.startswith('#'):
            return
        else:
            ...