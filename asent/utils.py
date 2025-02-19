from typing import Dict
import catalogue

lexicons = catalogue.create("asent", "lexicon", entry_points=True)
lexicons = catalogue.create("asent", "lexicon", entry_points=True)


def register_lexicon(name: str, lexicon: Dict[str, float]) -> None:
    """Registers a lexicon in asent.lexicons

    Args:
        name (str): The name of the lexicon
        lexicon (Dict[str, float]): The lexicon supplies as a dictionary.

    Example:
        >>> asent.register("my_lexicon_v1", {"happy": 4})
        >>> asent.lexicons.get("my_lexicon_v1")
        {"happy": 4}
    """
    lexicons.register(name, func=lexicon)
