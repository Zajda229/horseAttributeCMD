speed = "minecraft:generic.movement_speed"
jump ="minecraft:horse.jump_strength"
hearts="minecraft:generic.max_health"
savedStats = []


print("\nx -> end program\n\n")

while(True):
    try:
        i = input("Attributs: ")

        if(i.lower() == "x"):
            break
    
        speedID = i.index(speed)
        jumpID = i.index(jump)
        heartsID = i.index(hearts)
    
        spd =""
        jmp =""
        hrts=""
        for y in range(5):
            spd+=i[speedID-29+y]
            jmp+=i[jumpID-28+y]
            if(y<=3):
                hrts+=i[heartsID-14+y]

        hrts=str(float(hrts)/2)
        spdBlock = "{:.2f}".format((42.16*float(spd)))
        if(not savedStats):
            final ="\n\nSpeed: "+spd+"  ->  "+spdBlock+" Blocks/s (max 14.23)"+"\nJump: "+jmp+" (0.4 - 1)"+"\nHearts: "+hrts
        else:
            final ="\n\nSpeed: "+spd+" ["+savedStats[0]+"] "+"  ->  "+spdBlock+" ["+savedStats[1]+"] "+" Blocks/s (max 14.23)"+"\nJump: "+jmp+" ["+savedStats[2]+"] "+" (0.4 - 1)"+"\nHearts: "+hrts+" ["+savedStats[3]+"] "    

        print(final,"\n")
        if(input("save? (y/n): ").lower()=="y"):
            savedStats = [spd, spdBlock, jmp, hrts]
    except(ValueError):
        print("\n!Wrong data!\n")