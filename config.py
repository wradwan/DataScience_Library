#Define paths for files
spectrogramsPath = "/ds/dataset/quran/999/Spectrograms/"
slicesPath = "/ds/dataset/quran/999/Slices/"
datasetPath = "/ds/dataset/quran/999/"
rawDataPath = "/ds/dataset/quran/999/"

#Spectrogram resolution
pixelPerSecond = 50

#Slice parameters
sliceSize = 128

#Dataset parameters
filesPerGenre = 1000
validationRatio = 0.3
testRatio = 0.1

#Model parameters
batchSize = 128
learningRate = 0.001
nbEpoch = 20