import json
import os

FILENAME = "todo_list.json"

# データ読み込み
def load_todos():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# データ保存
def save_todos(todos):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

# メニュー表示
def show_menu():
    print("\nToDoリストアプリ")
    print("1. リスト表示")
    print("2. やること追加")
    print("3. やること削除")
    print("4. 終了")

def main():
    todos = load_todos()

    while True:
        show_menu()
        choice = input("選択肢を入力してください（1-4）：")

        if choice == "1":
            if todos:
                print("\n--- 現在のToDo ---")
                for i, todo in enumerate(todos, 1):
                    print(f"{i}. {todo}")
            else:
                print("\nToDoはまだありません。")

        elif choice == "2":
            new_todo = input("追加するやること：")
            todos.append(new_todo)
            save_todos(todos)
            print("追加しました！")

        elif choice == "3":
            for i, todo in enumerate(todos, 1):
                print(f"{i}. {todo}")
            try:
                idx = int(input("削除する番号を入力：")) - 1
                if 0 <= idx < len(todos):
                    removed = todos.pop(idx)
                    save_todos(todos)
                    print(f"「{removed}」を削除しました。")
                else:
                    print("番号が無効です。")
            except ValueError:
                print("数字を入力してください。")

        elif choice == "4":
            print("終了します。おつかれさまでした！")
            break
        else:
            print("1〜4の数字を入力してください。")

if __name__ == "__main__":
    main()