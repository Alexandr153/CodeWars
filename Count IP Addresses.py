def ips_between(start, end) -> int:
    start, end = start.split('.'), end.split('.')
    return (int(end[0]) * 256 ** 3 + int(end[1]) * 256 ** 2 + int(end[2]) * 256 ** 1 + int(end[3]) * 256 ** 0) - (int(start[0]) * 256 ** 3 + int(start[1]) * 256 ** 2 + int(start[2]) * 256 ** 1 + int(start[3]) * 256 ** 0)
