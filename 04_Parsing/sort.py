import os
import matplotlib.pyplot as plt
path = os.getcwd()

#dictionary of each lang used; will contain name of language and pairing (add below)
lang = {}
lang[0] = ['Arabic']
lang[1] = ['Chinese']
lang[2] = ['English']
lang[3] = ['French']
lang[4] = ['German']
lang[5] = ['Hebrew']
lang[6] = ['Japanese']
lang[7] = ['Korean']
lang[8] = ['Russian']
lang[9] = ['Spanish']

#initialize Verb-Obj and Obj-Verb variables 
OV = 0
VO = 0
ovValues = []
voValues = []

langLoc = {}
langLoc[1] = "/UD_Arabic-NYUAD/ar_nyuad-ud-dev.conllu"
langLoc[2] = "/UD_Chinese-GSD/zh_gsd-ud-dev.conllu"
langLoc[3] = "/UD_English-EWT/en_ewt-ud-dev.conllu"
langLoc[4] = "/UD_French-FTB/fr_ftb-ud-dev.conllu"
langLoc[5] = "/UD_German-HDT/de_hdt-ud-dev.conllu"
langLoc[6] = "/UD_Hebrew-HTB/he_htb-ud-dev.conllu"
langLoc[7] = "/UD_Japanese-BCCWJ/ja_bccwj-ud-dev.conllu"
langLoc[8] = "/UD_Korean-Kaist/ko_kaist-ud-dev.conllu"
langLoc[9] = "/UD_Russian-SynTagRus/ru_syntagrus-ud-dev.conllu"
langLoc[10] = "/UD_Spanish-AnCora/es_ancora-ud-dev.conllu"

def sort(file, OV, VO):
    objFlag = False
    rootFlag = False
    for line in file: 
        #splits lines into lists to make things easier to compute
        info =[]
        info = line.split("\t")
        count = 0
        for x in info:
            if '\n' in x:
                x = x.strip("\n")
                x = x.strip()
                info[count] = x
            x = x.strip()
            info[count] = x
            count += 1
        #obtains relative count of Obj-Verb and Verb-Obj as well as a total
        if "" in info: 
            objFlag = False
            rootFlag = False
        elif 'root' in info:
            rootFlag = True
        elif 'obj' in info:
            objFlag = True
        if rootFlag == True and objFlag == False:
            VO += 1
        elif rootFlag == False and objFlag == True:
            OV += 1

    total = OV + VO

    #find pairings on scale of 0 - 1
    x = OV / total
    y = VO / total
    return (x,y)


for i in langLoc:
    file = open(path + str(langLoc[i]))
    pair = sort(file, OV, VO)
    ovValues.append(pair[0])
    voValues.append(pair[1])
    # uncomment if you want to see the values associated with each language
    #lang[i].append(pair)



# plots the data; this does not work on WSL, but was verified on windows to ensure that a plot was actually created
labels = lang
x = ovValues  # proportion of OV
y = voValues  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
plt.show()
