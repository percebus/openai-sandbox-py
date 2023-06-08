import re


def clean(s: str, separator: str = "\n") -> str:
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r". ,", "", s)
    # remove all instances of multiple spaces
    return s.replace("..", ".").replace(". .", ".").replace(separator, "").strip()
