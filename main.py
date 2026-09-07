def is_mirror(text: str) -> bool:
    """Whether a word reads the same backwards, ignoring case."""
    folded = [one.lower() for one in text if one.isalnum()]
    return folded == folded[::-1]


if __name__ == "__main__":
    print(is_mirror("Never odd or even"))
