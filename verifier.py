def check_solution(output):
    lines = [line.strip() for line in output.strip().splitlines()]

    return (
        len(lines) >= 2
        and lines[0] == "Best student: Sara"
        and lines[1] == "Average: 19.0"
    )