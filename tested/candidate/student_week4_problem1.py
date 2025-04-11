def Hanoi(n, source="A", destination="C", auxiliary="B"):
    if n == 1:
        print(f"Move disk {n} from source {source} to destination {destination}")
        return
    Hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from source {source} to destination {destination}")
    Hanoi(n - 1, auxiliary, destination, source)


def main():
    Hanoi(n=4, source="A", destination="C", auxiliary="B")
    """
    Move disk 1 from source A to destination B
    Move disk 2 from source A to destination C
    Move disk 1 from source B to destination C
    Move disk 3 from source A to destination B
    Move disk 1 from source C to destination A
    Move disk 2 from source C to destination B
    Move disk 1 from source A to destination B
    Move disk 4 from source A to destination C
    Move disk 1 from source B to destination C
    Move disk 2 from source B to destination A
    Move disk 1 from source C to destination A
    Move disk 3 from source B to destination C
    Move disk 1 from source A to destination B
    Move disk 2 from source A to destination C
    Move disk 1 from source B to destination C
    """


if __name__ == '__main__':
    main()
