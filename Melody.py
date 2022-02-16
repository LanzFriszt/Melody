import winsound
import time
import random
NoteNames = ['E5', 'DS5', 'D5', 'CS5', 'C5', 'B4', 'AS4', 'A4', 'GS4', 'G4', 'FS4', 'F4', 'E4', 'DS4', 'D4', 'CS4', 'C4', 'B3', 'AS3', 'A3']
Frequencies = {'E5': 659,'DS5': 554,'D5': 587,'CS5': 554,'C5': 523,'B4': 494,'AS4': 466,'A4': 440,'GS4': 415,'G4': 392,'FS4': 370,'F4': 349,'E4': 330,'DS4': 311,'D4': 294,'CS4': 277,'C4': 261,'B3': 247,'AS3': 233,'A3': 220,}
Key = 'C4'
Tempo = 120
Beat = int(60000 / Tempo)
Division = int(Beat / 4)
#Uses the key and the NoteNames currently stored to find every note in the diatonic scale.
Mode = input("Major or Minor? ")
KeyPlace = NoteNames.index(Key)

if Mode == 'Major':
    Do = NoteNames[KeyPlace]
    Re = NoteNames[KeyPlace - 2]
    Mi = NoteNames[KeyPlace - 4]
    Fa = NoteNames[KeyPlace - 5]
    Sol = NoteNames[KeyPlace - 7]
    La = NoteNames[KeyPlace - 9]
    Ti = NoteNames[KeyPlace - 11]
    HighDo = NoteNames[KeyPlace - 12]
elif Mode == 'Minor':
    Do = NoteNames[KeyPlace]
    Re = NoteNames[KeyPlace - 2]
    Mi = NoteNames[KeyPlace - 3]
    Fa = NoteNames[KeyPlace - 5]
    Sol = NoteNames[KeyPlace - 7]
    La = NoteNames[KeyPlace - 8]
    Ti = NoteNames[KeyPlace - 11]
    HighDo = NoteNames[KeyPlace - 12]
#DS stands for "Diatonic Scale"
DS = [Do, Re, Mi, Fa, Sol, La, Ti, HighDo]
Melody = []
def PlayMelody(Melody):
    for Note in Melody:
        try:
            if Note[:1] == 'L':
                NextLength = int(Note[1:])
                next
        except:
            winsound.Beep(Frequencies[DS[Note]],Division * NextLength)
def GenerateMelody(Melody):
    Melody = Melody
    ##Determines how long the offbeat should be
    CurrentOffBeat = random.choice([2, 4, 8])
    CurrentOnBeat = 16 - CurrentOffBeat
    ##Determines how long the second offbeat should be
    CounterOnBeat = random.choice([2, 4, 8, 12, 14])
    CounterOffBeat = 16 - CounterOnBeat
    GenerateIdea(Melody, CurrentOnBeat, CurrentOffBeat, CounterOnBeat, CounterOffBeat)
def GenerateIdea(Melody, CurrentOnBeat, CurrentOffBeat, CounterOnBeat, CounterOffBeat):
    CounterOnBeat = CounterOnBeat
    CounterOffBeat = CounterOffBeat
    CurrentOnBeat = CurrentOnBeat
    CurrentOffBeat = CurrentOffBeat
    Melody = Melody
    Melody.append("L{}".format(CurrentOnBeat))
    Melody.append(random.choice([0,0, 0, 2,4,7]))
    ##If the offbeat is very short, it shouldn't leap too far
    Melody.append("L{}".format(CurrentOffBeat))
    if CurrentOffBeat == 2:
        Melody.append(random.randint(0, 5))
    elif CurrentOffBeat == 4:
        Melody.append(random.randint(0, 6))
    elif CurrentOffBeat == 8:
        Melody.append(random.randint(0, 7))
    ##At this early point, if the melody has gone away from the tonic, there is nothing to do except go back, so we go straight to CreateCadence
    if Melody[-1] not in [0, 2, 4, 7]:
        CreateCadence(Melody, CurrentOnBeat, CurrentOffBeat, CounterOnBeat, CounterOffBeat)
        return
    ##Now, the melody needs to be forced to leave the tonic in some way. There are a few rules here.
    elif Melody[-1] in [0, 2, 4, 7]:
        Options = []
        ##Now the program needs to choose some non-tonic notes to continue with.
        Melody.append("L{}".format(CurrentOnBeat))
        Melody.append(random.choice([1,3,5,6]))
        Melody.append("L{}".format(CurrentOffBeat))
        Melody.append(random.choice([1,3,5,6]))
        ##and close with cadence.
        CreateCadence(Melody, CurrentOnBeat, CurrentOffBeat, CounterOnBeat, CounterOffBeat)
        return
def CreateCadence(Melody, CurrentOnBeat, CurrentOffBeat, CounterOnBeat, CounterOffBeat):
        ##The program picks a random tonic note and a pre-resolution note next to it.
        Arrival = random.choice([0,2,4,7])
        Midpoint = Arrival + random.choice([-1,1])
        ##To prevent overshooting
        if Midpoint == -1:
            Midpoint = 1
        if Midpoint == 8:
            Midpoint = 6
        Melody.append("L{}".format(CounterOnBeat))
        Melody.append(Midpoint)
        Melody.append("L{}".format(CounterOffBeat))
        Melody.append(Arrival)
        Melody.append("L8".format(CounterOffBeat))
        Melody.append(Arrival)
        return
while True:
    GenerateMelody(Melody)
    PlayMelody(Melody)
    Melody = []

