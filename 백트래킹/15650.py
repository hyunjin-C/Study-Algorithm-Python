n, m = map(int, input().split())
arr = []


def back():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if i not in arr:
            if arr == [] or arr[-1] < i:  # 증가하는 순서의 수열만
                arr.append(i)
                back()
                arr.pop()


back()
