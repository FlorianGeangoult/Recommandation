# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:26:51 2021

@author: floly
"""

from matplotlib.pyplot import *   
from numpy import *
import pandas as pd

path = 'C:/Users/floly/OneDrive - Groupe IGS/Documents/DUT S3/projet python/toy_incomplet.csv'
df = pd.read_csv(path, encoding="UTF-8", sep='\t') 

print(" jeu incomplet initial : ") 
print(df)
df = df.dropna(axis=1)

p = 'C:/Users/floly/OneDrive - Groupe IGS/Documents/DUT S3/projet python/toy_complet.csv'
df2 = pd.read_csv(p, encoding="UTF-8", sep='\t') 

print(" jeu incomplet initial : ") 
print(df)

#print(df.loc[0])
#print(df.columns)


df.head()
p = 0
c = 0


df2 = df2.dropna(axis=1)

#Parcourir les valeurs
def parcoursValeurs():
    #i represente les utilisateurs
    for i in range(df.shape[0]):
        #j represente les items
        for j in range(df.shape[1]):
            # si il n'y a pas de note sur l'item j de l'utilisateur i, on met le resultat de la methode 
            #predite dans une copie du jeu de donnée
            if df.iloc[i,j] == -1:
                print("l'utilisateur " , i , " a n'a pas de note colonne : " , j )
                print(df.iloc[i,j])
                IncompletComplété.iloc[i,j] = predite(i,j)
                #IncompletComplété2.iloc[i,j] = predite(i,j)
                print(IncompletComplété.iloc[i,j])
                
                
#Calcul des moyennes             
def moyennes(i):
        moyenne2 = 0
        nbTermes2 = 0
        #Parcours des colonnes
        for t in range(df.shape[1]):
            if df.iloc[i,t]!=-1:
                moyenne2+=df.iloc[i,t]
                nbTermes2+=1
        moyenne2=moyenne2/nbTermes2
        return moyenne2
    
                
#Prediction de la note j pour l'utilisateur k
def predite(k, j):
    simTotal = 0
    prediteNum = 0
    
    for i in range(df.shape[0]):
        #Si il y a bien une note à la position i j
        if df.iloc[i,j] != -1:
            #On ajoute a la valeur SimTotal la valeur de similarite entre l'utilisateur k et i
            simTotal += simtabcos.iloc[k,i]
            #simTotal += simtabpearson.iloc[k,i]
            
            #On ajoute a la valeur PrediteNum le produit de la similarite entre l'utilisateur k et i 
            #et la difference de la note donner à l'item j de l'utilisateur i et de la moyenne des notes de l'user i
            prediteNum += (simtabcos.iloc[k,i]*(df.iloc[i,j]-moyennetab.iloc[i,0]))
            #prediteNum += (simtabpearson.iloc[k,i]*(df.iloc[i,j] -moyennetab.iloc[i,0]))
            
    #On retourne la valeur arrondie à l'entier de la note predite soit  la moyenne des notes 
    #de l'utilisateur k  + prediteNum/SimTotal     
    return round(moyennetab.iloc[k,0]+(prediteNum/simTotal),0)


#Calcul similarite de Pearson
def pearson(o,g) :
    
    num2 =0
    denom1=0
    denom2=0
   
    #Pour toute les colonnes du tableau
    for j in range (df.shape[1]):
        #Si l'utilisateur o et g ont bien une note pour l'item j
        if(df.iloc[o,j]!=-1 and df.iloc[g,j]!=-1):
            #On ajoute à la valeur num2, la note donné à l'item j de l'utilisateur o - la moyenne des notes de l'user o
            # multiplie la note donne à l'item j de l'utilisateur g - la moyenne des notes de l'user g 
            num2 += (df.iloc[o,j]-moyennetab.iloc[o,0])*(df.iloc[g,j]-moyennetab.iloc[g,0])
            #la note donnée à l'item j de l'utilisateur o - la moyenne des notes de l'utilisateur o le tout au carre
            denom1 += ((df.iloc[o,j]-moyennetab.iloc[o,0])**2)
            #la note donnée à l'item j de l'utilisateur g - la moyenne des notes de l'user g  le tout au carre
            denom2 += (df.iloc[g,j]-moyennetab.iloc[g,0])**2

    #Denominateur = racine du produit de denom1 * denom2
    denom = sqrt(denom1*denom2)
    simPearson=num2/denom
    return simPearson


def cosinus(o,g):
    dénom1 = 0
    dénom2 = 0
    num = 0
    
    for j in range(df.shape[1]) :
            if(df.iloc[o,j] != -1 and df.iloc[g,j] != -1) :
                    dénom1 += (df.iloc[o,j])**2
                    dénom2 += (df.iloc[g,j])**2
                    num +=(df.iloc[o,j]*df.iloc[g,j])
                    
    dénom2 = sqrt(dénom2)                
    dénom1 = sqrt(dénom1)
    sci = num/(dénom1*dénom2)
    sci = round(sci,6)
    
    return sci



def comparaisonCos():
    
    somme = 0
    q = 0
    sommenorm = 0
    
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if(df.iloc[i,j] == -1):
                somme += (completCos.iloc[i,j] - df2.iloc[i,j])
                sommenorm += abs(completCos.iloc[i,j] - df2.iloc[i,j])
              
                q += 1
    
    print("q = ", q)
    print("Biais avec cosinus : ", somme/q)
    global c 
    c = somme/q
    print("Erreur moyenne cosinus : ", sommenorm/q)
    
    
    return sommenorm/q

#Fonction comparaison Pearson 
def comparaisonPear():
    
    somme = 0
    sommenorm = 0
    q = 0
    
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if(df.iloc[i,j] == -1):
               
                somme += (completPear.iloc[i,j] - df2.iloc[i,j])
                sommenorm += abs(completPear.iloc[i,j] - df2.iloc[i,j])
                q += 1
    
    print("q = ", q)
    print("Biais avec Pearson : ",somme/q)
    global p 
    p = somme/q
    print("Erreur moyenne Pearson : ",sommenorm/q)
    return sommenorm/q
    
def graphique():
    
    noteCosinus =[]
    notePearson =[]
    vraieNote = []
    y = []
    
    for j in range(10):
        print(completCos.iloc[0,j])
        noteCosinus.append(completCos.iloc[0,j])
        notePearson.append(completPear.iloc[0,j])
        vraieNote.append(df2.iloc[0,j])
        y.append(j+1)
    
    size = 125
    scatter(y,vraieNote, s=size, label = 'Vraies notes')
    size=100
    scatter(y, noteCosinus, s=size, c='coral', label = 'Notes cosinus')
    size = 75
    scatter(y, notePearson, s=size, c= 'lightblue', label = 'Notes Pearson')
    
    legend()
    
    title('Nuage de points avec Matplotlib')
    xlabel('Note')
    ylabel('Item')
    savefig('ScatterPlot_03.png')
    show()
    
    fig = figure()
    
    width = 0.8
    bar(y, vraieNote, 1.0)
    bar(y, noteCosinus, width, color ='coral')
    bar(y, vraieNote, width, color ='lightblue')
    grid()
    ylabel('Notes')
    savefig('bar.png')
    show()
      
    

simtabcos=pd.read_csv("simCosinusTableau.csv")
simtabpearson=pd.read_csv("simPearsonTableau.csv")
IncompletComplété=df.copy()    
IncompletComplété2=df.copy()    
moyennetab = pd.read_csv("moyennesTableau.csv")
completCos = pd.read_csv("IncompletComplété.csv")
completPear = pd.read_csv("IncompletComplété2.csv")

print("notes avec cosinus : ")
print(completCos)
print("notes avec pearson : ")
print(completPear)
print("notes bonnes : ")
print(df2)
#parcoursValeurs()

#pd.DataFrame(IncompletComplété).to_csv("IncompletComplété.csv",index=False)
#pd.DataFrame(IncompletComplété2).to_csv("IncompletComplété2.csv",index=False)

#SimilaritesCos= np.zeros(shape=(100,100))
#for i in range(100):
    #for j in range(100):
        #SimilaritesCos[i][j]=cosinus(i,j)
        #print('case ', i, ' : ', j)
#pd.DataFrame(SimilaritesCos).to_csv("simCosinusTableau.csv",index=False)

#SimilaritesPearson= np.zeros(shape=(100,100))
#for i in range(100):
    #for j in range(100):
        #SimilaritesPearson[i][j]=pearson(i,j)
        #print('case', i, ' : ', j)
        #print(pearson(i,j))

#pd.DataFrame(SimilaritesPearson).to_csv("simPearsonTableau.csv",index=False)

#Moyenne = np.zeros(shape=(100,1))
#for i in range(100):

        #Moyenne[i][0]=moyennes(i)
        #print('hop : ', moyennes(i))
#pd.DataFrame(Moyenne).to_csv("moyennesTableau.csv",index=False)

print("jeu de similarité cosinus : ")
print(simtabcos)
print("jeu de similarité pearson : ")
print(simtabpearson)

        

print("moyennes des notes de chaque utilisateur : ")
print(moyennetab)

comparaisonCos()
comparaisonPear()
graphique()

fig = figure()
y= ['Cosinus','Pearson']
comparaison = [comparaisonCos(),comparaisonPear()]
    
width = 0.8
bar(y, comparaison, width, color ='coral')
grid()
ylabel('Erreur moyenne')
savefig('bar.png')
show()

print(c)
print(p)

fig = figure()
y= ['Cosinus','Pearson']
comparaison = [c, p]
    
width = 0.8
bar(y, comparaison, width, color ='coral')
grid()
ylabel('Biais')
savefig('bar.png')
show()


    
print("fin ")

print(max)


