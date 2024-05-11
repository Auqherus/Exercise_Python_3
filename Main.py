print("carSystem_1.0")

#Initialize software



isAutomaticMode = True
is80PrecentLight = True
isDirectLight = True
isRainy = False

print("Automatic Mode :", isAutomaticMode)
print("Bright Level over 80% : ", is80PrecentLight)
print("Blinding Light : ", isDirectLight)
print("Rainy Mode :", isRainy, "\n")


if (isAutomaticMode == True and
        is80PrecentLight == True and
        isDirectLight == False and
        isRainy == False):
    print("Lights OFF!")
elif (isAutomaticMode == True and
        is80PrecentLight == False and
        isDirectLight == False and
        isRainy == False):
    print("Lights ON!")
elif (isAutomaticMode == True and
        is80PrecentLight == True and
        isDirectLight == False and
        isRainy == True):
    print("Lights ON!")
elif (isAutomaticMode == True and
        is80PrecentLight == True and
        isDirectLight == True and
        isRainy == False):
    print("Lights ON!")
elif (isAutomaticMode == False and
        is80PrecentLight == True and
        isDirectLight == True and
        isRainy == True):
    print("Lights OFF!")
