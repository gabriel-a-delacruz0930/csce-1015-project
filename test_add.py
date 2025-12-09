def test_add():
    result = 2 + 5
    assert result == 7, "Addition should work"
    print("✅ PASS: Addition works")

def test_task_creation():
    task = task("Buy milk")
    assert task["text"] == "Buy milk", "Task text should match"
    print("✅ PASS: Task created correctly")


if __name__ == "__main__":
        test_add()
        test_task_creation()
        print("\nAll tests passed! 🎉")