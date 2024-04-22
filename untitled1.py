def getLyrics(lyricsfile):
    lyrics = []
  
    with open(lyricsfile, 'r') as lyricsfile: # Open in read mode
        for line in lyricsfile:
            lyrics.extend(line.strip().lower().split())
        lyricsfile.close()
        return lyrics
    
def createWordCount(lyrics):
    word_count = {}
    
    for word in lyrics:
        if word in word_count:
              word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def predictArtist(lyricfile1, lyricCounted1, lyricfile2, lyricCounted2, inputlyric):
    strippedLyricWords = inputlyric.strip().lower().split()
    artistBias1 = sum(lyricCounted1.get(word, 0) for word in strippedLyricWords)
    artistBias2 = sum(lyricCounted2.get(word, 0) for word in strippedLyricWords)
    
    if artistBias1 > artistBias2:
        return "Artist1"
    elif artistBias2 > artistBias1:
        return "Artist2"
    else:
        print("Unable to predict which artist sang that lyric.")
    
def main():
    artist1 = input("Artist 1: ")
    artistfilename1 = input("Artist 1 lyric file: ")
    
    artist2 = input("Artist 2: ")
    artistfilename2 = input("Artist 2 lyric file: ")
    
    lyrics1 = getLyrics(artistfilename1)
    wordCount1 = createWordCount(lyrics1)
    
    lyrics2 = getLyrics(artistfilename2)
    wordCount2 = createWordCount(lyrics2)
    
    lyricToPredict = input("Input lyric (NO PUNCTUATION) to predict: ")
    predictedArtist = predictArtist(lyrics1, wordCount1, lyrics2, wordCount2, lyricToPredict)
    if predictedArtist == "Artist1":
        print(artist1, "probably wrote that song!")
    elif predictedArtist == "Artist2":
        print(artist2, "probably wrote that song!")
    else:
        print("Unable to predict whether", artist1, "or", artist2, "wrote that song.")

if __name__ == "__main__":
  main()
