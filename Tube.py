from pytube import YouTube
import sys

def exit_program():
    print("Kilepes a programbol.")
    sys.exit()

def quality_choice(yt):
    print("Elerheto minosegek:")
    for stream in yt.streams:
        print(f"{stream.itag}. {stream.resolution} - {stream.mime_type}")

    quality = input("Valassz egy minoseget (vagy 0 a kilepeshez): ")
    return quality

while True:
    link = input("Link: ")

    try:
        yt = YouTube(link)
        print("Cim:", yt.title)
        print("Csatorna:", yt.author)
        print("Nezettseg:", yt.views)

        print("Hogyan szeretned letolteni a videot?")
        print("0. Letoltes (egyszeru)")
        print("1. Letoltes a minoseg kivalasztasaval")
        print("2. Audio (audio)")
        print("3. Kilepes")

        choice = input("Valassz egy opciot (0/1/2/3): ")

        if choice == "0":
            video = yt.streams.get_highest_resolution()
            video.download()
            print("Letoltes kesz!")
        
        elif choice == "1":
            quality = quality_choice(yt)

            try:
                itag = int(quality)
                video = yt.streams.get_by_itag(itag)
                if video:
                    video.download()
                    print("Letoltes kesz!")
                else:
                    print("Ervenytelen minoseg. Kerlek valassz ujra.")
            except ValueError:
                print("Ervenytelen itag. Kerlek szamot adj meg.")
        
        elif choice == "2":
            audio = yt.streams.filter(only_audio=True).first()
            audio.download()
            print("Letoltes kesz!")
        
        elif choice == "3":
            exit_program()
        
        else:
            print("Ervenytelen opcio. Kerlek valassz ujra.")
        
    except Exception as e:
        print("Hiba tortent:", str(e))
