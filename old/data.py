





ChampAttackBase = 20
ChampHPBase = 20
ChampDEFBase = 20
ChampBLBase = 20
ChampVPBase = 20

UltimAttackBase = 30
UltimHPBase = 30
UltimDEFBase = 30
UltimBLBase = 30
UltimVPBase = 30

MegaAttackBase = 0
MegaHPBase = 0
MegaDEFBase = 0
MegaBLBase = 0
MegaVPBase = 0

HPMaxConTx = 3
HPMaxStrTx = 1
AttackStrTx = 1
AttackDexTx = .5
DEFConTx = 1.5
DEFIntTx = .5
BLDexTx = 1.5
BLIntTx = 5
VPIntTx = 2
VPConTx = .5






MyStrength=0
MyDexterity =0
MyConstitution=0
MyIntelligence =0

statsLevel =[2,2,2,2]

ITAttackBase = 130
ITHPBase = 75
ITDEFBase = 67
ITBLBase = 195
ITVPBase = 80


RokieHPBase = 530
RokieAttackBase = 345
RokieDEFBase = 160
RokieBLBase = 410
RokieVPBase = 150



limit =110
Strength = 10 + (statsLevel[0] * (limit - 1)) + MyStrength 
Dexterity = 10 + (statsLevel[1] * (limit - 1)) + MyDexterity 
Constitution = 10 + (statsLevel[2] * (limit - 1)) + MyConstitution 
Intelligence = 10 + (statsLevel[3] * (limit - 1)) + MyIntelligence 


rookI=[ Strength , Dexterity , Constitution,  Intelligence ]


Attack = 530 + (  (539+290)   * 1.6) + (737 * 0.6)   +83*1.1

HPMax =  600 + (Constitution *1.5) + (Dexterity * 0.8) 

Defense = ITDEFBase + (Constitution * DEFConTx) + (Intelligence * DEFIntTx)
BattleLevel = ITVPBase + (Dexterity * 0.8) + (Intelligence * 1.5)

rookII=[ Attack ,  Defense  ,BattleLevel]
print ("max: "+ HPMax.__str__())




statsLevel2 =[4,3,1,0]
MyStrength2 =0
limit =30
CStrength = 20+  (statsLevel2[0] * (limit - 20)) + MyStrength2 +  Strength
CDexterity = 20+ (statsLevel2[1] * (limit - 20)) + MyDexterity  + Dexterity 
CConstitution = 20+ (statsLevel2[2] * (limit - 20)) + MyConstitution  + Constitution
CIntelligence = 20+ (statsLevel2[3] * (limit - 20)) + MyIntelligence + Intelligence


cI=[ CStrength , CDexterity , CConstitution,  CIntelligence ]


print(rookI)
print(rookII)
print("--------")
print(cI)


#140