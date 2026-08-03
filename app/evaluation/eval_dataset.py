from collections import defaultdict
import json

def load_eval_dataset(path:str = "data/eval_questions.json") -> list[dict]:
    """
    Load evaluation questions.
    """
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    return data


def validate_eval_item(item:dict) -> bool:
    """
    Check required fields.
    """
    # id 
    # question 
    # expected_answer
    # expected_sources
    # answerable
    # category 

    og_keys = ['id', 'question', 'expected_answer', 'expected_sources', 'answerable', 'category']
    item_keys = list(item.keys())

    # Check it has all keys
    if og_keys != item_keys:
        return False
    return True


def split_eval_dataset(items: list[dict]) -> dict:
    """
    Group questions by category.
    """
    category_dict = defaultdict(list)
    for item in items:
        category_dict[item['category']].append(item)

    return category_dict    