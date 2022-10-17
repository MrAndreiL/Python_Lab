def compose(notes, moves, start):
    if start >= len(notes):
        return []
    song = [notes[start]]

    for move in moves:
        start += move
        if start < len(moves):
            song.append(notes[start])
        else:
            start -= len(notes)
            song.append(notes[start])
    return song

def main():
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

if __name__ == "__main__":
    main()
