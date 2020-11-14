import os

from main import DEFAULT_BATCH


class Optimizer(object):
    def __init__(self, sql_file=None, output_sql_dir=None, batch=DEFAULT_BATCH):
        self.sql_file = sql_file
        self.output_sql_dir = output_sql_dir
        self.batch = batch

    def optimize(self):
        file_name = os.path.basename(self.sql_file)
        name, extension = os.path.splitext(file_name)
        optimized_file_name = "{}_optimized{}".format(name, extension)

        optimized_file_path = os.path.join(self.output_sql_dir, optimized_file_name)
        with open(optimized_file_path, "w") as fw:
            total = 0
            with open(self.sql_file, 'r') as fr:
                lines = []
                for i, line in enumerate(fr):
                    if (i + 1) % self.batch == 0:
                        optimizes_sql_insert = self._optimize(lines=lines)
                        fw.write(optimizes_sql_insert)
                        print("{} lines optimized".format(i + 1))
                        lines = []
                        total += self.batch

                    lines.append(line)

                if len(lines) > 0:
                    total += len(lines)
                    optimizes_sql_insert = self._optimize(lines=lines)
                    fw.write(optimizes_sql_insert)
            fw.flush()

    @staticmethod
    def _optimize(lines=[]):
        if len(lines) == 0:
            return ""

        first_line = lines[0]
        first_index_index = first_line.index("(")
        last_index = first_line.index("(", first_index_index + 1)
        insert_definition = first_line[:last_index]

        parts = []
        for line in lines:
            first_index = line.index("(")
            index = line.index("(", first_index + 1)
            last_index = line.rindex(")")
            insert_part = line[index:last_index + 1]
            parts.append(insert_part)

        values_part = ",\n".join(parts)

        return insert_definition + values_part + ";"
