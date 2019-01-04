from import_words import importAll, plotAll

numberOfFiles = 4;  #for now plotAll can only plot 4 subplots




def reduceDensity(soundDataHere):

    cleanSoundData = []

    for i in range(numberOfFiles):

        k = 0
        bufferForCleaning = []

        for j in range(0, soundDataHere[i].size-1, 30):

            bufferForCleaning.insert(k, soundDataHere[i][j])
            k += 1

        cleanSoundData.append(bufferForCleaning)

    return cleanSoundData





# soundData = importAll(numberOfFiles)
# cleanSoundData = reduceDensity(soundData)
#
# plotAll(cleanSoundData, numberOfFiles)







