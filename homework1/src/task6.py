#returns word count
def word_count(filename="/home/student/CS4300/homework1/task6_readme.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return len(text.split())