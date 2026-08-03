from app.evaluation.eval_dataset import *

eval_json = load_eval_dataset()
print(eval_json)

valid_items = [elem for elem in eval_json if validate_eval_item(elem)]
print(len(valid_items))

category_items = split_eval_dataset(valid_items)
for key,value in category_items.items():
    print(f"{key}:\n{value}")