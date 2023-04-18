from pytube import YouTube
import os

m_ytLinks: list[str] = []
downloadFolder = 'C:\\Users\\Carter\\Downloads\\YoutubeDownloadTest'

def printVideoInfo(p_yt: YouTube) -> str:
    outputString = f'> [Video] Downloading {p_yt.title}\n' \
                    f'[Title]: {p_yt.title}\n' \
                    f'[Channel]: {p_yt.author}\n' \
                    f'[Length]: {(p_yt.length/60).__round__(2)}m {p_yt.length%60}s\n' \
                    f'[File Size]: {p_yt.streams.get_highest_resolution().filesize/1000000}MB\n'
    return outputString

def main():
    # print('> Where should video(s) be downloaded to?')
    # downloadFolder = input('> ')
    os.listdir()

    print('> Input a Youtube video link on each blank line, select "YES" when asked to provide multiple')
    while True:
        inputLink = input('> ')
        m_ytLinks.append(inputLink)


        additionalLinks: str = input('> Enter an additional link? (Y/N): ')
        if additionalLinks.upper() == 'N':
            break
        else:
            pass

    if len(m_ytLinks) > 0:
        print(f'> Downloading {len(m_ytLinks)} videos...')
        for link in m_ytLinks:
            yt = YouTube(link)
            print(printVideoInfo(p_yt=yt))

            yt.streams.get_highest_resolution().download(filename=f'{yt.title}.mp4', output_path=downloadFolder)
            print('> ===== Done =====\n')
    else:
        additionalLinks: str = input('> Enter an additional link? (Y/N): ')
        if additionalLinks.upper() == 'N':
            pass
        else:
            main()

if __name__ == '__main__':
    main()