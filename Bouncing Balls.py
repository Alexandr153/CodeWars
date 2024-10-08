def bouncing_ball(h, bounce, window) -> int:
    if h != 0 and 0 < bounce < 1 and window < h:
        count = 1
        current = h * bounce
        while current > window:
            current *= bounce
            count += 2
        return count
    else:
        return -1
