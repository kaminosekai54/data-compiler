settings = {
"rawFilePath": "./raw_data/",
"resultPath" : "./results/",
"csvResultPath" : "./results/csv/",
"classicFastaResultPath" : "./results/classic-fasta/",
"genesFastaResultPath": r"./results/genes-fasta/",
"sequenceAlignementResultPath": r"./results/alignement/",
"musclePath": r"./tools/muscle/",
"mafftPath": r"./tools/mafft/",
"logPath": "./logs/",
"minColName" : "Minimum",
"maxColName" : "Maximum",
"nameColName" : "Name",
"typeColName" : "Type",
"useMuscle" : False,
"useMafft" : True,
}

def getSettings():
    return settings