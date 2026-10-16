def rotate_right(a: list[int], k: int) -> list[int]:
    """
    Xoay danh sách sang phải k bước.
    
    Difference from C++: Trong Python, chúng ta có thể sử dụng List Slicing 
    (cắt mảng) và chỉ số âm (negative indexing) để xoay danh sách chỉ với 
    một dòng code duy nhất, thay vì phải dùng vòng lặp thủ công hoặc hàm 
    std::rotate kết hợp với iterator như trong C++.
    """
    if not a:
        return []
    k = k % len(a)
    
    if k == 0:
        return a.copy()
        
    return a[-k:] + a[:-k]