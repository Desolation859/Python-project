def shift_lane_list(raw_input: str) -> str:
    lines = [line.strip() for line in raw_input.splitlines() if line.strip()]
    if not lines:
        return ""
    names = []
    for line in lines:
        dash_index = line.find('-')
        name_part = line[dash_index + 1:].strip() if dash_index != -1 else ""
        names.append(name_part)
    shifted_names = names[1:]
    result_lines = []
    for i, name in enumerate(shifted_names):
        result_lines.append(f"q{i + 1} - {name}")
    remaining_lanes = len(lines) - len(shifted_names)
    for i in range(remaining_lanes):
        lane_number = len(shifted_names) + i + 1
        result_lines.append(f"q{lane_number} - ")
    return "\n".join(result_lines)

if __name__ == "__main__":
    print("Вставьте лайн-лист и нажмите Enter дважды:")
    input_lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            input_lines.append(line)
        except EOFError:
            break
    raw_input = "\n".join(input_lines)
    output = shift_lane_list(raw_input)
    print("--- Обновлённый лайн-лист ---")
    print(output)