def combinationSum(candidates, target):
    result = []  # Danh sách các tổ hợp kết quả

    def backtrack(start, curr_sum, path):
        if curr_sum == target:  # Nếu tổng hiện tại bằng target, thêm tổ hợp vào kết quả
            result.append(path[:])
            return
        if curr_sum > target:  # Nếu tổng hiện tại lớn hơn target, kết thúc backtrack
            return
        for i in range(start, len(candidates)):
            num = candidates[i]
            path.append(num)  # Thêm số vào tổ hợp hiện tại
            backtrack(i, curr_sum + num, path)  # Tiếp tục tìm tổ hợp với tổng tăng lên
            path.pop()  # Quay lui bằng cách loại bỏ số cuối cùng

    candidates.sort()  # Sắp xếp mảng candidates
    backtrack(0, 0, [])  # Bắt đầu backtrack từ vị trí 0 với tổng hiện tại là 0 và tổ hợp rỗng
    return result

candidates = [2, 3, 5]
target = 8
result = combinationSum(candidates, target)
print(result)
