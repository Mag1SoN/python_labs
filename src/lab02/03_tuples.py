def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3:
        raise TypeError
    fio, group, gpa = rec
    if not isinstance(gpa, float):
        raise TypeError
    fio = fio.strip()
    group = group.strip()
    if not fio:
        raise ValueError
    if not group:
        raise ValueError

    name_parts = [part.strip() for part in fio.split() if part.strip()]
    if len(name_parts) < 2:
        raise ValueError
    surname = name_parts[0].title()
    initials = ".".join(part[0].upper() for part in name_parts[1:]) + "."
    formatted_fio = f"{surname} {initials}"

    gpa_formatted = f"{gpa:.2f}"
    return f"{formatted_fio}, гр. {group}, GPA {gpa_formatted}"


# print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
# print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
# print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# try:
#     print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
# except ValueError:
#     print("ValueError")
