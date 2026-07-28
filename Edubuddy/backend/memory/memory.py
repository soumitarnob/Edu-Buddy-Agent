import json
from pathlib import Path


MEMORY_FILE = Path("data/memory.json")


class Memory:

    def save(self, question, answer):

        MEMORY_FILE.parent.mkdir(exist_ok=True)

        if MEMORY_FILE.exists():

            data = json.loads(
                MEMORY_FILE.read_text()
            )

        else:

            data = []

        data.append({

            "question": question,

            "answer": answer

        })

        MEMORY_FILE.write_text(
            json.dumps(
                data,
                indent=4
            )
        )


memory = Memory()