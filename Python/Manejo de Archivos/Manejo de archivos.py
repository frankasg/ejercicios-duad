songs = []

def read_songs(path):
    global songs

    with open(path) as file:
        for line in file.readlines():
            songs.append(line)

def write_songs_in_order(path):
    global songs
    songs.sort()

    with open(path, "w") as file:
        for song in songs:            
            file.write(f"{song}")    

def main():
    read_songs("randomized_songs.txt")
    write_songs_in_order("songs_in_order.txt")
    print("Un nuevo archivo ha si creado con el nombre: songs_in_order.txt")


if __name__ == "__main__":
    main()