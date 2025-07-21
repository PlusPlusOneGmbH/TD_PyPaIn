'''Info Header Start
Name : compInstaller
Author : Wieland PlusPlusOne@AMB-ZEPH15
Saveorigin : PyPaIn.toe
Saveversion : 2023.12000
Info Header End'''
def installOpAt(targetOp, path:str, rootComp = None):
    currentComp = rootComp or op("/")
    for pathElement in path.strip("/").split("/"):
        currentComp = currentComp.op( pathElement ) or currentComp.create( baseCOMP, pathElement )
    return currentComp.copy( targetOp )

