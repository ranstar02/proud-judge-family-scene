"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (two lines, 191 characters) to
``<OUTPUT_DIR>/entry.txt``. The scene is a small Sunday-breakfast moment:
Dad burns the pancakes on purpose, because the year Mom was sick, burnt
pancakes were the only thing that made the family laugh at breakfast — so
he never stopped, and neither did the laughter. Warm, funny and heartfelt,
in a breath. Deterministic: it always writes the same scene.
"""

import os

SCENE = (
    "Every Sunday, Dad burns the pancakes on purpose.\n"
    "The year Mom was sick, burnt pancakes were the only thing that made us "
    "laugh at breakfast \u2014 so he never stopped, and neither did the laughter."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SCENE + "\n")
    print(f"characters: {len(SCENE)}")
    print(SCENE)


if __name__ == "__main__":
    main()
