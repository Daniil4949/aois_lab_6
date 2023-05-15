from solving.hash_table import HashTable


def main():
    hash_table = HashTable(1)
    print(hash_table)
    hash_table.add('Полк', "3 тысячи")
    hash_table.add("Бригада", "1 тысяча")
    hash_table.add('Корпус', "30 тысяч")
    print(hash_table)
    print()
    print(hash_table.look_up("Полк"))
    hash_table.delete("Корпус")
    print(hash_table)
    hash_table.update_value("Полк", "4 тысячи")
    print(hash_table)


if __name__ == '__main__':
    main()
